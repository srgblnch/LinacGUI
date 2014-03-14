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

#The widgets are stored in a subdirectory and needs to be added to the pythonpath
linacWidgetsPath = os.environ['PWD']+'/widgets'
if not linacWidgetsPath in sys.path:
    sys.path.append(linacWidgetsPath)

from taurus.core.util import argparse
from taurus.qt.qtgui.application import TaurusApplication
from taurus.qt.qtgui.container import TaurusMainWindow
from taurus.qt.qtgui.base import TaurusBaseComponent
from taurus.qt import Qt,QtGui
from taurus.qt.qtgui.util import ExternalAppAction

from ui_ctli import Ui_linacGui

import threading

LinacDeviceNameRoot = 'li/ct/plc'
LinacDeviceNames = []
for i in range(1,6):
    LinacDeviceNames.append("%s%d"%(LinacDeviceNameRoot,i))
DeviceRelocator = 'li/ct/linacDataRelocator-01'

class MainWindow(TaurusMainWindow):
    def __init__(self, parent=None):
        TaurusMainWindow.__init__(self)
        # setup main window
        self.ui = Ui_linacGui()
        self.ui.setupUi(self)
        #place the ui in the window
        self._init_threads = {}
        self.initComponents()
        #kill splash screen
        self.splashScreen().finish(self)
        
    def initComponents(self):
        self.centralwidget = self.ui.linacTabs
        self.setCentralWidget(self.centralwidget)
        self.centralwidget.setCurrentIndex(2)#Force to start in "main screen"
        #concurrency in the big setModel and early return
#         self._init_threads['Communications'] = threading.Thread(name="a",target=self.setCommunications)
#         self._init_threads['Startup'] = threading.Thread(name="b",target=self.setStartup)
#         for threadName in self._init_threads.keys():
#             self._init_threads[threadName].setDaemon(True)
#             self._init_threads[threadName].start()
        #serialised alternative of setModel
        self.setCommunications()
        self.setStartup()
        self.setMainscreen()
        #self.setConfiguration()
        self.setExternalApplications()

    ######
    #---- Auxiliar methods to configure widgets
    def _setupLed4UnknownAttr(self,widget):
        widget.setLedPatternName(":leds/images256/led_{color}_{status}.png")
        widget.setOnColor('green')
        widget.setOffColor('white')

    def _setupLed4Attr(self,widget,attrName,inverted=False,onColor='green',offColor='red',pattern='on'):
        widget.setModel(attrName)
        if pattern == 'on':
            widget.setLedPatternName(":leds/images256/led_{color}_on.png")
        widget.setOnColor(onColor)
        widget.setOffColor(offColor)
        if inverted:
            widget.setLedInverted(True)

    def _setupCheckbox4UnknownAttr(self,widget):
        widget.setEnabled(False)

    def _setupCheckbox4Attr(self,widget,attrName,
                            isRst=False,DangerMsg='',
                            riseEdge=False,fallingEdge=False):
        widget.setModel(attrName)
        if isRst:
            widget.setResetCheckBox(True)
        if len(DangerMsg) > 0:
            widget.setDangerMessage(DangerMsg)
        if riseEdge:
            widget.setDangerRiseEdge(True)
        if fallingEdge:
            widget.setDangerFallingEdge(True)
        if not riseEdge and not fallingEdge:
            widget.setAutoApply(True)
            widget.setForcedApply(True)

    def _setupSpinBox4Attr(self,widget,attrName,step=None):
        widget.setModel(attrName)
        widget.setAutoApply(True)
        widget.setForcedApply(True)
        #if not step == widget.getSingleStep():
        if not step == None:
            widget.setSingleStep(step)

    def _setupTaurusLabel4Attr(self,widget,attrName,unit=None):
        widget.setModel(attrName)
        if unit:
            widget.setSuffixText(' %s'%unit)

    def _setupCombobox4Attr(self,widget,attrName,valueNames=None):
        widget.setModel(attrName)
        widget.setAutoApply(True)
        widget.setForcedApply(True)
        if valueNames != None and type(valueNames) == list and len(valueNames) > 0:
            widget.addValueNames(valueNames)
            
    def _setupActionWidget(self,widget,attrName,text='on/off',isRst=False,
                           DangerMsg='',riseEdge=False,fallingEdge=False):
        widget._ui.Label.setText(text)
        if isRst:
            self._setupLed4Attr(widget._ui.Led,attrName,
                                offColor='black',onColor='yellow')
        else:
            self._setupLed4Attr(widget._ui.Led,attrName,pattern='')
        self._setupCheckbox4Attr(widget._ui.Check,attrName,
                                 isRst)#,DangerMsg,riseEdge,fallingEdge)
    #---- Done auxiliar methods to configure widgets
    ######

    def setCommunications(self):
        #about the overview
        linacOverview = self.ui.linacOverview._ui
        
        linacOverview.plcLastUpdateTrend.setModel(['li/ct/plc1/lastUpdate',
                                                   'li/ct/plc2/lastUpdate',
                                                   'li/ct/plc3/lastUpdate',
                                                   'li/ct/plc4/lastUpdate',
                                                   'li/ct/plc5/lastUpdate'])
        #linacOverview.plcLastUpdateTrend #FIXME: show dev_name in inspector mode
        linacOverview.plcLastUpdateTrend.showLegend(False)
        linacOverview.moveLocal.setModel(DeviceRelocator)
        linacOverview.moveLocal.setCommand('MoveAllInstances')
        linacOverview.moveLocal.setParameters('local')
        linacOverview.moveLocal.setCustomText('Local')
        linacOverview.moveLocal.setDangerMessage(\
                                   "Be sure Labview is not link to these PLCs!")
        linacOverview.moveRemote.setDisabled(True)
#        linacOverview.moveRemote.setModel(DeviceRelocator)
#        linacOverview.moveRemote.setCommand('MoveAllInstances')
#        linacOverview.moveRemote.setParameters('remote')
        linacOverview.moveRemote.setCustomText('Remote')
#        linacOverview.moveRemote.setDangerMessage(\
#                                "After this action you will lose write access.")
        linacOverview.resetInstance.setModel(DeviceRelocator)
        linacOverview.resetInstance.setCommand('RestartAllInstance')
        linacOverview.resetInstance.setCustomText('Restart all')
        linacOverview.resetInstance.setDangerMessage(\
                                       "This will stop the control temporally.")
        #for each of the plcs
        plcWidgets = [self.ui.plc1,self.ui.plc2,self.ui.plc3,self.ui.plc4,self.ui.plc5]
        for i,plc in enumerate(plcWidgets):
            #plc._ui.plcGroup.setTitle("PLC %d"%(i+1))
            plc._ui.plcGroup.setModel("%s%d"%(LinacDeviceNameRoot,i+1))
            plc._ui.ResetState.setModel("%s%d"%(LinacDeviceNameRoot,i+1))
            plc._ui.ResetState.setCommand('ResetState')
            plc._ui.instanceStateRead.setModel('%s/LinacData.plc%d_state'%(DeviceRelocator,i+1))
            plc._ui.instanceLocationRead.setModel('%s/LinacData.plc%d_location'%(DeviceRelocator,i+1))
            plc._ui.moveLocal.setModel(DeviceRelocator)
            plc._ui.moveLocal.setCommand('MoveInstance')
            plc._ui.moveLocal.setParameters(['LinacData/plc%d'%(i+1),'local'])
            plc._ui.moveLocal.setCustomText('Local')
            plc._ui.moveLocal.setDangerMessage("Be sure Labview is not link to this PLC!")
            plc._ui.moveRemote.setModel(DeviceRelocator)
            plc._ui.moveRemote.setCommand('MoveInstance')
            plc._ui.moveRemote.setParameters(['LinacData/plc%d'%(i+1),'remote'])
            plc._ui.moveRemote.setCustomText('Remote')
            plc._ui.moveRemote.setDangerMessage("After this action you will lose write access.")
            plc._ui.resetInstance.setModel(DeviceRelocator)
            plc._ui.resetInstance.setCommand('RestartInstance')
            plc._ui.resetInstance.setParameters(['LinacData/plc%d'%(i+1)])
            plc._ui.resetInstance.setCustomText('Restart')
            plc._ui.resetInstance.setDangerMessage("This will stop the control temporally.")
    
    #---- setModel & others for the Start up Tab
    def setStartup(self):
        #following the synoptic regions from left to right and from top to bottom
        self._setStartup_InterlockUnit()
        self._setStartup_klystronLV()
        self._setStartup_egun()
        self._setStartup_cooling()
        self._setStartup_magnets()
        self._setStartup_vacuum()
        startup_ui = self.ui.linacStartupSynoptic._ui
        startup_ui.StartUpSchematic.lower()
        

    def _setStartup_InterlockUnit(self):
        startup_ui = self.ui.linacStartupSynoptic._ui
        #---- configure the widgets in the top left corner diagram
        self._setupLed4Attr(startup_ui.klystronAmplifierEnabledLed,
                            'li/ct/plc1/KA_ENB')                        #KA_ENB
        self._setupLed4Attr(startup_ui.magnetInterlockStateLed,
                            'li/ct/plc1/MG_IS')                          #MI_IS
        self._setupActionWidget(startup_ui.iuRst,'li/ct/plc1/interlock_rc',
                                text='Reset',isRst=True)                   #Rst
        self._setupLed4Attr(startup_ui.utilitiesInterlockStateLed,
                            'li/ct/plc1/UT_IS')                          #UI_IS
        self._setupLed4Attr(startup_ui.compressedAirStateLed,
                            'li/ct/plc2/ac_is')                          #AC_IS
        self._setupLed4Attr(startup_ui.transferlineVacuumStateLed,
                            'li/ct/plc1/TL_VOK')                        #TL_VOK
        self._setupLed4Attr(startup_ui.linacVacuumStateLed,
                            'li/ct/plc2/vc_ok')                         #LI_VOK
        self._setupLed4Attr(startup_ui.electronGunEnabledLed,
                            'li/ct/plc1/EG_ENB')                        #EG_ENB
        self._setupLed4Attr(startup_ui.gmdiLed,
                            'li/ct/plc1/GM_DI')                          #GM_DI
        self._setupLed4Attr(startup_ui.interlockUnitReadyStateLed,
                            'li/ct/plc1/IU_RDY')                            #UI
        self._setupLed4Attr(startup_ui.klystron2AmplifierEnabledLed,
                            'li/ct/plc1/ka2_ok')                        #KA2_EN
        self._setupLed4Attr(startup_ui.klystron1AmplifierEnabledLed,
                            'li/ct/plc1/ka1_ok')                        #KA1_EN
        self._setupLed4Attr(startup_ui.linacVacuumStateLed_2,
                            'li/ct/plc2/vc_ok')                         #LI_VOK
                                        #(repeated on the right side of the IU)
        self._setupLed4Attr(startup_ui.linacReadyStateLed,
                            'li/ct/plc1/li_ok')                         #LI_RDY
        #---- configure the klystrons popups:
        klystrons = {1:{'check':startup_ui.klystron1InterlockPopupCheck,
                        'widget':startup_ui.klystron1InterlockPopupWidget,
                        'sf6':startup_ui.klystron1InterlockPopupWidget._ui.sf6p1Led,
                        'sf6_attrName':'li/ct/plc1/sf6_p1_st',
                        'rfw':[startup_ui.klystron1InterlockPopupWidget._ui.rfw1Led,
                               startup_ui.klystron1InterlockPopupWidget._ui.rfw2Led],
                        'rfw_attrName':['li/ct/plc1/w1_uf','li/ct/plc1/w2_uf'],
                        'rfl':[startup_ui.klystron1InterlockPopupWidget._ui.rfl1Led,
                               startup_ui.klystron1InterlockPopupWidget._ui.rfl2Led],
                        'rfl_attrName':['li/ct/plc1/rl1_uf','li/ct/plc1/rl2_uf'],
                       },
                     2:{'check':startup_ui.klystron2InterlockPopupCheck,
                        'widget':startup_ui.klystron2InterlockPopupWidget,
                        'sf6':startup_ui.klystron2InterlockPopupWidget._ui.sf6p2Led,
                        'sf6_attrName':'li/ct/plc1/sf6_p2_st',
                        'rfw':[startup_ui.klystron2InterlockPopupWidget._ui.rfw3Led],
                        'rfw_attrName':['li/ct/plc1/w3_uf'],
                        'rfl':[startup_ui.klystron2InterlockPopupWidget._ui.rfl3Led],
                        'rfl_attrName':['li/ct/plc1/rl3_uf'],
                       }
                    }
        self._klystronsInterlocks = {}#to avoid garbage collection on the CkechboxManagers
        #Using the previous structure configure each of the klystrons interlock widgets
        for number in klystrons.keys():
            klystron = klystrons[number]
            #klystron['check'].setCheckState(False)
            klystron['widget'].hide()
            self._klystronsInterlocks[number] = CheckboxManager(klystron['check'],
                                                                klystron['widget'],
                                                                'klystron%dInterlock'%number)
            self._setupLed4Attr(klystron['sf6'],klystron['sf6_attrName'])
            for i in range(len(klystron['rfw'])):
                self._setupLed4Attr(klystron['rfw'][i],klystron['rfw_attrName'][i])
            for i in range(len(klystron['rfl'])):
                self._setupLed4Attr(klystron['rfl'][i],klystron['rfl_attrName'][i])

    def _setStartup_klystronLV(self):
        startup_ui = self.ui.linacStartupSynoptic._ui
        klystrons = {1:{'plc':4,
                        'on':startup_ui.klystron1On,
                        'rst':startup_ui.klystron1Rst,
                        'check':startup_ui.klystron1LVPopupCheck,
                        'widget':startup_ui.klystron1LVWidget},
                     2:{'plc':5,
                        'on':startup_ui.klystron2On,
                        'rst':startup_ui.klystron2Rst,
                        'check':startup_ui.klystron2LVPopupCheck,
                        'widget':startup_ui.klystron2LVWidget}}
        self._klystronLV = {}
        for number in klystrons.keys():
            #---- on/off klystron low voltage
            attrName = 'li/ct/plc%d/LV_ONC'%(klystrons[number]['plc'])
            msg="ALERT: this will shutdown the klystron %d low voltage!"%number
            self._setupActionWidget(klystrons[number]['on'],attrName,
                                    text='on/off',DangerMsg=msg,fallingEdge=True)
            #---- reset klystron low voltage
            attrName = 'li/ct/plc%d/LV_Interlock_RC'%(klystrons[number]['plc'])
            self._setupActionWidget(klystrons[number]['rst'],attrName,
                                    text='Reset',isRst=True)
            #---- popup more information
            widget = klystrons[number]['check']
            #prepare the checkmanager
            #klystrons[number]['check'].setCheckState(False)
            klystrons[number]['widget'].hide()
            self._klystronLV[number] = CheckboxManager(klystrons[number]['check'],
                                                       klystrons[number]['widget'],
                                                       "Klystron%dLVManager"%number)
            #setmodel for the contents in the popup
            widget = klystrons[number]['widget']
            widget._ui.lowVoltageGroup.setTitle('klystron%d low voltage'%(number))
            widget._ui.LV_Status.setModel('li/ct/plc%d/LV_Status'%(klystrons[number]['plc']))
            widget._ui.LV_TimeValue.setModel('li/ct/plc%d/LV_Time'%(klystrons[number]['plc']))
            widget._ui.heatStatus.setModel('li/ct/plc%d/Heat_Status'%(klystrons[number]['plc']))
            widget._ui.heatVValue.setModel('li/ct/plc%d/Heat_V'%(klystrons[number]['plc']))
            widget._ui.heatIValue.setModel('li/ct/plc%d/Heat_I'%(klystrons[number]['plc']))
            widget._ui.heatTValue.setModel('li/ct/plc%d/Heat_Time'%(klystrons[number]['plc']))

    def _setStartup_egun(self):
        startup_ui = self.ui.linacStartupSynoptic._ui
        #---- on/off electron gun low voltage
        attrName = 'li/ct/plc1/GUN_LV_ONC'
        msg = "ALERT: this will shutdown the electron gun low voltage!"
        self._setupActionWidget(startup_ui.eGunOn,attrName,
                                text='on/off',DangerMsg=msg,fallingEdge=True)
        #---- widgets in the KD box
        self._setupSpinBox4Attr(startup_ui.filamentSetpoint,'li/ct/plc1/GUN_Filament_V_setpoint',step=0.1)
        self._setupSpinBox4Attr(startup_ui.cathodeSetpoint,'li/ct/plc1/GUN_Kathode_V_setpoint',step=0.1)
        self._setupTaurusLabel4Attr(startup_ui.filamentCurrent,'li/ct/plc1/GUN_Filament_I','A')
        self._setupTaurusLabel4Attr(startup_ui.temperatureValue,'li/ct/plc1/GUN_Kathode_T','C')
        #---- popup information shown in the KD box
        startup_ui.kdeGunLVWidget.hide()
        self._egunManager = CheckboxManager(startup_ui.kdeGunLVPopupCheck,
                                            startup_ui.kdeGunLVWidget,
                                            "EGunPopup")
        popupWidget = startup_ui.kdeGunLVWidget._ui
        self._setupTaurusLabel4Attr(popupWidget.eGunStatus,'li/ct/plc1/Gun_Status')
        self._setupTaurusLabel4Attr(popupWidget.filamentValue,'li/ct/plc1/GUN_Filament_V','V')
        self._setupTaurusLabel4Attr(popupWidget.cathodeValue,'li/ct/plc1/GUN_Kathode_V','V')

    def _setStartup_cooling(self):
        startup_ui = self.ui.linacStartupSynoptic._ui
        coolingLoops = {1:{'on':startup_ui.coolingLoop1On,
                           'on_attrName':'li/ct/plc2/CL1_ONC',
                           'Temperature':startup_ui.coolingLoop1TemperatureValue,
                           'Temperature_attrName':'li/ct/plc2/CL1_T',
                           'check':startup_ui.coolingLoop1PopupCheck,
                           'widget':startup_ui.coolingLoop1Widget,
                           'status_attrName':'li/ct/plc2/CL1_Status',
                           'power_attrName':'li/ct/plc2/CL1_PWD',
                           'window':startup_ui.w1Led,
                           'window_attrName':'li/ct/plc1/w1_uf',
                           'resistorLoad':startup_ui.rl1Led,
                           'resistorLoad_attrName':'li/ct/plc1/rl1_uf'},
                        2:{'on':startup_ui.coolingLoop2On,
                           'on_attrName':'li/ct/plc2/CL2_ONC',
                           'Temperature':startup_ui.coolingLoop2TemperatureValue,
                           'Temperature_attrName':'li/ct/plc2/CL2_T',
                           'check':startup_ui.coolingLoop2PopupCheck,
                           'widget':startup_ui.coolingLoop2Widget,
                           'status_attrName':'li/ct/plc2/CL2_Status',
                           'power_attrName':'li/ct/plc2/CL2_PWD',
                           'window':startup_ui.w2Led,
                           'window_attrName':'li/ct/plc1/w2_uf',
                           'resistorLoad':startup_ui.rl2Led,
                           'resistorLoad_attrName':'li/ct/plc1/rl2_uf'},
                        3:{'on':startup_ui.coolingLoop3On,
                           'on_attrName':'li/ct/plc2/CL3_ONC',
                           'Temperature':startup_ui.coolingLoop3TemperatureValue,
                           'Temperature_attrName':'li/ct/plc2/CL3_T',
                           'check':startup_ui.coolingLoop3PopupCheck,
                           'widget':startup_ui.coolingLoop3Widget,
                           'status_attrName':'li/ct/plc2/CL3_Status',
                           'power_attrName':'li/ct/plc2/CL3_PWD',
                           'window':startup_ui.w3Led,
                           'window_attrName':'li/ct/plc1/w3_uf',
                           'resistorLoad':startup_ui.rl3Led,
                           'resistorLoad_attrName':'li/ct/plc1/rl3_uf'}
                       }
        self._coolingLoopManagers = {}
        for number in coolingLoops.keys():
            #---- on/off the cooling loops
            widget = coolingLoops[number]['on']
            attrName = coolingLoops[number]['on_attrName']
            msg = "ALERT: this will shutdown the cooling loop %d!"%number
            self._setupActionWidget(widget,attrName,text='on/off',
                                    DangerMsg=msg,fallingEdge=True)
            #---- cooling temperature setpoint
            widget = coolingLoops[number]['Temperature']
            attrName = coolingLoops[number]['Temperature_attrName']+'_setpoint'
            self._setupSpinBox4Attr(widget,attrName,step=0.1)
            #---- popup information about each cooling loop
            button = coolingLoops[number]['check']
            widget = coolingLoops[number]['widget']
            title = "CollingLoopPopup%d"%number
            widget.hide()
            self._coolingLoopManagers[number] = CheckboxManager(button,widget,
                                                                title)
            popupWidget = widget._ui
            popupWidget.coolingLoopGroup.setTitle('Cooling Loop %d'%number)
            #inside the popup
            self._setupTaurusLabel4Attr(popupWidget.coolingLoopStatus,
                                       coolingLoops[number]['status_attrName'])
            self._setupTaurusLabel4Attr(popupWidget.temperatureValue,
                              coolingLoops[number]['Temperature_attrName'],'C')
            self._setupTaurusLabel4Attr(popupWidget.powerValue,
                                    coolingLoops[number]['power_attrName'],'%')
            self._setupLed4Attr(coolingLoops[number]['window'],
                                coolingLoops[number]['window_attrName'])
            self._setupLed4Attr(coolingLoops[number]['resistorLoad'],
                                coolingLoops[number]['resistorLoad_attrName'])

    def _setStartup_magnets(self):
        startup_ui = self.ui.linacStartupSynoptic._ui
        self._setupLed4Attr(startup_ui.sl1Led,'li/ct/plc3/SL1_cooling')
        self._setupLed4Attr(startup_ui.sl2Led,'li/ct/plc3/SL2_cooling')
        self._setupLed4Attr(startup_ui.sl3Led,'li/ct/plc3/SL3_cooling')
        self._setupLed4Attr(startup_ui.sl4Led,'li/ct/plc3/SL4_cooling')
        self._setupLed4Attr(startup_ui.bc1Led,'li/ct/plc3/BC1_cooling')
        self._setupLed4Attr(startup_ui.bc2Led,'li/ct/plc3/BC2_cooling')
        self._setupLed4Attr(startup_ui.glLed,'li/ct/plc3/GL_cooling')
        self._setupLed4Attr(startup_ui.as1Led,'li/ct/plc3/AS1_cooling')
        self._setupLed4Attr(startup_ui.qtLed,'li/ct/plc3/QT_cooling')
        self._setupLed4Attr(startup_ui.as2Led,'li/ct/plc3/AS2_cooling')

    def _setStartup_vacuum(self):
        startup_ui = self.ui.linacStartupSynoptic._ui
        vacuumValves = {1:{'open':startup_ui.vacuumValve1On,
                           'led':startup_ui.vacuumValve1OnLedInfo,
                           'open_attrName':'li/ct/plc2/VV1_OC',
                           'status':startup_ui.vacuumValve1OnStatus,
                           'status_attrName':'li/ct/plc2/VV1_Status'},
                        2:{'open':startup_ui.vacuumValve2On,
                           'led':startup_ui.vacuumValve2OnLedInfo,
                           'open_attrName':'li/ct/plc2/VV2_OC',
                           'status':startup_ui.vacuumValve2OnStatus,
                           'status_attrName':'li/ct/plc2/VV2_Status'},
                        3:{'open':startup_ui.vacuumValve3On,
                           'led':startup_ui.vacuumValve3OnLedInfo,
                           'open_attrName':'li/ct/plc2/VV3_OC',
                           'status':startup_ui.vacuumValve3OnStatus,
                           'status_attrName':'li/ct/plc2/VV3_Status'},
                        4:{'open':startup_ui.vacuumValve4On,
                           'led':startup_ui.vacuumValve4OnLedInfo,
                           'open_attrName':'li/ct/plc2/VV4_OC',
                           'status':startup_ui.vacuumValve4OnStatus,
                           'status_attrName':'li/ct/plc2/VV4_Status'},
                        5:{'open':startup_ui.vacuumValve5On,
                           'led':startup_ui.vacuumValve5OnLedInfo,
                           'open_attrName':'li/ct/plc2/VV5_OC',
                           'status':startup_ui.vacuumValve5OnStatus,
                           'status_attrName':'li/ct/plc2/VV5_Status'},
                        6:{'open':startup_ui.vacuumValve6On,
                           'led':startup_ui.vacuumValve6OnLedInfo,
                           'open_attrName':'li/ct/plc2/VV6_OC',
                           'status':startup_ui.vacuumValve6OnStatus,
                           'status_attrName':'li/ct/plc2/VV6_Status'},
                        7:{'open':startup_ui.vacuumValve7On,
                           'led':startup_ui.vacuumValve7OnLedInfo,
                           'open_attrName':'li/ct/plc2/VV7_OC',
                           'status':startup_ui.vacuumValve7OnStatus,
                           'status_attrName':'li/ct/plc2/VV7_Status'},
                       }
        #---- open/close all valve in one action
        widget = startup_ui.vvOn
        attrName = 'li/ct/plc2/VVall_oc'
        self._setupActionWidget(widget,attrName,text='open/close')
        #---- reset vacuum interlocks
        widget = startup_ui.vvRst
        attrName = 'li/ct/plc2/VC_Interlock_RC'
        self._setupActionWidget(widget,attrName,text='Reset',isRst=True)
        for number in vacuumValves.keys():
            #---- on/off each vacuum valve
            attrName = vacuumValves[number]['open_attrName']
            widget = vacuumValves[number]['led']
            self._setupLed4Attr(widget,attrName)
            widget = vacuumValves[number]['open']
            self._setupActionWidget(widget,attrName,text='open/close')
            #---- status of each vacuum valve
            widget = vacuumValves[number]['status']
            attrName = vacuumValves[number]['status_attrName']
            self._setupTaurusLabel4Attr(widget,attrName)

        #---- area of the vacuum information (TODO: may not well written)
        startup_ui.ip1Led.setModel('li/ct/plc2/IP1_IS')
        startup_ui.ip2Led.setModel('li/ct/plc2/IP2_IS')
        startup_ui.ip3Led.setModel('li/ct/plc2/IP3_IS')
        startup_ui.ip4Led.setModel('li/ct/plc2/IP4_IS')
        startup_ui.ip5Led.setModel('li/ct/plc2/IP5_IS')
        startup_ui.ip6Led.setModel('li/ct/plc2/IP6_IS')
        startup_ui.ip7Led.setModel('li/ct/plc2/IP7_IS')
        startup_ui.ip8Led.setModel('li/ct/plc2/IP8_IS')
        startup_ui.ip9Led.setModel('li/ct/plc2/IP9_IS')
        startup_ui.hvg1Led.setModel('li/ct/plc2/HVG1_IS')
        self._setupTaurusLabel4Attr(startup_ui.hvg1Value,
                                    'li/ct/plc2/HVG1_P','mbar')
        startup_ui.hvg2Led.setModel('li/ct/plc2/HVG2_IS')
        self._setupTaurusLabel4Attr(startup_ui.hvg2Value,
                                    'li/ct/plc2/HVG2_P','mbar')
        startup_ui.hvg3Led.setModel('li/ct/plc2/HVG3_IS')
        self._setupTaurusLabel4Attr(startup_ui.hvg3Value,
                                    'li/ct/plc2/HVG3_P','mbar')
        startup_ui.hvg4Led.setModel('li/ct/plc2/HVG4_IS')
        self._setupTaurusLabel4Attr(startup_ui.hvg4Value,
                                    'li/ct/plc2/HVG4_P','mbar')
        startup_ui.hvg5Led.setModel('li/ct/plc2/HVG5_IS')
        self._setupTaurusLabel4Attr(startup_ui.hvg5Value,
                                    'li/ct/plc2/HVG5_P','mbar')
        self._setupTaurusLabel4Attr(startup_ui.ipc1Value1,
                                    'li/ct/plc2/IP1_P','mbar')
        self._setupTaurusLabel4Attr(startup_ui.ipc1Value2,
                                    'li/ct/plc2/IP2_P','mbar')
        self._setupTaurusLabel4Attr(startup_ui.ipc2Value1,
                                    'li/ct/plc2/IP3_P','mbar')
        self._setupTaurusLabel4Attr(startup_ui.ipc2Value2,
                                    'li/ct/plc2/IP4_P','mbar')
        self._setupTaurusLabel4Attr(startup_ui.ipc3Value1,
                                    'li/ct/plc2/IP5_P','mbar')
        self._setupTaurusLabel4Attr(startup_ui.ipc3Value2,
                                    'li/ct/plc2/IP6_P','mbar')
        self._setupTaurusLabel4Attr(startup_ui.ipc4Value1,
                                    'li/ct/plc2/IP7_P','mbar')
        self._setupTaurusLabel4Attr(startup_ui.ipc4Value2,
                                    'li/ct/plc2/IP8_P','mbar')
        self._setupTaurusLabel4Attr(startup_ui.ipc5Value1,
                                    'li/ct/plc2/IP9_P','mbar')

    #---- setModel & others for the Main Screen Tab
    def setMainscreen(self):
        #following the synoptic regions from left to right and 
        #from top to bottom
        self._setMainscreen_tb()
        self._setMainscreen_klystronHV()
        self._setMainscreen_rf()
        self._setMainscreen_cl()
        self._setMainscreen_kd()
        self._setMainscreen_magnets()
        self._setMainscreen_hvs()
        self._setMainscreen_vacuum()
        self._setMainscreen_fs()
        self._setMainscreen_bcm()
        startup_ui = self.ui.linacMainscreenSynoptic._ui
        startup_ui.MainScreenSchematic.lower()
        
    def _setMainscreen_tb(self):
        mainscreen_ui = self.ui.linacMainscreenSynoptic._ui
        self._setupSpinBox4Attr(mainscreen_ui.tbKaDelay1Value,
                                    'li/ct/plc1/TB_KA1_Delay')
        self._setupSpinBox4Attr(mainscreen_ui.tbKaDelay2Value,
                                    'li/ct/plc1/TB_KA2_Delay')
        self._setupTaurusLabel4Attr(mainscreen_ui.tbRf2DelayValue,
                                    'li/ct/plc1/TB_RF2_Delay',unit='ns')
        self._setupSpinBox4Attr(mainscreen_ui.tbGunLevelValue,
                                'li/ct/plc1/TB_GPA',step=0.1)
        self._setupTaurusLabel4Attr(mainscreen_ui.tbMultiBunchValue,
                                    'li/ct/plc1/TB_MBM_status')
        self._setupCheckbox4Attr(mainscreen_ui.tbMultiBunchCheck,
                                 'li/ct/plc1/TB_MBM')
        self._operationModeMonitor = OperationModeManager(mainscreen_ui)
        #---- FIXME: the addValueNames fails in some versions of taurus,
        #            but it works in the control's room version
        try:
            self._setupCombobox4Attr(mainscreen_ui.tbGatedPulseModeCombo,
                                     'li/ct/plc1/TB_GPM',
                                     [('beam on',0),('mix',1),('beam off',2)])
        except:
            mainscreen_ui.tbGatedPulseModeValue.setEnabled(False)
        self._setupSpinBox4Attr(mainscreen_ui.tbGunDelayValue,
                                'li/ct/plc1/TB_Gun_Delay',step=32)
        self._setupSpinBox4Attr(mainscreen_ui.tbWidthValue,
                                'li/ct/plc1/TB_GPI',step=2)
        self._setupSpinBox4Attr(mainscreen_ui.tbNumberValue,
                                'li/ct/plc1/TB_GPN',step=1)
        self._setupLed4Attr(mainscreen_ui.tbTimerStatusStateLed,
                            'li/ct/plc1/TB_ST')
        self._setupLed4Attr(mainscreen_ui.rfEnbLed,'li/ct/plc1/RF_OK')
    
    def _setMainscreen_klystronHV(self):
        mainscreen_ui = self.ui.linacMainscreenSynoptic._ui
        klystrons = {1:{'readBack':{'widget':mainscreen_ui.klystron1HVRead,
                                    'attrName':'li/ct/plc4/HVPS_V'},
                        'setpoint':{'widget':mainscreen_ui.klystron1HVWrite,
                                    'attrName':'li/ct/plc4/HVPS_V_setpoint'},
                        'rst':{'widget':mainscreen_ui.klystron1Rst,
                               'attrName':'li/ct/plc4/HVPS_Interlock_RC'},
                        'on':{'widget':mainscreen_ui.klystron1On,
                              'attrName':'li/ct/plc4/HVPS_ONC'},
                        'check':mainscreen_ui.klystron1HVPopupCheck,
                        'widget':mainscreen_ui.klystron1HVPopupWidget},
                     2:{'readBack':{'widget':mainscreen_ui.klystron2HVRead,
                                    'attrName':'li/ct/plc5/HVPS_V'},
                        'setpoint':{'widget':mainscreen_ui.klystron2HVWrite,
                                    'attrName':'li/ct/plc5/HVPS_V_setpoint'},
                        'rst':{'widget':mainscreen_ui.klystron2Rst,
                               'attrName':'li/ct/plc5/HVPS_Interlock_RC'},
                        'on':{'widget':mainscreen_ui.klystron2On,
                              'attrName':'li/ct/plc5/HVPS_ONC'},
                        'check':mainscreen_ui.klystron2HVPopupCheck,
                        'widget':mainscreen_ui.klystron2HVPopupWidget}
                    }
        self._klystronHV = {}
        for number in klystrons.keys():
            #---- readback for the klystron HV
            widget = klystrons[number]['readBack']['widget']
            attrName = klystrons[number]['readBack']['attrName']
            self._setupTaurusLabel4Attr(widget,attrName,unit='kV')
            #---- setpoint for the klystron HV
            widget = klystrons[number]['setpoint']['widget']
            attrName = klystrons[number]['setpoint']['attrName']
            self._setupSpinBox4Attr(widget,attrName,step=0.1)
            #---- on/off klystron HV
            widget = klystrons[number]['on']['widget']
            attrName = klystrons[number]['on']['attrName']
            self._setupActionWidget(widget,attrName,text='on/off')
            #---- reset klystron HV
            widget = klystrons[number]['rst']['widget']
            attrName = klystrons[number]['rst']['attrName']
            self._setupActionWidget(widget,attrName,text='Reset',isRst=True)
            #---- popup more information
            klystrons[number]['widget'].hide()
            self._klystronHV[number] = CheckboxManager(\
                                                     klystrons[number]['check'],
                                                    klystrons[number]['widget'],
                                                   "Klystron%dHVManager"%number)
            widget = klystrons[number]['widget']._ui
            self._setupTaurusLabel4Attr(widget.hvStatusValue,
                                        'li/ct/plc%d/HVPS_Status'%(number+3))
            self._setupTaurusLabel4Attr(widget.hvVoltageValue,
                                        'li/ct/plc%d/HVPS_V'%(number+3),'kV')
            self._setupTaurusLabel4Attr(widget.hvCurrentValue,
                                        'li/ct/plc%d/HVPS_I'%(number+3),'mA')
            self._setupLed4Attr(widget.hvRampEnableLed,
                                'li/ct/plc%d/HVPS_V_setpointRampEnable'
                                %(number+3))
            self._setupCheckbox4Attr(widget.hvRampEnableCheck,
                                     'li/ct/plc%d/HVPS_V_setpointRampEnable'
                                     %(number+3))
            self._setupTaurusLabel4Attr(widget.hvRampStepValue,
                                        'li/ct/plc%d/HVPS_V_setpointStep'
                                        %(number+3),'kV')
            self._setupTaurusLabel4Attr(widget.hvRampStepTimeValue,
                                        'li/ct/plc%d/HVPS_V_setpointStepTime'
                                        %(number+3),'s')
            self._setupTaurusLabel4Attr(widget.hvRampThresholdValue,
                                        'li/ct/plc%d/HVPS_V_setpointThreshold'
                                        %(number+3),'kV')
            self._setupTaurusLabel4Attr(widget.pulseStatusValue,
                                        'li/ct/plc%d/Pulse_Status'%(number+3))
            self._setupTaurusLabel4Attr(widget.klystronVoltageValue,
                                        'li/ct/plc%d/Peak_V'%(number+3),'kV')
            self._setupTaurusLabel4Attr(widget.klystronCurrentValue,
                                        'li/ct/plc%d/Peak_I'%(number+3),'A')

    def _setMainscreen_rf(self):
        mainscreen_ui = self.ui.linacMainscreenSynoptic._ui
        timePhaseShifters = {'0':mainscreen_ui.rfTimePhaseShifter0Value,
                             '1':mainscreen_ui.rfTimePhaseShifter1Value,
                             '2':mainscreen_ui.rfTimePhaseShifter2Value,
                             'X':mainscreen_ui.rfTimePhaseShifterXValue}
        for timeShifter in timePhaseShifters.keys():
            attrName = 'li/ct/plc1/TPS%s_Phase'%timeShifter
            if timeShifter in ['0']:
                self._setupSpinBox4Attr(timePhaseShifters[timeShifter],attrName,step=0.1)
            else:
                self._setupSpinBox4Attr(timePhaseShifters[timeShifter],attrName,step=1)
        self._setupSpinBox4Attr(mainscreen_ui.rfA0OutputPowerValue,'li/ct/plc1/A0_OP',step=1)
        self._setupLed4Attr(mainscreen_ui.rfA0StatusLed,'li/ct/plc1/RFS_ST')
        self._setupSpinBox4Attr(mainscreen_ui.attenuator2Value,'li/ct/plc1/ATT2_P_setpoint',step=0.1)
        phaseShifters = {'1':{'write':mainscreen_ui.rfPhaseShifter1Value,
                              'check':mainscreen_ui.phaseShifter1PopupCheck,
                              'widget':mainscreen_ui.phaseShifter1PopupWidget},
                         '2':{'write':mainscreen_ui.rfPhaseShifter2Value,
                              'check':mainscreen_ui.phaseShifter2PopupCheck,
                              'widget':mainscreen_ui.phaseShifter2PopupWidget}}
        for shifter in phaseShifters.keys():
            attrName = 'li/ct/plc1/PHS%s_Phase_setpoint'%shifter
            self._setupSpinBox4Attr(phaseShifters[shifter]['write'],attrName,step=1)
        sf6pressures = {'1':mainscreen_ui.sf6p1Value,
                        '2':mainscreen_ui.sf6p2Value}
        for pressure in sf6pressures.keys():
            attrName = 'li/ct/plc1/SF6_P%s'%pressure
            self._setupTaurusLabel4Attr(sf6pressures[pressure],attrName,'bar')
        self._setupLed4Attr(mainscreen_ui.rfSourceStatusLed,'li/ct/plc1/RFS_ST')
        #popups
        #mainscreen_ui.attenuatorPopupCheck.setCheckState(False)
        mainscreen_ui.attenuatorPopupWidget.hide()
        self._attenuator = CheckboxManager(mainscreen_ui.attenuatorPopupCheck,
                                           mainscreen_ui.attenuatorPopupWidget,
                                           "Attenuator2")
        widget = mainscreen_ui.attenuatorPopupWidget._ui
        widget.attenuatorGroup.setTitle("Attenuator 2")
        self._setupTaurusLabel4Attr(widget.statusValue,'li/ct/plc1/ATT2_Status')
        self._setupTaurusLabel4Attr(widget.AttrValue,'li/ct/plc1/ATT2_P','dB')
        self._phaseShifters = {}
        for shifter in phaseShifters.keys():
            #phaseShifters[shifter]['check'].setCheckState(False)
            phaseShifters[shifter]['widget'].hide()
            self._phaseShifters[shifter] = CheckboxManager(phaseShifters[shifter]['check'],
                                                           phaseShifters[shifter]['widget'],
                                                           "PhaseShifter%s"%shifter)
            widget = phaseShifters[shifter]['widget']._ui
            widget.phaseShifterGroup.setTitle("Phase Shifter %s"%shifter)
            self._setupTaurusLabel4Attr(widget.statusValue,'li/ct/plc1/PHS%s_Status'%shifter)
            self._setupTaurusLabel4Attr(widget.attrValue,'li/ct/plc1/PHS%s_Phase'%shifter)

    def _setMainscreen_cl(self):
        mainscreen_ui = self.ui.linacMainscreenSynoptic._ui
        coolingLoops = {1:mainscreen_ui.coolingLoop1Led,
                        2:mainscreen_ui.coolingLoop2Led,
                        3:mainscreen_ui.coolingLoop3Led,
                        }
        for loop in coolingLoops.keys():
            attrName = 'li/ct/plc2/CL%s_ONC'%loop
            self._setupLed4Attr(coolingLoops[loop], attrName)
    def _setMainscreen_kd(self):
        mainscreen_ui = self.ui.linacMainscreenSynoptic._ui
        self._setupSpinBox4Attr(mainscreen_ui.filamentSetpoint,'li/ct/plc1/GUN_Filament_V_setpoint',step=0.1)
        self._setupSpinBox4Attr(mainscreen_ui.cathodeSetpoint,'li/ct/plc1/GUN_Kathode_V_setpoint',step=0.1)
        self._setupTaurusLabel4Attr(mainscreen_ui.filamentCurrent,'li/ct/plc1/GUN_Filament_I','A')
        self._setupTaurusLabel4Attr(mainscreen_ui.temperatureValue,'li/ct/plc1/GUN_Kathode_T','C')

    def _setMainscreen_magnets(self):
        mainscreen_ui = self.ui.linacMainscreenSynoptic._ui
        magnets = {'sl1':{'info':  mainscreen_ui.sl1LedInfo,
                          'check': mainscreen_ui.sl1PopupCheck,
                          'widget':mainscreen_ui.sl1PopupWidget,
                          'h':     mainscreen_ui.sl1hValue,
                          'v':     mainscreen_ui.sl1vValue,
                          'f':     mainscreen_ui.sl1fValue,
                          'on':    mainscreen_ui.sl1On},
                   'sl2':{'info':  mainscreen_ui.sl2LedInfo,
                          'check': mainscreen_ui.sl2PopupCheck,
                          'widget':mainscreen_ui.sl2PopupWidget,
                          'h':     mainscreen_ui.sl2hValue,
                          'v':     mainscreen_ui.sl2vValue,
                          'f':     mainscreen_ui.sl2fValue,
                          'on':    mainscreen_ui.sl2On},
                   'sl3':{'info':  mainscreen_ui.sl3LedInfo,
                          'check': mainscreen_ui.sl3PopupCheck,
                          'widget':mainscreen_ui.sl3PopupWidget,
                          'h':     mainscreen_ui.sl3hValue,
                          'v':     mainscreen_ui.sl3vValue,
                          'f':     mainscreen_ui.sl3fValue,
                          'on':    mainscreen_ui.sl3On},
                   'sl4':{'info':  mainscreen_ui.sl4LedInfo,
                          'check': mainscreen_ui.sl4PopupCheck,
                          'widget':mainscreen_ui.sl4PopupWidget,
                          'h':     mainscreen_ui.sl4hValue,
                          'v':     mainscreen_ui.sl4vValue,
                          'f':     mainscreen_ui.sl4fValue,
                          'on':    mainscreen_ui.sl4On},
                   'bc1':{'info':  mainscreen_ui.bc1LedInfo,
                          'check': mainscreen_ui.bc1PopupCheck,
                          'widget':mainscreen_ui.bc1PopupWidget,
                          'h':     mainscreen_ui.bc1hValue,
                          'v':     mainscreen_ui.bc1vValue,
                          'f':     mainscreen_ui.bc1fValue,
                          'on':    mainscreen_ui.bc1On},
                   'bc2':{'info':  mainscreen_ui.bc2LedInfo,
                          'check': mainscreen_ui.bc2PopupCheck,
                          'widget':mainscreen_ui.bc2PopupWidget,
                          'h':     mainscreen_ui.bc2hValue,
                          'v':     mainscreen_ui.bc2vValue,
                          'f':     mainscreen_ui.bc2fValue,
                          'on':    mainscreen_ui.bc2On},
                   'gl': {'info':  mainscreen_ui.glLedInfo,
                          'check': mainscreen_ui.glPopupCheck,
                          'widget':mainscreen_ui.glPopupWidget,
                          'h':     mainscreen_ui.glhValue,
                          'v':     mainscreen_ui.glvValue,
                          'f':     mainscreen_ui.glfValue,
                          'on':    mainscreen_ui.glOn},
                   'as1':{'info':  mainscreen_ui.as1LedInfo,
                          'check': mainscreen_ui.as1PopupCheck,
                          'widget':mainscreen_ui.as1PopupWidget,
                          'h':     mainscreen_ui.as1hValue,
                          'v':     mainscreen_ui.as1vValue,
                          'on':    mainscreen_ui.as1On},
                   'qt' :{'info':  mainscreen_ui.qtLedInfo,
                          'on':    mainscreen_ui.qtOn},
                   'qt1':{'h':     mainscreen_ui.qt1hValue,
                          'v':     mainscreen_ui.qt1vValue,
                          'f':     mainscreen_ui.qt1fValue,
                          'check': mainscreen_ui.qt1PopupCheck,
                          'widget':mainscreen_ui.qt1PopupWidget},
                   'qt2':{'f':     mainscreen_ui.qt2fValue,
                          'check': mainscreen_ui.qt2PopupCheck,
                          'widget':mainscreen_ui.qt2PopupWidget},
                   'as2':{'info':  mainscreen_ui.as2LedInfo,
                          'check': mainscreen_ui.as2PopupCheck,
                          'widget':mainscreen_ui.as2PopupWidget,
                          'h':     mainscreen_ui.as2hValue,
                          'v':     mainscreen_ui.as2vValue,
                          'on':    mainscreen_ui.as2On},
                   }
        self._magnets = {}
        for magnet in magnets.keys():
            deviceName = 'li/ct/plc3'
            if magnets[magnet].has_key('info'):
                widget = magnets[magnet]['info']
                attrName = '%s/%s_current_ok'%(deviceName,magnet)
                self._setupLed4Attr(widget,attrName)
            if magnets[magnet].has_key('h'):
                widget = magnets[magnet]['h']
                attrName = '%s/%sh_I_setpoint'%(deviceName,magnet)
                self._setupSpinBox4Attr(widget,attrName,step=0.01)
            if magnets[magnet].has_key('v'):
                widget = magnets[magnet]['v']
                attrName = '%s/%sv_I_setpoint'%(deviceName,magnet)
                self._setupSpinBox4Attr(widget,attrName,step=0.01)
            if magnets[magnet].has_key('f'):
                widget = widget = magnets[magnet]['f']
                attrName = '%s/%sf_I_setpoint'%(deviceName,magnet)
                #Special exception:
                if magnet in ['qt1','qt2']:
                    step = 0.005
                else:
                    step = 0.01
                self._setupSpinBox4Attr(widget,attrName,step)
            if magnets[magnet].has_key('on'):
                widget = magnets[magnet]['on']
                attrName = '%s/%s_onc'%(deviceName,magnet)
                self._setupActionWidget(widget,attrName,text='on/off')
            if magnets[magnet].has_key('check') and \
               magnets[magnet].has_key('widget'):
                #---- popup with more magnet information
                magnets[magnet]['widget'].hide()
                button = magnets[magnet]['check']
                widget = magnets[magnet]['widget']
                title = "%s"%magnet
                self._magnets[magnet] = CheckboxManager(button,widget,title)
                #---- information with in the popup
                widget = magnets[magnet]['widget']._ui
                widget.magnetGroup.setTitle(magnet)
                #x,y,width,height = widget.x(),widget.y(),
                #                   widget.width(),widget.height()
                #final_height = 25
                if magnets[magnet].has_key('h'):
                    self._setupTaurusLabel4Attr(widget.horizontalValue,
                                                '%s/%sh_I'%(deviceName,magnet),
                                                'A')
                    self._setupTaurusLabel4Attr(widget.horizontalStatus,
                                                '%s/%sh_Status'
                                                %(deviceName,magnet))
                    #final_height+=25
                else:
                    widget.horizontalLabel.hide()
                    widget.horizontalValue.hide()
                    widget.horizontalStatus.hide()
                if magnets[magnet].has_key('v'):
                    self._setupTaurusLabel4Attr(widget.verticalValue,
                                                '%s/%sv_I'%(deviceName,magnet),
                                                'A')
                    self._setupTaurusLabel4Attr(widget.verticalStatus,
                                                '%s/%sv_Status'
                                                %(deviceName,magnet))
                    #final_height+=25
                else:
                    widget.verticalLabel.hide()
                    widget.verticalValue.hide()
                    widget.verticalStatus.hide()
                if magnets[magnet].has_key('f'):
                    self._setupTaurusLabel4Attr(widget.focusValue,
                                                '%s/%sf_I'%(deviceName,magnet),
                                                'A')
                    self._setupTaurusLabel4Attr(widget.focusStatus,
                                                '%s/%sf_Status'
                                                %(deviceName,magnet))
                    #final_height+=25
                else:
                    widget.focusLabel.hide()
                    widget.focusValue.hide()
                    widget.focusStatus.hide()
                #wiget.setGeometry(Qt.QtCore.QRect(x,y,width,final_height))
        #---- Reset magnets interlocks
        widget = mainscreen_ui.magnetsRst
        attrName = 'li/ct/plc3/MA_Interlock_RC'
        self._setupActionWidget(widget,attrName,text='Reset',isRst=True)
        #---- on/off all the magnets
        widget = mainscreen_ui.magnetsOn
        attrName = 'li/ct/plc3/all_onc'
        self._setupActionWidget(widget,attrName,text='on/off')

    def _setMainscreen_hvs(self):
        mainscreen_ui = self.ui.linacMainscreenSynoptic._ui
        self._setupTaurusLabel4Attr(mainscreen_ui.eGunHVStatus,
                                    'li/ct/plc1/Gun_HV_Status')
        self._setupTaurusLabel4Attr(mainscreen_ui.eGunHVValue,
                                    'li/ct/plc1/GUN_HV_V','kV')
        self._setupSpinBox4Attr(mainscreen_ui.hvsVoltageValue,
                                'li/ct/plc1/GUN_HV_V_setpoint',step=0.1)
        self._setupTaurusLabel4Attr(mainscreen_ui.hvsCurrentValue,
                                    'li/ct/plc1/GUN_HV_I','uA')
        #---- on/off the HVS
        widget = mainscreen_ui.hvsOn
        attrName = 'li/ct/plc1/gun_hv_onc'
        self._setupActionWidget(widget,attrName,text='on/off')
        #---- popup with extra information
        mainscreen_ui.hvsPopupWidget.hide()
        self._hvs = CheckboxManager(mainscreen_ui.hvsPopupCheck,
                                    mainscreen_ui.hvsPopupWidget,"HVS")
        widget = mainscreen_ui.hvsPopupWidget._ui
        self._setupLed4Attr(widget.doorInterlockLed,'li/ct/plc1/gm_di')
        
    def _setMainscreen_vacuum(self):
        mainscreen_ui = self.ui.linacMainscreenSynoptic._ui
        attrName = 'li/ct/plc2/VCV_ONC'
        widget = mainscreen_ui.vcvOnLedInfo
        self._setupLed4Attr(widget,attrName)
        widget = mainscreen_ui.vcvOn
        self._setupActionWidget(widget,attrName,text='open/close')
        vacuumCavities = {'eGun':{'check':mainscreen_ui.eGunVacuumCheck,
                                  'widget':mainscreen_ui.eGunVacuumWidget,
                                  'hvg':'li/ct/plc2/HVG1_P',
                                  'ipA':'IP1',
                                  'ipB':'IP2'},
                          'preBuncher':{'check':mainscreen_ui.preBuncherVacuumCheck,
                                        'widget':mainscreen_ui.preBuncherVacuumWidget,
                                        'hvg':'li/ct/plc2/HVG2_P',
                                        'ipA':'IP3'},
                          'buncher':{'check':mainscreen_ui.buncherVacuumCheck,
                                     'widget':mainscreen_ui.buncherVacuumWidget,
                                     'hvg':'li/ct/plc2/HVG3_P',
                                     'ipA':'IP4',
                                     'ipB':'IP5'},
                          'as1':{'check':mainscreen_ui.as1VacuumCheck,
                                 'widget':mainscreen_ui.as1VacuumWidget,
                                  'hvg':'li/ct/plc2/HVG4_P',
                                  'ipA':'IP6',
                                  'ipB':'IP7'},
                          'as2':{'check':mainscreen_ui.as2VacuumCheck,
                                 'widget':mainscreen_ui.as2VacuumWidget,
                                 'hvg':'li/ct/plc2/HVG5_P',
                                 'ipA':'IP8',
                                 'ipB':'IP9'}}
        self._vacuumCavities = {}
        for cavity in vacuumCavities.keys():
            check = vacuumCavities[cavity]['check']
            widget = vacuumCavities[cavity]['widget']
            widget.hide()
            self._vacuumCavities[cavity] = CheckboxManager(check,widget)
            widget._ui.vacuumGroup.setTitle(cavity)
            hvg = vacuumCavities[cavity]['hvg']
            self._setupTaurusLabel4Attr(widget._ui.HVGValue,hvg,'bar')
            if vacuumCavities[cavity].has_key('ipA'):
                ipA = vacuumCavities[cavity]['ipA']
                widget._ui.IonPumpALabel.setText(ipA)
                self._setupLed4Attr(widget._ui.IonPumpALed,'li/ct/plc2/%s_IS'%(ipA))
            else:
                widget._ui.IonPumpALabel.hide()
                widget._ui.IonPumpALed.hide()
            if vacuumCavities[cavity].has_key('ipB'):
                ipB = vacuumCavities[cavity]['ipB']
                widget._ui.IonPumpBLabel.setText(ipB)
                self._setupLed4Attr(widget._ui.IonPumpBLed,'li/ct/plc2/%s_IS'%(ipB))
            else:
                widget._ui.IonPumpBLabel.hide()
                widget._ui.IonPumpBLed.hide()
        
    def _setMainscreen_fs(self):
        mainscreen_ui = self.ui.linacMainscreenSynoptic._ui
        fluorescentScreens = {1:{'valve':{'widget':mainscreen_ui.fluorescentScreen1Valve,
                                          'attrName':'li/ct/plc1/SCM1_DC'},
                                 'light':{'widget':mainscreen_ui.fluorescentScreen1Light,
                                          'attrName':'li/ct/plc1/SCM1_LC'},
                                 'status':{'widget':mainscreen_ui.fluorescentScreen1Status,
                                           'attrName':'li/ct/plc1/SCM1_Status'},
                                 'view':{'widget':mainscreen_ui.fluorescentScreen1View,
                                         'attrName':'li/di/fs-01'}},
                              2:{'valve':{'widget':mainscreen_ui.fluorescentScreen2Valve,
                                          'attrName':'li/ct/plc1/SCM2_DC'},
                                 'light':{'widget':mainscreen_ui.fluorescentScreen2Light,
                                          'attrName':'li/ct/plc1/SCM2_LC'},
                                 'status':{'widget':mainscreen_ui.fluorescentScreen2Status,
                                           'attrName':'li/ct/plc1/SCM2_Status'},
                                 'view':{'widget':mainscreen_ui.fluorescentScreen2View,
                                         'attrName':'li/di/fs-02'}},
                              3:{'valve':{'widget':mainscreen_ui.fluorescentScreen3Valve,
                                          'attrName':'li/ct/plc1/SCM3_DC'},
                                 'light':{'widget':mainscreen_ui.fluorescentScreen3Light,
                                          'attrName':'li/ct/plc1/SCM3_LC'},
                                 'status':{'widget':mainscreen_ui.fluorescentScreen3Status,
                                           'attrName':'li/ct/plc1/SCM3_Status'},
                                 'view':{'widget':mainscreen_ui.fluorescentScreen3View,
                                         'attrName':'li/di/fs-03'}}}
        self._fluorescentScreensViewButtons = []
        for fs in fluorescentScreens.keys():
            for element in fluorescentScreens[fs].keys():
                if element in ['valve','light']:
                    widget = fluorescentScreens[fs][element]['widget']
                    attrName = fluorescentScreens[fs][element]['attrName']
                    if element == 'valve':
                        text = 'in/out'
                    else:
                        text = 'on/off'
                    self._setupActionWidget(widget,attrName,text)
                elif element == 'status':
                    widget = fluorescentScreens[fs][element]['widget']
                    attrName = fluorescentScreens[fs][element]['attrName']
                    self._setupTaurusLabel4Attr(widget,attrName)
                elif element == 'view':
                    button = fluorescentScreens[fs][element]['widget']
                    attrName = fluorescentScreens[fs][element]['attrName']
                    listener = ViewButtonListener(button,attrName)
                    self._fluorescentScreensViewButtons.append(listener)

    def _setMainscreen_bcm(self):
        bcm = self.ui.linacMainscreenSynoptic._ui.beamChargeMonitors._ui
        self._setupTaurusLabel4Attr(bcm.liValue,'li/di/bcm-01/charge', unit='nC')
        self._setupTaurusLabel4Attr(bcm.lt01Value,'lt01/di/bcm-01/charge', unit='nC')
        self._setupTaurusLabel4Attr(bcm.lt02Value,'lt02/di/bcm-01/charge', unit='nC')

#    #---- setModel & others for the Configuration Tab
#    def setConfiguration(self):
#        configuration_ui = self.ui.linacConfigurationScreen._ui
#        self._configurationWidgets = {}
#        #---- configure the widgets in the panels
#        self.electronGunConfiguration(configuration_ui.electronGunSnapshot._ui)
#        self.coolingLoopsConfiguration(configuration_ui.coolingLoopSnapshot._ui)
#        self.vacuumValvesConfiguration(configuration_ui.vacuumValveSnapshot._ui)
#        self.magnetsConfiguration(configuration_ui.magnetSnapshot._ui)
#        self.radiofrequencyConfiguration(configuration_ui.radioFrequencySnapshot._ui)
#        self.timingConfiguration(configuration_ui.timingSnapshot._ui)
#        self.klystronsConfiguration(configuration_ui.klystronSnapshot._ui)
#        #---- TODO: connect buttons to their actions
#        self.buttonsConfiguration(configuration_ui.buttonBox)
#        # Those actions must have DangerMessage for eGunLV, CLs and KaLV
#        #---- TODO: load current values to the "save/retrieve" column of widgets
#        #           (this is the reset button action)
#        
#    def electronGunConfiguration(self,ui):
#        devName = 'li/ct/plc1'
#        widgetsSet = {}
#        
#        attrName = '%s/GUN_Filament_V_setpoint'%(devName)
#        widgetsSet[attrName] = {'read': ui.GunFilamentLowVoltageRead,
#                                'write':ui.GunFilamentLowVoltageWrite,
#                                'check':ui.GunFilamentLowVoltageCheck}
#        self._setupTaurusLabel4Attr(widgetsSet[attrName]['read'],attrName)
#        
#        attrName = '%s/Gun_kathode_v_setpoint'%(devName)
#        widgetsSet[attrName] = {'read': ui.GunKathodeLowVoltageRead,
#                                'write':ui.GunKathodeLowVoltageWrite,
#                                'check':ui.GunKathodeLowVoltageCheck}
#        self._setupTaurusLabel4Attr(widgetsSet[attrName]['read'],attrName)
#        
#        attrName = '%s/Gun_hv_v_setpoint'%(devName)
#        widgetsSet[attrName] = {'read':ui.GunHighVoltagePowerSupplyRead,
#                                'write':ui.GunHighVoltagePowerSupplyWrite,
#                                'check':ui.GunHighVoltagePowerSupplyCheck}
#        self._setupTaurusLabel4Attr(widgetsSet[attrName]['read'],attrName)
#        
#        #---- TODO: connect the ToApplyTitle to check/uncheck all the *Check
#        self._configurationWidgets['eGun'] = widgetsSet
#
#    def coolingLoopsConfiguration(self,ui):
#        devName = 'li/ct/plc2'
#        widgetsSet = {}
#        
#        #CL1
#        attrName = '%s/cl1_t_setpoint'%(devName)
#        widgetsSet[attrName] = {'read':ui.coolingLoop1SetpointRead,
#                                'write':ui.coolingLoop1SetpointWrite,
#                                'check':ui.coolingLoop1SetpointCheck}
#        self._setupTaurusLabel4Attr(widgetsSet[attrName]['read'],attrName)
#        
#        #----
#        #CL2
#        attrName = '%s/cl2_t_setpoint'%(devName)
#        widgetsSet[attrName] = {'read':ui.coolingLoop2SetpointRead,
#                                'write':ui.coolingLoop2SetpointWrite,
#                                'check':ui.coolingLoop2SetpointCheck}
#        self._setupTaurusLabel4Attr(widgetsSet[attrName]['read'],attrName)
#        #CL3
#        attrName = '%s/cl3_t_setpoint'%(devName)
#        widgetsSet[attrName] = {'read':ui.coolingLoop3SetpointRead,
#                                'write':ui.coolingLoop3SetpointWrite,
#                                'check':ui.coolingLoop3SetpointCheck}
#        self._setupTaurusLabel4Attr(widgetsSet[attrName]['read'],attrName)
#        #---- TODO: connect the ToApplyTitle to check/uncheck all the *Check
#        self._configurationWidgets['coolingLoop'] = widgetsSet
#    
#    def vacuumValvesConfiguration(self,ui):
#        self._setupLed4Attr(ui.VaccumCollimatorValveRead,'li/ct/plc2/VCV_ONC')
#        
#        #---- TODO: connect the ToApplyTitle to check/uncheck all the *Check
#
#    def magnetsConfiguration(self,ui):
#        magnets = {'sl':{'1':{'h':ui.sl1HRead,
#                              'v':ui.sl1VRead,
#                              'f':ui.sl1FRead},
#                         '2':{'h':ui.sl2HRead,
#                              'v':ui.sl2VRead,
#                              'f':ui.sl2FRead},
#                         '3':{'h':ui.sl3HRead,
#                              'v':ui.sl3VRead,
#                              'f':ui.sl3FRead},
#                         '4':{'h':ui.sl4HRead,
#                              'v':ui.sl4VRead,
#                              'f':ui.sl4FRead}},
#                   'bc':{'1':{'h':ui.bc1HRead,
#                              'v':ui.bc1VRead,
#                              'f':ui.bc1FRead},
#                         '2':{'h':ui.bc2HRead,
#                              'v':ui.bc2VRead,
#                              'f':ui.bc2FRead}},
#                   'gl':{'':{'h':ui.glHRead,
#                             'v':ui.glVRead,
#                             'f':ui.glFRead}},
#                   'as':{'1':{'h':ui.as1HRead,
#                              'v':ui.as1VRead},
#                         '2':{'h':ui.as2HRead,
#                              'v':ui.as2VRead}},
#                   'qt':{'1':{'h':ui.qt1HRead,
#                              'v':ui.qt1VRead,
#                              'f':ui.qt1FRead},
#                         '2':{'f':ui.qt2FRead}}
#                   }
#        for family in magnets.keys():
#            for magnet in magnets[family].keys():
#                for component in magnets[family][magnet].keys():
#                    widget = magnets[family][magnet][component]
#                    if component in ['h','v','f']:
#                        attrName = 'li/ct/plc3/%s%s%s_I_setpoint'%(family,magnet,component)
#                        self._setupTaurusLabel4Attr(widget,attrName)
#        #---- TODO: connect the ToApplyTitle to check/uncheck all the *Check
#    
#    def radiofrequencyConfiguration(self,ui):
#        self._setupTaurusLabel4Attr(ui.TPS0PhaseRead,'li/ct/plc1/TPS0_Phase')
#        self._setupTaurusLabel4Attr(ui.TPSXPhaseRead,'li/ct/plc1/TPSX_Phase')
#        self._setupTaurusLabel4Attr(ui.TPS1PhaseRead,'li/ct/plc1/TPS1_Phase')
#        self._setupTaurusLabel4Attr(ui.TPS2PhaseRead,'li/ct/plc1/TPS2_Phase')
#        self._setupTaurusLabel4Attr(ui.A0OPRead,'li/ct/plc1/A0_OP')
#        self._setupTaurusLabel4Attr(ui.ATT2Read,'li/ct/plc1/ATT2_P_setpoint')
#        self._setupTaurusLabel4Attr(ui.PHS1Read,'li/ct/plc1/PHS1_Phase_setpoint')
#        self._setupTaurusLabel4Attr(ui.PHS2Read,'li/ct/plc1/PHS2_Phase_setpoint')
#        #---- TODO: connect the ToApplyTitle to check/uncheck all the *Check
#    
#    def timingConfiguration(self,ui):
#        self._setupLed4Attr(ui.MBMRead,'LI/CT/PLC1/TB_MBM')
#        self._setupTaurusLabel4Attr(ui.GunDelayRead,'li/ct/plc1/TB_GUN_delay')
#        self._setupTaurusLabel4Attr(ui.ka1DelayRead,'li/ct/plc1/TB_ka1_delay')
#        self._setupTaurusLabel4Attr(ui.ka2DelayRead,'li/ct/plc1/TB_ka2_delay')
#        self._setupTaurusLabel4Attr(ui.GPIRead,'li/ct/plc1/TB_GPI')
#        self._setupTaurusLabel4Attr(ui.GPNRead,'li/ct/plc1/TB_GPN')
#        self._setupTaurusLabel4Attr(ui.GPARead,'li/ct/plc1/TB_GPA')
#        #---- TODO: connect the ToApplyTitle to check/uncheck all the *Check
#    
#    def klystronsConfiguration(self,ui):
#        klystrons = {1:{'setp':ui.ka1HVPSRead},
#                     2:{'setp':ui.ka2HVPSRead}}
#        for number in klystrons.keys():
#            for element in klystrons[number].keys():
#                widget = klystrons[number][element]
#                devName = 'li/ct/plc%d'%(number+3)
#                if element == 'setp':
#                    self._setupTaurusLabel4Attr(widget,"%s/HVPS_V_setpoint"%(devName))
#                
#        #---- TODO: connect the ToApplyTitle to check/uncheck all the *Check
#    
#    def buttonsConfiguration(self,buttons):
#        buttons.button(QtGui.QDialogButtonBox.Reset).setDisabled(True)#.clicked.connect(self.reset)
#        buttons.button(QtGui.QDialogButtonBox.Save).setDisabled(True)#.clicked.connect(self.save)
#        buttons.button(QtGui.QDialogButtonBox.Open).setDisabled(True)#.clicked.connect(self.open)
#        buttons.button(QtGui.QDialogButtonBox.Apply).setDisabled(True)#.clicked.connect(self.apply)
#    
#    #---- TODO: should the *Reading widgets be connected to the *Value?
#    #           Doing this, the operation of the other tabs will be shown in 
#    #           this Configuration tab according to when it's happening.
#    
#    def reset(self):
#        '''With this call (from a button or at the loading step) we must travel
#           all the *Reading widgets and copy the value to the *Value widget.
#        '''
#        print "Reset()"
#        
#        
#        
#    def save(self):
#        '''Travelling along the *Check widgets, the checked ones (name and 
#           value) will be written in a file indicated by the user.
#        '''
#        print "Save()"
#    def open(self):
#        '''Given a file of settings provided by the user, show those values in 
#           the *Value widgets.
#           Mark (TODO: how?) the changes from the previous value 
#           in the *Value widget
#        '''
#        print "Open()"
#    def apply(self):
#        '''Travelling along the *Check, apply the value in *Value 
#           to the model in the *Reading.
#        '''
#        print "Apply()"

    #---- Configure the access to external applications
    def setExternalApplications(self):
#        bcm = ExternalAppAction(['taurusform',
#                                 '{li,lt01,lt02}/di/bcm-01/Charge',
#                                 '--window-name=BCM'],
#                                text="BCM")
#        self.addExternalAppLauncher(bcm)
        lt_magnets = ExternalAppAction(['ctpcgrid','lt'],text="LT magnets")
        self.addExternalAppLauncher(lt_magnets)
        mach_ccds = ExternalAppAction(['ctdiccd'],text="CCDs")
        self.addExternalAppLauncher(mach_ccds)

'''First approach to the Labview blinking leds with subboxes of sets of attrs.
'''
class CheckboxManager(TaurusBaseComponent,Qt.QObject):
    #TODO: instead of checkboxes them should be leds with a composition of the
    #      internal values in the subbox
    def __init__(self,checker,widget,name=None,qt_parent=None,designMode=False):
        if not name: name = "CheckboxManager"
        self.call__init__wo_kw(Qt.QObject, qt_parent)
        self.call__init__(TaurusBaseComponent, name, designMode=designMode)
        self._checker = checker
        self._widget = widget
        Qt.QObject.connect(self._checker,Qt.SIGNAL('clicked(bool)'),self._checkboxChanged)
        self.debug("Build the checkbox manager")

    def _checkboxChanged(self,checked):
        if self._checker.isChecked():
            self._widget.show()
        else:
            self._widget.hide()

class OperationModeManager(TaurusBaseComponent,Qt.QObject):
    def __init__(self,mainscreen_ui,name=None,qt_parent=None,designMode=False):
        if not name: name = "OperationModeManager"
        self.call__init__wo_kw(Qt.QObject, qt_parent)
        self.call__init__(TaurusBaseComponent, name, designMode=designMode)
        self._checker = mainscreen_ui.tbMultiBunchCheck
        self._mainscreen_ui = mainscreen_ui
        Qt.QObject.connect(self._checker,Qt.SIGNAL('stateChanged(int)'),self._operationModeChanges)
    def _operationModeChanges(self,mode):
        if self._checker.isChecked():
            self._mainscreen_ui.tbWidthLabel.setText('Width')
            self._mainscreen_ui.tbNumberLabel.setEnabled(False)
            self._mainscreen_ui.tbNumberValue.setEnabled(False)
        else:
            self._mainscreen_ui.tbWidthLabel.setText('Interval')
            self._mainscreen_ui.tbNumberLabel.setEnabled(True)
            self._mainscreen_ui.tbNumberValue.setEnabled(True)

#---- This is a copy from fsotrGUI
from PyQt4 import QtCore
import traceback
import getpass,socket

class ViewButtonListener:
    def __init__(self,button,screen):
        self.__button = button
        self.__screen = str(screen)
        QtCore.QObject.connect(self.__button,QtCore.SIGNAL("clicked()"),self.launchGui)
        #print "build button listener for %s"%self.__screen
        self.__qpro = None
    def launchGui(self):
        try:
            print "Listener button clicked for %s"%self.__screen
            if not self.__qpro == None and self.__qpro.state() == QtCore.QProcess.Running:
                answer = QtGui.QMessageBox.warning(None,"Gui already running",
                                                   "This screen is already open.\n"
                                                   "Are you sure to kill it?",
                                                   Qt.QString("Kill"),#button0Text
                                                   Qt.QString("Cancel"),#button1Text
                                                   "",#used button2
                                                   1)#defaultButtonNumber
                if answer == 0:
                    self.__qpro.kill()
                return
            self.__qpro = QtCore.QProcess()
            self.__qpro.setProcessChannelMode(QtCore.QProcess.ForwardedChannels)
            QtCore.QObject.connect(self.__qpro,QtCore.SIGNAL("error()"),self.__FsotrGUI_error)
            QtCore.QObject.connect(self.__qpro,QtCore.SIGNAL("finished(int)"),self.__FsotrGUI_finished)
            fsotr = "--screen=%s"%(self.__screen)
            ccd = "--ccd=%s-ccd"%(self.__screen)
            iba = "--iba=%s-iba"%(self.__screen)
            cmd = "ctdiccd %s %s %s"%(fsotr,iba,ccd)
            cmd += " --from=%s@%s"%(getpass.getuser(),socket.gethostname())
            print("[ButtonsListener] %s.launchGui cmd: %s"%(self.__screen,cmd))
            self.__qpro.start(Qt.QString(cmd))
            
        except Exception,e:
            print "[ButtonsListener] %s.launchGui exception: %s"%(self.__screen,e)
            traceback.print_exc()
    def __FsotrGUI_started(self):
        print "[ButtonsListener] %s.__FsotrGUI_started"%self.__screen
    def __FsotrGUI_error(self):
        print "[ButtonsListener] %s.__error: %s"%(self.__screen,str(self.__qpro.exitCode()))
        
    def __FsotrGUI_finished(self,exitStatus):
        print "[ButtonsListener] %s.__finished() exit Code: %d"%(self.__screen,exitStatus)

    def printer(self,type,output):
        for line in output:
            print("%s %s\t%s"%(self.__screen,type,line))

def main():
    parser = argparse.get_taurus_parser()
    app = TaurusApplication(sys.argv, cmd_line_parser=parser,
                      app_name='cttifilling', app_version='0.1',
                      org_domain='ALBA', org_name='ALBA')
    options = app.get_command_line_options()
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
