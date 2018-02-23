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

from taurus.core.taurusbasetypes import TaurusEventType
from taurus.core.util import argparse
from taurus.external.qt import Qt, QtGui
from taurus.qt.qtgui.application import TaurusApplication
from taurus.qt.qtgui.base.taurusbase import TaurusBaseComponent
from taurus.qt.qtgui.container import TaurusWidget
from taurus.qt.qtgui.display import (TaurusLabel, TaurusLed)
from taurus.qt.qtgui.util.ui import UILoadable

from .ctliaux import (VERSION,
                      _setupLed4UnknownAttr,
                      _setupLed4Attr,
                      _setupCheckbox4UnknownAttr,
                      _setupCheckbox4Attr,
                      _setupSpinBox4Attr,
                      _setupTaurusLabel4Attr,
                      _setupCombobox4Attr,
                      _setupActionWidget,
                      prepareToLog,
                      defaultConfigurations,
                      commentsfile,
                      sandbox)

from PyTango import AttributeProxy, DevFailed


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

whiteBackground = "background-color: rgb(255, 255, 255);"
yellowBackground = "background-color: rgb(255, 255, 0);"
blueCharacters = "color: rgb(0, 0, 255);"
blackCharacters = "color: rgb(0, 0, 0);"
fontSize = "font: 7pt \"DejaVu Sans\";"
boldFont = "font-weight: bold;"

modifiedSpinBox = yellowBackground+blueCharacters
wmodifiedSpinBox = yellowBackground+blueCharacters+boldFont
modifiedCheckBox = yellowBackground+blueCharacters
notModifiedSpinBox = whiteBackground+blackCharacters
notModifiedCheckBox = whiteBackground+blackCharacters


class AttrStruct(Qt.QObject, TaurusBaseComponent):

    _attrName = None
    _attrProxy = None
    _attrFormat = None
    _storedValue = None
    _styleMod = False

    _minVal = None
    _maxVal = None
    _decimals = None
    _step = None

    _labelWidget = None
    _readWidget = None
    _writeWidget = None
    _checkWidget = None

    def __init__(self, attrName, label=None, read=None, write=None, check=None,
                 minVal=None, maxVal=None, decimals=None, step=None,
                 *args, **kwargs):
        name = "AttrStruct(%s)" % (attrName.split('/', 2)[2])
        Qt.QObject.__init__(self, None)
        TaurusBaseComponent.__init__(self, name=name, *args, **kwargs)
        self._attrName = attrName
        self._attrProxy = taurus.Attribute(self._attrName)
        self._attrProxy.addListener(self)
        self.taurusEvent.connect(self.filterEvent)
        self._minVal = minVal
        self._maxVal = maxVal
        self._decimals = decimals
        self._step = step
        self.labelWidget = label
        self.readWidget = read
        self.writeWidget = write
        self.subscribeQtChangeEvent()
        self.checkWidget = check

    def __del__(self):
        self._attrProxy.removeListener(self)

    @property
    def attrName(self):
        return self._attrName

    # # widgets ---
    @property
    def labelWidget(self):
        return self._labelWidget

    @labelWidget.setter
    def labelWidget(self, widget):
        if isinstance(widget, QtGui.QLabel):
            self._labelWidget = widget
        else:
            raise AssertionError("Not allowed Label widget type %s"
                                 % (type(widget)))

    @property
    def readWidget(self):
        return self._readWidget

    @readWidget.setter
    def readWidget(self, widget):
        isTaurusLabel = isinstance(widget, TaurusLabel)
        isTaurusLed = isinstance(widget, TaurusLed)
        if isTaurusLabel or isTaurusLed:
            self._readWidget = widget
            if isTaurusLabel:
                model = "%s#rvalue.magnitude" % self._attrName
            else:
                model = self._attrName
            self._readWidget.setModel(model)
            self._storedValue = self.readWidgetValue
            if self._writeWidget is not None and self._storedValue is not None:
                self._changeWriteWidgetValue(self._storedValue)
        else:
            raise AssertionError("Not allowed read widget type %s"
                                 % (type(widget)))

    @property
    def writeWidget(self):
        return self._writeWidget

    @writeWidget.setter
    def writeWidget(self, widget):
        if self.__isCheckBox(widget) or self.__isSpinBox(widget):
            self._writeWidget = widget
            if self._minVal:
                self._writeWidget.setMinimum(self._minVal)
            if self._maxVal:
                self._writeWidget.setMaximum(self._maxVal)
            if self._decimals and hasattr(self._writeWidget, 'setDecimals'):
                self._writeWidget.setDecimals(self._decimals)
            if self._step:
                self._writeWidget.setSingleStep(self._step)
            if self._storedValue is not None:
                self._changeWriteWidgetValue(self._storedValue)
        else:
            raise AssertionError("Not allowed write widget type %s"
                                 % (type(widget)))

    @property
    def checkWidget(self):
        return self._checkWidget

    @checkWidget.setter
    def checkWidget(self, widget):
        if isinstance(widget, QtGui.QCheckBox):
            self._checkWidget = widget
        else:
            raise AssertionError("Not allowed check widget type %s"
                                 % (type(widget)))

    # # interactions ---
    @property
    def attrValue(self):
        value = self._attrProxy.read().rvalue
        if hasattr(value, 'magnitude'):
            value = value.magnitude
        return value

    @property
    def attrWValue(self):
        value = self._attrProxy.read().wvalue
        if hasattr(value, 'magnitude'):
            value = value.magnitude
        return value

    @property
    def attrFormat(self):
        if self._attrFormat is None:
            try:
                attrCfg = AttributeProxy(self.attrName).get_config()
                self._attrFormat = attrCfg.format
            except DevFailed as e:
                self.error("Attribute %s not ready to check format"
                           % self.attrName)
            except Exception as e:
                self.warning("Cannot get attribute format: %s" % (e))
        return self._attrFormat

    @property
    def readWidgetValue(self):
        if self._readWidget is not None:
            value = self._readWidget.getDisplayValue()
            return value

    @property
    def writeWidgetValue(self):
        if self.__isCheckBox():
            return self._writeWidget.isChecked()
        elif self.__isSpinBox():
            return self._writeWidget.value()

    @writeWidgetValue.setter
    def writeWidgetValue(self, value):
        self.debug("%s.writeWidgetValue = %s" % (self.attrName, value))
        self._modifyStyle(value)
        self._changeWriteWidgetValue(value)
        if self.checkWidget:
            if self._styleMod:
                self.checkWidget.setChecked(True)
            else:
                self.checkWidget.setChecked(False)

    def __str2bool(self, string):
        if string.lower() in ["false", "0"]:
            return False
        elif string.lower() in ["true", "1"]:
            return True
        try:
            return bool(string)
        except:
            pass
        return False

    def _changeWriteWidgetValue(self, value):
        # FIXME: rework this
        if isinstance(value, str):
            try:
                strvalue = value
                if strvalue == self._readWidget.getNoneValue():
                    return  # when there is no read from the device
                format = self.attrFormat
                if self.__isCheckBox(self._writeWidget):
                    value = self.__str2bool(strvalue)
                    wtype = "bool"
                elif self.__isIntegerSpinBox(self._writeWidget):
                    value = float(strvalue)
                    if format is not None:
                        value = int(float(format % value))
                    wtype = "int"
                elif self.__isDoubleSpinBox(self._writeWidget):
                    value = float(strvalue)
                    if format is not None:
                        value = float(format % value)
                    wtype = "float"
                self.debug("Convert string value %r "
                           "to write widget type %s: %s"
                           % (strvalue, wtype, value))
            except Exception as e:
                self.error("Exception converting to %r string: %s"
                           % (self.attrFormat, e))
                traceback.print_exc()
                value = None
        if value is not None:
            if self.__isCheckBox():
                # self.info("setChecked(%s)" % (value))
                self._writeWidget.setChecked(value)
            elif self.__isSpinBox():
                self._writeWidget.setValue(value)

    # # events ---
    def eventReceived(self, evt_src, evt_type, evt_value):
        """Reception of the event from tango. Fire an event to be catch by Qt.
        """
        try:
            if evt_type != TaurusEventType['Change']:
                return
            if evt_src.getFullName() != self._attrProxy.getFullName():
                self.warning("eventReceived from %s" % (evt_src))
                return
            if hasattr(evt_value.rvalue, 'magnitude'):
                rvalue = evt_value.rvalue.magnitude
            else:
                rvalue = evt_value.rvalue
            self.debug("eventReceived(%s) previous value %s"
                       % (rvalue, self._storedValue))
            writeWidgetValue = self.writeWidgetValue
            if writeWidgetValue is None or \
                    self._valuesAreDifferent(rvalue, writeWidgetValue):
                self.debug("eventReceived(%s) value changed" % (rvalue))
                TaurusBaseComponent.eventReceived(self, evt_src, evt_type,
                                                  evt_value)
            elif self._styleMod:
                self.debug("eventReceived(%s) equal values but style say its "
                           "modified" % (rvalue))
                TaurusBaseComponent.eventReceived(self, evt_src, evt_type,
                                                  evt_value)
            else:
                self.debug("eventReceived(%s) didn't change" % (rvalue))
        except Exception as e:
            self.error("eventReceived() Exception '%s'" % (e))
            traceback.print_exc()

    def filterEvent(self, evt_src=-1, evt_type=-1, evt_value=-1):
        self.debug("filterEvent(%s)" % (evt_value.rvalue))
        TaurusBaseComponent.filterEvent(self, evt_src, evt_type, evt_value)

    def handleEvent(self, evt_src, evt_type, evt_value):
        """Reception of an event from Qt to be drawn in the GUI.
        """
        try:
            if hasattr(evt_value.rvalue, 'magnitude'):
                rvalue = evt_value.rvalue.magnitude
            else:
                rvalue = evt_value.rvalue
            self.debug("handleEvent(%s (%s)) previous stored value %s"
                       "(readWidget %s, writeWidget %s)"
                       % (rvalue, evt_value.quality,
                          self._storedValue, self.readWidgetValue,
                          self.writeWidgetValue))
            self._modifyStyle(rvalue, fromTaurus=True)
        except Exception as e:
            self.error("handleEvent() Exception '%s'" % (e))
            traceback.print_exc()

    def subscribeQtChangeEvent(self):
        if self.__isCheckBox():
            signalName = 'stateChanged(int)'
        elif self.__isIntegerSpinBox():
            signalName = 'valueChanged(int)'
        elif self.__isDoubleSpinBox():
            signalName = 'valueChanged(double)'
        else:
            self.error("Unsupported widget to connect Qt signal")
            return
        Qt.QObject.connect(self.writeWidget, Qt.SIGNAL(signalName),
                           self.changeEvent)

    def changeEvent(self, evt):
        try:
            self._modifyStyle(evt, fromQt=True)
        except Exception as e:
            self.error("changeEvent() Exception '%s'" % (e))
            traceback.print_exc()

    # # low level ---
    def __isCheckBox(self, widget=None):
        if widget is None:
            widget = self._writeWidget
        return isinstance(widget, QtGui.QCheckBox)

    def __isSpinBox(self, widget=None):
        return self.__isIntegerSpinBox(widget) or \
            self.__isDoubleSpinBox(widget)

    def __isIntegerSpinBox(self, widget=None):
        if widget is None:
            widget = self._writeWidget
        return isinstance(widget, QtGui.QSpinBox)

    def __isDoubleSpinBox(self, widget=None):
        if widget is None:
            widget = self._writeWidget
        return isinstance(widget, QtGui.QDoubleSpinBox)

    def _modifyStyle(self, newValue, fromTaurus=False, fromQt=False):
        if not fromTaurus and not fromQt:
            # self.info("Write widget value modified")
            refValue = value = self.writeWidgetValue
            if self._valuesAreDifferent(newValue, refValue):
                self._styleMod = True
            else:
                self._styleMod = False
            style = self.__buildStyle(self._styleMod, yellow=True)
        else:
            if fromTaurus:
                # self.info("Modification from Taurus")
                refValue = value = self.writeWidgetValue
                if self._valuesAreDifferent(newValue, refValue):
                    if self._styleMod:
                        style = None  # ignore
                    else:
                        self._styleMod = True
                        style = self.__buildStyle(self._styleMod)
                else:
                    self._styleMod = False
                    style = self.__buildStyle(self._styleMod)
            if fromQt:
                # self.info("Modification from Qt")
                refValue = value = self.readWidgetValue
                if self._valuesAreDifferent(newValue, refValue):
                    if self._styleMod:
                        style = None  # ignore
                    else:
                        self._styleMod = True
                        style = self.__buildStyle(self._styleMod)
                else:
                    self._styleMod = False
                    style = self.__buildStyle(self._styleMod)
        if style is not None:
            self.writeWidget.setStyleSheet(style)

    def __buildStyle(self, modified, yellow=False):
        newStyle = ""
        if modified:
            if yellow:
                newStyle += yellowBackground
            newStyle += blueCharacters+boldFont
            self.checkWidget.setChecked(True)
        else:
            self.checkWidget.setChecked(False)
        newStyle += fontSize
        self.debug("newStyle: %r" % (newStyle))
        return newStyle

    def _valuesAreDifferent(self, v1, v2):
        try:
            self.debug("Compare %s (%s) with %s (%s) (format: %r)"
                       % (v1, type(v1), v2, type(v2), self.attrFormat))
            if self.__isCheckBox():
                for v in [v1, v2]:
                    if type(v) == str:
                        v = self.__str2bool(v)
                    else:
                        v = bool(v)
                return v1 != v2
            elif self.attrFormat is not None:
                if not isinstance(v1, str):
                    value1 = self.attrFormat % v1
                else:
                    value1 = v1
                if not isinstance(v2, str):
                    value2 = self.attrFormat % v2
                else:
                    value2 = v2
                return float(value1) != float(value2)
            else:
                return float(v1) != float(v2)
        except Exception as e:
            self.error("Cannot compare %s and %s: %s" % (v1, v2, e))
            return False

    def setReadValueToWriteWidget(self):
        self._changeWriteWidgetValue(self.readWidgetValue)
        if self.checkWidget:
            self.checkWidget.setChecked(False)


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
            self.loadUi(filename="linacconfigurationscreen.ui",
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
        self.setProgressBarValue(1, 1)
        self.doneProgressBar()  # self.ui.progressBar.hide()  # setValue(100)
        self._statusMsgLst = []

    def initComponents(self):
        # if hasattr(self.parent(),'setWindowTitle'):
        #     self.parent().setWindowTitle("Linac Save/Retrieve Interface")
        self.setWindowTitle("Linac Save/Retrieve Interface")
        if hasattr(self.parent(), 'setCentralWidget'):
            self.centralwidget = self.ui.centralFrame
            self.setCentralWidget(self.centralwidget)
        self.setConfiguration()
        # self.loadFromDevices()

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
        widgetsSet[attrName] = AttrStruct(attrName,
                                          ui.GunFilamentLowVoltageLabel,
                                          ui.GunFilamentLowVoltageRead,
                                          ui.GunFilamentLowVoltageWrite,
                                          ui.GunFilamentLowVoltageCheck,
                                          minVal=0.0, maxVal=10.0, step=0.1,)

        attrName = '%s/Gun_kathode_v_setpoint' % (devName)
        attrName = attrName.lower()
        widgetsSet[attrName] = AttrStruct(attrName,
                                          ui.GunKathodeLowVoltageLabel,
                                          ui.GunKathodeLowVoltageRead,
                                          ui.GunKathodeLowVoltageWrite,
                                          ui.GunKathodeLowVoltageCheck,
                                          minVal=0.0, maxVal=50.0, step=0.1)

        attrName = '%s/Gun_hv_v_setpoint' % (devName)
        attrName = attrName.lower()
        widgetsSet[attrName] = AttrStruct(attrName,
                                          ui.GunHighVoltagePowerSupplyLabel,
                                          ui.GunHighVoltagePowerSupplyRead,
                                          ui.GunHighVoltagePowerSupplyWrite,
                                          ui.GunHighVoltagePowerSupplyCheck,
                                          minVal=-90.0, maxVal=0.0, step=0.1)

        self._configurationWidgets['eGun'] = widgetsSet

    def coolingLoopsConfiguration(self, ui):
        devName = 'li/ct/plc2'
        widgetsSet = {}

        # CL1
        attrName = '%s/cl1_t_setpoint' % (devName)
        attrName = attrName.lower()
        widgetsSet[attrName] = AttrStruct(attrName,
                                          ui.coolingLoop1SetpointLabel,
                                          ui.coolingLoop1SetpointRead,
                                          ui.coolingLoop1SetpointWrite,
                                          ui.coolingLoop1SetpointCheck,
                                          minVal=0.0, maxVal=50.0, step=0.1)
        # CL2
        attrName = '%s/cl2_t_setpoint' % (devName)
        attrName = attrName.lower()
        widgetsSet[attrName] = AttrStruct(attrName,
                                          ui.coolingLoop2SetpointLabel,
                                          ui.coolingLoop2SetpointRead,
                                          ui.coolingLoop2SetpointWrite,
                                          ui.coolingLoop2SetpointCheck,
                                          minVal=0.0, maxVal=50.0, step=0.1)
        # CL3
        attrName = '%s/cl3_t_setpoint' % (devName)
        attrName = attrName.lower()
        widgetsSet[attrName] = AttrStruct(attrName,
                                          ui.coolingLoop3SetpointLabel,
                                          ui.coolingLoop3SetpointRead,
                                          ui.coolingLoop3SetpointWrite,
                                          ui.coolingLoop3SetpointCheck,
                                          minVal=0.0, maxVal=50.0, step=0.1)

        self._configurationWidgets['coolingLoop'] = widgetsSet

    def vacuumValvesConfiguration(self, ui):
        widgetsSet = {}

        attrName = 'li/ct/plc2/VCV_ONC'.lower()
        widgetsSet[attrName] = AttrStruct(attrName,
                                          ui.VaccumCollimatorValveLabel,
                                          ui.VaccumCollimatorValveRead,
                                          ui.VaccumCollimatorValveWrite,
                                          ui.VaccumCollimatorValveCheck)

        self._configurationWidgets['vacuumValves'] = widgetsSet

    def magnetsConfiguration(self, ui):
        widgetsSet = {}

        magnets = {'sl': {'1': ['H', 'V', 'F'], '2': ['H', 'V', 'F'],
                          '3': ['H', 'V', 'F'], '4': ['H', 'V', 'F']},
                   'bc': {'1': ['H', 'V', 'F'], '2': ['H', 'V', 'F']},
                   'gl': {'':  ['H', 'V', 'F']},
                   'as': {'1': ['H', 'V'], '2': ['H', 'V']},
                   'qt': {'1': ['H', 'V', 'F'], '2': ['F']}}

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
                    if component in ['H', 'V']:
                        if family == 'qt':
                            minVal, maxVal = -16, 16
                        else:
                            minVal, maxVal = -2, 2
                        step, decimals = 0.01, 2
                    else:
                        if family == 'sl':
                            minVal, maxVal, step, decimals = 0, 1, 0.01, 2
                        elif family == 'bc':
                            minVal, maxVal, step, decimals = 0, 200, 0.01, 2
                        elif family == 'gl':
                            minVal, maxVal, step, decimals = 0, 130, 0.01, 2
                        elif family == 'qt':
                            minVal, maxVal, step, decimals = 0, 6, 0.005, 3
                    widgetsSet[attrName] = AttrStruct(attrName, labelWidget,
                                                      readWidget, writeWidget,
                                                      checkWidget,
                                                      minVal=minVal,
                                                      maxVal=maxVal, step=step,
                                                      decimals=decimals)
        # TODO: connect the ToApplyTitle to check/uncheck all the *Check ---
        self._configurationWidgets['magnets'] = widgetsSet

    def radiofrequencyConfiguration(self, ui):
        widgetsSet = {}

        attrName = 'li/ct/plc1/TPS0_Phase'.lower()
        widgetsSet[attrName] = AttrStruct(attrName, ui.TPS0PhaseLabel,
                                          ui.TPS0PhaseRead, ui.TPS0PhaseWrite,
                                          ui.TPS0PhaseCheck, minVal=0.0,
                                          maxVal=380, decimals=1, step=0.1)

        attrName = 'li/ct/plc1/TPSX_Phase'.lower()
        widgetsSet[attrName] = AttrStruct(attrName, ui.TPSXPhaseLabel,
                                          ui.TPSXPhaseRead, ui.TPSXPhaseWrite,
                                          ui.TPSXPhaseCheck, minVal=0.0,
                                          maxVal=380, decimals=0, step=1)

        attrName = 'li/ct/plc1/TPS1_Phase'.lower()
        widgetsSet[attrName] = AttrStruct(attrName, ui.TPS1PhaseLabel,
                                          ui.TPS1PhaseRead, ui.TPS1PhaseWrite,
                                          ui.TPS1PhaseCheck, minVal=0.0,
                                          maxVal=380, decimals=0, step=1)

        attrName = 'li/ct/plc1/TPS2_Phase'.lower()
        widgetsSet[attrName] = AttrStruct(attrName, ui.TPS2PhaseLabel,
                                          ui.TPS2PhaseRead, ui.TPS2PhaseWrite,
                                          ui.TPS2PhaseCheck, minVal=0.0,
                                          maxVal=380, decimals=0, step=1)

        attrName = 'li/ct/plc1/A0_OP'.lower()
        widgetsSet[attrName] = AttrStruct(attrName, ui.A0OPLabel,
                                          ui.A0OPRead, ui.A0OPWrite,
                                          ui.A0OPCheck, minVal=75, maxVal=760,
                                          decimals=0, step=1)

        attrName = 'li/ct/plc1/ATT2_P_setpoint'.lower()
        widgetsSet[attrName] = AttrStruct(attrName, ui.ATT2Label,
                                          ui.ATT2Read, ui.ATT2Write,
                                          ui.ATT2Check, minVal=-10.0, maxVal=0,
                                          decimals=1, step=0.1)

        attrName = 'li/ct/plc1/PHS1_Phase_setpoint'.lower()
        widgetsSet[attrName] = AttrStruct(attrName, ui.PHS1Label,
                                          ui.PHS1Read, ui.PHS1Write,
                                          ui.PHS1Check, minVal=0.0, maxVal=160,
                                          decimals=0, step=1)

        attrName = 'li/ct/plc1/PHS2_Phase_setpoint'.lower()
        widgetsSet[attrName] = AttrStruct(attrName, ui.PHS2Label,
                                          ui.PHS2Read, ui.PHS2Write,
                                          ui.PHS2Check, minVal=0.0, maxVal=380,
                                          decimals=0, step=1)

        self._configurationWidgets['radioFrequency'] = widgetsSet

    def timingConfiguration(self, ui):
        widgetsSet = {}

        attrName = 'li/ct/plc1/TB_MBM'.lower()
        widgetsSet[attrName] = AttrStruct(attrName, ui.MBMLabel, ui.MBMRead,
                                          ui.MBMWrite, ui.MBMCheck)

        attrName = 'li/ct/plc1/TB_GUN_delay'.lower()
        widgetsSet[attrName] = AttrStruct(attrName, ui.GunDelayLabel,
                                          ui.GunDelayRead, ui.GunDelayWrite,
                                          ui.GunDelayCheck, minVal=32,
                                          maxVal=4096, step=32)

        attrName = 'li/ct/plc1/TB_ka1_delay'.lower()
        widgetsSet[attrName] = AttrStruct(attrName, ui.ka1DelayLabel,
                                          ui.ka1DelayRead, ui.ka1DelayWrite,
                                          ui.ka1DelayCheck, minVal=1,
                                          maxVal=56, step=1)

        attrName = 'li/ct/plc1/TB_ka2_delay'.lower()
        widgetsSet[attrName] = AttrStruct(attrName, ui.ka2DelayLabel,
                                          ui.ka2DelayRead, ui.ka2DelayWrite,
                                          ui.ka2DelayCheck, minVal=2720,
                                          maxVal=4096, step=32)

        attrName = 'li/ct/plc1/TB_GPI'.lower()
        widgetsSet[attrName] = AttrStruct(attrName, ui.GPILabel,
                                          ui.GPIRead, ui.GPIWrite,
                                          ui.GPICheck, minVal=6, maxVal=1054,
                                          step=2)

        attrName = 'li/ct/plc1/TB_GPN'.lower()
        widgetsSet[attrName] = AttrStruct(attrName, ui.GPNLabel, ui.GPNRead,
                                          ui.GPNWrite, ui.GPNCheck, minVal=1,
                                          maxVal=16, step=1)

        attrName = 'li/ct/plc1/TB_GPA'.lower()
        widgetsSet[attrName] = AttrStruct(attrName, ui.GPALabel, ui.GPARead,
                                          ui.GPAWrite, ui.GPACheck,
                                          minVal=-40.0, maxVal=0, decimals=1,
                                          step=0.1)

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
                widgetsSet[attrName] = AttrStruct(attrName, Label, Read,
                                                  Write, Check, minVal=0,
                                                  maxVal=1e10, step=8,
                                                  decimals=0)

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
                        AttrStruct(attrName, getattr(ui, 'ka%dHVPSLabel'
                                                     % (number)),
                                   getattr(ui, 'ka%dHVPSRead' % (number)),
                                   getattr(ui, 'ka%dHVPSWrite' % (number)),
                                   getattr(ui, 'ka%dHVPSCheck' % (number)),
                                   minVal=0.0, maxVal=33, decimals=1, step=0.1)
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
        rstButton = buttons.button(QtGui.QDialogButtonBox.Reset)
        rstButton.setText("Reload")
        rstButton.clicked.connect(self.loadFromDevices)
        rstButton.setDefault(True)
        saveButton = buttons.button(QtGui.QDialogButtonBox.Save)
        saveButton.clicked.connect(self.saveToFile)
        openButton = buttons.button(QtGui.QDialogButtonBox.Open)
        openButton.clicked.connect(self.loadFromFile)
        applyButton = buttons.button(QtGui.QDialogButtonBox.Apply)
        applyButton.clicked.connect(self.applyToDevices)

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
    def _setStyleToModified(self, attrStruct, wvalueChange=False):
        saver = attrStruct.writeWidget
        if self._isSpinBox(saver):
            if wvalueChange:
                saver.setStyleSheet(blueCharacters+fontSize)
            else:
                saver.setStyleSheet(yellowBackground+blueCharacters+fontSize)
        elif self._isCheckBox(saver):
            saver.setStyleSheet(yellowBackground+blueCharacters)
        else:
            raise Exception("Unmanaged %s widget type to tag modified"
                            % (type(widget)))
        attrStruct.checkWidget.setChecked(True)

    def _setStyleToNoModified(self, attrStruct):
        saver = attrStruct.writeWidget
        if self._isSpinBox(saver):
            saver.setStyleSheet(whiteBackground+blackCharacters+fontSize)
        elif self._isCheckBox(saver):
            saver.setStyleSheet(blackCharacters)
        else:
            raise Exception("Unmanaged %s widget type to tag modified"
                            % (type(widget)))
        attrStruct.checkWidget.setChecked(False)
    # done widget backgrounds ---
    ######

    ######
    # # Value setters and getters ---
    def _getAttrValue(self, attrName):
        value = taurus.Attribute(attrName).read().rvalue
        if hasattr(value, 'magnitude'):
            value = value.magnitude
        return value

    def _getAttrWValue(self, attrName):
        value = taurus.Attribute(attrName).read().wvalue
        if hasattr(value, 'magnitude'):
            value = value.magnitude
        return value

    def _setAttrValue(self, attrName, value):
        rvalue = self._getAttrValue(attrName)
        writeNearResult = None
        if value == rvalue:
            self.warning("Write near feature requested for %s and %g value"
                         % (attrName, value))
            self.appendStatusBarMsg("(write near for %s = %g)"
                                    % (attrName, value))
            # hackish to because we've seen some attributes not well applied
            # and we don't have rights to study further why this had happen
            writeNearResult = self._nearWrite(attrName, value)
            self.popOneStatusBarMsg()
        self.info('_setAttrValue(%s, %s) (%s)'
                  % (attrName, value, type(value)))
        try:
            taurus.Attribute(attrName).write(value)
        except Exception as e:
            self.error("Exception in the %s write(%s) operation: %s\n%s"
                       % (attrName, value, e, traceback.format_exc()))
            raise ValueError("Write operation failed")
        self._checkReadWrite(attrName, rvalue, value)
        if writeNearResult is not None and not writeNearResult:
            raise ValueError("Write near operation failed")

    def _nearWrite(self, attrName, value):
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
                    # FIXME: it would have an step bigger than 1
                    taurus.Attribute(attrName).write(int(value+1))
                except:
                    try:
                        time.sleep(0.3)
                        taurus.Attribute(attrName).write(int(value-1))
                    except:
                        self.error("It hasn't been possible to write a near "
                                   "setpoint for attribute %s" % (attrName))
                        return False
                time.sleep(0.3)
            elif type(value) == float:
                try:
                    near = 0.99
                    taurus.Attribute(attrName).write(value*near)
                    time.sleep(0.3)
                except:
                    return False
            return True
        except Exception as e:
            # in boundary cases it had seen that this produces an exception
            # but it's not a blocking issue and we can continue.
            self.warning("Attribute %s fail the '%s' hackish: "
                         "value=%g value*near=%g. The exception was: %s"
                         % (attrName, near, value, value*near, e))
            return False

    def _checkReadWrite(self, attrName, rvalue, wvalue):
        # check if the write has been acknowledge by the plc reading
        i = 0
        waitTime = 0.3  # (1 second of rechecks maximum)
        while i < 10:
            if self._checkValue(rvalue, wvalue, attrName):
                self.warning("For %s, reading corresponds to what has been "
                             "written: %s (%d)" % (attrName, rvalue, i))
                return
            i += 1
            self.warning("For %s, read value %g didn't correspond with write "
                         "value %g. Wait %f seconds and retry (%d)"
                         % (attrName, rvalue, wvalue, waitTime, i))
            time.sleep(waitTime)
            rvalue = self._getAttrValue(attrName)
        raise ValueError("The attribute reading (%s) didn't "
                         "correspond to what has been set (%s)"
                         % (rvalue, wvalue))

    def _checkValue(self, a, b, attrName):
        # With bools and integers the compare is simple, but floats,
        # because of the different byte precisions, can be equivalent
        # not being exacly the same.
        if isinstance(a,float) or isinstance(b, float):
            if a == b:
                return True
            try:
                attr = AttributeProxy(attrName)
                attrFormat = attr.get_config().format
            except Exception as e:
                self.error("It hasn't been possible to get %s's format: %s"
                           % (attrName, e))
                attrFormat = '%6.3f'
            aStr = attrFormat % a
            bStr = attrFormat % b
            if aStr == bStr:
                self.warning("For %s, the format (%s) representation matches, "
                             "even the floats would not be exactly equal "
                             "%g != %g" % (attrName, attrFormat, a, b))
                return True
            # self.warning("For attribute %s %g != %g "
            #              "(representations %s != %s)"
            #               % (attrName, a, b, aStr, bStr))
        else:
            return a == b
        return False

    def _getValueFromSaverWidget(self, attrStruct):
        saver = attrStruct.writeWidget
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
                                             defaultConfigurations))
        if not directory == '' and not directory.startswith(sandbox):
            QtGui.QMessageBox.warning(
                self, "Sandbox warning", "Your selected directory is not in "
                "the storage shared by NFS")
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
        msg, ok = QtGui.QInputDialog.getText(
            self, "Select file name", "would you like to write something "
            "after the file prefix %s?" % (prefix), QtGui.QLineEdit.Normal)
        return (str(msg), ok)

    def _requestFileName(self):
        dialogTitle = "Select linac's configuration file"
        filters = "Linac configuration (*.li);;All files (*)"
        return str(QtGui.QFileDialog.
                   getOpenFileName(self, dialogTitle,
                                   defaultConfigurations, filters))

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
        tag = attrStruct.labelWidget.text()
        rvalue = attrStruct.attrValue
        # to raise exception if not available:
        wvalue = self._getValueFromSaverWidget(attrStruct)
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
        if os.path.isfile(commentsfile):
            with open(commentsfile, 'r') as file:
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
        with open(commentsfile, 'w') as file:
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
        self.ui.progressBar.setEnabled(True)
        self.ui.progressBar.setValue(0)

    def getNumberOfElements(self):
        nElements = 0
        for group in self._configurationWidgets.keys():
            nElements += len(self._configurationWidgets[group].keys())
        return nElements

    def getPending2ApplyElements(self):
        n = 0
        elements = []
        for group in self._configurationWidgets.keys():
            for attrName in self._configurationWidgets[group].keys():
                attrStruct = self._configurationWidgets[group][attrName]
                if attrStruct.checkWidget.isChecked():
                    n += 1
                    elements.append(attrName)
        return n, elements

    def setProgressBarValue(self, i, nElements):
        self.ui.progressBar.setValue(i*100/nElements)

    def doneProgressBar(self):
        self.ui.progressBar.setEnabled(False)

    def setWorkingAttrText(self, attrName):
        self.ui.workingAttr.setText(attrName)

    def setStatusBarMsg(self, msg):
        self._statusMsgLst = [msg]
        self._updateStatusBarMsg()

    def appendStatusBarMsg(self, msg):
        self._statusMsgLst.append(msg)
        self._updateStatusBarMsg()

    def appendTemporalStatusBarMsg(self, msg):
        self._updateStatusBarMsg([msg])

    def popOneStatusBarMsg(self):
        self._statusMsgLst.pop()
        self._updateStatusBarMsg()

    def cleanStatusBar(self):
        self._statusMsgLst = []
        self._updateStatusBarMsg()

    def _updateStatusBarMsg(self, extraLst=None):
        msg = ""
        for each in self._statusMsgLst:
            msg = ''.join("%s %s" % (msg, each))
        try:
            for each in extraLst:
                msg = ''.join("%s %s" % (msg, each))
        except:
            pass
        self.ui.statusBar.setText(msg)

    ######
    # # ActionButtons callbacks ---
    def loadFromDevices(self):
        '''With this call (from a button or at the loading step) we must travel
           all the *Reading widgets and copy the value to the *Value widget.
        '''
        exceptions = {}
        # prepare progress bar
        self.prepareProgressBar()
        self.setStatusBarMsg("Loading values from devices")
        nElements = self.getNumberOfElements()
        i = 0
        for group in self._configurationWidgets.keys():
            self.debug(">  %s" % group)
            for attrName in self._configurationWidgets[group].keys():
                attrStruct = self._configurationWidgets[group][attrName]
                try:
                    attrStruct.setReadValueToWriteWidget()
                except Exception as e:
                    self.error("Exception trying to load %s value. %s"
                               % (attrName, e))
                    label = str(attrStruct.labelWidget.text())
                    self.__collectLoadExceptions(group, label, exceptions)
                # progressbar
                i += 1
                self.setProgressBarValue(i, nElements)
        self._raiseCollectedExceptions("load", exceptions)
        self.doneProgressBar()
        self.cleanStatusBar()

    def __collectLoadExceptions(self, group, label, exceptions):
        if group in exceptions.keys():
            exceptions[group].append(str(label))
        else:
            exceptions[group] = [str(label)]

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
            self.setStatusBarMsg("Saving to file: %r" % (filename))
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
            self.cleanStatusBar()

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
            msg = "Loading from file: %r" % (filename)
            self.debug(msg)
            self.setStatusBarMsg(msg)
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
            self.cleanStatusBar()
        # else:
        #     raise NameError("No file name specified: %r"%(filename))

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
                    attrStruct.writeWidgetValue = value
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
        klystronInformation = {}
        self.prepareProgressBar()
        self.setStatusBarMsg("Applying values to devices:")
        self._collectKlystronStatus(klystronInformation, 'pre')
        self._iterateAttribute(exceptions)
        self._raiseCollectedExceptions('apply', exceptions)
        self.doneProgressBar()
        self.cleanStatusBar()
        self._collectKlystronStatus(klystronInformation, 'post')
        self._evaluateKlystronStatus(klystronInformation)
        self._cleanSpecialCommentsFromFile()

    # Descending level for the applyToDevices() ---
    def _iterateAttribute(self, exceptions):
        i = 0
        nElements = self.getNumberOfElements()
        groups = self._configurationWidgets.keys()
        groups.sort()
        for group in groups:
            self.appendStatusBarMsg("group '%s'" % (group))
            attributeNames = self._configurationWidgets[group].keys()
            attributeNames.sort()
            for attrName in attributeNames:
                attrStruct = self._configurationWidgets[group][attrName]
                if self._attrIsSelected(attrStruct):
                    self._attrApplyValue(attrName, attrStruct,
                                         group, exceptions)
                # progressBar
                i += 1
                self.setProgressBarValue(i, nElements)
            self.popOneStatusBarMsg()

    def _attrIsSelected(self, attrStruct):
        if attrStruct.checkWidget.isChecked():
            return True
        return False

    def _attrApplyValue(self, attrName, attrStruct, group, exceptions):
        try:
            value = self._getValueFromSaverWidget(attrStruct)
            self._setAttrValue(attrName, value)
            self._setStyleToNoModified(attrStruct)
        except Exception as e:
            msg = "Exception applying %s" % (attrName)
            self.appendTemporalStatusBarMsg(msg)
            self.error("%s: %s" % (msg, traceback.format_exc()))
            if group in exceptions.keys():
                exceptions[group].append(attrName)
            else:
                exceptions[group] = [attrName]
    # done ActionButtons callbacks ---
    ######

    def _raiseCollectedExceptions(self, operation, exceptions):
        msg = ""
        if len(exceptions.keys()) != 0:
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
        n, attrLst = self.getPending2ApplyElements()
        if operation in ["apply"] and n > 0:
            msg = ''.join("%s%d values change from outside the "
                          "application:\n" % (msg, n))
            if len(attrLst) > 5:
                for i in range(5):
                    msg = ''.join("%s\t%s" % (msg, attrLst[i]))
                msg = ''.join("%s\t ...and another %d\n"
                              % (msg, len(attrLst)-5))
            else:
                for attrName in attrLst:
                    msg = ''.join("%s\t-%s\n" % (msg, attrName))
        if len(msg) > 0:
            QtGui.QMessageBox.warning(self, "Exceptions when %s from "
                                      "devices" % (operation), msg)

    def _collectKlystronStatus(self, infoDct, situation):
        try:
            HVPSstate = "li/ct/plc%d/HVPS_ST"
            HVPSstatus = "li/ct/plc%d/HVPS_Status"
            for klystron in [4, 5]:
                try:
                    if klystron not in infoDct:
                        infoDct[klystron] = {}
                    state = taurus.Attribute(HVPSstate % klystron)
                    status = taurus.Attribute(HVPSstatus % klystron)
                    infoDct[klystron][situation] = [state.read().rvalue,
                                                    status.read().rvalue]
                except Exception as e:
                    self.error("Exception building current klystron %d status"
                               % klystron-3)
        except Exception as e:
            self.error("Cannot get the klystron status: %s" % (e))

    def _evaluateKlystronStatus(self, infoDct):
        msg = ""
        interlock = []
        for klystron in [4, 5]:
            if klystron in infoDct:
                if 'post' in infoDct[klystron]:
                    if 'pre' in infoDct[klystron]:
                        pre = infoDct[klystron]['pre']
                        post = infoDct[klystron]['post']
                        if pre[0] != post[0]:
                            submsg = "klystron %d has change status from %s "\
                                "to %s" % (klystron, pre[1], post[1])
                            self.warning(submsg)
                        else:
                            submsg = "klystron %d has still the same status "\
                                "%s" % (klystron, post[1])
                        msg = ''.join("%s%s\n" % (msg, submsg))
                    if post[0] in [6]:  # this is the interlock code
                        submsg = "Found klystron %d in interlock status"\
                                 % (klystron)
                        self.warning(submsg)
                        msg = ''.join("%s%s\n" % (msg, submsg))
                        interlock.append(True)
                    else:
                        interlock.append(False)
            else:
                self.error("klystron %d not in %s"
                           % (klystron-3, infoDct.keys()))
        if any(interlock):
            answer = QtGui.QMessageBox.warning(self, "KLYSTRON interlock:",
                                               msg, "Reset", "Ignore")
            if answer == 0:  # "reset"
                rstAttr = "li/ct/plc%d/HVPS_Interlock_RC"
                for klystron, value in enumerate(interlock):
                    if value:
                        attrName = rstAttr % (klystron+4)
                        attr = taurus.Attribute(attrName)
                        attr.write(True)
                self.info("klystron interlocks reseted")
            else:
                self.info("Ignore the klystron interlocks")


def main():
    parser = argparse.get_taurus_parser()
    APPNAME = 'ctlisetup'
    app = TaurusApplication(sys.argv, cmd_line_parser=parser,
                            app_name=APPNAME, app_version=VERSION,
                            org_domain='ALBA', org_name='ALBA')
    options = app.get_command_line_options()
    prepareToLog(app, APPNAME)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
