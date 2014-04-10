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
        self.load()
    
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
    #---- Done auxiliar methods to configure widgets
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
        
        #print self._configurationWidgets
        
        #---- TODO: connect buttons to their actions
        self.buttonsConfiguration(configuration_ui.buttonBox)
        # Those actions must have DangerMessage for eGunLV, CLs and KaLV
        #---- TODO: load current values to the "save/retrieve" column of widgets
        #           (this is the reset button action)
        
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
        
        attrName = '%s/Gun_kathode_v_setpoint'%(devName)
        attrName = attrName.lower()
        widgetsSet[attrName] = {'label':ui.GunKathodeLowVoltageLabel,
                                'read': ui.GunKathodeLowVoltageRead,
                                'write':ui.GunKathodeLowVoltageWrite,
                                'check':ui.GunKathodeLowVoltageCheck}
        self._setupTaurusLabel4Attr(widgetsSet[attrName]['read'],attrName)
        
        attrName = '%s/Gun_hv_v_setpoint'%(devName)
        attrName = attrName.lower()
        widgetsSet[attrName] = {'label':ui.GunHighVoltagePowerSupplyLabel,
                                'read': ui.GunHighVoltagePowerSupplyRead,
                                'write':ui.GunHighVoltagePowerSupplyWrite,
                                'check':ui.GunHighVoltagePowerSupplyCheck}
        self._setupTaurusLabel4Attr(widgetsSet[attrName]['read'],attrName)
        
        #---- TODO: connect the ToApplyTitle to check/uncheck all the *Check
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
        
        #----
        #CL2
        attrName = '%s/cl2_t_setpoint'%(devName)
        attrName = attrName.lower()
        widgetsSet[attrName] = {'label':ui.coolingLoop2SetpointLabel,
                                'read': ui.coolingLoop2SetpointRead,
                                'write':ui.coolingLoop2SetpointWrite,
                                'check':ui.coolingLoop2SetpointCheck}
        self._setupTaurusLabel4Attr(widgetsSet[attrName]['read'],attrName)
        #CL3
        attrName = '%s/cl3_t_setpoint'%(devName)
        attrName = attrName.lower()
        widgetsSet[attrName] = {'label':ui.coolingLoop3SetpointLabel,
                                'read': ui.coolingLoop3SetpointRead,
                                'write':ui.coolingLoop3SetpointWrite,
                                'check':ui.coolingLoop3SetpointCheck}
        self._setupTaurusLabel4Attr(widgetsSet[attrName]['read'],attrName)
        #---- TODO: connect the ToApplyTitle to check/uncheck all the *Check
        self._configurationWidgets['coolingLoop'] = widgetsSet
    
    def vacuumValvesConfiguration(self,ui):
        widgetsSet = {}
        
        attrName = 'li/ct/plc2/VCV_ONC'.lower()
        widgetsSet[attrName] = {'label':ui.VaccumCollimatorValveLabel,
                                'read': ui.VaccumCollimatorValveRead,
                                'write':ui.VaccumCollimatorValveWrite,
                                'check':ui.VaccumCollimatorValveCheck}
        self._setupLed4Attr(ui.VaccumCollimatorValveRead,attrName)
        #---- TODO: connect the ToApplyTitle to check/uncheck all the *Check
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
            #print "> %s"%(family)
            for magnet in magnets[family].keys():
                #print ">> %s%s"%(family,magnet)
                for component in magnets[family][magnet]:
                    attrName = 'li/ct/plc3/%s%s%s_I_setpoint'\
                               %(family,magnet,component)
                    attrName = attrName.lower()
                    widgetPrefix = "%s%s%s"%(family,magnet,component)
                    #print ">>> %s"%(widgetPrefix)
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
        
        attrName = 'li/ct/plc1/TPSX_Phase'.lower()
        widgetsSet[attrName] = {'label':ui.TPSXPhaseLabel,
                                'read': ui.TPSXPhaseRead,
                                'write':ui.TPSXPhaseWrite,
                                'check':ui.TPSXPhaseCheck}
        self._setupTaurusLabel4Attr(ui.TPSXPhaseRead,attrName)
        
        attrName = 'li/ct/plc1/TPS1_Phase'.lower()
        widgetsSet[attrName] = {'label':ui.TPS1PhaseLabel,
                                'read': ui.TPS1PhaseRead,
                                'write':ui.TPS1PhaseWrite,
                                'check':ui.TPS1PhaseCheck}
        self._setupTaurusLabel4Attr(ui.TPS1PhaseRead,attrName)
        
        attrName = 'li/ct/plc1/TPS2_Phase'.lower()
        widgetsSet[attrName] = {'label':ui.TPS2PhaseLabel,
                                'read': ui.TPS2PhaseRead,
                                'write':ui.TPS2PhaseWrite,
                                'check':ui.TPS2PhaseCheck}
        self._setupTaurusLabel4Attr(ui.TPS2PhaseRead,attrName)
        
        attrName = 'li/ct/plc1/A0_OP'.lower()
        widgetsSet[attrName] = {'label':ui.A0OPLabel,
                                'read': ui.A0OPRead,
                                'write':ui.A0OPWrite,
                                'check':ui.A0OPCheck}
        self._setupTaurusLabel4Attr(ui.A0OPRead,attrName)
        
        attrName = 'li/ct/plc1/ATT2_P_setpoint'.lower()
        widgetsSet[attrName] = {'label':ui.ATT2Label,
                                'read': ui.ATT2Read,
                                'write':ui.ATT2Write,
                                'check':ui.ATT2Check}
        self._setupTaurusLabel4Attr(ui.ATT2Read,attrName)
        
        attrName = 'li/ct/plc1/PHS1_Phase_setpoint'.lower()
        widgetsSet[attrName] = {'label':ui.PHS1Label,
                                'read': ui.PHS1Read,
                                'write':ui.PHS1Write,
                                'check':ui.PHS1Check}
        self._setupTaurusLabel4Attr(ui.PHS1Read,attrName)
        
        attrName = 'li/ct/plc1/PHS2_Phase_setpoint'.lower()
        widgetsSet[attrName] = {'label':ui.PHS2Label,
                                'read': ui.PHS2Read,
                                'write':ui.PHS2Write,
                                'check':ui.PHS2Check}
        self._setupTaurusLabel4Attr(ui.PHS2Read,attrName)
        #---- TODO: connect the ToApplyTitle to check/uncheck all the *Check
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
        
        attrName = 'li/ct/plc1/TB_ka1_delay'.lower()
        widgetsSet[attrName] = {'label':ui.ka1DelayLabel,
                                'read': ui.ka1DelayRead,
                                'write':ui.ka1DelayWrite,
                                'check':ui.ka1DelayCheck}
        self._setupTaurusLabel4Attr(ui.ka1DelayRead,attrName)
        
        attrName = 'li/ct/plc1/TB_ka2_delay'.lower()
        widgetsSet[attrName] = {'label':ui.ka2DelayLabel,
                                'read': ui.ka2DelayRead,
                                'write':ui.ka2DelayWrite,
                                'check':ui.ka2DelayCheck}
        self._setupTaurusLabel4Attr(ui.ka2DelayRead,attrName)
        
        attrName = 'li/ct/plc1/TB_GPI'.lower()
        widgetsSet[attrName] = {'label':ui.GPILabel,
                                'read': ui.GPIRead,
                                'write':ui.GPIWrite,
                                'check':ui.GPICheck}
        self._setupTaurusLabel4Attr(ui.GPIRead,attrName)
        
        attrName = 'li/ct/plc1/TB_GPN'.lower()
        widgetsSet[attrName] = {'label':ui.GPNLabel,
                                'read': ui.GPNRead,
                                'write':ui.GPNWrite,
                                'check':ui.GPNCheck}
        self._setupTaurusLabel4Attr(ui.GPNRead,attrName)
        
        attrName = 'li/ct/plc1/TB_GPA'.lower()
        widgetsSet[attrName] = {'label':ui.GPALabel,
                                'read': ui.GPARead,
                                'write':ui.GPAWrite,
                                'check':ui.GPACheck}
        self._setupTaurusLabel4Attr(ui.GPARead,attrName)
        #---- TODO: connect the ToApplyTitle to check/uncheck all the *Check
        self._configurationWidgets['timing'] = widgetsSet
    
    def klystronsConfiguration(self,ui):
        widgetsSet = {}
        
        klystrons = {1:{'setp':ui.ka1HVPSRead},
                     2:{'setp':ui.ka2HVPSRead}}
        for number in klystrons.keys():
            #print "> %s"%(number)
            for element in klystrons[number].keys():
                #print ">> ka%s_%s"%(number,element)
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
        #---- TODO: connect the ToApplyTitle to check/uncheck all the *Check
        self._configurationWidgets['klystrons'] = widgetsSet
    
    def commentConfiguration(self,ui):
        ui.commentGroup.hide()
        #ui.textLoadedLabel.hide()
        #ui.textLoaded.hide()
    
    def buttonsConfiguration(self,buttons):
        buttons.button(QtGui.QDialogButtonBox.Reset).setText("Reload")
        buttons.button(QtGui.QDialogButtonBox.Reset).clicked.connect(self.load)
        buttons.button(QtGui.QDialogButtonBox.Save).clicked.connect(self.save)
        buttons.button(QtGui.QDialogButtonBox.Open).clicked.connect(self.open)
        buttons.button(QtGui.QDialogButtonBox.Apply).clicked.connect(self.apply)
    
    #---- TODO: should the *Reading widgets be connected to the *Value?
    #           Doing this, the operation of the other tabs will be shown in 
    #           this Configuration tab according to when it's happening.
    
    def load(self):
        '''With this call (from a button or at the loading step) we must travel
           all the *Reading widgets and copy the value to the *Value widget.
        '''
        
        #print("In Load: %r"%(self._configurationWidgets))
        #dump(self._configurationWidgets)
        for group in self._configurationWidgets.keys():
            #print(">  %s"%group)
            for attrName in self._configurationWidgets[group].keys():
                try:
                    value = PyTango.AttributeProxy(attrName).read().value
                    widget = self._configurationWidgets[group][attrName]['write']
                    self.debug("%s value %g to a %s"
                               %(attrName,value,type(widget)))
                    self.value2widget(value,widget)
                except Exception,e:
                    self.error("Exception trying to load %s value. %s"
                               %(attrName,e))
    
    def value2widget(self,value,widget):
        if hasattr(widget,'setValue'):
            widget.setValue(value)
            widget.setStyleSheet('background-color: rgb(255, 255, 255);\ncolor: rgb(0, 0, 0);')
        elif hasattr(widget,'setChecked'):
            widget.setChecked(value)
            widget.setStyleSheet('\ncolor: rgb(0, 0, 0);')
        else:
            raise Exception("unknown how to apply a value to a %s widget"
                            %(type(widget)))
    
    def save(self):
        '''Travelling along the *Check widgets, the checked ones (name and 
           value) will be written in a file indicated by the user.
        '''
        now = time.time()
        now_struct = time.localtime(now)
        #---- filename suggestion pattern: 
        #           1 - %Y%m%d_%H%m
        fileprefix = time.strftime("%Y%m%d_%H%M",now_struct)
        #           2.1 - MBM_width
        widget = self._configurationWidgets['timing']['LI/CT/PLC1/TB_MBM'.lower()]['write']
        value = self.widgetGetValue(widget)
        if value:
            widget = self._configurationWidgets['timing']['LI/CT/PLC1/TB_GPI'.lower()]['write']
            width = self.widgetGetValue(widget)
            fileprefix = ''.join("%s_MBM_%d"%(fileprefix,width))
        #           2.2 - SBM_pulses_interval
        else:
            widget = self._configurationWidgets['timing']['LI/CT/PLC1/TB_GPN'.lower()]['write']
            pulses = self.widgetGetValue(widget)
            widget = self._configurationWidgets['timing']['LI/CT/PLC1/TB_GPI'.lower()]['write']
            interval = self.widgetGetValue(widget)
            fileprefix = ''.join("%s_SBM_%d_%d"%(fileprefix,pulses,interval))
        #---- TODO: request filename to the user
        directory = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory",sandbox))
        if directory != '':
            filename = "%s/%s.li"%(directory,fileprefix)
            print("! filename: %s"%(filename))
            #file header
            t_str = time.strftime("%Y/%m/%d at %H%m",now_struct)
            saving = "# File stored the %s\n"%(t_str)
            for group in self._configurationWidgets.keys():
                saving = ''.join("%s\n# group: %s"%(saving,group))
                attributeNames = self._configurationWidgets[group].keys()
                attributeNames.sort()
                for attrName in attributeNames:
                    #print(">> %s"%attrName)
                    try:
                        tag = self._configurationWidgets[group][attrName]['label'].text()
                        widget = self._configurationWidgets[group][attrName]['write']
                        value = self.widgetGetValue(widget)
                        saving = ''.join("%s\n%30s\t%g\t%s"
                                         %(saving,tag,value,attrName))
                    except Exception,e:
                        print('!  %s'%e)
            saving = ''.join('%s\n'%(saving))
            #print(saving)
            f = open(filename,'w')
            f.write(saving)
            f.close()
        else:
            print("Save() cancelled")
    
    def widgetGetValue(self,widget):
        if hasattr(widget,'value'):
            return widget.value()
        elif hasattr(widget,'isChecked'):
            return widget.isChecked()
        else:
            raise Exception("unknown how to get widget's value for %s widget"
                            %(type(widget)))

    def open(self):
        '''Given a file of settings provided by the user, show those values in 
           the *Value widgets.
           Mark (TODO: how?) the changes from the previous value 
           in the *Value widget
        '''
        filename = str(QtGui.QFileDialog.getOpenFileName(self, "Select linac's configuration file",
                                                         sandbox,"Linac configuration (*.li);;All files (*)"))
        group = ''
        if filename != '':
            f = open(filename,'r')
            for line in f:
                #print(line)
                if line[0] == '#':
                    if line.split()[1][:-1] == 'group' and line.split()[2] in self._configurationWidgets.keys():
                        group = line.split()[2]
                        print("found group %s"%(group))
                    else:
                        print("comment: %s"%(line))
                else:
                    try:
                        elements = line.split()
                        attrName = elements[-1]
                        value = elements[-2]
                        if value.count('.'):
                            value = float(value)
                        else:
                            value = int(value)
                    except Exception,e:
                        print("exception splitting line \"%s\""%(line))
                    else:
                        print("found attr %s = %g (group:%s)"%(attrName,value,group))
                        try:
                            widget = self._configurationWidgets[group][attrName]['write']
                            check = self._configurationWidgets[group][attrName]['check']
                            self.widgetSetValue(widget, value, check)
                        except Exception,e:
                            print("exception in attr %s: %s"%(attrName,e))
        else:
            print("Open() cancelled")
        
    def widgetSetValue(self,widget,value,check):
        if hasattr(widget,'value'):
            if value != widget.value():
                widget.setStyleSheet('background-color: rgb(255, 255, 0);\ncolor: rgb(0, 0, 255); font-weight: bold;')
                widget.setValue(value)
                check.setChecked(True)
            else:
                widget.setStyleSheet('color: rgb(0, 0, 0)')
                check.setChecked(False)
        elif hasattr(widget,'isChecked'):
            value = bool(value)
            if value != widget.isChecked():
                widget.setStyleSheet('background-color: rgb(255, 255, 0);\ncolor: rgb(0, 0, 255);')
                widget.setChecked(value)
                check.setChecked(True)
            else:
                widget.setStyleSheet('color: rgb(0, 0, 255);')
                check.setChecked(False)
        else:
            raise Exception("unknown how to set widget's value for %s widget"%(type(widget)))
        
    def apply(self):
        '''Travelling along the *Check, apply the value in *Value 
           to the model in the *Reading.
        '''
        exceptions = {}
        for group in self._configurationWidgets.keys():
            for attrName in self._configurationWidgets[group]:
                if self._configurationWidgets[group][attrName]['check'].isChecked():
                    try:
                        widget = self._configurationWidgets[group][attrName]['write']
                        self.widgetApplyValue2Attr(widget, attrName)
                        self._configurationWidgets[group][attrName]['check'].setChecked(False)
                    except PyTango.DevFailed,e:
                        print("Cannot apply %s: %s"%(attrName,e[0].desc))
                        exceptions[attrName] = e[0].desc
                    except Exception,e:
                        print("Exception applying %s: %s"%(attrName,e))
        if len(exceptions.keys()) != 0:
            msg = ""
            for attrName in exceptions.keys():
                msg = ''.join("%sAttribute %s not applied:\n-%s\n"%(msg,attrName,exceptions[attrName]))
            QtGui.QMessageBox.warning(self, "Exceptions when apply",
                                      msg)

    def widgetApplyValue2Attr(self,widget,attrName):
        if hasattr(widget,'value'):
            PyTango.AttributeProxy(attrName).write(widget.value())
            widget.setStyleSheet('background-color: rgb(255, 255, 255);\ncolor: rgb(0, 0, 0);')
        elif hasattr(widget,'isChecked'):
            PyTango.AttributeProxy(attrName).write(widget.isChecked())
            widget.setStyleSheet('\ncolor: rgb(0, 0, 0);')
        else:
            raise Exception("unknown how to clean widget's background for %s widget"%(type(widget)))
        

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