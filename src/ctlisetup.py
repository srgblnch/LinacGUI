#!/usr/bin/env python

#############################################################################
##
## This file is part of Taurus, a Tango User Interface Library
## 
## http://www.tango-controls.org/static/taurus/latest/doc/html/index.html
##
## Copyright 2013 CELLS / ALBA Synchrotron, Bellaterra, Spain
## 
## Taurus is free software: you can redistribute it and/or modify
## it under the terms of the GNU Lesser General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
## 
## Taurus is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU Lesser General Public License for more details.
## 
## You should have received a copy of the GNU Lesser General Public License
## along with Taurus.  If not, see <http://www.gnu.org/licenses/>.
##
###########################################################################

import os,sys
import time
import traceback

#The widgets are stored in a subdirectory and needs to be added to the pythonpath
linacWidgetsPath = os.environ['PWD']+'/widgets'
if not linacWidgetsPath in sys.path:
    sys.path.append(linacWidgetsPath)

from taurus.core.util import argparse
from taurus.qt.qtgui.application import TaurusApplication
from taurus.qt.qtgui.container import TaurusMainWindow
from taurus.qt import Qt,QtGui

import ctliaux

import PyTango

from ui_linacConfigurationScreen import Ui_linacConfigurationScreen

#---- storage sandbox
sandbox = '/data'

def dump(obj, nested_level=0, output=sys.stdout):
    """Method found in http://stackoverflow.com/questions/15785719/how-to-print-a-dictionary-line-by-line-in-python
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
                print >> output, '%s%s: %s' % ((nested_level + 1) * spacing, k, v)
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

class MainWindow(TaurusMainWindow):
    def __init__(self, parent=None):
        TaurusMainWindow.__init__(self)
        # setup main window
        self.ui = Ui_linacConfigurationScreen()
        self.ui.setupUi(self)
        #place the ui in the window
        self.initComponents()
        #kill splash screen
        self.splashScreen().finish(self)

    def initComponents(self):
        self.centralwidget = self.ui.centralFrame
        self.setCentralWidget(self.centralwidget)
        self.setConfiguration()
        self.loadFromDevices()
    
    ######
    #---- Auxiliar methods to configure widgets
    def _setupLed4UnknownAttr(self,widget):
        ctliaux._setupLed4UnknownAttr(widget)

    def _setupLed4Attr(self,widget,attrName,inverted=False,onColor='green',offColor='red',pattern='on'):
        ctliaux._setupLed4Attr(widget,attrName,inverted,onColor,offColor,pattern)

    def _setupCheckbox4UnknownAttr(self,widget):
        ctliaux._setupCheckbox4UnknownAttr(widget)

    def _setupCheckbox4Attr(self,widget,attrName,
                            isRst=False,DangerMsg='',
                            riseEdge=False,fallingEdge=False):
        ctliaux._setupCheckbox4Attr(widget,attrName,
                                    isRst,DangerMsg,riseEdge,fallingEdge)

    def _setupSpinBox4Attr(self,widget,attrName,step=None):
        ctliaux._setupSpinBox4Attr(widget,attrName,step)

    def _setupTaurusLabel4Attr(self,widget,attrName,unit=None):
        ctliaux._setupTaurusLabel4Attr(widget,attrName,unit)

    def _setupCombobox4Attr(self,widget,attrName,valueNames=None):
        ctliaux._setupCombobox4Attr(self,widget,attrName,valueNames)

    def _setupActionWidget(self,widget,attrName,text='on/off',isRst=False,
                           DangerMsg='',riseEdge=False,fallingEdge=False):
        ctliaux._setupActionWidget(widget,attrName,text,isRst,
                           DangerMsg,riseEdge,fallingEdge)
    
    def _setupQSpinBox(self,widget,min=0,max=99,decimals=2,step=1):
        widget.setMinimum(min)
        widget.setMaximum(max)
        if hasattr(widget,'setDecimals'):
            widget.setDecimals(decimals)
        widget.setSingleStep(step)
    #---- Done auxiliar methods to configure widgets
    ######
    
    ######
    #---- setModel & others for the Configuration Tab
    def setConfiguration(self):
        configuration_ui = self.ui
        self._configurationWidgets = {}
        #---- configure the widgets in the panels
        self.electronGunConfiguration(configuration_ui.electronGunSnapshot._ui)
        self.coolingLoopsConfiguration(configuration_ui.coolingLoopSnapshot._ui)
        self.vacuumValvesConfiguration(configuration_ui.vacuumValveSnapshot._ui)
        self.magnetsConfiguration(configuration_ui.magnetSnapshot._ui)
        self.radiofrequencyConfiguration(configuration_ui.radioFrequencySnapshot._ui)
        self.timingConfiguration(configuration_ui.timingSnapshot._ui)
        self.klystronsConfiguration(configuration_ui.klystronSnapshot._ui)
        self.commentConfiguration(configuration_ui)
        
        
        #---- connect buttons to their actions
        self.buttonsConfiguration(configuration_ui.buttonBox)
        # Those actions doesn't need DangerMessage because eGunLV, CLs and KaLV
        # are not included in the save/retrive
        
    def electronGunConfiguration(self,ui):
        devName = 'li/ct/plc1'
        widgetsSet = {}
        
        attrName = '%s/GUN_Filament_V_setpoint'%(devName)
        attrName = attrName.lower()
        widgetsSet[attrName] = {'label':ui.GunFilamentLowVoltageLabel,
                                'read': ui.GunFilamentLowVoltageRead,
                                'write':ui.GunFilamentLowVoltageWrite,
                                'check':ui.GunFilamentLowVoltageCheck}
        self._setupTaurusLabel4Attr(widgetsSet[attrName]['read'],attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            min=0.0,max=10.0,step=0.1)
        
        attrName = '%s/Gun_kathode_v_setpoint'%(devName)
        attrName = attrName.lower()
        widgetsSet[attrName] = {'label':ui.GunKathodeLowVoltageLabel,
                                'read': ui.GunKathodeLowVoltageRead,
                                'write':ui.GunKathodeLowVoltageWrite,
                                'check':ui.GunKathodeLowVoltageCheck}
        self._setupTaurusLabel4Attr(widgetsSet[attrName]['read'],attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            min=0.0,max=50.0,step=0.1)
        
        attrName = '%s/Gun_hv_v_setpoint'%(devName)
        attrName = attrName.lower()
        widgetsSet[attrName] = {'label':ui.GunHighVoltagePowerSupplyLabel,
                                'read': ui.GunHighVoltagePowerSupplyRead,
                                'write':ui.GunHighVoltagePowerSupplyWrite,
                                'check':ui.GunHighVoltagePowerSupplyCheck}
        self._setupTaurusLabel4Attr(widgetsSet[attrName]['read'],attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            min=-90.0,max=0.0,step=0.1)
        
        self._configurationWidgets['eGun'] = widgetsSet

    def coolingLoopsConfiguration(self,ui):
        devName = 'li/ct/plc2'
        widgetsSet = {}
        
        #CL1
        attrName = '%s/cl1_t_setpoint'%(devName)
        attrName = attrName.lower()
        widgetsSet[attrName] = {'label':ui.coolingLoop1SetpointLabel,
                                'read': ui.coolingLoop1SetpointRead,
                                'write':ui.coolingLoop1SetpointWrite,
                                'check':ui.coolingLoop1SetpointCheck}
        self._setupTaurusLabel4Attr(widgetsSet[attrName]['read'],attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            min=0.0,max=50.0,step=0.1)
        #CL2
        attrName = '%s/cl2_t_setpoint'%(devName)
        attrName = attrName.lower()
        widgetsSet[attrName] = {'label':ui.coolingLoop2SetpointLabel,
                                'read': ui.coolingLoop2SetpointRead,
                                'write':ui.coolingLoop2SetpointWrite,
                                'check':ui.coolingLoop2SetpointCheck}
        self._setupTaurusLabel4Attr(widgetsSet[attrName]['read'],attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            min=0.0,max=50.0,step=0.1)
        #CL3
        attrName = '%s/cl3_t_setpoint'%(devName)
        attrName = attrName.lower()
        widgetsSet[attrName] = {'label':ui.coolingLoop3SetpointLabel,
                                'read': ui.coolingLoop3SetpointRead,
                                'write':ui.coolingLoop3SetpointWrite,
                                'check':ui.coolingLoop3SetpointCheck}
        self._setupTaurusLabel4Attr(widgetsSet[attrName]['read'],attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            min=0.0,max=50.0,step=0.1)
        self._configurationWidgets['coolingLoop'] = widgetsSet
    
    def vacuumValvesConfiguration(self,ui):
        widgetsSet = {}
        
        attrName = 'li/ct/plc2/VCV_ONC'.lower()
        widgetsSet[attrName] = {'label':ui.VaccumCollimatorValveLabel,
                                'read': ui.VaccumCollimatorValveRead,
                                'write':ui.VaccumCollimatorValveWrite,
                                'check':ui.VaccumCollimatorValveCheck}
        self._setupLed4Attr(ui.VaccumCollimatorValveRead,attrName)
        self._configurationWidgets['vacuumValves'] = widgetsSet

    def magnetsConfiguration(self,ui):
        widgetsSet = {}
        
        magnets = {'sl':{'1':['H','V','F'],
                         '2':['H','V','F'],
                         '3':['H','V','F'],
                         '4':['H','V','F']},
                   'bc':{'1':['H','V','F'],
                         '2':['H','V','F']},
                   'gl':{'': ['H','V','F']},
                   'as':{'1':['H','V'],
                         '2':['H','V']},
                   'qt':{'1':['H','V','F'],
                         '2':['F']}}
        
        for family in magnets.keys():
            self.debug("> %s"%(family))
            for magnet in magnets[family].keys():
                self.debug(">> %s%s"%(family,magnet))
                for component in magnets[family][magnet]:
                    attrName = 'li/ct/plc3/%s%s%s_I_setpoint'\
                               %(family,magnet,component)
                    attrName = attrName.lower()
                    widgetPrefix = "%s%s%s"%(family,magnet,component)
                    self.debug(">>> %s"%(widgetPrefix))
                    labelWidget = getattr(ui,widgetPrefix+'Label')
                    readWidget =  getattr(ui,widgetPrefix+'Read')
                    writeWidget = getattr(ui,widgetPrefix+'Write')
                    checkWidget = getattr(ui,widgetPrefix+'Check')
                    widgetsSet[attrName] = {'label':labelWidget,
                                            'read': readWidget,
                                            'write':writeWidget,
                                            'check':checkWidget}
                    widget = widgetsSet[attrName]['read']
                    self._setupTaurusLabel4Attr(widget,attrName)
                    if component in ['H','V']:
                        if family == 'qt':
                            min=-16
                            max=16
                        else:
                            min=-2
                            max=2
                        step=0.01
                        decimals=2
                    else:
                        if family == 'sl':
                            min=0
                            max=1
                            step=0.01
                            decimals=2
                        elif family == 'bc':
                            min=0
                            max=200
                            step=0.01
                            decimals=2
                        elif family == 'gl':
                            min=0
                            max=130
                            step=0.01
                            decimals=2
                        elif family == 'qt':
                            min=0
                            max=6
                            step=0.005
                            decimals=3
                    self._setupQSpinBox(widgetsSet[attrName]['write'],
                            min=min,max=max,step=step,decimals=decimals)
        #---- TODO: connect the ToApplyTitle to check/uncheck all the *Check
        self._configurationWidgets['magnets'] = widgetsSet
    
    def radiofrequencyConfiguration(self,ui):
        widgetsSet = {}
        
        attrName = 'li/ct/plc1/TPS0_Phase'.lower()
        widgetsSet[attrName] = {'label':ui.TPS0PhaseLabel,
                                'read': ui.TPS0PhaseRead,
                                'write':ui.TPS0PhaseWrite,
                                'check':ui.TPS0PhaseCheck}
        self._setupTaurusLabel4Attr(ui.TPS0PhaseRead,attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            min=0.0,max=380,decimals=1,step=0.1)
        
        attrName = 'li/ct/plc1/TPSX_Phase'.lower()
        widgetsSet[attrName] = {'label':ui.TPSXPhaseLabel,
                                'read': ui.TPSXPhaseRead,
                                'write':ui.TPSXPhaseWrite,
                                'check':ui.TPSXPhaseCheck}
        self._setupTaurusLabel4Attr(ui.TPSXPhaseRead,attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            min=0.0,max=380,decimals=0,step=1)
        
        attrName = 'li/ct/plc1/TPS1_Phase'.lower()
        widgetsSet[attrName] = {'label':ui.TPS1PhaseLabel,
                                'read': ui.TPS1PhaseRead,
                                'write':ui.TPS1PhaseWrite,
                                'check':ui.TPS1PhaseCheck}
        self._setupTaurusLabel4Attr(ui.TPS1PhaseRead,attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            min=0.0,max=380,decimals=0,step=1)
        
        attrName = 'li/ct/plc1/TPS2_Phase'.lower()
        widgetsSet[attrName] = {'label':ui.TPS2PhaseLabel,
                                'read': ui.TPS2PhaseRead,
                                'write':ui.TPS2PhaseWrite,
                                'check':ui.TPS2PhaseCheck}
        self._setupTaurusLabel4Attr(ui.TPS2PhaseRead,attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            min=0.0,max=380,decimals=0,step=1)
        
        attrName = 'li/ct/plc1/A0_OP'.lower()
        widgetsSet[attrName] = {'label':ui.A0OPLabel,
                                'read': ui.A0OPRead,
                                'write':ui.A0OPWrite,
                                'check':ui.A0OPCheck}
        self._setupTaurusLabel4Attr(ui.A0OPRead,attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            min=75,max=760,decimals=0,step=1)
        
        attrName = 'li/ct/plc1/ATT2_P_setpoint'.lower()
        widgetsSet[attrName] = {'label':ui.ATT2Label,
                                'read': ui.ATT2Read,
                                'write':ui.ATT2Write,
                                'check':ui.ATT2Check}
        self._setupTaurusLabel4Attr(ui.ATT2Read,attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            min=-10.0,max=0,decimals=1,step=0.1)
        
        attrName = 'li/ct/plc1/PHS1_Phase_setpoint'.lower()
        widgetsSet[attrName] = {'label':ui.PHS1Label,
                                'read': ui.PHS1Read,
                                'write':ui.PHS1Write,
                                'check':ui.PHS1Check}
        self._setupTaurusLabel4Attr(ui.PHS1Read,attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            min=0.0,max=160,decimals=0,step=1)
        
        attrName = 'li/ct/plc1/PHS2_Phase_setpoint'.lower()
        widgetsSet[attrName] = {'label':ui.PHS2Label,
                                'read': ui.PHS2Read,
                                'write':ui.PHS2Write,
                                'check':ui.PHS2Check}
        self._setupTaurusLabel4Attr(ui.PHS2Read,attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            min=0.0,max=380,decimals=0,step=1)
        
        self._configurationWidgets['radioFrequency'] = widgetsSet
    
    def timingConfiguration(self,ui):
        widgetsSet = {}
        
        attrName = 'li/ct/plc1/TB_MBM'.lower()
        widgetsSet[attrName] = {'label':ui.MBMLabel,
                                'read': ui.MBMRead,
                                'write':ui.MBMWrite,
                                'check':ui.MBMCheck}
        self._setupLed4Attr(ui.MBMRead,attrName)
        
        attrName = 'li/ct/plc1/TB_GUN_delay'.lower()
        widgetsSet[attrName] = {'label':ui.GunDelayLabel,
                                'read': ui.GunDelayRead,
                                'write':ui.GunDelayWrite,
                                'check':ui.GunDelayCheck}
        self._setupTaurusLabel4Attr(ui.GunDelayRead,attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            min=32,max=4096,step=32)
        
        attrName = 'li/ct/plc1/TB_ka1_delay'.lower()
        widgetsSet[attrName] = {'label':ui.ka1DelayLabel,
                                'read': ui.ka1DelayRead,
                                'write':ui.ka1DelayWrite,
                                'check':ui.ka1DelayCheck}
        self._setupTaurusLabel4Attr(ui.ka1DelayRead,attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            min=1,max=56,step=1)
        
        attrName = 'li/ct/plc1/TB_ka2_delay'.lower()
        widgetsSet[attrName] = {'label':ui.ka2DelayLabel,
                                'read': ui.ka2DelayRead,
                                'write':ui.ka2DelayWrite,
                                'check':ui.ka2DelayCheck}
        self._setupTaurusLabel4Attr(ui.ka2DelayRead,attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            min=2720,max=4096,step=32)
        
        attrName = 'li/ct/plc1/TB_GPI'.lower()
        widgetsSet[attrName] = {'label':ui.GPILabel,
                                'read': ui.GPIRead,
                                'write':ui.GPIWrite,
                                'check':ui.GPICheck}
        self._setupTaurusLabel4Attr(ui.GPIRead,attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            min=6,max=1054,step=2)
        
        attrName = 'li/ct/plc1/TB_GPN'.lower()
        widgetsSet[attrName] = {'label':ui.GPNLabel,
                                'read': ui.GPNRead,
                                'write':ui.GPNWrite,
                                'check':ui.GPNCheck}
        self._setupTaurusLabel4Attr(ui.GPNRead,attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            min=1,max=16,step=1)
        
        attrName = 'li/ct/plc1/TB_GPA'.lower()
        widgetsSet[attrName] = {'label':ui.GPALabel,
                                'read': ui.GPARead,
                                'write':ui.GPAWrite,
                                'check':ui.GPACheck}
        self._setupTaurusLabel4Attr(ui.GPARead,attrName)
        self._setupQSpinBox(widgetsSet[attrName]['write'],
                            min=-40.0,max=0,decimals=1,step=0.1)
        #---- TODO: connect the ToApplyTitle to check/uncheck all the *Check
        self._configurationWidgets['timing'] = widgetsSet
    
    def klystronsConfiguration(self,ui):
        widgetsSet = {}
        
        klystrons = {1:{'setp':ui.ka1HVPSRead},
                     2:{'setp':ui.ka2HVPSRead}}
        for number in klystrons.keys():
            self.debug("> %s"%(number))
            for element in klystrons[number].keys():
                self.debug(">> ka%s_%s"%(number,element))
                widget = klystrons[number][element]
                devName = 'li/ct/plc%d'%(number+3)
                if element == 'setp':
                    attrName = "%s/HVPS_V_setpoint"%(devName).lower()
                    widgetsSet[attrName] = {'label':getattr(ui,'ka%dHVPSLabel'%(number)),
                                            'read': getattr(ui,'ka%dHVPSRead'%(number)),
                                            'write':getattr(ui,'ka%dHVPSWrite'%(number)),
                                            'check':getattr(ui,'ka%dHVPSCheck'%(number)),}
                    widget = widgetsSet[attrName]['read']
                    self._setupTaurusLabel4Attr(widget,attrName)
                    self._setupQSpinBox(widgetsSet[attrName]['write'],
                                        min=0.0,max=33,decimals=1,step=0.1)
        #---- TODO: connect the ToApplyTitle to check/uncheck all the *Check
        self._configurationWidgets['klystrons'] = widgetsSet
    
    def commentConfiguration(self,ui):
        ui.commentGroup.hide()
        #ui.textLoadedLabel.hide()
        #ui.textLoaded.hide()
    #---- Done configure subwidgets
    ######
    
    def buttonsConfiguration(self,buttons):
        buttons.button(QtGui.QDialogButtonBox.Reset).setText("Reload")
        #buttons.button(QtGui.QDialogButtonBox.Reset).clicked.connect(self.loadFromDevices)
        Qt.QObject.connect(buttons.button(QtGui.QDialogButtonBox.Reset),
                           Qt.SIGNAL('clicked(bool)'),self.loadFromDevices)
        #buttons.button(QtGui.QDialogButtonBox.Save).clicked.connect(self.saveToFile)
        Qt.QObject.connect(buttons.button(QtGui.QDialogButtonBox.Save),
                           Qt.SIGNAL('clicked(bool)'),self.saveToFile)
        #buttons.button(QtGui.QDialogButtonBox.Open).clicked.connect(self.loadFromFile)
        Qt.QObject.connect(buttons.button(QtGui.QDialogButtonBox.Open),
                           Qt.SIGNAL('clicked(bool)'),self.loadFromFile)
        #buttons.button(QtGui.QDialogButtonBox.Apply).clicked.connect(self.applyToDevices)
        Qt.QObject.connect(buttons.button(QtGui.QDialogButtonBox.Apply),
                           Qt.SIGNAL('clicked(bool)'),self.applyToDevices)
    
    #---- TODO: should the *Reading widgets be connected to the *Value?
    #           Doing this, the operation of the other tabs will be shown in 
    #           this Configuration tab according to when it's happening.
    
    ######
    #---- Distinguish between widget types
    def _isSpinBox(self,widget):
        return hasattr(widget,'setValue')
    def _isCheckBox(self,widget):
        return hasattr(widget,'setChecked')
    ######
    
    ######
    #---- Widget backgrounds
    def _setStyleToModified(self,attrStruct):
        saver = attrStruct['write']
        if self._isSpinBox(saver):
            saver.setStyleSheet("background-color: rgb(255, 255, 0);"\
                                 "color: rgb(0, 0, 255); "\
                                 "font-weight: bold;")
        elif self._isCheckBox(saver):
            saver.setStyleSheet("background-color: rgb(255, 255, 0);"\
                                 "color: rgb(0, 0, 255);")
        else:
            raise Exception("Unmanaged %s widget type to tag modified"%(type(widget)))
        attrStruct['check'].setChecked(True)
        
    def _setStyleToNoModified(self,attrStruct):
        saver = attrStruct['write']
        if self._isSpinBox(saver):
            saver.setStyleSheet("background-color: rgb(255, 255, 255);"\
                                 "color: rgb(0, 0, 0); ")
        elif self._isCheckBox(saver):
            saver.setStyleSheet("color: rgb(0, 0, 0);")
        else:
            raise Exception("Unmanaged %s widget type to tag modified"%(type(widget)))
        attrStruct['check'].setChecked(False)
    ######
    
    ######
    #---- Value setters and getters
    def _getAttrValue(self,attrName):
        return PyTango.AttributeProxy(attrName).read().value
    def _setAttrValue(self,attrName,value):
        PyTango.AttributeProxy(attrName).write(value)
    
    def _setValueToSaverWidget(self,attrStruct,value,style=True):
        saver = attrStruct['write']
        if self._isSpinBox(saver):
            haschanged = (value != saver.value())
            saver.setValue(value)
        elif self._isCheckBox(saver):
            haschanged = (value != saver.isChecked())
            saver.setChecked(value)
        else:
            raise Exception("Unmanaged %s widget type"%(type(saver)))
        if style and haschanged:
            self._setStyleToModified(attrStruct)
        else:
            self._setStyleToNoModified(attrStruct)
    
    def _getValueFromSaverWidget(self,attrStruct):
        saver = attrStruct['write']
        if self._isSpinBox(saver):
            return saver.value()
        elif self._isCheckBox(saver):
            return saver.isChecked()
        else:
            raise Exception("Unmanaged %s widget type"%(type(saver)))
    ######
        
    ######
    #---- manage files
    def _getStorageDirectory(self):
        directory = str(QtGui.QFileDialog.getExistingDirectory(self,
                                                            "Select Directory",
                                                            sandbox))
        if not directory.startswith(sandbox):
            QtGui.QMessageBox.warning(self, "Sandbox warning",
                                      "Your selected directory is not in the "\
                                      "storage shared by NFS")
        return directory
    
    def _getFilePrefix(self,now_struct):
        #---- Start all the files with the date, 
        #     then mode and highlight some field on the name
        # 1 - %Y%m%d_%H%m
        fileprefix = time.strftime("%Y%m%d_%H%M",now_struct)
        # 2 MBM vs SBM
        modeAttrName = 'LI/CT/PLC1/TB_MBM'.lower()
        try:
            isMBM = self._getAttrValue(modeAttrName)
            # 2.1 - MBM_width
            if isMBM:
                widthAttrName = 'LI/CT/PLC1/TB_GPI'.lower()
                width = self._getAttrValue(widthAttrName)
                fileprefix = ''.join("%s_MBM_%dns"%(fileprefix,width))
            # 2.2 - SBM_pulses_interval
            else:
                npulsesAttrName = 'LI/CT/PLC1/TB_GPN'.lower()
                intervalAttrName = 'LI/CT/PLC1/TB_GPI'.lower()
                npulses = self._getAttrValue(npulsesAttrName)
                interval = self._getAttrValue(intervalAttrName)
                fileprefix = ''.join("%s_SBM_%dns_%d"%(fileprefix,pulses,interval))
        except Exception,e:
            self.error("Cannot build a file prefix!")
        return fileprefix
    
    def _getFileSuffix(self,prefix=None):
        msg,ok = QtGui.QInputDialog.getText(self,"Select file name",
                                          "would you like to write something "\
                                          "after the file prefix %s?"%(prefix),
                                          QtGui.QLineEdit.Normal)
        return str(msg)
    
    def _requestFileName(self):
        dialogTitle = "Select linac's configuration file"
        filters = "Linac configuration (*.li);;All files (*)"
        return str(QtGui.QFileDialog.getOpenFileName(self,dialogTitle,
                                                         sandbox,filters))
    
    def _prepareFileHeader(self,now_struct):
        return "# File stored the %s\n"\
               %(time.strftime("%Y/%m/%d at %H:%m",now_struct))

    def _isCommentLine(self,line):
        if line[0] == '#' and \
           not (line.split()[1][:-1] == 'group' and \
                line.split()[2] in self._configurationWidgets.keys()):
            return True
        return False

    def _prepareGroupTag(self,group):
        return "# group: %s"%(group)

    def _isGroupTagLine(self,line):
        if line[0] == '#' and \
           line.split()[1][:-1] == 'group' and \
           line.split()[2] in self._configurationWidgets.keys():
            return True
        return False

    def _prepareAttrLine(self,attrStruct,attrName):
        tag = attrStruct['label'].text()
        self._getAttrValue(attrName)#to rise exception if not available
        value = self._getValueFromSaverWidget(attrStruct)
        return "%24s\t%g\t%s"%(tag,value,attrName)

    def _getAttrLine(self,line,n):
        try:
            elements = line.split()
            attrName = elements[-1]
            value = elements[-2]
            if value.count('.'):
                value = float(value)
            else:
                value = int(value)
            return (attrName,value)
        except Exception,e:
            self.error("misunderstanding in line %d: %s"%(n,line))
            return (None,None)
    ######

    ######
    #---- ActionButtons callbacks
    def loadFromDevices(self):
        '''With this call (from a button or at the loading step) we must travel
           all the *Reading widgets and copy the value to the *Value widget.
        '''
        exceptions = {}
        #dump(self._configurationWidgets)
        for group in self._configurationWidgets.keys():
            self.debug(">  %s"%group)
            for attrName in self._configurationWidgets[group].keys():
                attrStruct = self._configurationWidgets[group][attrName]
                try:
                    value = self._getAttrValue(attrName)
                    self._setValueToSaverWidget(attrStruct, value,style=False)
                except Exception,e:
                    self.error("Exception trying to load %s value. %s"
                               %(attrName,e))
                    label = attrStruct['label'].text()
                    if group in exceptions.keys():
                        exceptions[group].append(str(label))
                    else:
                        exceptions[group] = [str(label)]
        if len(exceptions.keys()) != 0:
            msg = ""
            for group in exceptions.keys():
                msg = ''.join("%sIn group %s, %d values not uploaded\n"
                              %(msg,group,len(exceptions[group])))
                if len(exceptions[group]) > 5:
                    for i in range(5):
                        msg = ''.join("%s\t-%s\n"%(msg,exceptions[group][i]))
                    msg = ''.join("%s\t ...and another %d\n"%(msg,len(exceptions[group])-5))
                else:
                    for label in exceptions[group]:
                        msg = ''.join("%s\t-%s\n"%(msg,label))
            QtGui.QMessageBox.warning(self, "Exceptions when load from devices",
                                      msg)
    
    def saveToFile(self):
        '''Travelling along the *Check widgets, the checked ones (name and 
           value) will be written in a file indicated by the user.
        '''
        now = time.time()
        now_struct = time.localtime(now)
        directory = self._getStorageDirectory()
        prefix = self._getFilePrefix(now_struct)
        #---- TODO: request suffix to the user.
        suffix = ''
        if directory != '':
            suffix = self._getFileSuffix(prefix)
            if suffix == '':
                filename = "%s/%s.li"%(directory,prefix)
            else:
                filename = "%s/%s-%s.li"%(directory,prefix,suffix)
            self.debug("saveToFile() filename: %s"%(filename))
            saving = self._prepareFileHeader(now_struct)
            exceptions = {}
            for group in self._configurationWidgets.keys():
                saving = ''.join("%s\n%s"
                                 %(saving,self._prepareGroupTag(group)))
                groupAttrNames = self._configurationWidgets[group].keys()
                groupAttrNames.sort()
                for attrName in groupAttrNames:
                    attrStruct = self._configurationWidgets[group][attrName]
                    try:
                        saving = ''.join("%s\n%s"
                          %(saving,self._prepareAttrLine(attrStruct,attrName)))
                    except Exception,e:
                        if group in exceptions.keys():
                            exceptions[group].append(attrName)
                        else:
                            exceptions[group] = [attrName]
            saving = ''.join('%s\n'%(saving))
            f = open(filename,'w')
            f.write(saving)
            f.close()
            if len(exceptions.keys()) != 0:
                msg = ""
                for group in exceptions.keys():
                    msg = ''.join("%sIn group %s happen %d errors\n"\
                                  %(msg,group,len(exceptions[group])))
                    if len(exceptions[group]) > 5:
                        for i in range(5):
                            msg = ''.join("%s\t-%s\n"%(msg,exceptions[group][i]))
                        msg = ''.join("%s\t ...and another %d\n"%(msg,len(exceptions[group])-5))
                    else:
                        for attrName in exceptions[group]:
                            msg = ''.join("%s\t-%s\n"%(msg,attrName))
                QtGui.QMessageBox.warning(self, "Exceptions when save",
                                          msg)

    def loadFromFile(self):
        '''Given a file of settings provided by the user, show those values in 
           the *Value widgets.
           Mark (TODO: how?) the changes from the previous value 
           in the *Value widget
        '''
        filename = self._requestFileName()
        group = ''
        exceptions = {}
        if filename != '':
            file = open(filename,'r')
            nline = 0
            for line in file:
                if self._isCommentLine(line):
                    pass#Nothing to do with pure comment lines
                elif self._isGroupTagLine(line):
                    group = line.split()[2]
                else:
                    attrName,value = self._getAttrLine(line, nline)
                    if group != '' and attrName != None:
                        try:
                            attrStruct = self._configurationWidgets[group][attrName]
                        except:
                            self.error("attribute %s is not member of the "\
                                       "group %s"%(attrName,group))
                            if group in exceptions.keys():
                                exceptions[group].append(attrName)
                            else:
                                exceptions[group]=[attrName]
                        else:
                            self._setValueToSaverWidget(attrStruct,value)
            file.close()
            if len(exceptions.keys()) != 0:
                msg = ""
                for group in exceptions.keys():
                    msg = ''.join("%sIn group %s found %d orphan "\
                                  "attributes:\n"%(msg,group,
                                                   len(exceptions[group])))
                    if len(exceptions[group]) > 5:
                        for i in range(5):
                            msg = ''.join("%s\t-%s\n"%(msg,exceptions[group][i]))
                        msg = ''.join("%s\t ...and another %d\n"%(msg,len(exceptions[group])-5))
                    else:
                        for attrName in exceptions[group]:
                            msg = ''.join("%s\t-%s\n"%(msg,attrName))
                QtGui.QMessageBox.warning(self, "Exceptions when load file",
                                          msg)

    def applyToDevices(self):
        '''Travelling along the *Check, apply the value in *Value 
           to the model in the *Reading.
        '''
        exceptions = {}
        for group in self._configurationWidgets.keys():
            for attrName in self._configurationWidgets[group]:
                attrStruct = self._configurationWidgets[group][attrName]
                if attrStruct['check'].isChecked():
                    try:
                        value = self._getValueFromSaverWidget(attrStruct)
                        self._setAttrValue(attrName, value)
                        self._setStyleToNoModified(attrStruct)
                    except Exception,e:
                        self.error("Exception applying %s: %s"%(attrName,e))
                        if group in exceptions.keys():
                            exceptions[group].append(attrName)
                        else:
                            exceptions[group] = [attrName]
        if len(exceptions.keys()) != 0:
            msg = ""
            for group in exceptions.keys():
                msg = ''.join("%sIn group %s found %d applying errors:\n"
                              %(msg,group,len(exceptions[group])))
                if len(exceptions[group]) > 5:
                    for i in range(5):
                        msg = ''.join("%s\t-%s\n"%(msg,exceptions[group][i]))
                    msg = ''.join("%s\t ...and another %d\n"%(msg,len(exceptions[group])-5))
                else:
                    for attrName in exceptions[group]:
                        msg = ''.join("%s\t-%s\n"%(msg,attrName))
            QtGui.QMessageBox.warning(self, "Exceptions when apply",
                                      msg)
    ######

def main():
    parser = argparse.get_taurus_parser()
    app = TaurusApplication(sys.argv, cmd_line_parser=parser,
                      app_name='ctlisetup', app_version='0.1',
                      org_domain='ALBA', org_name='ALBA')
    options = app.get_command_line_options()
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()