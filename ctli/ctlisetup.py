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
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

__author__ = "Sergi Blanch-Torne"
__copyright__ = "Copyright 2015, CELLS / ALBA Synchrotron"
__license__ = "GPLv3+"

import os
import sys
import taurus
import time
import traceback

# The widgets are stored in a subdirectory and
# needs to be added to the pythonpath
# linacWidgetsPath = os.environ['PWD']+'/widgets'
# if linacWidgetsPath not in sys.path:
#     sys.path.append(linacWidgetsPath)

from taurus.core.util import argparse
from taurus.qt import Qt, QtGui
from taurus.qt.qtgui.application import TaurusApplication
from taurus.qt.qtgui.container import TaurusWidget
from taurus.qt.qtgui.util.ui import UILoadable

from .ctliaux import _setupLed4UnknownAttr, _setupLed4Attr
from .ctliaux import _setupCheckbox4UnknownAttr, _setupCheckbox4Attr
from .ctliaux import _setupSpinBox4Attr
from .ctliaux import _setupTaurusLabel4Attr
from .ctliaux import _setupCombobox4Attr
from .ctliaux import _setupActionWidget

import PyTango


def dump(obj, nested_level=0, output=sys.stdout):
    """Method found in http://stackoverflow.com/questions/15785719/\
       how-to-print-a-dictionary-line-by-line-in-python
       that helps to print in a human readable way nested dictionaries
    """
    spacing = '   '
    if type(obj) == dict:
        print >> output, '%s{' % ((nested_level) * spacing)
        for k, v in obj.items():
            if hasattr(v, '__iter__'):
                print >> output, '%s%s:' % ((nested_level + 1) * spacing, k)
                dump(v, nested_level + 1, output)
            else:
                print >> output, '%s%s: %s' % ((nested_level + 1) * spacing,
                                               k, v)
        print >> output, '%s}' % (nested_level * spacing)
    elif type(obj) == list:
        print >> output, '%s[' % ((nested_level) * spacing)
        for v in obj:
            if hasattr(v, '__iter__'):
                dump(v, nested_level + 1, output)
            else:
                print >> output, '%s%s' % ((nested_level + 1) * spacing, v)
        print >> output, '%s]' % ((nested_level) * spacing)
    else:
        print >> output, '%s%s' % (nested_level * spacing, obj)


@UILoadable(with_ui="ui")
class MainWindow(TaurusWidget):
    def __init__(self, parent=None, name=None, designMode=None):
        # setup main window
        try:
            self.__name = name.__name__
        except:
            self.__name = "ctlisetup"
        super(MainWindow, self).__init__(parent, designMode=designMode)
        try:
            self.debug("[%s]__init__()" % (self.__name))
            basePath = os.path.dirname(__file__)
            if len(basePath) == 0:
                basePath = '.'
            self.loadUi(filename="linacConfigurationScreen.ui",
                        path=basePath+"/widgets/ui")
        except Exception as e:
            self.warning("[%s]__init__(): MainWindow exception! %s"
                         % (self.__name, e))
            traceback.print_exc()
            self.traceback()
        # place the ui in the window
        self.initComponents()
        # kill splash screen
        # self.splashScreen().finish(self)
        self.ui.progressBar.hide()  # setValue(100)

    def initComponents(self):
        # if hasattr(self.parent(),'setWindowTitle'):
        #     self.parent().setWindowTitle("Linac Save/Retrieve Interface")
        self.setWindowTitle("Linac Save/Retrieve Interface")
        if hasattr(self.parent(), 'setCentralWidget'):
            self.centralwidget = self.ui.centralFrame
            self.setCentralWidget(self.centralwidget)
        self.setConfiguration()
        self.loadFromDevices()

    ######
    # # Auxiliar methods to configure widgets ---
    def _setupLed4UnknownAttr(self, widget):
        _setupLed4UnknownAttr(widget)

    def _setupLed4Attr(self, widget, attrName, inverted=False,
                       onColor='green', offColor='red', pattern='on'):
        _setupLed4Attr(widget, attrName, inverted, onColor,
                               offColor, pattern)

    def _setupCheckbox4UnknownAttr(self, widget):
        _setupCheckbox4UnknownAttr(widget)

    def _setupCheckbox4Attr(self, widget, attrName,
                            isRst=False, DangerMsg='',
                            riseEdge=False, fallingEdge=False):
        _setupCheckbox4Attr(widget, attrName,
                                    isRst, DangerMsg, riseEdge, fallingEdge)

    def _setupSpinBox4Attr(self, widget, attrName, step=None):
        _setupSpinBox4Attr(widget, attrName, step)

    def _setupTaurusLabel4Attr(self, widget, attrName, unit=None):
        _setupTaurusLabel4Attr(widget, attrName, unit)

    def _setupCombobox4Attr(self, widget, attrName, valueNames=None):
        _setupCombobox4Attr(self, widget, attrName, valueNames)

    def _setupActionWidget(self, widget, attrName, text='on/off', isRst=False,
                           DangerMsg='', riseEdge=False, fallingEdge=False):
        _setupActionWidget(widget, attrName, text, isRst,
                                   DangerMsg, riseEdge, fallingEdge)

    def _setupQSpinBox(self, widget, minVal=0, maxVal=99, decimals=2, step=1):
        widget.setMinimum(minVal)
        widget.setMaximum(maxVal)
        if hasattr(widget, 'setDecimals'):
            widget.setDecimals(decimals)
        widget.setSingleStep(step)
    # Done auxiliar methods to configure widgets ---
    ######

    ######
    # # setModel & others for the Configuration Tab ---
    def setConfiguration(self):
        configuration_ui = self.ui
        self._configurationWidgets = {}
        # configure the widgets in the panels ---
        self.electronGunConfiguration(configuration_ui.
                                      electronGunSnapshot._ui)
        self.coolingLoopsConfiguration(configuration_ui.
                                       coolingLoopSnapshot._ui)
        self.vacuumValvesConfiguration(configuration_ui.
                                       vacuumValveSnapshot._ui)
        self.magnetsConfiguration(configuration_ui.magnetSnapshot._ui)
        self.radiofrequencyConfiguration(configuration_ui.
                                         radioFrequencySnapshot._ui)
        self.timingConfiguration(configuration_ui.timingSnapshot._ui)
        self.evrConfiguration(configuration_ui.evrSnapshot._ui)
        self.klystronsConfiguration(configuration_ui.klystronSnapshot._ui)
        self.commentConfiguration(configuration_ui)
        # connect buttons to their actions ---
        self.buttonsConfiguration(configuration_ui.buttonBox)
        # Those actions doesn't need DangerMessage because eGunLV, CLs and KaLV
        # are not included in the save/retrive

    def electronGunConfiguration(self, ui):
        devName = 'li/ct/plc1'
        widgetsSet = {}

        attrName = '%s/GUN_Filament_V_setpoint' % (devName)
        attrName = attrName.lower()
        widgetsSet[attrName] = {'label': ui.GunFilamentLowVoltageLabel,
                                'read':  ui.GunFilamentLowVoltageRead,
                                'write': ui.GunFilamentLowVoltageWrite,
                                'check': ui.GunFilamentLowVoltageCheck}
        self._setupTaurusLabel4Attr(widgetsSet[attrName]['read'], attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            minVal=0.0, maxVal=10.0, step=0.1)

        attrName = '%s/Gun_kathode_v_setpoint' % (devName)
        attrName = attrName.lower()
        widgetsSet[attrName] = {'label': ui.GunKathodeLowVoltageLabel,
                                'read':  ui.GunKathodeLowVoltageRead,
                                'write': ui.GunKathodeLowVoltageWrite,
                                'check': ui.GunKathodeLowVoltageCheck}
        self._setupTaurusLabel4Attr(widgetsSet[attrName]['read'], attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            minVal=0.0, maxVal=50.0, step=0.1)

        attrName = '%s/Gun_hv_v_setpoint' % (devName)
        attrName = attrName.lower()
        widgetsSet[attrName] = {'label': ui.GunHighVoltagePowerSupplyLabel,
                                'read':  ui.GunHighVoltagePowerSupplyRead,
                                'write': ui.GunHighVoltagePowerSupplyWrite,
                                'check': ui.GunHighVoltagePowerSupplyCheck}
        self._setupTaurusLabel4Attr(widgetsSet[attrName]['read'], attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            minVal=-90.0, maxVal=0.0, step=0.1)

        self._configurationWidgets['eGun'] = widgetsSet

    def coolingLoopsConfiguration(self, ui):
        devName = 'li/ct/plc2'
        widgetsSet = {}

        # CL1
        attrName = '%s/cl1_t_setpoint' % (devName)
        attrName = attrName.lower()
        widgetsSet[attrName] = {'label': ui.coolingLoop1SetpointLabel,
                                'read':  ui.coolingLoop1SetpointRead,
                                'write': ui.coolingLoop1SetpointWrite,
                                'check': ui.coolingLoop1SetpointCheck}
        self._setupTaurusLabel4Attr(widgetsSet[attrName]['read'], attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            minVal=0.0, maxVal=50.0, step=0.1)
        # CL2
        attrName = '%s/cl2_t_setpoint' % (devName)
        attrName = attrName.lower()
        widgetsSet[attrName] = {'label': ui.coolingLoop2SetpointLabel,
                                'read':  ui.coolingLoop2SetpointRead,
                                'write': ui.coolingLoop2SetpointWrite,
                                'check': ui.coolingLoop2SetpointCheck}
        self._setupTaurusLabel4Attr(widgetsSet[attrName]['read'], attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            minVal=0.0, maxVal=50.0, step=0.1)
        # CL3
        attrName = '%s/cl3_t_setpoint' % (devName)
        attrName = attrName.lower()
        widgetsSet[attrName] = {'label': ui.coolingLoop3SetpointLabel,
                                'read':  ui.coolingLoop3SetpointRead,
                                'write': ui.coolingLoop3SetpointWrite,
                                'check': ui.coolingLoop3SetpointCheck}
        self._setupTaurusLabel4Attr(widgetsSet[attrName]['read'], attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            minVal=0.0, maxVal=50.0, step=0.1)
        self._configurationWidgets['coolingLoop'] = widgetsSet

    def vacuumValvesConfiguration(self, ui):
        widgetsSet = {}

        attrName = 'li/ct/plc2/VCV_ONC'.lower()
        widgetsSet[attrName] = {'label': ui.VaccumCollimatorValveLabel,
                                'read':  ui.VaccumCollimatorValveRead,
                                'write': ui.VaccumCollimatorValveWrite,
                                'check': ui.VaccumCollimatorValveCheck}
        self._setupLed4Attr(ui.VaccumCollimatorValveRead, attrName)
        self._configurationWidgets['vacuumValves'] = widgetsSet

    def magnetsConfiguration(self, ui):
        widgetsSet = {}

        magnets = {'sl': {'1': ['H', 'V', 'F'],
                          '2': ['H', 'V', 'F'],
                          '3': ['H', 'V', 'F'],
                          '4': ['H', 'V', 'F']},
                   'bc': {'1': ['H', 'V', 'F'],
                          '2': ['H', 'V', 'F']},
                   'gl': {'':  ['H', 'V', 'F']},
                   'as': {'1': ['H', 'V'],
                          '2': ['H', 'V']},
                   'qt': {'1': ['H', 'V', 'F'],
                          '2': ['F']}}

        for family in magnets.keys():
            self.debug("> %s" % (family))
            for magnet in magnets[family].keys():
                self.debug(">> %s%s" % (family, magnet))
                for component in magnets[family][magnet]:
                    attrName = 'li/ct/plc3/%s%s%s_I_setpoint'\
                               % (family, magnet, component)
                    attrName = attrName.lower()
                    widgetPrefix = "%s%s%s" % (family, magnet, component)
                    self.debug(">>> %s" % (widgetPrefix))
                    labelWidget = getattr(ui, widgetPrefix+'Label')
                    readWidget = getattr(ui, widgetPrefix+'Read')
                    writeWidget = getattr(ui, widgetPrefix+'Write')
                    checkWidget = getattr(ui, widgetPrefix+'Check')
                    widgetsSet[attrName] = {'label': labelWidget,
                                            'read':  readWidget,
                                            'write': writeWidget,
                                            'check': checkWidget}
                    widget = widgetsSet[attrName]['read']
                    self._setupTaurusLabel4Attr(widget, attrName)
                    if component in ['H', 'V']:
                        if family == 'qt':
                            minVal = -16
                            maxVal = 16
                        else:
                            minVal = -2
                            maxVal = 2
                        step = 0.01
                        decimals = 2
                    else:
                        if family == 'sl':
                            minVal = 0
                            maxVal = 1
                            step = 0.01
                            decimals = 2
                        elif family == 'bc':
                            minVal = 0
                            maxVal = 200
                            step = 0.01
                            decimals = 2
                        elif family == 'gl':
                            minVal = 0
                            maxVal = 130
                            step = 0.01
                            decimals = 2
                        elif family == 'qt':
                            minVal = 0
                            maxVal = 6
                            step = 0.005
                            decimals = 3
                    self._setupQSpinBox(widgetsSet[attrName]['write'],
                                        minVal=minVal, maxVal=maxVal,
                                        step=step, decimals=decimals)
        # TODO: connect the ToApplyTitle to check/uncheck all the *Check ---
        self._configurationWidgets['magnets'] = widgetsSet

    def radiofrequencyConfiguration(self, ui):
        widgetsSet = {}

        attrName = 'li/ct/plc1/TPS0_Phase'.lower()
        widgetsSet[attrName] = {'label': ui.TPS0PhaseLabel,
                                'read':  ui.TPS0PhaseRead,
                                'write': ui.TPS0PhaseWrite,
                                'check': ui.TPS0PhaseCheck}
        self._setupTaurusLabel4Attr(ui.TPS0PhaseRead, attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            minVal=0.0, maxVal=380, decimals=1, step=0.1)

        attrName = 'li/ct/plc1/TPSX_Phase'.lower()
        widgetsSet[attrName] = {'label': ui.TPSXPhaseLabel,
                                'read':  ui.TPSXPhaseRead,
                                'write': ui.TPSXPhaseWrite,
                                'check': ui.TPSXPhaseCheck}
        self._setupTaurusLabel4Attr(ui.TPSXPhaseRead, attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            minVal=0.0, maxVal=380, decimals=0, step=1)

        attrName = 'li/ct/plc1/TPS1_Phase'.lower()
        widgetsSet[attrName] = {'label': ui.TPS1PhaseLabel,
                                'read':  ui.TPS1PhaseRead,
                                'write': ui.TPS1PhaseWrite,
                                'check': ui.TPS1PhaseCheck}
        self._setupTaurusLabel4Attr(ui.TPS1PhaseRead, attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            minVal=0.0, maxVal=380, decimals=0, step=1)

        attrName = 'li/ct/plc1/TPS2_Phase'.lower()
        widgetsSet[attrName] = {'label': ui.TPS2PhaseLabel,
                                'read':  ui.TPS2PhaseRead,
                                'write': ui.TPS2PhaseWrite,
                                'check': ui.TPS2PhaseCheck}
        self._setupTaurusLabel4Attr(ui.TPS2PhaseRead, attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            minVal=0.0, maxVal=380, decimals=0, step=1)

        attrName = 'li/ct/plc1/A0_OP'.lower()
        widgetsSet[attrName] = {'label': ui.A0OPLabel,
                                'read':  ui.A0OPRead,
                                'write': ui.A0OPWrite,
                                'check': ui.A0OPCheck}
        self._setupTaurusLabel4Attr(ui.A0OPRead, attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            minVal=75, maxVal=760, decimals=0, step=1)

        attrName = 'li/ct/plc1/ATT2_P_setpoint'.lower()
        widgetsSet[attrName] = {'label': ui.ATT2Label,
                                'read':  ui.ATT2Read,
                                'write': ui.ATT2Write,
                                'check': ui.ATT2Check}
        self._setupTaurusLabel4Attr(ui.ATT2Read, attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            minVal=-10.0, maxVal=0, decimals=1, step=0.1)

        attrName = 'li/ct/plc1/PHS1_Phase_setpoint'.lower()
        widgetsSet[attrName] = {'label': ui.PHS1Label,
                                'read':  ui.PHS1Read,
                                'write': ui.PHS1Write,
                                'check': ui.PHS1Check}
        self._setupTaurusLabel4Attr(ui.PHS1Read, attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            minVal=0.0, maxVal=160, decimals=0, step=1)

        attrName = 'li/ct/plc1/PHS2_Phase_setpoint'.lower()
        widgetsSet[attrName] = {'label': ui.PHS2Label,
                                'read':  ui.PHS2Read,
                                'write': ui.PHS2Write,
                                'check': ui.PHS2Check}
        self._setupTaurusLabel4Attr(ui.PHS2Read, attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            minVal=0.0, maxVal=380, decimals=0, step=1)

        self._configurationWidgets['radioFrequency'] = widgetsSet

    def timingConfiguration(self, ui):
        widgetsSet = {}

        attrName = 'li/ct/plc1/TB_MBM'.lower()
        widgetsSet[attrName] = {'label': ui.MBMLabel,
                                'read':  ui.MBMRead,
                                'write': ui.MBMWrite,
                                'check': ui.MBMCheck}
        self._setupLed4Attr(ui.MBMRead, attrName)

        attrName = 'li/ct/plc1/TB_GUN_delay'.lower()
        widgetsSet[attrName] = {'label': ui.GunDelayLabel,
                                'read':  ui.GunDelayRead,
                                'write': ui.GunDelayWrite,
                                'check': ui.GunDelayCheck}
        self._setupTaurusLabel4Attr(ui.GunDelayRead, attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            minVal=32, maxVal=4096, step=32)

        attrName = 'li/ct/plc1/TB_ka1_delay'.lower()
        widgetsSet[attrName] = {'label': ui.ka1DelayLabel,
                                'read':  ui.ka1DelayRead,
                                'write': ui.ka1DelayWrite,
                                'check': ui.ka1DelayCheck}
        self._setupTaurusLabel4Attr(ui.ka1DelayRead, attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            minVal=1, maxVal=56, step=1)

        attrName = 'li/ct/plc1/TB_ka2_delay'.lower()
        widgetsSet[attrName] = {'label': ui.ka2DelayLabel,
                                'read':  ui.ka2DelayRead,
                                'write': ui.ka2DelayWrite,
                                'check': ui.ka2DelayCheck}
        self._setupTaurusLabel4Attr(ui.ka2DelayRead, attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            minVal=2720, maxVal=4096, step=32)

        attrName = 'li/ct/plc1/TB_GPI'.lower()
        widgetsSet[attrName] = {'label': ui.GPILabel,
                                'read':  ui.GPIRead,
                                'write': ui.GPIWrite,
                                'check': ui.GPICheck}
        self._setupTaurusLabel4Attr(ui.GPIRead, attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            minVal=6, maxVal=1054, step=2)

        attrName = 'li/ct/plc1/TB_GPN'.lower()
        widgetsSet[attrName] = {'label': ui.GPNLabel,
                                'read':  ui.GPNRead,
                                'write': ui.GPNWrite,
                                'check': ui.GPNCheck}
        self._setupTaurusLabel4Attr(ui.GPNRead, attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            minVal=1, maxVal=16, step=1)

        attrName = 'li/ct/plc1/TB_GPA'.lower()
        widgetsSet[attrName] = {'label': ui.GPALabel,
                                'read':  ui.GPARead,
                                'write': ui.GPAWrite,
                                'check': ui.GPACheck}
        self._setupTaurusLabel4Attr(ui.GPARead, attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            minVal=-40.0, maxVal=0, decimals=1, step=0.1)

        # TODO: connect the ToApplyTitle to check/uncheck all the *Check ---
        self._configurationWidgets['timing'] = widgetsSet

    def evrConfiguration(self, ui):
        widgetsSet = {}

        LINAC_FINE_TIMING_DEVICE = 'LI/TI/EVR300-CLI0302-A'
        LINAC_OUTPUTS = [0, 1, 2, 3]
        ui.linac_wheels = {}
        for i in LINAC_OUTPUTS:
            for row, attr in enumerate(['PulseDelay', 'PulseWidth',
                                        'FineDelay']):
                model = '%s/%s%d' % (LINAC_FINE_TIMING_DEVICE, attr, i)
                attrName = model.lower()
                prefix = (s for s in ('Width', 'Fine', 'Delay')
                          if s in attr).next()+str(i)
                Label = getattr(ui, prefix+'Label')
                Read = getattr(ui, prefix+'Read')
                Write = getattr(ui, prefix+'Write')
                Check = getattr(ui, prefix+'Check')
                widgetsSet[attrName] = {'label': Label,
                                        'read':  Read,
                                        'write': Write,
                                        'check': Check}
                self._setupTaurusLabel4Attr(Read, attrName)
                self._setupQSpinBox(widgetsSet[attrName]['write'],
                                    minVal=0, maxVal=1e10, step=8, decimals=0)

        # TODO: connect the ToApplyTitle to check/uncheck all the *Check ---
        self._configurationWidgets['evr'] = widgetsSet

    def klystronsConfiguration(self, ui):
        widgetsSet = {}

        klystrons = {1: {'setp': ui.ka1HVPSRead},
                     2: {'setp': ui.ka2HVPSRead}}
        for number in klystrons.keys():
            self.debug("> %s" % (number))
            for element in klystrons[number].keys():
                self.debug(">> ka%s_%s" % (number, element))
                widget = klystrons[number][element]
                devName = 'li/ct/plc%d' % (number+3)
                if element == 'setp':
                    attrName = "%s/HVPS_V_setpoint" % (devName).lower()
                    widgetsSet[attrName] = \
                        {'label': getattr(ui, 'ka%dHVPSLabel' % (number)),
                         'read': getattr(ui, 'ka%dHVPSRead' % (number)),
                         'write': getattr(ui, 'ka%dHVPSWrite' % (number)),
                         'check': getattr(ui, 'ka%dHVPSCheck' % (number))}
                    widget = widgetsSet[attrName]['read']
                    self._setupTaurusLabel4Attr(widget, attrName)
                    self._setupQSpinBox(widgetsSet[attrName]['write'],
                                        minVal=0.0, maxVal=33,
                                        decimals=1, step=0.1)
        # TODO: connect the ToApplyTitle to check/uncheck all the *Check ---
        self._configurationWidgets['klystrons'] = widgetsSet

    def commentConfiguration(self, ui):
        # configure the splitter to start at 66%-33% relation.
        w = ui.commentGroup.width()
        ui.splitter.setSizes([2*w/3, w/3])
        self._loadPreviousComment(ui)
    # Done configure subwidgets ---
    ######

    def buttonsConfiguration(self, buttons):
        buttons.button(QtGui.QDialogButtonBox.Reset).setText("Reload")
        # buttons.button(QtGui.QDialogButtonBox.Reset).clicked.connect(\
        #    self.loadFromDevices)
        Qt.QObject.connect(buttons.button(QtGui.QDialogButtonBox.Reset),
                           Qt.SIGNAL('clicked(bool)'), self.loadFromDevices)
        # buttons.button(QtGui.QDialogButtonBox.Save).clicked.connect(\
        #    self.saveToFile)
        Qt.QObject.connect(buttons.button(QtGui.QDialogButtonBox.Save),
                           Qt.SIGNAL('clicked(bool)'), self.saveToFile)
        # buttons.button(QtGui.QDialogButtonBox.Open).clicked.connect(\
        #    self.loadFromFile)
        Qt.QObject.connect(buttons.button(QtGui.QDialogButtonBox.Open),
                           Qt.SIGNAL('clicked(bool)'), self.loadFromFile)
        # buttons.button(QtGui.QDialogButtonBox.Apply).clicked.connect(\
        #    self.applyToDevices)
        Qt.QObject.connect(buttons.button(QtGui.QDialogButtonBox.Apply),
                           Qt.SIGNAL('clicked(bool)'), self.applyToDevices)

    # TODO: should the *Reading widgets be connected to the *Value?
    #       Doing this, the operation of the other tabs will be shown in
    #       this Configuration tab according to when it's happening.

    ######
    # # Distinguish between widget types ---
    def _isSpinBox(self, widget):
        return hasattr(widget, 'setValue')

    def _isCheckBox(self, widget):
        return hasattr(widget, 'setChecked')
    # Done widget types ---
    ######

    ######
    # # Widget backgrounds ---
    def _setStyleToModified(self, attrStruct):
        saver = attrStruct['write']
        if self._isSpinBox(saver):
            saver.setStyleSheet("background-color: rgb(255, 255, 0);"
                                "color: rgb(0, 0, 255); "
                                "font-weight: bold;"
                                "font: 7pt \"DejaVu Sans\";")
        elif self._isCheckBox(saver):
            saver.setStyleSheet("background-color: rgb(255, 255, 0);"
                                "color: rgb(0, 0, 255);"
                                "font: 7pt \"DejaVu Sans\";")
        else:
            raise Exception("Unmanaged %s widget type to tag modified"
                            % (type(widget)))
        attrStruct['check'].setChecked(True)

    def _setStyleToNoModified(self, attrStruct):
        saver = attrStruct['write']
        if self._isSpinBox(saver):
            saver.setStyleSheet("background-color: rgb(255, 255, 255);"
                                "color: rgb(0, 0, 0); "
                                "font: 7pt \"DejaVu Sans\";")
        elif self._isCheckBox(saver):
            saver.setStyleSheet("color: rgb(0, 0, 0);"
                                "font: 7pt \"DejaVu Sans\";")
        else:
            raise Exception("Unmanaged %s widget type to tag modified"
                            % (type(widget)))
        attrStruct['check'].setChecked(False)
    # done widget backgrounds ---
    ######

    ######
    # # Value setters and getters ---
    def _getAttrValue(self, attrName):
        return PyTango.AttributeProxy(attrName).read().value

    def _setAttrValue(self, attrName, value):
        rvalue = self._getAttrValue(attrName)
        if value == rvalue:
            # hackish to because we've seen some attributes not well applied
            # and we don't have rights to study further why this had happen
            self._doubleWrite(attrName, value, 0.99)
        self.info('_setAttrValue(%s,%s,(%s))' % (attrName, value, type(value)))
        try:
            taurus.Attribute(attrName).write(value)
        except Exception as e:
            self.error("Exception in the %s write(%s) operation: %s\n%s"
                       % (attrName, value, e, traceback.format_exc()))
        self._checkReadWrite(attrName, rvalue, value)

    def _doubleWrite(self, attrName, value, near):
        '''This method is to do two different writes with close values to
           make sure the newer value is set.
        '''
        try:
            if type(value) == bool:
                return
            elif type(value) == int:
                # it would be in the maximum or in the minimum, but one above
                # or one below will be possible to be writable, isn't it?
                try:
                    taurus.Attribute(attrName).write(int(value+1))
                except:
                    try:
                        taurus.Attribute(attrName).write(int(value-1))
                    except:
                        self.error("It hasn't been possible to write a near "
                                   "setpoint for attribute %s" % (attrName))
                time.sleep(0.3)
            elif type(value) == float:
                taurus.Attribute(attrName).write(value*near)
                time.sleep(0.3)
        except Exception as e:
            # in boundary cases it had seen that this produces an exception
            # but it's not a blocking issue and we can continue.
            self.warning("Attribute %s fail the '%s' hackish: "
                         "value=%g value*near=%g. The exception was: %s"
                         % (attrName, near, value, value*near, e))

    def _checkReadWrite(self, attrName, rvalue, wvalue):
        # check if the write has been acknowledge by the plc reading
        i = 0
        while i < 10:
            if self._checkValue(rvalue, wvalue, attrName):
                self.debug("For %s, reading corresponds to what has been "
                           "written (%d)" % (attrName, i))
                return
            time.sleep(0.1)  # when they are different, wait to recheck
            i += 1
            rvalue = self._getAttrValue(attrName)
            # (1 second of rechecks maximum)
        raise ValueError("The attribute reading (%s) didn't "
                         "correspond to what has been set (%s)"
                         % (rvalue, wvalue))

    def _checkValue(self, a, b, attrName):
        # With bools and integers the compare is simple, but floats,
        # because of the different byte precisions, can be equivalent
        # not being exacly the same.
        if type(a) == float or type(b) == float:
            try:
                attr = PyTango.AttributeProxy(attrName)
                attrFormat = attr.get_config().format
            except Exception as e:
                self.error("It hasn't been possible to get %s's format"
                           % (attrName))
                attrFormat = '%6.3f'
            aStr = attrFormat % a
            bStr = attrFormat % b
            if aStr == bStr:
                self.warning("The format (%s) representation matches, "
                             "even the floats are not exactly equal "
                             "%g != %g" % (attrFormat, a, b))
                return True
            self.warning("For attribute %s %g != %g and %s != %s"
                         % (attrName, a, b, aStr, bStr))
        else:
            return a == b
        return False

    def _setValueToSaverWidget(self, attrStruct, value, style=True):
        saver = attrStruct['write']
        if self._isSpinBox(saver):
            haschanged = (value != saver.value())
            saver.setValue(value)
        elif self._isCheckBox(saver):
            haschanged = (value != saver.isChecked())
            saver.setChecked(value)
        else:
            raise Exception("Unmanaged %s widget type" % (type(saver)))
        if style and haschanged:
            self._setStyleToModified(attrStruct)
        else:
            self._setStyleToNoModified(attrStruct)

    def _getValueFromSaverWidget(self, attrStruct):
        saver = attrStruct['write']
        if self._isSpinBox(saver):
            return saver.value()
        elif self._isCheckBox(saver):
            return saver.isChecked()
        else:
            raise Exception("Unmanaged %s widget type" % (type(saver)))
    # done Value setters and getters ---
    ######

    ######
    # # manage files ---
    def _getStorageDirectory(self):
        directory = str(QtGui.QFileDialog.
                        getExistingDirectory(self, "Select Directory",
                                             ctliaux.defaultConfigurations))
        if not directory == '' and not directory.startswith(ctliaux.sandbox):
            QtGui.QMessageBox.warning(self, "Sandbox warning",
                                      "Your selected directory is not in the "
                                      "storage shared by NFS")
        return directory

    def _getFilePrefix(self, now_struct):
        # Start all the files with the date,
        # then mode and highlight some field on the name
        # 1.- %Y%m%d_%H%M
        fileprefix = time.strftime("%Y%m%d_%H%M", now_struct)
        # 2.- MBM vs SBM
        modeAttrName = 'LI/CT/PLC1/TB_MBM'.lower()
        try:
            isMBM = self._getAttrValue(modeAttrName)
            # 2.1- MBM_width
            if isMBM:
                widthAttrName = 'LI/CT/PLC1/TB_GPI'.lower()
                width = self._getAttrValue(widthAttrName)
                fileprefix = ''.join("%s_MBM_%dns" % (fileprefix, width))
            # 2.2- SBM_pulses_interval
            else:
                npulsesAttrName = 'LI/CT/PLC1/TB_GPN'.lower()
                intervalAttrName = 'LI/CT/PLC1/TB_GPI'.lower()
                npulses = self._getAttrValue(npulsesAttrName)
                # interval = self._getAttrValue(intervalAttrName)
                fileprefix = ''.join("%s_SBM_%dpulses" % (fileprefix, npulses))
        except Exception as e:
            self.error("Cannot build a file prefix! %s" % (e))
        return fileprefix

    def _getFileSuffix(self, prefix=None):
        msg, ok = QtGui.QInputDialog.getText(self, "Select file name",
                                             "would you like to write "
                                             "something after the file "
                                             "prefix %s?" % (prefix),
                                             QtGui.QLineEdit.Normal)
        return (str(msg), ok)

    def _requestFileName(self):
        dialogTitle = "Select linac's configuration file"
        filters = "Linac configuration (*.li);;All files (*)"
        return str(QtGui.QFileDialog.
                   getOpenFileName(self, dialogTitle,
                                   ctliaux.defaultConfigurations, filters))

    def _prepareFileHeader(self, now_struct):
        return "# File stored the %s\n" % (time.strftime("%Y/%m/%d at %H:%m",
                                                         now_struct))

    def _isCommentLine(self, line):
        if line[0] == '#':
            if not self._isGroupTagLine(line):
                return True
        return False

    def _isGroupTagLine(self, line):
        try:
            if line[0] == '#' and \
               line.split()[1][:-1] == 'group' and \
               line.split()[2] in self._configurationWidgets.keys():
                return True
        except:
            pass
        return False

    def _isSpecialCommentLine(self, line):
        if self._isCommentLine(line) and line[1] == '@':
            return True
        return False

    def _prepareGroupTag(self, group):
        return "# group: %s" % (group)

    def _prepareAttrLine(self, attrStruct, attrName):
        tag = attrStruct['label'].text()
        rvalue = self._getAttrValue(attrName)
        # to raise exception if not available
        wvalue = self._getValueFromSaverWidget(attrStruct)
        if rvalue != wvalue:
            print('%s: %s != %s' % (attrName, rvalue, wvalue))
        value = wvalue or rvalue
        return "%24s\t%g\t%s" % (tag, value, attrName)

    def _getAttrLine(self, line, n):
        try:
            elements = line.split()
            attrName = elements[-1]
            value = elements[-2]
            if value.count('.'):
                value = float(value)
            else:
                value = int(value)
            return (attrName, value)
        except Exception as e:
            self.error("misunderstanding in line %d: '%s'" % (n+1, line))
            return (None, None)
    # done manage files ---
    ######

    ######
    # # Comments region ---
    def _loadPreviousComment(self, ui):
        if os.path.isfile(ctliaux.commentsfile):
            with open(ctliaux.commentsfile, 'r') as file:
                lines = file.readlines()
                text = ""
                for line in lines:
                    text = ''.join("%s%s" % (text, line))
                ui.textToSave.setText(text)
        else:
            self.warning("The previous-comments file doesn't exist.")

    def _storeComments(self):
        comments = self.ui.textToSave.toPlainText()
        if len(comments) == 0:
            self.warning("No comments to be stored.")
            return None
        with open(ctliaux.commentsfile, 'w') as file:
            file.write(comments)
        # the tag #@ is to distinguish it in the file
        comments = "#@ %s" % (comments)
        comments = comments.replace('\n', '\n#@ ')
        return comments

    def _cleanSpecialCommentsFromFile(self):
        self.ui.textLoaded.setText("")

    def _recoverSpecialCommentLine(self, line):
        self.ui.textLoaded.setText("%s%s"
                                   % (self.ui.textLoaded.toPlainText(),
                                      line.replace('#@ ', '')))
    # done commects region ---
    ######

    def prepareProgressBar(self):
        self.ui.progressBar.show()
        self.ui.progressBar.setValue(0)

    def getNumberOfElements(self):
        nElements = 0
        for group in self._configurationWidgets.keys():
            nElements += len(self._configurationWidgets[group].keys())
        return nElements

    def setProgressBarValue(self, i, nElements):
        self.ui.progressBar.setValue(i*100/nElements)

    def doneProgressBar(self):
        self.ui.progressBar.hide()

    ######
    # # ActionButtons callbacks ---
    def loadFromDevices(self):
        '''With this call (from a button or at the loading step) we must travel
           all the *Reading widgets and copy the value to the *Value widget.
        '''
        exceptions = {}
        # prepare progress bar
        self.prepareProgressBar()
        nElements = self.getNumberOfElements()
        i = 0
        for group in self._configurationWidgets.keys():
            self.debug(">  %s" % group)
            for attrName in self._configurationWidgets[group].keys():
                attrStruct = self._configurationWidgets[group][attrName]
                try:
                    value = self._getAttrValue(attrName)
                    self._setValueToSaverWidget(attrStruct, value, style=False)
                except Exception as e:
                    self.error("Exception trying to load %s value. %s"
                               % (attrName, e))
                    label = attrStruct['label'].text()
                    if group in exceptions.keys():
                        exceptions[group].append(str(label))
                    else:
                        exceptions[group] = [str(label)]
                # progressbar
                i += 1
                self.setProgressBarValue(i, nElements)
        self._raiseCollectedExceptions("load", exceptions)
        self.doneProgressBar()

    def saveToFile(self):
        '''Travelling along the *Check widgets, the checked ones (name and
           value) will be written in a file indicated by the user.
        '''
        now = time.time()
        now_struct = time.localtime(now)
        directory = self._getStorageDirectory()
        if directory == '':  # when cancel the QFileDialog
            QtGui.QMessageBox.warning(self, "Operation Cancelled",
                                      "The Save action has been cancelled!\n"
                                      "No file written.")
        prefix = self._getFilePrefix(now_struct)
        # TODO: request suffix to the user. ---
        suffix = ''
        if directory != '':
            suffix, ok = self._getFileSuffix(prefix)
            if not ok:
                QtGui.QMessageBox.warning(self, "Operation Cancelled",
                                          "The Save action has been "
                                          "cancelled!\n No file written.")
            elif suffix == '':
                filename = "%s/%s.li" % (directory, prefix)
            else:
                filename = "%s/%s-%s.li" % (directory, prefix, suffix)
            self.debug("saveToFile() filename: %s" % (filename))
            saving = self._prepareFileHeader(now_struct)
            # TODO: store comments
            try:
                comments = self._storeComments()
            except:
                traceback.print_exc()
                comments = None
            if comments is not None and len(comments) > 0:
                saving = ''.join("%s\n%s\n" % (saving, comments))
            exceptions = {}
            self.prepareProgressBar()
            nElements = self.getNumberOfElements()
            i = 0
            for group in self._configurationWidgets.keys():
                saving = ''.join("%s\n%s"
                                 % (saving, self._prepareGroupTag(group)))
                groupAttrNames = self._configurationWidgets[group].keys()
                groupAttrNames.sort()
                for attrName in groupAttrNames:
                    attrStruct = self._configurationWidgets[group][attrName]
                    try:
                        saving = ''.join("%s\n%s"
                                         % (saving,
                                            self._prepareAttrLine(attrStruct,
                                                                  attrName)))
                    except Exception as e:
                        if group in exceptions.keys():
                            exceptions[group].append(attrName)
                        else:
                            exceptions[group] = [attrName]
                    # progressbar
                    i += 1
                    self.setProgressBarValue(i, nElements)
            saving = ''.join('%s\n' % (saving))
            try:
                with open(filename, 'w') as file:  # file = open(filename, 'w')
                    file.write(saving)
                # file.close()
            except Exception as e:
                QtGui.QMessageBox.critical(self, "Exceptions when save",
                                           "File with the settings was "
                                           "NOT saved!\nException: %s" % (e))
                traceback.print_exc()
            self._raiseCollectedExceptions("save", exceptions)
            self.doneProgressBar()

    # #loadFromFile() ---
    def loadFromFile(self):
        '''Given a file of settings provided by the user, show those values
           in the *Value widgets.
           Mark (TODO: how?) the changes from the previous value
           in the *Value widget
        '''
        filename = self._requestFileName()
        self._cleanSpecialCommentsFromFile()
        self._doLoadFromFile(filename)

    # Descending level for the loadFromFile() ---
    def _doLoadFromFile(self, filename):
        group = ''
        exceptions = {}
        if filename != '':
            self.debug("Loading from file: %r" % (filename))
            with open(filename, 'r') as file:
                self.debug("File open()")
                lines = file.readlines()
                nElements = len(lines)
                self.debug("Read %d lines" % (nElements))
                i = 0
                self.prepareProgressBar()
                environment = {'nline': 0, 'group': ''}
                for nline in range(nElements):
                    environment['nline'] = nline
                    self.debug("Processing line %d" % (nline))
                    self._processLine(lines[nline], environment, exceptions)
                    # progressBar
                    self.setProgressBarValue(nline, nElements)
            # file.close()
            self._raiseCollectedExceptions('load', exceptions)
            self.doneProgressBar()
        else:
            raise NameError("No file name specified: %r" % (filename))

    def _processLine(self, line, environment, exceptions):
        if line == '\n':
            self.debug("line with no content")
            pass  # line with no content
        elif self._isSpecialCommentLine(line):
            self.debug("Special Comment line")
            self._recoverSpecialCommentLine(line)
        elif self._isCommentLine(line):
            self.debug("Normal Comment line")
            pass  # Nothing to do with pure comment lines
        elif self._isGroupTagLine(line):
            environment['group'] = line.split()[2]
            self.debug("group tag line: %s" % (environment['group']))
        else:
            group = environment['group']
            attrName, value = self._getAttrLine(line, environment['nline'])
            self.debug("Attribute line: %s = %s" % (attrName, value))
            if group != '' and attrName is not None:
                try:
                    attrStruct = \
                        self._configurationWidgets[group][attrName]
                except:
                    msg = ("attribute %s is not member of the "
                           "group %s" % (attrName, group))
                    self.error(msg)
                    if group in exceptions.keys():
                        exceptions[group].append(attrName)
                    else:
                        exceptions[group] = [attrName]
                else:
                    self.debug("Value2Widget")
                    self._setValueToSaverWidget(attrStruct, value)
            else:
                if group == '':
                    self.warning("No group defined!")
                elif attrName is None:
                    self.warning("No attribute name!")

    # #applyToDevices() ---
    def applyToDevices(self):
        '''Travelling along the *Check, apply the value in *Value
           to the model in the *Reading.
        '''
        exceptions = {}
        self.prepareProgressBar()
        self._iterateAttribute(exceptions)
        self._raiseCollectedExceptions('apply', exceptions)
        self.doneProgressBar()
        self._cleanSpecialCommentsFromFile()

    # Descending level for the applyToDevices() ---
    def _iterateAttribute(self, exceptions):
        i = 0
        nElements = self.getNumberOfElements()
        for group in self._configurationWidgets.keys():
            for attrName in self._configurationWidgets[group]:
                attrStruct = self._configurationWidgets[group][attrName]
                if self._attrIsSelected(attrStruct):
                    self._attrApplyValue(attrName, attrStruct,
                                         group, exceptions)
                # progressBar
                i += 1
                self.setProgressBarValue(i, nElements)

    def _attrIsSelected(self, attrStruct):
        if 'check' in attrStruct and attrStruct['check'].isChecked():
            return True
        return False

    def _attrApplyValue(self, attrName, attrStruct, group, exceptions):
        try:
            value = self._getValueFromSaverWidget(attrStruct)
            self._setAttrValue(attrName, value)
            self._setStyleToNoModified(attrStruct)
        except Exception as e:
            self.error("Exception applying %s: %s"
                       % (attrName, traceback.format_exc()))
            if group in exceptions.keys():
                exceptions[group].append(attrName)
            else:
                exceptions[group] = [attrName]
    # done ActionButtons callbacks ---
    ######

    def _raiseCollectedExceptions(self, operation, exceptions):
        if len(exceptions.keys()) != 0:
            msg = ""
            for group in exceptions.keys():
                msg = ''.join("%sIn group %s, %d values not uploaded\n"
                              % (msg, group, len(exceptions[group])))
                if len(exceptions[group]) > 5:
                    for i in range(5):
                        msg = ''.join("%s\t-%s\n"
                                      % (msg, exceptions[group][i]))
                    msg = ''.join("%s\t ...and another %d\n"
                                  % (msg, len(exceptions[group])-5))
                else:
                    for label in exceptions[group]:
                        msg = ''.join("%s\t-%s\n" % (msg, label))
            QtGui.QMessageBox.warning(self, "Exceptions when %s from "
                                      "devices" % (operation), msg)


def main():
    parser = argparse.get_taurus_parser()
    APPNAME = 'ctlisetup'
    app = TaurusApplication(sys.argv, cmd_line_parser=parser,
                            app_name=APPNAME, app_version=ctliaux.VERSION,
                            org_domain='ALBA', org_name='ALBA')
    options = app.get_command_line_options()
    ctliaux.prepareToLog(app, APPNAME)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
