# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 3
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; If not, see <http://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####

__author__ = "Sergi Blanch-Torne"
__copyright__ = "Copyright 2015, CELLS / ALBA Synchrotron"
__license__ = "GPLv3+"

from getpass import getuser
import os
from socket import gethostname
import sys

# The widgets are stored in a subdirectory and needs to be added to the
# pythonpath
# linacWidgetsPath = os.environ['PWD']+'/widgets'
# if linacWidgetsPath not in sys.path:
#     sys.path.append(linacWidgetsPath)

from taurus.core.util import argparse
from taurus.core.util.log import LogExceptHook, Logger
from taurus.external.qt import Qt, QtGui, QtCore
from taurus.qt.qtgui.application import TaurusApplication
from taurus.qt.qtgui.base import TaurusBaseComponent
from taurus.qt.qtgui.container import TaurusMainWindow
from taurus.qt.qtgui.display import TaurusLed
from taurus.qt.qtgui.container import TaurusWidget
from taurus.qt.qtgui.plot import TaurusPlot
from taurus.qt.qtgui.util import ExternalAppAction
from taurus.qt.qtgui.util.ui import UILoadable
from taurus.qt.qtgui.table import TaurusValuesTable
from taurus import Release as taurusRelease
try:
    from taurus.external.qt import Qwt5
except:
    from taurus.qt import Qwt5

from .widgets.attrautostopper import AttrAutostopper
from .widgets.attrramps import AttrRamps
from .widgets.componentswindow import CompomentsWindow
from .widgets.devicesevents import DevicesEvents
from .widgets.evr300 import EVR300

from .ctliaux import _setupLed4UnknownAttr, _setupLed4Attr
from .ctliaux import _setupCheckbox4UnknownAttr, _setupCheckbox4Attr
from .ctliaux import _setupSpinBox4Attr
from .ctliaux import _setupTaurusLabel4Attr
from .ctliaux import _setupCombobox4Attr
from .ctliaux import _setupActionWidget
from .ctliaux import defaultPreconfTrends, VERSION, prepareToLog

import subprocess
import threading
import time

LinacDeviceNameRoot = 'li/ct/plc'
LinacDeviceNames = []
for i in range(1, 6):
    LinacDeviceNames.append("%s%d" % (LinacDeviceNameRoot, i))
DeviceRelocator = 'li/ct/linacDataRelocator-01'


@UILoadable(with_ui="ui")
class LinacMainWindow(TaurusMainWindow, TaurusWidget):
    def __init__(self, parent=None, name=None, designMode=None):
        try:
            self.__name = name.__name__
        except:
            self.__name = "LinacMainWindow"
        super(LinacMainWindow, self).__init__(parent, designMode=designMode)
        self.info("Using taurus %s" % (taurusRelease.version))
        # setup main window
        self._loadUI()
        # place the ui in the window
        self._init_threads = {}
        self._initComponentsTask = ""
        self._initComponentsSubtask = ""
        self._initComponentsNsubtask = 0
        self._readonlyWidgets = []
        self._readwriteWidgets = []
        self.initComponents()
        # kill splash screen
        self.splashScreen().finish(self)

    def _loadUI(self):
        try:
            self.debug("[%s]__init__()" % (self.__name))
            basePath = os.path.dirname(__file__)
            if len(basePath) == 0:
                basePath = '.'
            filename = "ctli.ui"
            path = basePath+"/widgets/ui"
            self.loadUi(filename, path)
        except Exception as e:
            self.warning("[%s]__init__(): Widget (%s, %s) exception! %s"
                         % (self.__name, filename, path, e))
            # traceback.print_exc()
            self.traceback()
            raise e

    def initComponents(self):
        self.setWindowTitle("Linac Taurus User Interface")
        self.centralwidget = self.ui.linacTabs
        self.setCentralWidget(self.centralwidget)
        self.centralwidget.setCurrentIndex(2)
        # Force to start in "main screen"
        self.setDockNestingEnabled(True)
        # concurrency in the big setModel and early return
#        self._init_threads['Communications'] = \
#            threading.Thread(name="'Communications'",
#                             target=self.setCommunications)
#        self._init_threads['Startup'] = \
#            threading.Thread(name="Startup", target=self.setStartup)
#        self._init_threads['MainScreen'] = \
#            threading.Thread(name="MainScreen", target=self.setMainscreen)
#        for threadName in self._init_threads.keys():
#            self._init_threads[threadName].setDaemon(True)
#            self._init_threads[threadName].start()
        # serialised alternative of setModel
        self._setSplashScreenTask("Preparing communication")
        self.setCommunications()
        self._setSplashScreenTask("Preparing stat up tab")
        self.setStartup()
        self._setSplashScreenTask("Preparing main screen tab")
        self.setMainscreen()
        # self.setConfiguration()
        self._setSplashScreenTask("Preparing External applications")
        self.setExternalApplications()
        self._setSplashScreenTask("Preparing the status bar")
        self.setStatusBar()
        self._setSplashScreenTask("Preparing Menus")
        self.setMenuOptions()

    def closeEvent(self, event):
        if hasattr(self, '_eventPlotWindow') and \
                self._eventPlotWindow is not None:
            self._eventPlotWindow.close()
            self._eventPlotWindow = None
        if hasattr(self, '_evr300Window') and \
                self._evr300Window is not None:
            self._evr300Window.close()
            self._evr300Window = None
        if hasattr(self, '_attrRampsWindow') and \
                self._attrRampsWindow is not None:
            self._attrRampsWindow.close()
            self._eventPlotWindow = None
        if hasattr(self, '_compomentWindow') and \
                self._compomentWindow is not None:
            self._compomentWindow.close()
            self._compomentWindow = None

    ######
    # Section for the splashScreen message ---
    def refreshSplashScreenMessage(self):
        msg = "Preparing %s... " % (self._initComponentsTask)
        if len(self._initComponentsSubtask) > 0:
            msg = "%s(%s)" % (msg, self._initComponentsSubtask)
        self.debug("Setting SplashScreen message: %s" % (msg))
        self.splashScreen().showMessage(msg)

    def _setSplashScreenTask(self, task):
        self._initComponentsTask = task
        self.refreshSplashScreenMessage()

    def _setSplashScreenSubtask(self, subtask):
        self._initComponentsSubtask = subtask
        self.refreshSplashScreenMessage()
    # done section for the splashScreen message ---
    ######

    ######
    # Auxiliar methods to configure widgets ---
    def _setupLed4UnknownAttr(self, widget):
        _setupLed4UnknownAttr(widget)

    def _setupLed4Attr(self, widget, attrName, inverted=False, onColor='green',
                       offColor='red', pattern='on', blinkOnChange=None):
        _setupLed4Attr(widget, attrName, inverted, onColor, offColor,
                       pattern, blinkOnChange)
        self._readonlyWidgets.append(widget)

    def _setupCheckbox4UnknownAttr(self, widget):
        _setupCheckbox4UnknownAttr(widget)
        self._readwriteWidgets.append(widget)

    def _setupCheckbox4Attr(self, widget, attrName, isRst=False, DangerMsg='',
                            riseEdge=False, fallingEdge=False):
        _setupCheckbox4Attr(widget, attrName, isRst, DangerMsg,
                            riseEdge, fallingEdge)
        self._readwriteWidgets.append(widget)

    def _setupSpinBox4Attr(self, widget, attrName, step=None, DangerMsg='',
                           dangerAbove=None, dangerBelow=None):
        _setupSpinBox4Attr(widget, attrName, step, DangerMsg, dangerAbove,
                           dangerBelow)
        # if hasattr(widget, 'wheelEvent'):
        #     def wheelEvent(evt):
        #         pass  # spinboxes in the ctli shall not react to wheelEvent
        #     widget.wheelEvent = wheelEvent
        self._readwriteWidgets.append(widget)

    def _setupTaurusLabel4Attr(self, widget, attrName, unit=None):
        _setupTaurusLabel4Attr(widget, attrName, unit)
        self._readonlyWidgets.append(widget)

    def _setupCombobox4Attr(self, widget, attrName, valueNames=None):
        _setupCombobox4Attr(widget, attrName, valueNames)
        self._readwriteWidgets.append(widget)

    def _setupActionWidget(self, widget, attrName, text='on/off',
                           isRst=False, isValve=False, isLight=False,
                           DangerMsg='', riseEdge=False, fallingEdge=False):
        # Hackish!!
        pyqtVersion = QtCore.PYQT_VERSION_STR
        qtVersion = QtCore.QT_VERSION_STR
        # self.info("Detected Qt version: %s (PyQt %s)"
        #           % (qtVersion, pyqtVersion))
        major, middle, minor = qtVersion.split('.')
        major = int(major)
        middle = int(middle)
        minor = int(minor)
        if major == 4 and middle == 4:
            widget._ui.Check.setMinimumWidth(25)
        # This is because in Alba's qt version the text is very close to the
        # checkbox, but in newer ones the distance is bigger and this doesn't
        # allow to see the '!' when pending operations.
        _setupActionWidget(widget, attrName, text, isRst, isValve,
                           isLight, DangerMsg, riseEdge, fallingEdge)
        if isRst:
            try:
                widget._ui.actionFrame.setStyleSheet("background-color: "
                                                     "rgba(192, 192, 0, 63);")
                widget._ui.Check.setStyleSheet("background-color: white;")
            except Exception as e:
                self.error("Cannot modify the background color of the "
                           "actionWidget for the attribute %s: %s"
                           % (attrName, e))
        self._readwriteWidgets.append(widget)

    # Done auxiliar methods to configure widgets ---
    ######

    def setCommunications(self):
        # about the overview
        self.ui.linacOverview.hide()
        plcWidgets = [self.ui.plc1, self.ui.plc2, self.ui.plc3, self.ui.plc4,
                      self.ui.plc5]
        for i, plc in enumerate(plcWidgets):
            self._setSplashScreenSubtask("PLC%d" % (i+1))
            plc.setModel("%s%d" % (LinacDeviceNameRoot, i+1))
            plc.setRelocator(DeviceRelocator, i)

    # setModel & others for the Start up Tab ---
    def setStartup(self):
        # following the synoptic regions from left to right and
        # from top to bottom
        self._setSplashScreenSubtask("Interlock Unit")
        self._setStartup_InterlockUnit()
        self._setSplashScreenSubtask("klystron Low Voltage")
        self._setStartup_klystronLV()
        self._setSplashScreenSubtask("Electron Gun")
        self._setStartup_egun()
        self._setSplashScreenSubtask("Cooling")
        self._setStartup_cooling()
        self._setSplashScreenSubtask("Magnets")
        self._setStartup_magnets()
        self._setSplashScreenSubtask("Vacuum")
        self._setStartup_vacuum()
        startup_ui = self.ui.linacStartupSynoptic._ui
        startup_ui.StartUpSchematic.lower()

    def _setStartup_InterlockUnit(self):
        startup_ui = self.ui.linacStartupSynoptic._ui
        # configure the widgets in the top left corner diagram ---
        self._setupLed4Attr(startup_ui.klystronAmplifierEnabledLed,
                            'li/ct/plc1/KA_ENB')  # KA_ENB
        self._setupLed4Attr(startup_ui.klystron2InterlockLed,
                            'li/ct/plc1/ka2_ic')  # KA2_IC
        self._setupLed4Attr(startup_ui.magnetInterlockStateLed,
                            'li/ct/plc1/MG_IS')  # MI_IS
        self._setupActionWidget(startup_ui.iuRst, 'li/ct/plc1/interlock_rc',
                                text='PLC1\nReset', isRst=True)  # Rst
        self._setupLed4Attr(startup_ui.klystron1InterlockLed,
                            'li/ct/plc1/ka1_ic')  # KA1_IC
        self._setupLed4Attr(startup_ui.utilitiesInterlockStateLed,
                            'li/ct/plc1/UT_IS')  # UI_IS
        self._setupLed4Attr(startup_ui.compressedAirStateLed,
                            'li/ct/plc2/ac_is')  # AC_IS
        self._setupLed4Attr(startup_ui.transferlineVacuumStateLed,
                            'li/ct/plc1/TL_VOK')  # TL_VOK
        self._setupLed4Attr(startup_ui.linacVacuumStateLed,
                            'li/ct/plc2/vc_ok')  # LI_VOK
        self._setupLed4Attr(startup_ui.electronGunEnabledLed,
                            'li/ct/plc1/EG_ENB')  # EG_ENB
        self._setupLed4Attr(startup_ui.gmdiLed,
                            'li/ct/plc1/GM_DI')  # GM_DI
        self._setupLed4Attr(startup_ui.interlockUnitReadyStateLed,
                            'li/ct/plc1/IU_RDY')  # UI
        self._setupLed4Attr(startup_ui.klystron2AmplifierEnabledLed,
                            'li/ct/plc1/ka2_ok')  # KA2_EN
        self._setupLed4Attr(startup_ui.klystron1AmplifierEnabledLed,
                            'li/ct/plc1/ka1_ok')  # KA1_EN
        self._setupLed4Attr(startup_ui.linacVacuumStateLed_2,
                            'li/ct/plc2/vc_ok')  # LI_VOK
        # (repeated on the right side of the IU)
        self._setupLed4Attr(startup_ui.linacReadyStateLed,
                            'li/ct/plc1/li_ok')  # LI_RDY
        # configure the klystrons popups: ---
        klystrons = {1: {'check': startup_ui.klystron1InterlockPopupCheck,
                         'widget': startup_ui.klystron1InterlockPopupWidget,
                         'sf6':
                         startup_ui.klystron1InterlockPopupWidget._ui.sf6p1Led,
                         'sf6_attrName': 'li/ct/plc1/sf6_p1_st',
                         'rfw': [startup_ui.klystron1InterlockPopupWidget._ui.
                                 rfw1Led,
                                 startup_ui.klystron1InterlockPopupWidget._ui.
                                 rfw2Led],
                         'rfw_attrName': ['li/ct/plc1/w1_uf',
                                          'li/ct/plc1/w2_uf'],
                         'rfl': [startup_ui.klystron1InterlockPopupWidget._ui.
                                 rfl1Led,
                                 startup_ui.klystron1InterlockPopupWidget._ui.
                                 rfl2Led],
                         'rfl_attrName': ['li/ct/plc1/rl1_uf',
                                          'li/ct/plc1/rl2_uf']},
                     2: {'check': startup_ui.klystron2InterlockPopupCheck,
                         'widget': startup_ui.klystron2InterlockPopupWidget,
                         'sf6': startup_ui.klystron2InterlockPopupWidget._ui.
                         sf6p2Led,
                         'sf6_attrName': 'li/ct/plc1/sf6_p2_st',
                         'rfw': [startup_ui.klystron2InterlockPopupWidget._ui.
                                 rfw3Led],
                         'rfw_attrName': ['li/ct/plc1/w3_uf'],
                         'rfl': [startup_ui.klystron2InterlockPopupWidget._ui.
                                 rfl3Led],
                         'rfl_attrName': ['li/ct/plc1/rl3_uf']}}
        self._klystronsInterlocks = {}
        # to avoid garbage collection on the CkechboxManagers
        # Using the previous structure configure each of the klystrons
        # interlock widgets
        for number in klystrons.keys():
            klystron = klystrons[number]
            # klystron['check'].setCheckState(False)
            klystron['widget'].hide()
            self._klystronsInterlocks[number] = \
                CheckboxManager(klystron['check'], klystron['widget'],
                                'klystron%dInterlock' % (number))
            self._setupLed4Attr(klystron['sf6'], klystron['sf6_attrName'])
            for i in range(len(klystron['rfw'])):
                self._setupLed4Attr(klystron['rfw'][i],
                                    klystron['rfw_attrName'][i])
            for i in range(len(klystron['rfl'])):
                self._setupLed4Attr(klystron['rfl'][i],
                                    klystron['rfl_attrName'][i])

    def _setStartup_klystronLV(self):
        startup_ui = self.ui.linacStartupSynoptic._ui
        klystrons = {1: {'plc': 4,
                         'on': startup_ui.klystron1On,
                         'rst': startup_ui.klystron1Rst,
                         'led': startup_ui.klystron1LVLed,
                         'check': startup_ui.klystron1LVPopupCheck,
                         'widget': startup_ui.klystron1LVWidget},
                     2: {'plc': 5,
                         'on': startup_ui.klystron2On,
                         'rst': startup_ui.klystron2Rst,
                         'led': startup_ui.klystron2LVLed,
                         'check': startup_ui.klystron2LVPopupCheck,
                         'widget': startup_ui.klystron2LVWidget}}
        self._klystronLV = {}
        for number in klystrons.keys():
            # on/off klystron low voltage ---
            attrName = 'li/ct/plc%d/LV_ONC' % (klystrons[number]['plc'])
            msg = "ALERT: this will shutdown the klystron %d low voltage!"\
                % (number)
            self._setupActionWidget(klystrons[number]['on'], attrName,
                                    text='on/off', DangerMsg=msg,
                                    fallingEdge=True)
            # reset klystron low voltage ---
            attrName = 'li/ct/plc%d/LV_Interlock_RC'\
                % (klystrons[number]['plc'])
            self._setupActionWidget(klystrons[number]['rst'], attrName,
                                    text='Reset', isRst=True)
            # popup more information ---
            widget = klystrons[number]['led']
            self._setupLed4Attr(widget, 'li/ct/plc%d/LV_ready'
                                % (klystrons[number]['plc']))
            widget = klystrons[number]['check']
            # prepare the checkmanager
            # klystrons[number]['check'].setCheckState(False)
            klystrons[number]['widget'].hide()
            self._klystronLV[number] = \
                CheckboxManager(klystrons[number]['check'],
                                klystrons[number]['widget'],
                                "Klystron%dLVManager" % (number))
            # setmodel for the contents in the popup
            widget = klystrons[number]['widget']
            widget._ui.lowVoltageGroup.setTitle('klystron%d low voltage'
                                                % (number))
            widget._ui.LV_Status.setModel('li/ct/plc%d/LV_Status'
                                          % (klystrons[number]['plc']))
            widget._ui.LV_TimeValue.setModel('li/ct/plc%d/LV_Time'
                                             % (klystrons[number]['plc']))
            widget._ui.heatStatus.setModel('li/ct/plc%d/Heat_Status'
                                           % (klystrons[number]['plc']))
            widget._ui.heatVValue.setModel('li/ct/plc%d/Heat_V'
                                           % (klystrons[number]['plc']))
            widget._ui.heatIValue.setModel('li/ct/plc%d/Heat_I'
                                           % (klystrons[number]['plc']))
            widget._ui.heatTValue.setModel('li/ct/plc%d/Heat_Time'
                                           % (klystrons[number]['plc']))

    def _setStartup_egun(self):
        startup_ui = self.ui.linacStartupSynoptic._ui
        # on/off electron gun low voltage ---
        attrName = 'li/ct/plc1/GUN_LV_ONC'
        msg = "ALERT: this will shutdown the electron gun low voltage!"
        self._setupActionWidget(startup_ui.eGunOn, attrName,
                                text='on/off', DangerMsg=msg, fallingEdge=True)
        # widgets in the KD box ---
        self._setupSpinBox4Attr(startup_ui.filamentSetpoint,
                                'li/ct/plc1/GUN_Filament_V_setpoint', step=0.1)
        self._setupSpinBox4Attr(startup_ui.cathodeSetpoint,
                                'li/ct/plc1/GUN_Kathode_V_setpoint', step=0.1)
        self._setupTaurusLabel4Attr(startup_ui.filamentCurrent,
                                    'li/ct/plc1/GUN_Filament_I', 'A')
        self._setupTaurusLabel4Attr(startup_ui.temperatureValue,
                                    'li/ct/plc1/GUN_Kathode_T', 'C')
        # popup information shown in the KD box ---
        self._setupLed4Attr(startup_ui.kdeGunLVLed, 'li/ct/plc1/Gun_ready')
        startup_ui.kdeGunLVWidget.hide()
        self._egunManager = CheckboxManager(startup_ui.kdeGunLVPopupCheck,
                                            startup_ui.kdeGunLVWidget,
                                            "EGunPopup")
        popupWidget = startup_ui.kdeGunLVWidget._ui
        self._setupTaurusLabel4Attr(popupWidget.eGunStatus,
                                    'li/ct/plc1/Gun_Status')
        self._setupTaurusLabel4Attr(popupWidget.filamentValue,
                                    'li/ct/plc1/GUN_Filament_V', 'V')
        self._setupTaurusLabel4Attr(popupWidget.cathodeValue,
                                    'li/ct/plc1/GUN_Kathode_V', 'V')
        # ramp configuration
        # FIXME: temporally disabled all the ramps
#         button = popupWidget.RampConfigurator
#         device = 'li/ct/plc1'
#         title = "GUN_Filament_V"
#         formAttrs = ["GUN_Filament_V_setpoint_rampEnable",
#                      "GUN_Filament_V_setpoint_ascending_step",
#                      "GUN_Filament_V_setpoint_ascending_steptime",
#                      "GUN_Filament_V_setpoint_ascending_threshold",
#                      "GUN_Filament_V_setpoint_descending_step",
#                      "GUN_Filament_V_setpoint_descending_steptime",
#                      "GUN_Filament_V_setpoint_descending_threshold"]
#         plotAttrs = ["GUN_Filament_V", "GUN_Filament_V_setpoint"]
#         self._eGunLVRamp = \
#             RampConfigurationWidget(button, device, title, formAttrs,
#                                     plotAttrs, self)
        popupWidget.RampConfigurator.setEnabled(False)

    def _setStartup_cooling(self):
        startup_ui = self.ui.linacStartupSynoptic._ui
        coolingLoops = {1: {'on': startup_ui.coolingLoop1On,
                            'on_attrName': 'li/ct/plc2/CL1_ONC',
                            'Temperature':
                            startup_ui.coolingLoop1TemperatureValue,
                            'Temperature_attrName': 'li/ct/plc2/CL1_T',
                            'led': startup_ui.coolingLoop1Led,
                            'check': startup_ui.coolingLoop1PopupCheck,
                            'widget': startup_ui.coolingLoop1Widget,
                            'status_attrName': 'li/ct/plc2/CL1_Status',
                            'power_attrName': 'li/ct/plc2/CL1_PWD',
                            'window': startup_ui.w1Led,
                            'window_attrName': 'li/ct/plc1/w1_uf',
                            'resistorLoad': startup_ui.rl1Led,
                            'resistorLoad_attrName': 'li/ct/plc1/rl1_uf',
                            'epsTemperature_attrName':
                            'li/ct/cloops/CL1_Temp_Resistor',
                            'epsPressure_attrName': 'li/ct/cloops/CL1_P'},
                        2: {'on': startup_ui.coolingLoop2On,
                            'on_attrName': 'li/ct/plc2/CL2_ONC',
                            'Temperature':
                            startup_ui.coolingLoop2TemperatureValue,
                            'Temperature_attrName': 'li/ct/plc2/CL2_T',
                            'led': startup_ui.coolingLoop2Led,
                            'check': startup_ui.coolingLoop2PopupCheck,
                            'widget': startup_ui.coolingLoop2Widget,
                            'status_attrName': 'li/ct/plc2/CL2_Status',
                            'power_attrName': 'li/ct/plc2/CL2_PWD',
                            'window': startup_ui.w2Led,
                            'window_attrName': 'li/ct/plc1/w2_uf',
                            'resistorLoad': startup_ui.rl2Led,
                            'resistorLoad_attrName': 'li/ct/plc1/rl2_uf',
                            'epsTemperature_attrName':
                            'li/ct/cloops/CL2_Temp_Resistor',
                            'epsPressure_attrName': 'li/ct/cloops/CL2_P'},
                        3: {'on': startup_ui.coolingLoop3On,
                            'on_attrName': 'li/ct/plc2/CL3_ONC',
                            'Temperature':
                            startup_ui.coolingLoop3TemperatureValue,
                            'Temperature_attrName': 'li/ct/plc2/CL3_T',
                            'led': startup_ui.coolingLoop3Led,
                            'check': startup_ui.coolingLoop3PopupCheck,
                            'widget': startup_ui.coolingLoop3Widget,
                            'status_attrName': 'li/ct/plc2/CL3_Status',
                            'power_attrName': 'li/ct/plc2/CL3_PWD',
                            'window': startup_ui.w3Led,
                            'window_attrName': 'li/ct/plc1/w3_uf',
                            'resistorLoad': startup_ui.rl3Led,
                            'resistorLoad_attrName': 'li/ct/plc1/rl3_uf',
                            'epsTemperature_attrName':
                            'li/ct/cloops/CL3_Temp_Resistor',
                            'epsPressure_attrName': 'li/ct/cloops/CL3_P'}}
        self._coolingLoopManagers = {}
        self._coolingLoopHistory = {}
        for number in coolingLoops.keys():
            # on/off the cooling loops ---
            widget = coolingLoops[number]['on']
            attrName = coolingLoops[number]['on_attrName']
            msg = "ALERT: this will shutdown the cooling loop %d!" % (number)
            self._setupActionWidget(widget, attrName, text='on/off',
                                    DangerMsg=msg, fallingEdge=True)
            # cooling temperature setpoint ---
            widget = coolingLoops[number]['Temperature']
            attrName = coolingLoops[number]['Temperature_attrName']+'_setpoint'
            self._setupSpinBox4Attr(widget, attrName, step=0.1)
            # popup information about each cooling loop ---
            widget = coolingLoops[number]['led']
            self._setupLed4Attr(widget, 'li/ct/plc2/CL%d_ready' % (number))
            button = coolingLoops[number]['check']
            widget = coolingLoops[number]['widget']
            title = "CollingLoopPopup%d" % (number)
            widget.hide()
            self._coolingLoopManagers[number] = CheckboxManager(button, widget,
                                                                title)
            popupWidget = widget._ui
            popupWidget.coolingLoopGroup.setTitle('Cooling Loop %d' % (number))
            # inside the popup
            self._setupTaurusLabel4Attr(popupWidget.coolingLoopStatus,
                                        coolingLoops[number]
                                        ['status_attrName'])
            self._coolingLoopHistory[number] = \
                HistoryWidgetManager(popupWidget.coolingLoopStatusHistory,
                                     coolingLoops[number]['status_attrName'] +
                                     '_History', self)
            self._setupTaurusLabel4Attr(popupWidget.temperatureValue,
                                        coolingLoops[number]
                                        ['Temperature_attrName'], 'C')
            self._setupTaurusLabel4Attr(popupWidget.powerValue,
                                        coolingLoops[number]
                                        ['power_attrName'], '%')
            self._setupTaurusLabel4Attr(popupWidget.epsTempValue,
                                        coolingLoops[number]
                                        ['epsTemperature_attrName'], 'C')
            self._setupTaurusLabel4Attr(popupWidget.epsPressureValue,
                                        coolingLoops[number]
                                        ['epsPressure_attrName'], 'bar')
            self._setupLed4Attr(coolingLoops[number]['window'],
                                coolingLoops[number]['window_attrName'])
            self._setupLed4Attr(coolingLoops[number]['resistorLoad'],
                                coolingLoops[number]['resistorLoad_attrName'])

    def _setStartup_magnets(self):
        startup_ui = self.ui.linacStartupSynoptic._ui
        self._setupLed4Attr(startup_ui.sl1Led, 'li/ct/plc3/SL1_cooling')
        self._setupLed4Attr(startup_ui.sl2Led, 'li/ct/plc3/SL2_cooling')
        self._setupLed4Attr(startup_ui.sl3Led, 'li/ct/plc3/SL3_cooling')
        self._setupLed4Attr(startup_ui.sl4Led, 'li/ct/plc3/SL4_cooling')
        self._setupLed4Attr(startup_ui.bc1Led, 'li/ct/plc3/BC1_cooling')
        self._setupLed4Attr(startup_ui.bc2Led, 'li/ct/plc3/BC2_cooling')
        self._setupLed4Attr(startup_ui.glLed, 'li/ct/plc3/GL_cooling')
        # self._setupLed4Attr(startup_ui.as1Led, 'li/ct/plc3/AS1_cooling')
        self._setupLed4UnknownAttr(startup_ui.as1Led)
        self._setupLed4Attr(startup_ui.qtLed, 'li/ct/plc3/QT_cooling')
        # self._setupLed4Attr(startup_ui.as2Led, 'li/ct/plc3/AS2_cooling')
        self._setupLed4UnknownAttr(startup_ui.as2Led)

    def _setStartup_vacuum(self):
        startup_ui = self.ui.linacStartupSynoptic._ui
        vacuumValves = {1: {'open': startup_ui.vacuumValve1On,
                            'led': startup_ui.vacuumValve1OnLedInfo,
                            'open_attrName': 'li/ct/plc2/VV1_OC',
                            'status': startup_ui.vacuumValve1OnStatus,
                            'status_attrName': 'li/ct/plc2/VV1_Status'},
                        2: {'open': startup_ui.vacuumValve2On,
                            'led': startup_ui.vacuumValve2OnLedInfo,
                            'open_attrName': 'li/ct/plc2/VV2_OC',
                            'status': startup_ui.vacuumValve2OnStatus,
                            'status_attrName': 'li/ct/plc2/VV2_Status'},
                        3: {'open': startup_ui.vacuumValve3On,
                            'led': startup_ui.vacuumValve3OnLedInfo,
                            'open_attrName': 'li/ct/plc2/VV3_OC',
                            'status': startup_ui.vacuumValve3OnStatus,
                            'status_attrName': 'li/ct/plc2/VV3_Status'},
                        4: {'open': startup_ui.vacuumValve4On,
                            'led': startup_ui.vacuumValve4OnLedInfo,
                            'open_attrName': 'li/ct/plc2/VV4_OC',
                            'status': startup_ui.vacuumValve4OnStatus,
                            'status_attrName': 'li/ct/plc2/VV4_Status'},
                        5: {'open': startup_ui.vacuumValve5On,
                            'led': startup_ui.vacuumValve5OnLedInfo,
                            'open_attrName': 'li/ct/plc2/VV5_OC',
                            'status': startup_ui.vacuumValve5OnStatus,
                            'status_attrName': 'li/ct/plc2/VV5_Status'},
                        6: {'open': startup_ui.vacuumValve6On,
                            'led': startup_ui.vacuumValve6OnLedInfo,
                            'open_attrName': 'li/ct/plc2/VV6_OC',
                            'status': startup_ui.vacuumValve6OnStatus,
                            'status_attrName': 'li/ct/plc2/VV6_Status'},
                        7: {'open': startup_ui.vacuumValve7On,
                            'led': startup_ui.vacuumValve7OnLedInfo,
                            'open_attrName': 'li/ct/plc2/VV7_OC',
                            'status': startup_ui.vacuumValve7OnStatus,
                            'status_attrName': 'li/ct/plc2/VV7_Status'}}
        # open/close all valve in one action ---
        widget = startup_ui.vvOn
        attrName = 'li/ct/plc2/VVall_oc'
        self._setupActionWidget(widget, attrName, text='open/close')
        # reset vacuum interlocks ---
        widget = startup_ui.vvRst
        attrName = 'li/ct/plc2/Util_Interlock_RC'
        self._setupActionWidget(widget, attrName, text='Vacuum\nReset',
                                isRst=True)
        for number in vacuumValves.keys():
            # on/off each vacuum valve ---
            attrName = vacuumValves[number]['open_attrName']
            widget = vacuumValves[number]['led']
            self._setupLed4Attr(widget, attrName, offColor='red')
            widget = vacuumValves[number]['open']
            self._setupActionWidget(widget, attrName, text='open/close')
            # status of each vacuum valve ---
            widget = vacuumValves[number]['status']
            attrName = vacuumValves[number]['status_attrName']
            self._setupTaurusLabel4Attr(widget, attrName)

        # area of the vacuum information (TODO: may not well written) ---
        self._setupLed4Attr(startup_ui.ip1Led, 'li/ct/plc2/IP1_IS')
        self._setupLed4Attr(startup_ui.ip2Led, 'li/ct/plc2/IP2_IS')
        self._setupLed4Attr(startup_ui.ip3Led, 'li/ct/plc2/IP3_IS')
        self._setupLed4Attr(startup_ui.ip4Led, 'li/ct/plc2/IP4_IS')
        self._setupLed4Attr(startup_ui.ip5Led, 'li/ct/plc2/IP5_IS')
        self._setupLed4Attr(startup_ui.ip6Led, 'li/ct/plc2/IP6_IS')
        self._setupLed4Attr(startup_ui.ip7Led, 'li/ct/plc2/IP7_IS')
        self._setupLed4Attr(startup_ui.ip8Led, 'li/ct/plc2/IP8_IS')
        self._setupLed4Attr(startup_ui.ip9Led, 'li/ct/plc2/IP9_IS')
        self._setupLed4Attr(startup_ui.hvg1Led, 'li/ct/plc2/HVG1_IS')
        self._setupTaurusLabel4Attr(startup_ui.hvg1Value,
                                    'li/ct/plc2/HVG1_P', 'mbar')
        self._setupLed4Attr(startup_ui.hvg2Led, 'li/ct/plc2/HVG2_IS')
        self._setupTaurusLabel4Attr(startup_ui.hvg2Value,
                                    'li/ct/plc2/HVG2_P', 'mbar')
        self._setupLed4Attr(startup_ui.hvg3Led, 'li/ct/plc2/HVG3_IS')
        self._setupTaurusLabel4Attr(startup_ui.hvg3Value,
                                    'li/ct/plc2/HVG3_P', 'mbar')
        self._setupLed4Attr(startup_ui.hvg4Led, 'li/ct/plc2/HVG4_IS')
        self._setupTaurusLabel4Attr(startup_ui.hvg4Value,
                                    'li/ct/plc2/HVG4_P', 'mbar')
        self._setupLed4Attr(startup_ui.hvg5Led, 'li/ct/plc2/HVG5_IS')
        self._setupTaurusLabel4Attr(startup_ui.hvg5Value,
                                    'li/ct/plc2/HVG5_P', 'mbar')
        self._setupTaurusLabel4Attr(startup_ui.ipc1Value1,
                                    'li/ct/plc2/IP1_P', 'mbar')
        self._setupTaurusLabel4Attr(startup_ui.ipc1Value2,
                                    'li/ct/plc2/IP2_P', 'mbar')
        self._setupTaurusLabel4Attr(startup_ui.ipc2Value1,
                                    'li/ct/plc2/IP3_P', 'mbar')
        self._setupTaurusLabel4Attr(startup_ui.ipc2Value2,
                                    'li/ct/plc2/IP4_P', 'mbar')
        self._setupTaurusLabel4Attr(startup_ui.ipc3Value1,
                                    'li/ct/plc2/IP5_P', 'mbar')
        self._setupTaurusLabel4Attr(startup_ui.ipc3Value2,
                                    'li/ct/plc2/IP6_P', 'mbar')
        self._setupTaurusLabel4Attr(startup_ui.ipc4Value1,
                                    'li/ct/plc2/IP7_P', 'mbar')
        self._setupTaurusLabel4Attr(startup_ui.ipc4Value2,
                                    'li/ct/plc2/IP8_P', 'mbar')
        self._setupTaurusLabel4Attr(startup_ui.ipc5Value1,
                                    'li/ct/plc2/IP9_P', 'mbar')

    # setModel & others for the Main Screen Tab ---
    def setMainscreen(self):
        # following the synoptic regions from left to right and
        # from top to bottom
        self._setSplashScreenSubtask("Timing")
        self._setMainscreen_tb()
        self._setSplashScreenSubtask("Klystron High Voltage")
        self._setMainscreen_klystronHV()
        self._setSplashScreenSubtask("Radio Frequency")
        self._setMainscreen_rf()
        self._setSplashScreenSubtask("Cooling loops")
        self._setMainscreen_cl()
        self._setSplashScreenSubtask("KD")
        self._setMainscreen_kd()
        self._setSplashScreenSubtask("Magnets")
        self._setMainscreen_magnets()
        self._setSplashScreenSubtask("HVS")
        self._setMainscreen_hvs()
        self._setSplashScreenSubtask("Vacuum")
        self._setMainscreen_vacuum()
        self._setSplashScreenSubtask("Fluorescent screens")
        self._setMainscreen_fs()
        self._setSplashScreenSubtask("Beam Charge Monitors")
        self._setMainscreen_bcm()
        startup_ui = self.ui.linacMainscreenSynoptic._ui
        startup_ui.MainScreenSchematic.lower()

    def _setMainscreen_tb(self):
        mainscreen_ui = self.ui.linacMainscreenSynoptic._ui
        # tbKaDelay1
        self._setupTaurusLabel4Attr(mainscreen_ui.tbKaDelay1Value,
                                    'li/ct/plc1/TB_KA1_Delay', unit='us')
        self._setupSpinBox4Attr(mainscreen_ui.tbKaDelay1Setpoint,
                                'li/ct/plc1/TB_KA1_Delay', step=1)
        # tbKaDelay2
        self._setupTaurusLabel4Attr(mainscreen_ui.tbKaDelay2Value,
                                    'li/ct/plc1/TB_KA2_Delay', unit='ns')
        self._setupSpinBox4Attr(mainscreen_ui.tbKaDelay2Setpoint,
                                'li/ct/plc1/TB_KA2_Delay', step=32)
        # tbRf2Delay
        self._setupTaurusLabel4Attr(mainscreen_ui.tbRf2DelayValue,
                                    'li/ct/plc1/TB_RF2_Delay', unit='ns')
        # tbGunLevel
        self._setupTaurusLabel4Attr(mainscreen_ui.tbGunLevelValue,
                                    'li/ct/plc1/TB_GPA', unit='dB')
        self._setupSpinBox4Attr(mainscreen_ui.tbGunLevelSetpoint,
                                'li/ct/plc1/TB_GPA', step=0.1)
        # tbMultiBunch
        self._setupTaurusLabel4Attr(mainscreen_ui.tbMultiBunchValue,
                                    'li/ct/plc1/TB_MBM_status')
        self._setupCheckbox4Attr(mainscreen_ui.tbMultiBunchCheck,
                                 'li/ct/plc1/TB_MBM')
        self._operationModeMonitor = OperationModeManager(mainscreen_ui)
        # FIXME: the addValueNames fails in some versions of taurus,
        #        but it works in the control's room version
        # tbGatedPulse
        self._setupTaurusLabel4Attr(mainscreen_ui.tbGatedPulseModeValue,
                                    'li/ct/plc1/TB_GPM_status')
        try:
            self._setupCombobox4Attr(mainscreen_ui.tbGatedPulseModeCombo,
                                     'li/ct/plc1/TB_GPM',
                                     [('beam on', 0), ('mix', 1),
                                      ('beam off', 2)])
        except:
            mainscreen_ui.tbGatedPulseModeCombo.setEnabled(False)
        # tbGunDelay
        self._setupTaurusLabel4Attr(mainscreen_ui.tbGunDelayValue,
                                    'li/ct/plc1/TB_Gun_Delay', unit='ns')
        self._setupSpinBox4Attr(mainscreen_ui.tbGunDelaySetpoint,
                                'li/ct/plc1/TB_Gun_Delay', step=32)
        # tbWidth
        self._setupTaurusLabel4Attr(mainscreen_ui.tbWidthValue,
                                    'li/ct/plc1/TB_GPI', unit='ns')
        self._setupSpinBox4Attr(mainscreen_ui.tbWidthSetpoint,
                                'li/ct/plc1/TB_GPI', step=2)
        # tbNumber
        self._setupTaurusLabel4Attr(mainscreen_ui.tbNumberValue,
                                    'li/ct/plc1/TB_GPN')
        self._setupSpinBox4Attr(mainscreen_ui.tbNumberSetpoint,
                                'li/ct/plc1/TB_GPN', step=1)
        # tbTimerStatusStateLed
        self._setupLed4Attr(mainscreen_ui.tbTimerStatusStateLed,
                            'li/ct/plc1/TB_ST', offColor='white',
                            onColor='red')
        # rfEnb
        self._setupLed4Attr(mainscreen_ui.rfEnbLed, 'li/ct/plc1/RF_OK')

    def _setMainscreen_klystronHV(self):
        mainscreen_ui = self.ui.linacMainscreenSynoptic._ui
        klystrons = {1: {'readBack': {'widget': mainscreen_ui.klystron1HVRead,
                                      'attrName': 'li/ct/plc4/HVPS_V'},
                         'setpoint': {'widget': mainscreen_ui.klystron1HVWrite,
                                      'attrName':
                                      'li/ct/plc4/HVPS_V_setpoint',
                                      'dangerAbove': 32},
                         'rst': {'widget': mainscreen_ui.klystron1Rst,
                                 'attrName': 'li/ct/plc4/HVPS_Interlock_RC'},
                         'on': {'widget': mainscreen_ui.klystron1On,
                                'attrName': 'li/ct/plc4/HVPS_ONC'},
                         'led': mainscreen_ui.klystron1HVLed,
                         'check': mainscreen_ui.klystron1HVPopupCheck,
                         'widget': mainscreen_ui.klystron1HVPopupWidget},
                     2: {'readBack': {'widget': mainscreen_ui.klystron2HVRead,
                                      'attrName': 'li/ct/plc5/HVPS_V'},
                         'setpoint': {'widget': mainscreen_ui.klystron2HVWrite,
                                      'attrName':
                                      'li/ct/plc5/HVPS_V_setpoint',
                                      'dangerAbove': 27},
                         'rst': {'widget': mainscreen_ui.klystron2Rst,
                                 'attrName': 'li/ct/plc5/HVPS_Interlock_RC'},
                         'on': {'widget': mainscreen_ui.klystron2On,
                                'attrName': 'li/ct/plc5/HVPS_ONC'},
                         'led': mainscreen_ui.klystron2HVLed,
                         'check': mainscreen_ui.klystron2HVPopupCheck,
                         'widget': mainscreen_ui.klystron2HVPopupWidget}}
        self._klystronHV = {}
        self._klystronHVRamps = {}
        for number in klystrons.keys():
            # readback for the klystron HV ---
            widget = klystrons[number]['readBack']['widget']
            attrName = klystrons[number]['readBack']['attrName']
            self._setupTaurusLabel4Attr(widget, attrName, unit='kV')
            # setpoint for the klystron HV ---
            widget = klystrons[number]['setpoint']['widget']
            attrName = klystrons[number]['setpoint']['attrName']
            dangerAbove = klystrons[number]['setpoint']['dangerAbove']
            msg = "ALERT: this setpoint is above %gkV, the klystron %d " \
                  "operation high voltage user limit!" % (dangerAbove, number)
            self._setupSpinBox4Attr(widget, attrName, step=0.1,
                                    DangerMsg=msg, dangerAbove=dangerAbove)
            # on/off klystron HV ---
            widget = klystrons[number]['on']['widget']
            attrName = klystrons[number]['on']['attrName']
            self._setupActionWidget(widget, attrName, text='on/off')
            # reset klystron HV ---
            widget = klystrons[number]['rst']['widget']
            attrName = klystrons[number]['rst']['attrName']
            self._setupActionWidget(widget, attrName, text='Reset', isRst=True)
            # popup more information ---
            klystrons[number]['widget'].hide()
            widget = klystrons[number]['led']
            self._setupLed4Attr(widget, 'li/ct/plc%d/HVPS_ready' % (number+3))
            self._klystronHV[number] = \
                CheckboxManager(klystrons[number]['check'],
                                klystrons[number]['widget'],
                                "Klystron%dHVManager" % (number))
            widget = klystrons[number]['widget']._ui
            self._setupTaurusLabel4Attr(widget.hvStatusValue,
                                        'li/ct/plc%d/HVPS_Status' % (number+3))
            self._setupTaurusLabel4Attr(widget.hvCurrentValue,
                                        'li/ct/plc%d/HVPS_I' % (number+3),
                                        'mA')
            self._setupTaurusLabel4Attr(widget.hvVoltageValue,
                                        'li/ct/plc%d/HVPS_V' % (number+3),
                                        'kV')
            self._setupTaurusLabel4Attr(widget.hvSetpointValue,
                                        'li/ct/plc%d/HVPS_V_setpoint'
                                        % (number+3), 'kV')
            # FIXME: temporally disabled all the ramps
            button = widget.RampConfigurator
#             device = 'li/ct/plc%d' % (number+3)
#             title = "HVPS_V"
#             formAttrs = ["HVPS_V_setpoint_rampEnable",
#                          "HVPS_V_setpoint_ascending_step",
#                          "HVPS_V_setpoint_ascending_steptime",
#                          "HVPS_V_setpoint_ascending_threshold"]
#             plotAttrs  = ["HVPS_V", "HVPS_V_setpoint"]
#             self._klystronHVRamps[number] = \
#                 RampConfigurationWidget(button, device, title, formAttrs,
#                                         plotAttrs, self)
            button.setEnabled(False)
#            widget.hvRamp.hide()
#            widget.hvRampEnableLed.hide()
# #           self._setupLed4Attr(widget.hvRampEnableLed,
# #                               'li/ct/plc%d/HVPS_V_setpointRampEnable'
# #                               % (number+3))
#            widget.hvRampEnableCheck.hide()
# #           self._setupCheckbox4Attr(widget.hvRampEnableCheck,
# #                                    'li/ct/plc%d/HVPS_V_setpointRampEnable'
# #                                    % (number+3))
#            widget.hvRampStepLabel.hide()
#            widget.hvRampStepValue.hide()
# #           self._setupTaurusLabel4Attr(widget.hvRampStepValue,
# #                                       'li/ct/plc%d/HVPS_V_setpointStep'
# #                                       % (number+3),'kV')
#            widget.hvRampStepTimeLabel.hide()
#            widget.hvRampStepTimeValue.hide()
# #           self._setupTaurusLabel4Attr(widget.hvRampStepTimeValue,
# #                                       'li/ct/plc%d/HVPS_V_setpointStepTime'
# #                                       % (number+3), 's')
#            widget.hvRampThresholdLabel.hide()
#            widget.hvRampThresholdValue.hide()
# #           self._setupTaurusLabel4Attr(widget.hvRampThresholdValue,
# #                                       'li/ct/plc%d/'
# #                                       'HVPS_V_setpointThreshold'
# #                                       % (number+3), 'kV')
            bar = klystrons[number]['widget'].geometry()
            klystrons[number]['widget'].setGeometry(bar)
            # End section of the ramp widgets ---
            self._setupTaurusLabel4Attr(widget.pulseStatusValue,
                                        'li/ct/plc%d/Pulse_Status'
                                        % (number+3))
            self._setupTaurusLabel4Attr(widget.klystronVoltageValue,
                                        'li/ct/plc%d/Peak_V' % (number+3),
                                        'kV')
            self._setupTaurusLabel4Attr(widget.klystronCurrentValue,
                                        'li/ct/plc%d/Peak_I' % (number+3), 'A')

    def _setMainscreen_rf(self):
        mainscreen_ui = self.ui.linacMainscreenSynoptic._ui
        timePhaseShifters = {'0': {'read':
                                   mainscreen_ui.rfTimePhaseShifter0Value,
                                   'write':
                                   mainscreen_ui.rfTimePhaseShifter0Setpoint},
                             '1': {'read':
                                   mainscreen_ui.rfTimePhaseShifter1Value,
                                   'write':
                                   mainscreen_ui.rfTimePhaseShifter1Setpoint},
                             '2': {'read':
                                   mainscreen_ui.rfTimePhaseShifter2Value,
                                   'write':
                                   mainscreen_ui.rfTimePhaseShifter2Setpoint},
                             'X': {'read':
                                   mainscreen_ui.rfTimePhaseShifterXValue,
                                   'write':
                                   mainscreen_ui.rfTimePhaseShifterXSetpoint}}
        for timeShifter in timePhaseShifters.keys():
            attrName = 'li/ct/plc1/TPS%s_Phase' % (timeShifter)
            widget = timePhaseShifters[timeShifter]['read']
            self._setupTaurusLabel4Attr(widget, attrName)
            widget = timePhaseShifters[timeShifter]['write']
            if timeShifter in ['0']:
                self._setupSpinBox4Attr(widget, attrName, step=0.1)
            else:
                self._setupSpinBox4Attr(widget, attrName, step=1)
        #
        attrName = 'li/ct/plc1/A0_OP'
        widget = mainscreen_ui.rfA0OutputPowerValue
        self._setupTaurusLabel4Attr(widget, attrName, unit='W')
        widget = mainscreen_ui.rfA0OutputPowerSetpoint
        self._setupSpinBox4Attr(widget, attrName, step=1)
        #
        attrName = 'li/ct/plc1/RFS_ST'
        widget = mainscreen_ui.rfA0StatusLed
        self._setupLed4Attr(widget, attrName)
        #
        attrName = 'li/ct/plc1/ATT2_P'
        widget = mainscreen_ui.attenuator2Value
        self._setupTaurusLabel4Attr(widget, attrName, unit='dB')
        widget = mainscreen_ui.attenuator2Setpoint
        self._setupSpinBox4Attr(widget, attrName+'_setpoint', step=0.1)
        #
        phaseShifters = {'1': {'read': mainscreen_ui.rfPhaseShifter1Value,
                               'write': mainscreen_ui.rfPhaseShifter1Setpoint,
                               'led': mainscreen_ui.phaseShifter1Led,
                               'check': mainscreen_ui.phaseShifter1PopupCheck,
                               'widget':
                               mainscreen_ui.phaseShifter1PopupWidget},
                         '2': {'read': mainscreen_ui.rfPhaseShifter2Value,
                               'write': mainscreen_ui.rfPhaseShifter2Setpoint,
                               'led': mainscreen_ui.phaseShifter2Led,
                               'check': mainscreen_ui.phaseShifter2PopupCheck,
                               'widget':
                               mainscreen_ui.phaseShifter2PopupWidget}}
        for shifter in phaseShifters.keys():
            attrName = 'li/ct/plc1/PHS%s_Phase' % (shifter)
            widget = phaseShifters[shifter]['read']
            self._setupTaurusLabel4Attr(widget, attrName)
            widget = phaseShifters[shifter]['write']
            self._setupSpinBox4Attr(widget, attrName+'_setpoint', step=1)
        #
        sf6pressures = {'1': mainscreen_ui.sf6p1Value,
                        '2': mainscreen_ui.sf6p2Value}
        for pressure in sf6pressures.keys():
            attrName = 'li/ct/plc1/SF6_P%s' % (pressure)
            self._setupTaurusLabel4Attr(sf6pressures[pressure], attrName,
                                        'bar')
        self._setupLed4Attr(mainscreen_ui.rfSourceStatusLed,
                            'li/ct/plc1/RFS_ST')
        # popups
        self._setupLed4Attr(mainscreen_ui.attenuatorLed,
                            'li/ct/plc1/ATT2_ready')
        mainscreen_ui.attenuatorPopupWidget.hide()
        self._attenuator = CheckboxManager(mainscreen_ui.attenuatorPopupCheck,
                                           mainscreen_ui.attenuatorPopupWidget,
                                           "Attenuator2")
        widget = mainscreen_ui.attenuatorPopupWidget._ui
        widget.attenuatorGroup.setTitle("Attenuator 2")
        self._setupTaurusLabel4Attr(widget.statusValue,
                                    'li/ct/plc1/ATT2_Status')
        self._setupTaurusLabel4Attr(widget.AttrValue, 'li/ct/plc1/ATT2_P',
                                    'dB')
        self._phaseShifters = {}
        for shifter in phaseShifters.keys():
            phaseShifters[shifter]['widget'].hide()
            self._setupLed4Attr(phaseShifters[shifter]['led'],
                                'li/ct/plc1/PHS%s_ready' % (shifter))
            self._phaseShifters[shifter] = \
                CheckboxManager(phaseShifters[shifter]['check'],
                                phaseShifters[shifter]['widget'],
                                "PhaseShifter%s" % (shifter))
            widget = phaseShifters[shifter]['widget']._ui
            widget.phaseShifterGroup.setTitle("Phase Shifter %s" % shifter)
            self._setupTaurusLabel4Attr(widget.statusValue,
                                        'li/ct/plc1/PHS%s_Status' % shifter)
            self._setupTaurusLabel4Attr(widget.attrValue,
                                        'li/ct/plc1/PHS%s_Phase' % shifter)

    def _setMainscreen_cl(self):
        mainscreen_ui = self.ui.linacMainscreenSynoptic._ui
        coolingLoops = {1: mainscreen_ui.coolingLoop1Led,
                        2: mainscreen_ui.coolingLoop2Led,
                        3: mainscreen_ui.coolingLoop3Led}
        for loop in coolingLoops.keys():
            attrName = 'li/ct/plc2/CL%s_ONC' % (loop)
            self._setupLed4Attr(coolingLoops[loop], attrName)

    def _setMainscreen_kd(self):
        mainscreen_ui = self.ui.linacMainscreenSynoptic._ui
        self._setupTaurusLabel4Attr(mainscreen_ui.cathodeCurrent,
                                    'li/ct/plc1/GUN_Kathode_V', 'V')
        self._setupTaurusLabel4Attr(mainscreen_ui.filamentCurrent,
                                    'li/ct/plc1/GUN_Filament_I', 'A')
        self._setupTaurusLabel4Attr(mainscreen_ui.temperatureValue,
                                    'li/ct/plc1/GUN_Kathode_T', 'C')

    def _setMainscreen_magnets(self):
        mainscreen_ui = self.ui.linacMainscreenSynoptic._ui
        magnets = {'sl1': {'info': mainscreen_ui.sl1LedInfo,
                           'check': mainscreen_ui.sl1PopupCheck,
                           'widget': mainscreen_ui.sl1PopupWidget,
                           'h': mainscreen_ui.sl1hValue,
                           'v': mainscreen_ui.sl1vValue,
                           'f': mainscreen_ui.sl1fValue,
                           'on': mainscreen_ui.sl1On},
                   'sl2': {'info': mainscreen_ui.sl2LedInfo,
                           'check': mainscreen_ui.sl2PopupCheck,
                           'widget': mainscreen_ui.sl2PopupWidget,
                           'h': mainscreen_ui.sl2hValue,
                           'v': mainscreen_ui.sl2vValue,
                           'f': mainscreen_ui.sl2fValue,
                           'on': mainscreen_ui.sl2On},
                   'sl3': {'info': mainscreen_ui.sl3LedInfo,
                           'check': mainscreen_ui.sl3PopupCheck,
                           'widget': mainscreen_ui.sl3PopupWidget,
                           'h': mainscreen_ui.sl3hValue,
                           'v': mainscreen_ui.sl3vValue,
                           'f': mainscreen_ui.sl3fValue,
                           'on': mainscreen_ui.sl3On},
                   'sl4': {'info': mainscreen_ui.sl4LedInfo,
                           'check': mainscreen_ui.sl4PopupCheck,
                           'widget': mainscreen_ui.sl4PopupWidget,
                           'h': mainscreen_ui.sl4hValue,
                           'v': mainscreen_ui.sl4vValue,
                           'f': mainscreen_ui.sl4fValue,
                           'on': mainscreen_ui.sl4On},
                   'bc1': {'info': mainscreen_ui.bc1LedInfo,
                           'check': mainscreen_ui.bc1PopupCheck,
                           'widget': mainscreen_ui.bc1PopupWidget,
                           'h': mainscreen_ui.bc1hValue,
                           'v': mainscreen_ui.bc1vValue,
                           'f': mainscreen_ui.bc1fValue,
                           'on': mainscreen_ui.bc1On},
                   'bc2': {'info': mainscreen_ui.bc2LedInfo,
                           'check': mainscreen_ui.bc2PopupCheck,
                           'widget': mainscreen_ui.bc2PopupWidget,
                           'h': mainscreen_ui.bc2hValue,
                           'v': mainscreen_ui.bc2vValue,
                           'f': mainscreen_ui.bc2fValue,
                           'on': mainscreen_ui.bc2On},
                   'gl': {'info': mainscreen_ui.glLedInfo,
                          'check': mainscreen_ui.glPopupCheck,
                          'widget': mainscreen_ui.glPopupWidget,
                          'h': mainscreen_ui.glhValue,
                          'v': mainscreen_ui.glvValue,
                          'f': mainscreen_ui.glfValue,
                          'on': mainscreen_ui.glOn},
                   'as1': {'info': mainscreen_ui.as1LedInfo,
                           'check': mainscreen_ui.as1PopupCheck,
                           'widget': mainscreen_ui.as1PopupWidget,
                           'h': mainscreen_ui.as1hValue,
                           'v': mainscreen_ui.as1vValue,
                           'on': mainscreen_ui.as1On},
                   'qt': {'info': mainscreen_ui.qtLedInfo,
                          'on': mainscreen_ui.qtOn,
                          '1h': mainscreen_ui.qt1hValue,
                          '1v': mainscreen_ui.qt1vValue,
                          '1f': mainscreen_ui.qt1fValue,
                          '2f': mainscreen_ui.qt2fValue,
                          'check': mainscreen_ui.qtPopupCheck,
                          'widget': mainscreen_ui.qtPopupWidget},
                   'as2': {'info': mainscreen_ui.as2LedInfo,
                           'check': mainscreen_ui.as2PopupCheck,
                           'widget': mainscreen_ui.as2PopupWidget,
                           'h': mainscreen_ui.as2hValue,
                           'v': mainscreen_ui.as2vValue,
                           'on': mainscreen_ui.as2On},
                   }
        self._magnets = {}
        for magnet in magnets.keys():
            deviceName = 'li/ct/plc3'
            if 'info' in magnets[magnet]:
                widget = magnets[magnet]['info']
                attrName = '%s/%s_current_ok' % (deviceName, magnet)
                self._setupLed4Attr(widget, attrName)
            # horizontal magnets
            if 'h' in magnets[magnet]:
                widget = magnets[magnet]['h']
                attrName = '%s/%sh_I_setpoint' % (deviceName, magnet)
                self._setupSpinBox4Attr(widget, attrName, step=0.01)
            if '1h' in magnets[magnet]:
                widget = magnets[magnet]['1h']
                attrName = '%s/%s1h_I_setpoint' % (deviceName, magnet)
                self._setupSpinBox4Attr(widget, attrName, step=0.01)
            # vertical magnets
            if 'v' in magnets[magnet]:
                widget = magnets[magnet]['v']
                attrName = '%s/%sv_I_setpoint' % (deviceName, magnet)
                self._setupSpinBox4Attr(widget, attrName, step=0.01)
            if '1v' in magnets[magnet]:
                widget = magnets[magnet]['1v']
                attrName = '%s/%s1v_I_setpoint' % (deviceName, magnet)
                self._setupSpinBox4Attr(widget, attrName, step=0.01)
            # focus magnets
            if 'f' in magnets[magnet]:
                widget = widget = magnets[magnet]['f']
                attrName = '%s/%sf_I_setpoint' % (deviceName, magnet)
                self._setupSpinBox4Attr(widget, attrName, step=0.01)
            if '1f' in magnets[magnet]:
                widget = widget = magnets[magnet]['1f']
                attrName = '%s/%s1f_I_setpoint' % (deviceName, magnet)
                self._setupSpinBox4Attr(widget, attrName, step=0.005)
            if '2f' in magnets[magnet]:
                widget = widget = magnets[magnet]['2f']
                attrName = '%s/%s2f_I_setpoint' % (deviceName, magnet)
                self._setupSpinBox4Attr(widget, attrName, step=0.005)
            # power on/off magnets
            if 'on' in magnets[magnet]:
                widget = magnets[magnet]['on']
                attrName = '%s/%s_onc' % (deviceName, magnet)
                self._setupActionWidget(widget, attrName, text='on/off')
            # pops up for more information
            if 'check' in magnets[magnet] and 'widget' in magnets[magnet]:
                # popup with more magnet information ---
                magnets[magnet]['widget'].hide()
                button = magnets[magnet]['check']
                widget = magnets[magnet]['widget']
                title = "%s" % (magnet)
                self._magnets[magnet] = CheckboxManager(button, widget,
                                                        title.upper())
                # information with in the popup ---
                widget = magnets[magnet]['widget']._ui
                self._setupContentsInMagnetPopup(deviceName, magnet,
                                                 magnets[magnet], widget)
        # Reset magnets interlocks ---
        widget = mainscreen_ui.magnetsRst
        attrName = 'li/ct/plc3/MA_Interlock_RC'
        self._setupActionWidget(widget, attrName, text='Magnets\nReset',
                                isRst=True)
        # on/off all the magnets ---
        widget = mainscreen_ui.magnetsOn
        attrName = 'li/ct/plc3/all_onc'
        self._setupActionWidget(widget, attrName, text='on/off')

    def _setupContentsInMagnetPopup(self, devName, magnetName, contentsDict,
                                    widget):
        widget.magnetGroup.setTitle(magnetName)
        if 'h' in contentsDict or '1h' in contentsDict:
            if 'h' in contentsDict:
                magnetType = 'h'
            elif '1h' in contentsDict:
                magnetType = '1h'
            self._setupMagnetLine(devName, magnetName, magnetType,
                                  widget.horizontalLabel,
                                  widget.horizontalValue,
                                  widget.horizontalStatus)
        else:
            self._hideMagnetLine(widget.horizontalLabel,
                                 widget.horizontalValue,
                                 widget.horizontalStatus)
        if 'v' in contentsDict or '1v' in contentsDict:
            if 'v' in contentsDict:
                magnetType = 'v'
            elif '1v' in contentsDict:
                magnetType = '1v'
            self._setupMagnetLine(devName, magnetName, magnetType,
                                  widget.verticalLabel,
                                  widget.verticalValue,
                                  widget.verticalStatus)
        else:
            self._hideMagnetLine(widget.verticalLabel,
                                 widget.verticalValue,
                                 widget.verticalStatus)
        if 'f' in contentsDict or '1f' in contentsDict:
            if 'f' in contentsDict:
                magnetType = 'f'
            elif '1f' in contentsDict:
                magnetType = '1f'
            self._setupMagnetLine(devName, magnetName, magnetType,
                                  widget.focusLabel,
                                  widget.focusValue,
                                  widget.focusStatus)
        else:
            self._hideMagnetLine(widget.focusLabel,
                                 widget.focusValue,
                                 widget.focusStatus)
        if '2f' in contentsDict:
            magnetType = '2f'
            self._setupMagnetLine(devName, magnetName, magnetType,
                                  widget.focus2Label,
                                  widget.focus2Value,
                                  widget.focus2Status)
        else:
            self._hideMagnetLine(widget.focus2Label,
                                 widget.focus2Value,
                                 widget.focus2Status)

    def _setupMagnetLine(self, deviceName, magnetName, magnetAxis,
                         label, value, status):
        label.setText("%s%s" % (magnetName.upper(), magnetAxis.upper()))
        self._setupTaurusLabel4Attr(value, '%s/%s%s_I'
                                    % (deviceName, magnetName, magnetAxis),
                                    'A')
        self._setupTaurusLabel4Attr(status, '%s/%s%s_Status'
                                    % (deviceName, magnetName, magnetAxis))

    def _hideMagnetLine(self, label, value, status):
        label.hide()
        value.hide()
        status.hide()

    def _setMainscreen_hvs(self):
        mainscreen_ui = self.ui.linacMainscreenSynoptic._ui
        self._setupTaurusLabel4Attr(mainscreen_ui.eGunHVStatus,
                                    'li/ct/plc1/Gun_HV_Status')
        self._setupTaurusLabel4Attr(mainscreen_ui.eGunHVValue,
                                    'li/ct/plc1/GUN_HV_V', 'kV')
        self._setupSpinBox4Attr(mainscreen_ui.hvsVoltageValue,
                                'li/ct/plc1/GUN_HV_V_setpoint', step=0.1)
        self._setupTaurusLabel4Attr(mainscreen_ui.hvsCurrentValue,
                                    'li/ct/plc1/GUN_HV_I', 'uA')
        # on/off the HVS ---
        widget = mainscreen_ui.hvsOn
        attrName = 'li/ct/plc1/gun_hv_onc'
        self._setupActionWidget(widget, attrName, text='on/off')
        # popup with extra information ---
        widget = mainscreen_ui.hvsLed
        attrName = 'li/ct/plc1/Gun_HV_ready'
        self._setupLed4Attr(widget, attrName, offColor='red')
        mainscreen_ui.hvsPopupWidget.hide()
        self._hvs = CheckboxManager(mainscreen_ui.hvsPopupCheck,
                                    mainscreen_ui.hvsPopupWidget, "HVS")
        widget = mainscreen_ui.hvsPopupWidget._ui
        self._setupLed4Attr(widget.doorInterlockLed, 'li/ct/plc1/gm_di')
        # widget = mainscreen_ui.AutostopperTrigger
        attrName = "li/ct/plc1/GUN_HV_I_AutoStop_Triggered"
        self._setupLed4Attr(widget.AutostopperTriggerLed, attrName,
                            onColor='red', offColor='green')
        # ramp configuration
        # FIXME: temporally disabled all the ramps
        button = widget.RampConfigurator
#         device = 'li/ct/plc1'
#         title = "GUN_HV_V"
#         formAttrs = ["GUN_HV_V_setpoint_rampEnable",
# #                     "GUN_HV_V_setpoint_ascending_step",
# #                     "GUN_HV_V_setpoint_ascending_steptime",
# #                     "GUN_HV_V_setpoint_ascending_threshold",
#                      "GUN_HV_V_setpoint_descending_step",
#                      "GUN_HV_V_setpoint_descending_steptime",
#                      "GUN_HV_V_setpoint_descending_threshold"]
#         plotAttrs = ["GUN_HV_V", "GUN_HV_V_setpoint"]
#         self._eGunHVRamp = RampConfigurationWidget(button, device, title,
#                                                    formAttrs, plotAttrs,
#                                                    self)
        button.setEnabled(False)
        # autostop configuration
        button = widget.AutoStopConfiguration
        device = 'li/ct/plc1'
        attributes = ["GUN_HV_I",
                      "GUN_HV_I_AutoStop_Below_Threshold",
                      "GUN_HV_I_AutoStop_IntegrationTime",
                      "GUN_HV_I_AutoStop_Enable",
                      "GUN_HV_I_AutoStop_Mean",
                      "GUN_HV_I_AutoStop_Std",
                      "GUN_HV_I_AutoStop_Triggered",
                      "GUN_HV_I_AutoStop"]
        redLeds = ["GUN_HV_I_AutoStop_Triggered"]
        self._filamentAutoStop = \
            AutoStopConfigurationWidget(button, device, attributes, self,
                                        redLedAttrs=redLeds)

    def _setMainscreen_vacuum(self):
        mainscreen_ui = self.ui.linacMainscreenSynoptic._ui
        # collimator valve ---
        attrName = 'li/ct/plc2/VCV_Status'
        widget = mainscreen_ui.vacuumCollimatorValveOnStatus
        self._setupTaurusLabel4Attr(widget, attrName)
        attrName = 'li/ct/plc2/VCV_ONC'
        widget = mainscreen_ui.vcvOnLedInfo
        self._setupLed4Attr(widget, attrName)
        # attrName = 'li/ct/plc2/VCV_ONC'
        widget = mainscreen_ui.vcvOn
        self._setupActionWidget(widget, attrName,
                                text='collimator\nopen/close')
        vacuumCavities = {'eGun': {'check': mainscreen_ui.eGunVacuumCheck,
                                   'widget': mainscreen_ui.eGunVacuumWidget,
                                   'hvg': 'li/ct/plc2/HVG1_P',
                                   'ipA': 'IP1',
                                   'ipB': 'IP2'},
                          'preBuncher': {'check':
                                         mainscreen_ui.preBuncherVacuumCheck,
                                         'widget':
                                         mainscreen_ui.preBuncherVacuumWidget,
                                         'hvg': 'li/ct/plc2/HVG2_P',
                                         'ipA': 'IP3'},
                          'buncher': {'check':
                                      mainscreen_ui.buncherVacuumCheck,
                                      'widget':
                                      mainscreen_ui.buncherVacuumWidget,
                                      'hvg': 'li/ct/plc2/HVG3_P',
                                      'ipA': 'IP4',
                                      'ipB': 'IP5'},
                          'as1': {'check': mainscreen_ui.as1VacuumCheck,
                                  'widget': mainscreen_ui.as1VacuumWidget,
                                  'hvg': 'li/ct/plc2/HVG4_P',
                                  'ipA': 'IP6',
                                  'ipB': 'IP7'},
                          'as2': {'check': mainscreen_ui.as2VacuumCheck,
                                  'widget': mainscreen_ui.as2VacuumWidget,
                                  'hvg': 'li/ct/plc2/HVG5_P',
                                  'ipA': 'IP8',
                                  'ipB': 'IP9'}}
        self._vacuumCavities = {}
        for cavity in vacuumCavities.keys():
            check = vacuumCavities[cavity]['check']
            widget = vacuumCavities[cavity]['widget']
            widget.hide()
            self._vacuumCavities[cavity] = CheckboxManager(check, widget)
            widget._ui.vacuumGroup.setTitle(cavity)
            hvg = vacuumCavities[cavity]['hvg']
            self._setupTaurusLabel4Attr(widget._ui.HVGValue, hvg, 'mbar')
            if 'ipA' in vacuumCavities[cavity]:
                ipA = vacuumCavities[cavity]['ipA']
                widget._ui.IonPumpALabel.setText(ipA)
                self._setupLed4Attr(widget._ui.IonPumpALed,
                                    'li/ct/plc2/%s_IS' % (ipA))
            else:
                widget._ui.IonPumpALabel.hide()
                widget._ui.IonPumpALed.hide()
            if 'ipB' in vacuumCavities[cavity]:
                ipB = vacuumCavities[cavity]['ipB']
                widget._ui.IonPumpBLabel.setText(ipB)
                self._setupLed4Attr(widget._ui.IonPumpBLed,
                                    'li/ct/plc2/%s_IS' % (ipB))
            else:
                widget._ui.IonPumpBLabel.hide()
                widget._ui.IonPumpBLed.hide()
        # The led at the end of the linac about the vacuum valve
        widget = mainscreen_ui.vacuumValve7OnLedInfo
        attrName = 'li/ct/plc2/VV7_OC'
        self._setupLed4Attr(widget, attrName)
        # The led at the end of the linac about the LT vacuum state.
        widget = mainscreen_ui.tl_vokLedInfo
        attrName = 'li/ct/plc1/TL_VOK'
        self._setupLed4Attr(widget, attrName)

    def _setMainscreen_fs(self):
        mainscreen_ui = self.ui.linacMainscreenSynoptic._ui
        fluorescentScreens = \
            {1: {'valve': {'widget': mainscreen_ui.fluorescentScreen1Valve,
                           'attrName': 'li/ct/plc1/SCM1_DC'},
                 'light': {'widget': mainscreen_ui.fluorescentScreen1Light,
                           'attrName': 'li/ct/plc1/SCM1_LC'},
                 'status': {'led': mainscreen_ui.sm1Led,
                            'widget': mainscreen_ui.fluorescentScreen1Status,
                            'attrName': 'li/ct/plc1/SCM1_Status'},
                 'view': {'widget': mainscreen_ui.fluorescentScreen1View,
                          'attrName': 'li/di/fs-01'}},
             2: {'valve': {'widget': mainscreen_ui.fluorescentScreen2Valve,
                           'attrName': 'li/ct/plc1/SCM2_DC'},
                 'light': {'widget': mainscreen_ui.fluorescentScreen2Light,
                           'attrName': 'li/ct/plc1/SCM2_LC'},
                 'status': {'led': mainscreen_ui.sm2Led,
                            'widget': mainscreen_ui.fluorescentScreen2Status,
                            'attrName': 'li/ct/plc1/SCM2_Status'},
                 'view': {'widget': mainscreen_ui.fluorescentScreen2View,
                          'attrName': 'li/di/fs-02'}},
             3: {'valve': {'widget': mainscreen_ui.fluorescentScreen3Valve,
                           'attrName': 'li/ct/plc1/SCM3_DC'},
                 'light': {'widget': mainscreen_ui.fluorescentScreen3Light,
                           'attrName': 'li/ct/plc1/SCM3_LC'},
                 'status': {'led': mainscreen_ui.sm3Led,
                            'widget': mainscreen_ui.fluorescentScreen3Status,
                            'attrName': 'li/ct/plc1/SCM3_Status'},
                 'view': {'widget': mainscreen_ui.fluorescentScreen3View,
                          'attrName': 'li/di/fs-03'}}}
        self._fluorescentScreensViewButtons = []
        for fs in fluorescentScreens.keys():
            for element in fluorescentScreens[fs].keys():
                if element in ['valve', 'light']:
                    widget = fluorescentScreens[fs][element]['widget']
                    attrName = fluorescentScreens[fs][element]['attrName']
                    if element == 'valve':
                        text = 'in/out'
                        self._setupActionWidget(widget, attrName, text,
                                                isValve=True)
                    else:
                        text = 'on/off'
                        self._setupActionWidget(widget, attrName, text,
                                                isLight=True)
                elif element == 'status':
                    widget = fluorescentScreens[fs][element]['led']
                    attrName = 'li/ct/plc1/SCM%d_alert' % (fs)
                    self._setupLed4Attr(widget, attrName, onColor='red',
                                        offColor='green', blinkOnChange='on')
                    widget = fluorescentScreens[fs][element]['widget']
                    attrName = fluorescentScreens[fs][element]['attrName']
                    self._setupTaurusLabel4Attr(widget, attrName)
                elif element == 'view':
                    button = fluorescentScreens[fs][element]['widget']
                    attrName = fluorescentScreens[fs][element]['attrName']
                    listener = ViewButtonListener(button, attrName)
                    self._fluorescentScreensViewButtons.append(listener)

    def _setMainscreen_bcm(self):
        bcm = self.ui.linacMainscreenSynoptic._ui.beamChargeMonitors._ui
        self._setupTaurusLabel4Attr(bcm.liValue, 'li/di/bcm-01/charge',
                                    unit='nC')
        self._setupTaurusLabel4Attr(bcm.lt01Value, 'lt01/di/bcm-01/charge',
                                    unit='nC')
        self._setupTaurusLabel4Attr(bcm.lt02Value, 'lt02/di/bcm-01/charge',
                                    unit='nC')

    # Configure the access to external applications ---
    def setExternalApplications(self):
        self._setSplashScreenSubtask("ctpcgrid")
        lt_magnets = ExternalAppAction(['ctpcgrid', 'lt'], text="LT magnets")
        self.addExternalAppLauncher(lt_magnets)
        self._setSplashScreenSubtask("ctdiccd")
        mach_ccds = ExternalAppAction(['ctdiccd'], text="CCDs")
        self.addExternalAppLauncher(mach_ccds)
        self._setSplashScreenSubtask("Save and retrieve")
        saveretrieve = ExternalAppAction(['ctlisetup'], text="save/retrieve")
        self.addExternalAppLauncher(saveretrieve)

    def setStatusBar(self):
        # PLCs state leds in the statusBar ---
        for i in range(1, 6):
            self._setSplashScreenSubtask("Status Bar")
            stateLed = TaurusLed(self)
            stateLed.setModel('li/ct/plc%d/state' % (i))
#             stateLed.setStyleSheet(stylesheet)
            stateText = QtGui.QLabel(self)
            stateText.setText("PLC%d" % (i))
#             stateText.setStyleSheet(stylesheet)
            self.statusBar().addWidget(stateLed)
            self.statusBar().addWidget(stateText)
        separator = QtGui.QLabel(self)
        separator.setText(" "*10)
#         separator.setStyleSheet(stylesheet)
        self.statusBar().addWidget(separator)
        # Linac's IU ready to the status bar ---
        self._setSplashScreenSubtask("Linac IU ready")
        iuLed = TaurusLed(self)
        self._setupLed4Attr(iuLed, 'LI/CT/ALARM/LI_INTERLOCK_UNIT',
                            onColor='red', offColor='green')
#         iuLed.setStyleSheet(stylesheet)
        iuText = QtGui.QLabel(self)
        iuText.setText("Interlock Alarm")
#         iuText.setStyleSheet(stylesheet)
        self.statusBar().addWidget(iuLed)
        self.statusBar().addWidget(iuText)

    def setMenuOptions(self):
        self.perspectivesToolBar.clear()
        self._setSplashScreenSubtask("Plot events info")
        self.setToolsMenu(self.toolsMenu)
        self.setHelpMenu(self.helpMenu)

    def setToolsMenu(self, toolsMenu):
        # Access to preconfigured trends ---
        self.taurustrendLauncherAction = \
            Qt.QAction('Preconfigured trends', self)
        Qt.QObject.connect(self.taurustrendLauncherAction,
                           Qt.SIGNAL("triggered()"),
                           self.taurustrendLauncher)
        toolsMenu.addAction(self.taurustrendLauncherAction)
        # View the values of the EVR300 ---
        self.EVR300Action = Qt.QAction("EVR300", self)
        Qt.QObject.connect(self.EVR300Action, Qt.SIGNAL("triggered()"),
                           self.EVR300Launcher)
        self.toolsMenu.addAction(self.EVR300Action)
        # Enumeration attributes configuration ---
        self.CompomentAction = Qt.QAction("Linac Components Settings", self)
        Qt.QObject.connect(self.CompomentAction, Qt.SIGNAL("triggered()"),
                           self.CompomentLauncher)
        self.toolsMenu.addAction(self.CompomentAction)
        # Controls submenu ---
        self.setControlsToolsSubmenu(self.toolsMenu)
        # Reset write widgets blue value
        self.ResetAction = Qt.QAction("Reset writable values", self)
        Qt.QObject.connect(self.ResetAction, Qt.SIGNAL("triggered()"),
                           self.ResetLauncher)
        self.toolsMenu.addAction(self.ResetAction)

    def setHelpMenu(self, helpMenu):
        # Access to Linac's accelerators documentation ---
        self.LinacDocsAction = Qt.QAction("Linac's documentation", self)
        Qt.QObject.connect(self.LinacDocsAction, Qt.SIGNAL("triggered()"),
                           self.LinacDocsLauncher)
        helpMenu.addAction(self.LinacDocsAction)

    def setControlsToolsSubmenu(self, menu):
        controlsMenu = menu.addMenu("Controls")
        # Plot events info ---
        self.eventsPlotAction = Qt.QAction('Plot events info', self)
        Qt.QObject.connect(self.eventsPlotAction, Qt.SIGNAL("triggered()"),
                           self.plotEventsInfo)
        controlsMenu.addAction(self.eventsPlotAction)

    def plotEventsInfo(self):
        if not hasattr(self, '_eventPlotWindow') or \
                self._eventPlotWindow is None:
            self._eventPlotWindow = DevicesEvents()
            attributes = ['EventsNumber', 'EventsTime']
            widgets = {1: self._eventPlotWindow._ui.eventsplc1,
                       2: self._eventPlotWindow._ui.eventsplc2,
                       3: self._eventPlotWindow._ui.eventsplc3,
                       4: self._eventPlotWindow._ui.eventsplc4,
                       5: self._eventPlotWindow._ui.eventsplc5}
            for i in widgets.keys():
                widget = widgets[i]
                device = "%s%d" % (LinacDeviceNameRoot, i)
                widget.setModel(device)
        self._eventPlotWindow.show()

    def taurustrendLauncher(self):
        """Provide the user with a dialog to a default directory where some
           preconfigured trends are save to select one. Then launch a system
           process like if the user executes it from the console.
        """
        fileName = self._requestPreconfigFileName()
        self.info("Receive a request to launch a taurustrend with the %r "
                  "configuration file" % (fileName))
        cmd = "taurustrend"
        args = "--config=%s" % (fileName)
        self.info("Ready to launch the command: %r with args %r" % (cmd, args))
        subprocess.Popen([cmd, args])  # Don't use 'call' because it's blocking
        # FIXME: if the command fails, there is no way to report the user!

    def LinacDocsLauncher(self):
        """
            Provide access to the directory where accelerators stores
            information about the Linac.
            Important: this is accelerators information
        """
        cmd = "dolphin"
        args = "/data/LINAC/Documentation"
        self.info("Ready to launch the command: %r with args %r" % (cmd, args))
        subprocess.Popen([cmd, args])

    def EVR300Launcher(self):
        if not hasattr(self, '_evr300Window') or self._evr300Window is None:
            self._evr300Window = EVR300()
            self._evr300Window.setModel('li/ti/evr300-cli0302-a')
        self._evr300Window.show()

    def CompomentLauncher(self):
        if not hasattr(self, '_compomentWindow') or\
                self._compomentWindow is None:
            self._compomentWindow = CompomentsWindow()
        self._compomentWindow.show()

    def ResetLauncher(self):
        for widget in self._readwriteWidgets:
            try:
                widget.resetPendingOperations()
            except Exception as e:
                self.error("Couldn't reset pending operations on %s"
                           % (widget.getLogName()))

    def _requestPreconfigFileName(self):
        dialogTitle = "Select preconfigured taurustrend"
        filters = "Taurustrend preconfig (*.pck);;All files (*)"
        fileName = \
            QtGui.QFileDialog.getOpenFileName(self, dialogTitle,
                                              defaultPreconfTrends,
                                              filters)
        return str(fileName)


class CheckboxManager(TaurusBaseComponent, Qt.QObject):
    '''
        First approach to the Labview blinking leds with
        subboxes of sets of attrs.
    '''
    # TODO: instead of checkboxes them should be leds with a composition of the
    #       internal values in the subbox
    def __init__(self, checker, widget, name=None, qt_parent=None,
                 designMode=False):
        if not name:
            name = "CheckboxManager"
        self.call__init__wo_kw(Qt.QObject, qt_parent)
        self.call__init__(TaurusBaseComponent, name, designMode=designMode)
        self._checker = checker
        self._widget = widget
        Qt.QObject.connect(self._checker, Qt.SIGNAL('clicked(bool)'),
                           self._checkboxChanged)
        self.debug("Build the checkbox manager")

    def _checkboxChanged(self, checked):
        if self._checker.isChecked():
            self._widget.show()
        else:
            self._widget.hide()


class HistoryWidgetManager(TaurusBaseComponent, Qt.QWidget):
    def __init__(self, button, attrName, mainWindow, name=None,
                 qt_parent=None, designMode=False):
        if not name:
            name = "HistoryWidgetManager"
        self.call__init__wo_kw(Qt.QWidget, qt_parent)
        self.call__init__(TaurusBaseComponent, name, designMode=designMode)
        self._attrName = attrName
        self._mainWindow = mainWindow
        self._dockwidget = None
        self._table = None
        Qt.QObject.connect(button, Qt.SIGNAL("clicked(bool)"),
                           self._clicked)
        self.debug("Build a dock widget launcher for %s" % (self._attrName))

    def _clicked(self, checked):
        try:
            if self._dockwidget is None:
                self._dockwidget = QtGui.QDockWidget(self._attrName, self)
                # FIXME: check what's need and what can be excluded
                self._dockwidget.\
                    setFeatures(QtGui.QDockWidget.DockWidgetClosable
                                | QtGui.QDockWidget.DockWidgetMovable
                                | QtGui.QDockWidget.DockWidgetFloatable)
                self._dockwidget.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
                self._dockwidget.setWindowTitle(self._attrName)
                Qt.QObject.connect(self._dockwidget,
                                   Qt.SIGNAL('visibilityChanged(bool)'),
                                   self._close)
                self._mainWindow.addDockWidget(QtCore.Qt.LeftDockWidgetArea,
                                               self._dockwidget)
            if self._table is None:
                self._table = TaurusValuesTable()
                self._table.setModel(self._attrName)
                self._table._applyBT.setVisible(False)
                self._table._cancelBT.setVisible(False)
                self._table._rwModeCB.setVisible(False)
                self._dockwidget.setWidget(self._table)
            self._dockwidget.show()
            self.debug("Showing a dock widget for attribute %s"
                       % (self._attrName))
        except Exception as e:
            self.error("Error when click to open the %s dockwidget: %s"
                       % (self._attrName, e))
            traceback.print_exc()

    def _close(self, visible):
        if not visible:
            self.info("Close the dock widget for %s" % (self._attrName))
            # self._dockwidget.setWidget(None)
            # self._table = None
            # self._mainWindow.removeDockWidget(self._dockwidget)


class RampConfigurationWidget(TaurusBaseComponent, Qt.QWidget):
    def __init__(self, button, devicaName, title, formAttrs, plotAttrs,
                 mainWindow, name=None, qt_parent=None, designMode=False):
        if not name:
            name = "RampConfigurationWidget"
        self.call__init__wo_kw(Qt.QWidget, qt_parent)
        self.call__init__(TaurusBaseComponent, name, designMode=designMode)
        self._devicaName = devicaName
        self._title = title
        self._formAttrs = formAttrs
        self._plotAttrs = plotAttrs
        self._mainWindow = mainWindow
        self._dockwidget = None
        self._widget = None
        Qt.QObject.connect(button, Qt.SIGNAL("clicked(bool)"),
                           self._clicked)
        self.debug("Build a dock widget launcher for %s" % (self._devicaName))

    def _clicked(self, checked):
        try:
            if self._dockwidget is None:
                self._dockwidget = QtGui.QDockWidget(self._devicaName, self)
                # FIXME: check what's need and what can be excluded
                self._dockwidget.\
                    setFeatures(QtGui.QDockWidget.DockWidgetClosable
                                | QtGui.QDockWidget.DockWidgetMovable
                                | QtGui.QDockWidget.DockWidgetFloatable)
                self._dockwidget.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
                self._dockwidget.\
                    setWindowTitle(self._devicaName+'/'+self._title)
                Qt.QObject.connect(self._dockwidget,
                                   Qt.SIGNAL('visibilityChanged(bool)'),
                                   self._close)
                self._mainWindow.addDockWidget(QtCore.Qt.BottomDockWidgetArea,
                                               self._dockwidget)
            if self._widget is None:
                # form
                models = ["%s/%s" % (self._devicaName, attr)
                          for attr in self._formAttrs]
                self._widget = AttrRamps()
                form = self._widget._ui.AttributesForm
                form.addModels(models)
                # plot
                models = ["%s/%s" % (self._devicaName, attr)
                          for attr in self._plotAttrs]
                plot = self._widget._ui.AttributesPlot
                plot.addModels(models)
                plot.setForcedReadingPeriod(1000)
                plot.setLegendPosition(Qwt5.QwtPlot.BottomLegend)
                self._dockwidget.setWidget(self._widget)
            self._dockwidget.show()
        except Exception as e:
            self.error("Error when click to open the %s dockwidget: %s"
                       % (self._devicaName, e))
            traceback.print_exc()

    def _close(self, visible):
        if not visible:
            self.info("Close the dock widget for %s" % (self._devicaName))
            # self._dockwidget.setWidget(None)
            # self._widget = None
            # self._mainWindow.removeDockWidget(self._dockwidget)


class AutoStopConfigurationWidget(TaurusBaseComponent, Qt.QWidget):
    def __init__(self, button, devicaName, attrList, mainWindow, name=None,
                 qt_parent=None, designMode=False, redLedAttrs=None):
        if not name:
            name = "AutoStopConfigurationWidget"
        self.call__init__wo_kw(Qt.QWidget, qt_parent)
        self.call__init__(TaurusBaseComponent, name, designMode=designMode)
        self._devicaName = devicaName
        self._attrList = attrList
        self._redLedAttrs = redLedAttrs
        self._mainWindow = mainWindow
        self._dockwidget = None
        self._widget = None
        Qt.QObject.connect(button, Qt.SIGNAL("clicked(bool)"),
                           self._clicked)
        self.debug("Build a dock widget launcher for %s" % (self._devicaName))

    def _clicked(self, checked):
        try:
            if self._dockwidget is None:
                self._dockwidget = QtGui.QDockWidget(self._devicaName, self)
                # FIXME: check what's need and what can be excluded
                self._dockwidget.\
                    setFeatures(QtGui.QDockWidget.DockWidgetClosable
                                | QtGui.QDockWidget.DockWidgetMovable
                                | QtGui.QDockWidget.DockWidgetFloatable)
                self._dockwidget.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
                self._dockwidget.\
                    setWindowTitle(self._devicaName+'/'+self._attrList[0])
                Qt.QObject.connect(self._dockwidget,
                                   Qt.SIGNAL('visibilityChanged(bool)'),
                                   self._close)
                self._mainWindow.addDockWidget(QtCore.Qt.BottomDockWidgetArea,
                                               self._dockwidget)
            if self._widget is None:
                models = ["%s/%s" % (self._devicaName, attr)
                          for attr in self._attrList[:-1]]
                self._widget = AttrAutostopper()
                form = self._widget._ui.AttributesForm
                form.addModels(models)
                # TODO: can be changed the 'on color' of the autostop trigger
                #       attribute to red?
                if self._redLedAttrs is not None and \
                        isinstance(self._redLedAttrs, list):
                    for attr in self._redLedAttrs:
                        widget = form.getItemByModel("%s/%s"
                                                     % (self._devicaName,
                                                        attr))
                        widget.readWidget().setOnColor('red')
                plot = self._widget._ui.AttributesPlot
                plot.addModels(["%s/%s" % (self._devicaName,
                                           self._attrList[-1])])
                # plot.setForcedReadingPeriod(1000)
                plot.setLegendPosition(Qwt5.QwtPlot.BottomLegend)
                self._dockwidget.setWidget(self._widget)
            self._dockwidget.show()
        except Exception as e:
            self.error("Error when click to open the %s dockwidget: %s"
                       % (self._devicaName, e))
            traceback.print_exc()

    def _close(self, visible):
        if not visible:
            self.info("Close the dock widget for %s" % (self._devicaName))
            # self._dockwidget.setWidget(None)
            # self._widget = None
            # self._mainWindow.removeDockWidget(self._dockwidget)


class OperationModeManager(TaurusBaseComponent, Qt.QObject):
    def __init__(self, mainscreen_ui, name=None, qt_parent=None,
                 designMode=False):
        if not name:
            name = "OperationModeManager"
        self.call__init__wo_kw(Qt.QObject, qt_parent)
        self.call__init__(TaurusBaseComponent, name, designMode=designMode)
        self._checker = mainscreen_ui.tbMultiBunchCheck
        self._mainscreen_ui = mainscreen_ui
        Qt.QObject.connect(self._checker, Qt.SIGNAL('stateChanged(int)'),
                           self._operationModeChanges)
        self._operationModeChanges(self._checker.isChecked())

    def _operationModeChanges(self, mode):
        if self._checker.isChecked():
            self._mainscreen_ui.tbWidthLabel.setText('Width')
            self._mainscreen_ui.tbNumberLabel.setEnabled(False)
            self._mainscreen_ui.tbNumberValue.setEnabled(False)
            self._mainscreen_ui.tbNumberSetpoint.setEnabled(False)
        else:
            self._mainscreen_ui.tbWidthLabel.setText('Interval')
            self._mainscreen_ui.tbNumberLabel.setEnabled(True)
            self._mainscreen_ui.tbNumberValue.setEnabled(True)
            self._mainscreen_ui.tbNumberSetpoint.setEnabled(True)

# This is a copy from fsotrGUI ---
from taurus.external.qt import QtCore
import traceback
import getpass
import socket


class ViewButtonListener:
    def __init__(self, button, screen):
        self.__button = button
        self.__screen = str(screen)
        QtCore.QObject.connect(self.__button, QtCore.SIGNAL("clicked()"),
                               self.launchGui)
        self.__qpro = None

    def launchGui(self):
        try:
            print("Listener button clicked for %s" % (self.__screen))
            if self.__qpro is not None and \
                    self.__qpro.state() == QtCore.QProcess.Running:
                answer = \
                    QtGui.QMessageBox.warning(None, "Gui already running",
                                              "This screen is already open.\n"
                                              "Are you sure to kill it?",
                                              Qt.QString("Kill"),
                                              Qt.QString("Cancel"),
                                              "", 1)
                if answer == 0:
                    self.__qpro.kill()
                return
            self.__qpro = QtCore.QProcess()
            self.__qpro.\
                setProcessChannelMode(QtCore.QProcess.ForwardedChannels)
            QtCore.QObject.connect(self.__qpro, QtCore.SIGNAL("error()"),
                                   self.__FsotrGUI_error)
            QtCore.QObject.connect(self.__qpro, QtCore.SIGNAL("finished(int)"),
                                   self.__FsotrGUI_finished)
            fsotr = "--screen=%s" % (self.__screen)
            ccd = "--ccd=%s-ccd" % (self.__screen)
            iba = "--iba=%s-iba" % (self.__screen)
            cmd = "ctdiccd %s %s %s --force-local" % (fsotr, iba, ccd)
            #cmd += " --from=%s@%s" % (getpass.getuser(), socket.gethostname())
            print("[ButtonsListener] %s.launchGui cmd: %s"
                  % (self.__screen, cmd))
            self.__qpro.start(Qt.QString(cmd))
        except Exception as e:
            print("[ButtonsListener] %s.launchGui exception: %s"
                  % (self.__screen, e))
            traceback.print_exc()

    def __FsotrGUI_started(self):
        print("[ButtonsListener] %s.__FsotrGUI_started" % (self.__screen))

    def __FsotrGUI_error(self):
        print("[ButtonsListener] %s.__error: %s"
              % (self.__screen, str(self.__qpro.exitCode())))

    def __FsotrGUI_finished(self, exitStatus):
        print("[ButtonsListener] %s.__finished() exit Code: %d"
              % (self.__screen, exitStatus))

    def printer(self, type, output):
        for line in output:
            print("%s %s\t%s" % (self.__screen, type, line))


class Debugger(Logger):
    """
        Build this object for debugging purposes from an ipython console.
        It will launch the graphical interface and the console will have access
        to internal objects of the gui.
    """
    def __init__(self):
        Logger.__init__(self, name="Debugger")
        self._thread = threading.Thread(target=self.__threadmain)
        self._thread.start()
        while not hasattr(self, "_ui"):
            self.info("waiting ui")
            time.sleep(1)
        self._AllObjects()
        self.info("objects dictionary done")

    def __threadmain(self):
        self._qapp = build_application()
        self.info("application build")
        self._ui = build_ui()
        self.info("UI build")
        self._ui.show()
        self.info("show")
        self._exitCode = self._qapp.exec_()
        self.info("Application exit code: %d" % (self._exitCode))

    def _AllObjects(self):
        self._objs = {}
        for widget in self._qapp.allWidgets():
            if hasattr(widget, 'getModel'):
                model = "%r" % (widget.getModel())
                if model not in self._objs:
                    self._objs[model] = []
                self._objs[model].append(widget)
        self.info("object models (%d)" % (len(self._objs.keys())))
        # for model in self._objs.keys():
        #     print("\t%s"%(model))

    def MonitorAttribute(self, attrName):
        pass


def build_application():
    parser = argparse.get_taurus_parser()
    APPNAME = 'ctli'
    app = TaurusApplication(sys.argv, cmd_line_parser=parser,
                            app_name=APPNAME, app_version=VERSION,
                            org_domain='ALBA', org_name='ALBA')
    options = app.get_command_line_options()
    prepareToLog(app, APPNAME)
    return app


def build_ui():
    return LinacMainWindow()


def refreshButton(w):
    try:
        sys.path.append('/control/user-packages')
        from ctguirefresh.guirefreshbutton import GuiRefreshButton
        GuiRefreshButton.attachToWindow(w)  # w is your main window instance
    except Exception as e:  # ImportError
        print("module ctguirefresh not loaded: %s" % (e))


def eventPlotWindow():
    app = build_application()
    ui = DevicesEvents()
    # attributes = ['EventsNumber', 'EventsTime']
    widgets = {1: ui._ui.eventsplc1,
               2: ui._ui.eventsplc2,
               3: ui._ui.eventsplc3,
               4: ui._ui.eventsplc4,
               5: ui._ui.eventsplc5}
    for i in widgets.keys():
        widget = widgets[i]
        device = "%s%d" % (LinacDeviceNameRoot, i)
        widget.setModel(device)
    ui.show()
    sys.exit(app.exec_())


def main():
    app = build_application()
    ui = build_ui()
    # refreshButton(ui)
    app.setStyleSheet("QStatusBar::item { border: 0px solid black }; ")
    ui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
