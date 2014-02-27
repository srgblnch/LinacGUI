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
from taurus.qt import Qt

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

    def _setupCheckbox4Attr(self,widget,attrName):
        widget.setModel(attrName)
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
    #---- Done auxiliar methods to configure widgets
    ######

    def setCommunications(self):
        #about the overview
        self.ui.linacOverview._ui.gunLowVoltageRead.setModel('li/ct/plc1/GUN_LV_ONC')
        self.ui.linacOverview._ui.gunLowVoltageWrite.setModel('li/ct/plc1/GUN_LV_ONC')
        self.ui.linacOverview._ui.HVPSRead.setModel('li/ct/plc1/GUN_HV_ONC')
        self.ui.linacOverview._ui.HVPSWrite.setModel('li/ct/plc1/GUN_HV_ONC')
        self.ui.linacOverview._ui.RFRead.setModel('li/ct/plc1/RF_OK')
        self.ui.linacOverview._ui.VCRead.setModel('li/ct/plc2/VC_OK')
        self.ui.linacOverview._ui.ACRead.setModel('li/ct/plc2/AC_IS')
        self.ui.linacOverview._ui.klystron1Read.setModel('li/ct/plc1/KA1_OK')
        self.ui.linacOverview._ui.klystron2Read.setModel('li/ct/plc1/KA2_OK')
        self.ui.linacOverview._ui.linacRead.setModel('li/ct/plc1/LI_OK')
        self.ui.linacOverview._ui.moveLocal.setModel(DeviceRelocator)
        self.ui.linacOverview._ui.moveLocal.setCommand('MoveAllInstances')
        self.ui.linacOverview._ui.moveLocal.setParameters('local')
        self.ui.linacOverview._ui.moveLocal.setCustomText('Local')
        self.ui.linacOverview._ui.moveLocal.setDangerMessage(\
                                   "Be sure Labview is not link to these PLCs!")
        self.ui.linacOverview._ui.moveRemote.setModel(DeviceRelocator)
        self.ui.linacOverview._ui.moveRemote.setCommand('MoveAllInstances')
        self.ui.linacOverview._ui.moveRemote.setParameters('remote')
        self.ui.linacOverview._ui.moveRemote.setCustomText('Remote')
        self.ui.linacOverview._ui.moveRemote.setDangerMessage(\
                                "After this action you will lose write access.")
        self.ui.linacOverview._ui.resetInstance.setModel(DeviceRelocator)
        self.ui.linacOverview._ui.resetInstance.setCommand('RestartAllInstance')
        self.ui.linacOverview._ui.resetInstance.setCustomText('Restart all')
        self.ui.linacOverview._ui.resetInstance.setDangerMessage(\
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
        self._setupLed4Attr(startup_ui.klystronAmplifierEnabledLed,'li/ct/plc1/KA_ENB')         #KA_ENB
        self._setupLed4Attr(startup_ui.magnetInterlockStateLed,'li/ct/plc1/MG_IS')              #MI_IS
        self._setupLed4Attr(startup_ui.interlockUnitResetLed,'li/ct/plc1/interlock_rc',offColor='black')
        self._setupCheckbox4Attr(startup_ui.interlockUnitResetCheck,'li/ct/plc1/interlock_rc')  #Rst
        self._setupLed4Attr(startup_ui.utilitiesInterlockStateLed,'li/ct/plc1/UT_IS')           #UI_IS
        self._setupLed4Attr(startup_ui.compressedAirStateLed,'li/ct/plc2/ac_is')                #AC_IS
        self._setupLed4Attr(startup_ui.transferlineVacuumStateLed,'li/ct/plc1/TL_VOK')          #TL_VOK
        self._setupLed4Attr(startup_ui.linacVacuumStateLed,'li/ct/plc2/vc_ok')                  #LI_VOK
        self._setupLed4Attr(startup_ui.electronGunEnabledLed,'li/ct/plc1/EG_ENB')               #EG_ENB
        self._setupLed4Attr(startup_ui.gmdiLed,'li/ct/plc1/GM_DI')                              #GM_DI FIXME!!! This was not well documented in the Labview
        self._setupLed4Attr(startup_ui.interlockUnitReadyStateLed,'li/ct/plc1/UI_RDY')          #UI
        self._setupLed4Attr(startup_ui.klystron2AmplifierEnabledLed,'li/ct/plc1/ka2_ok')        #KA2_EN
        self._setupLed4Attr(startup_ui.klystron1AmplifierEnabledLed,'li/ct/plc1/ka1_ok')        #KA1_EN
        self._setupLed4Attr(startup_ui.linacVacuumStateLed_2,'li/ct/plc2/vc_ok')                #LI_VOK (repeated on the right side of the IU)
        self._setupLed4Attr(startup_ui.linacReadyStateLed,'li/ct/plc1/li_ok')                   #LI_RDY
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
                        'on':[startup_ui.klystron1OnLed,startup_ui.klystron1OnCheck],
                        'rst':[startup_ui.klystron1RstLed,startup_ui.klystron1RstCheck],
                        'check':startup_ui.klystron1LVPopupCheck,
                        'widget':startup_ui.klystron1LVWidget},
                     2:{'plc':5,
                        'on':[startup_ui.klystron2OnLed,startup_ui.klystron2OnCheck],
                        'rst':[startup_ui.klystron2RstLed,startup_ui.klystron2RstCheck],
                        'check':startup_ui.klystron2LVPopupCheck,
                        'widget':startup_ui.klystron2LVWidget}}
        self._klystronLV = {}
        for number in klystrons.keys():
            for widget in klystrons[number]['on']:
                widget.setModel('li/ct/plc%d/LV_ONC'%(klystrons[number]['plc']))
            for widget in klystrons[number]['rst']:
                widget.setModel('li/ct/plc%d/LV_Interlock_RC'%(klystrons[number]['plc']))
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
        #command arrow to the KD box
        self._setupLed4Attr(startup_ui.egunonLed,'li/ct/plc1/GUN_LV_ONC')
        self._setupCheckbox4Attr(startup_ui.egunonCheck,'li/ct/plc1/GUN_LV_ONC')
        #information shown in the KD box
        #startup_ui.kdeGunLVPopupCheck.setCheckState(False)
        startup_ui.kdeGunLVWidget.hide()
        self._egunManager = CheckboxManager(startup_ui.kdeGunLVPopupCheck,
                                            startup_ui.kdeGunLVWidget,
                                            "EGunPopup")
        self._setupSpinBox4Attr(startup_ui.filamentSetpoint,'li/ct/plc1/GUN_Filament_V_setpoint',step=0.1)
        self._setupSpinBox4Attr(startup_ui.cathodeSetpoint,'li/ct/plc1/GUN_Kathode_V_setpoint',step=0.1)
        self._setupTaurusLabel4Attr(startup_ui.filamentCurrent,'li/ct/plc1/GUN_Filament_I','A')
        self._setupTaurusLabel4Attr(startup_ui.temperatureValue,'li/ct/plc1/GUN_Kathode_T','C')
        #setmodel for the contents in the popup
        popupWidget = startup_ui.kdeGunLVWidget._ui
        self._setupTaurusLabel4Attr(popupWidget.eGunStatus,'li/ct/plc1/Gun_Status')
        self._setupTaurusLabel4Attr(popupWidget.filamentValue,'li/ct/plc1/GUN_Filament_V','V')
        self._setupTaurusLabel4Attr(popupWidget.cathodeValue,'li/ct/plc1/GUN_Kathode_V','V')

    def _setStartup_cooling(self):
        startup_ui = self.ui.linacStartupSynoptic._ui
        coolingLoops = {1:{'cmdCheck':startup_ui.coolingLoop1OnCheck,
                           'cmdLed':startup_ui.coolingLoop1OnLed,
                           'cmd_attrName':'li/ct/plc2/CL1_ONC',
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
                        2:{'cmdCheck':startup_ui.coolingLoop2OnCheck,
                           'cmdLed':startup_ui.coolingLoop2OnLed,
                           'cmd_attrName':'li/ct/plc2/CL2_ONC',
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
                        3:{'cmdCheck':startup_ui.coolingLoop3OnCheck,
                           'cmdLed':startup_ui.coolingLoop3OnLed,
                           'cmd_attrName':'li/ct/plc2/CL3_ONC',
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
            #command area
            self._setupCheckbox4Attr(coolingLoops[number]['cmdCheck'],coolingLoops[number]['cmd_attrName'])
            self._setupLed4Attr(coolingLoops[number]['cmdLed'],coolingLoops[number]['cmd_attrName'])
            #information area
            self._setupSpinBox4Attr(coolingLoops[number]['Temperature'],
                                    coolingLoops[number]['Temperature_attrName']+'_setpoint',
                                    step=0.1)
            #coolingLoops[number]['check'].setCheckState(False)
            coolingLoops[number]['widget'].hide()
            self._coolingLoopManagers[number] = CheckboxManager(coolingLoops[number]['check'],
                                                                coolingLoops[number]['widget'],
                                                                "CollingLoopPopup%d"%number)
            popupWidget = coolingLoops[number]['widget']._ui
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
        self._setupLed4UnknownAttr(startup_ui.sl1Led)
        self._setupLed4UnknownAttr(startup_ui.sl2Led)
        self._setupLed4UnknownAttr(startup_ui.sl3Led)
        self._setupLed4UnknownAttr(startup_ui.sl4Led)
        self._setupLed4UnknownAttr(startup_ui.bc1Led)
        self._setupLed4UnknownAttr(startup_ui.bc2Led)
        self._setupLed4UnknownAttr(startup_ui.glLed)
        self._setupLed4UnknownAttr(startup_ui.as1Led)
        self._setupLed4UnknownAttr(startup_ui.qtLed)
        self._setupLed4UnknownAttr(startup_ui.as2Led)

    def _setStartup_vacuum(self):
        startup_ui = self.ui.linacStartupSynoptic._ui
        vacuumValves = {1:{'cmdCheck':startup_ui.vacuumValve1OnCheck,
                           'cmdLed':startup_ui.vacuumValve1OnLed,
                           'infoLed':startup_ui.vacuumValve1OnLedInfo,
                           'cmd_attrName':'li/ct/plc2/VV1_OC',
                           'status':startup_ui.vacuumValve1OnStatus,
                           'status_attrName':'li/ct/plc2/VV1_Status'},
                        2:{'cmdCheck':startup_ui.vacuumValve2OnCheck,
                           'cmdLed':startup_ui.vacuumValve2OnLed,
                           'infoLed':startup_ui.vacuumValve2OnLedInfo,
                           'cmd_attrName':'li/ct/plc2/VV2_OC',
                           'status':startup_ui.vacuumValve2OnStatus,
                           'status_attrName':'li/ct/plc2/VV2_Status'},
                        3:{'cmdCheck':startup_ui.vacuumValve3OnCheck,
                           'cmdLed':startup_ui.vacuumValve3OnLed,
                           'infoLed':startup_ui.vacuumValve3OnLedInfo,
                           'cmd_attrName':'li/ct/plc2/VV3_OC',
                           'status':startup_ui.vacuumValve3OnStatus,
                           'status_attrName':'li/ct/plc2/VV3_Status'},
                        4:{'cmdCheck':startup_ui.vacuumValve4OnCheck,
                           'cmdLed':startup_ui.vacuumValve4OnLed,
                           'infoLed':startup_ui.vacuumValve4OnLedInfo,
                           'cmd_attrName':'li/ct/plc2/VV4_OC',
                           'status':startup_ui.vacuumValve4OnStatus,
                           'status_attrName':'li/ct/plc2/VV4_Status'},
                        5:{'cmdCheck':startup_ui.vacuumValve5OnCheck,
                           'cmdLed':startup_ui.vacuumValve5OnLed,
                           'infoLed':startup_ui.vacuumValve5OnLedInfo,
                           'cmd_attrName':'li/ct/plc2/VV5_OC',
                           'status':startup_ui.vacuumValve5OnStatus,
                           'status_attrName':'li/ct/plc2/VV5_Status'},
                        6:{'cmdCheck':startup_ui.vacuumValve6OnCheck,
                           'cmdLed':startup_ui.vacuumValve6OnLed,
                           'infoLed':startup_ui.vacuumValve6OnLedInfo,
                           'cmd_attrName':'li/ct/plc2/VV6_OC',
                           'status':startup_ui.vacuumValve6OnStatus,
                           'status_attrName':'li/ct/plc2/VV6_Status'},
                        7:{'cmdCheck':startup_ui.vacuumValve7OnCheck,
                           'cmdLed':startup_ui.vacuumValve7OnLed,
                           'infoLed':startup_ui.vacuumValve7OnLedInfo,
                           'cmd_attrName':'li/ct/plc2/VV7_OC',
                           'status':startup_ui.vacuumValve7OnStatus,
                           'status_attrName':'li/ct/plc2/VV7_Status'},
                       }
        #TODO: there is an OPEN all valves not implemented in the device
        # startup_ui.vv_onc{Led,Check}
        self._setupLed4UnknownAttr(startup_ui.vv_oncLed)
        self._setupCheckbox4UnknownAttr(startup_ui.vv_oncCheck)
        #reset vacuum interlocks
        self._setupLed4Attr(startup_ui.vv_rstLed,'li/ct/plc2/VC_Interlock_RC',offColor='black')
        self._setupCheckbox4Attr(startup_ui.vv_rstCheck,'li/ct/plc2/VC_Interlock_RC')
        for number in vacuumValves.keys():
            self._setupLed4Attr(vacuumValves[number]['infoLed'],
                                vacuumValves[number]['cmd_attrName'])
            self._setupLed4Attr(vacuumValves[number]['cmdLed'],
                                vacuumValves[number]['cmd_attrName'])
            self._setupCheckbox4Attr(vacuumValves[number]['cmdCheck'],
                                     vacuumValves[number]['cmd_attrName'])
            self._setupTaurusLabel4Attr(vacuumValves[number]['status'],
                                        vacuumValves[number]['status_attrName'])

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
        self._setupTaurusLabel4Attr(startup_ui.hvg1Value,'li/ct/plc2/HVG1_P','bar')
        startup_ui.hvg2Led.setModel('li/ct/plc2/HVG2_IS')
        self._setupTaurusLabel4Attr(startup_ui.hvg2Value,'li/ct/plc2/HVG2_P','bar')
        startup_ui.hvg3Led.setModel('li/ct/plc2/HVG3_IS')
        self._setupTaurusLabel4Attr(startup_ui.hvg3Value,'li/ct/plc2/HVG3_P','bar')
        startup_ui.hvg4Led.setModel('li/ct/plc2/HVG4_IS')
        self._setupTaurusLabel4Attr(startup_ui.hvg4Value,'li/ct/plc2/HVG4_P','bar')
        startup_ui.hvg5Led.setModel('li/ct/plc2/HVG5_IS')
        self._setupTaurusLabel4Attr(startup_ui.hvg5Value,'li/ct/plc2/HVG5_P','bar')
        self._setupTaurusLabel4Attr(startup_ui.ipc1Value1,'li/ct/plc2/IP1_P','bar')
        self._setupTaurusLabel4Attr(startup_ui.ipc1Value2,'li/ct/plc2/IP2_P','bar')
        self._setupTaurusLabel4Attr(startup_ui.ipc2Value1,'li/ct/plc2/IP3_P','bar')
        self._setupTaurusLabel4Attr(startup_ui.ipc2Value2,'li/ct/plc2/IP4_P','bar')
        self._setupTaurusLabel4Attr(startup_ui.ipc3Value1,'li/ct/plc2/IP5_P','bar')
        self._setupTaurusLabel4Attr(startup_ui.ipc3Value2,'li/ct/plc2/IP6_P','bar')
        self._setupTaurusLabel4Attr(startup_ui.ipc4Value1,'li/ct/plc2/IP7_P','bar')
        self._setupTaurusLabel4Attr(startup_ui.ipc4Value2,'li/ct/plc2/IP8_P','bar')
        self._setupTaurusLabel4Attr(startup_ui.ipc5Value1,'li/ct/plc2/IP9_P','bar')

    def setMainscreen(self):
        #following the synoptic regions from left to right and from top to bottom
        self._setMainscreen_tb()
        self._setMainscreen_klystronHV()
        self._setMainscreen_rf()
        self._setMainscreen_cl()
        self._setMainscreen_kd()
        self._setMainscreen_magnets()
        self._setMainscreen_hvs()
        self._setMainscreen_vacuum()
        self._setMainscreen_fs()
        startup_ui = self.ui.linacMainscreenSynoptic._ui
        startup_ui.MainScreenSchematic.lower()
        
    def _setMainscreen_tb(self):
        mainscreen_ui = self.ui.linacMainscreenSynoptic._ui
        self._setupTaurusLabel4Attr(mainscreen_ui.tbKaDelay1Value,'li/ct/plc1/TB_KA1_Delay',unit='us')
        self._setupTaurusLabel4Attr(mainscreen_ui.tbKaDelay2Value,'li/ct/plc1/TB_KA2_Delay',unit='ns')
        self._setupTaurusLabel4Attr(mainscreen_ui.tbRf2DelayValue,'li/ct/plc1/TB_RF2_Delay',unit='ns')
        self._setupSpinBox4Attr(mainscreen_ui.tbGunLevelValue,'li/ct/plc1/TB_GPA',step=0.1)
        self._setupTaurusLabel4Attr(mainscreen_ui.tbMultiBunchValue, 'li/ct/plc1/TB_MBM_status')
        self._setupCheckbox4Attr(mainscreen_ui.tbMultiBunchCheck, 'li/ct/plc1/TB_MBM')
        self._operationModeMonitor = OperationModeManager(mainscreen_ui)
        #---- FIXME: the addValueNames fails in some versions of taurus,
        #            but it works in the control's room version
        try:
            self._setupCombobox4Attr(mainscreen_ui.tbGatedPulseModeCombo,'li/ct/plc1/TB_GPM',
                                     [('off',0),('mix',1),('on',2)])
        except:
            mainscreen_ui.tbGatedPulseModeValue.setEnabled(False)
        self._setupSpinBox4Attr(mainscreen_ui.tbGunDelayValue,'li/ct/plc1/TB_Gun_Delay',step=32)
        self._setupSpinBox4Attr(mainscreen_ui.tbWidthValue,'li/ct/plc1/TB_GPI',step=2)
        self._setupSpinBox4Attr(mainscreen_ui.tbNumberValue,'li/ct/plc1/TB_GPN',step=1)
        self._setupLed4Attr(mainscreen_ui.tbTimerStatusStateLed,'li/ct/plc1/TB_ST')
        self._setupLed4Attr(mainscreen_ui.rfEnbLed,'li/ct/plc1/RF_OK')
    
    def _setMainscreen_klystronHV(self):
        mainscreen_ui = self.ui.linacMainscreenSynoptic._ui
        klystrons = {1:{'setpoint':mainscreen_ui.klystron1HVValue,
                        'setpoint_attrName':'li/ct/plc4/HVPS_V_setpoint',
                        'rstCheck':mainscreen_ui.klystron1RstCheck,
                        'rstLed':mainscreen_ui.klystron1RstLed,
                        'rst_attrName':'li/ct/plc4/HVPS_Interlock_RC',
                        'onCheck':mainscreen_ui.klystron1OnCheck,
                        'onLed':mainscreen_ui.klystron1OnLed,
                        'on_attrName':'li/ct/plc4/HVPS_ONC',
                        'check':mainscreen_ui.klystron1HVPopupCheck,
                        'widget':mainscreen_ui.klystron1HVPopupWidget},
                     2:{'setpoint':mainscreen_ui.klystron2HVValue,
                        'setpoint_attrName':'li/ct/plc5/HVPS_V_setpoint',
                        'rstCheck':mainscreen_ui.klystron2RstCheck,
                        'rstLed':mainscreen_ui.klystron2RstLed,
                        'rst_attrName':'li/ct/plc5/HVPS_Interlock_RC',
                        'onCheck':mainscreen_ui.klystron2OnCheck,
                        'onLed':mainscreen_ui.klystron2OnLed,
                        'on_attrName':'li/ct/plc5/HVPS_ONC',
                        'check':mainscreen_ui.klystron2HVPopupCheck,
                        'widget':mainscreen_ui.klystron2HVPopupWidget}
                    }
        self._klystronHV = {}
        for number in klystrons.keys():
            self._setupSpinBox4Attr(klystrons[number]['setpoint'],
                                    klystrons[number]['setpoint_attrName'],step=0.1)
            self._setupCheckbox4Attr(klystrons[number]['rstCheck'],
                                     klystrons[number]['rst_attrName'])
            self._setupLed4Attr(klystrons[number]['rstLed'],
                                klystrons[number]['rst_attrName'],pattern='')
            self._setupCheckbox4Attr(klystrons[number]['onCheck'],
                                     klystrons[number]['on_attrName'])
            self._setupLed4Attr(klystrons[number]['onLed'],
                                klystrons[number]['on_attrName'],pattern='')
            #prepare the checkmanager
            #klystrons[number]['check'].setCheckState(False)
            klystrons[number]['widget'].hide()
            self._klystronHV[number] = CheckboxManager(klystrons[number]['check'],
                                                       klystrons[number]['widget'],
                                                       "Klystron%dHVManager"%number)
            widget = klystrons[number]['widget']._ui
            self._setupTaurusLabel4Attr(widget.hvStatusValue,'li/ct/plc%d/HVPS_Status'%(number+3))
            self._setupTaurusLabel4Attr(widget.hvVoltageValue,'li/ct/plc%d/HVPS_V'%(number+3),'kV')
            self._setupTaurusLabel4Attr(widget.hvCurrentValue,'li/ct/plc%d/HVPS_I'%(number+3),'mA')
            self._setupTaurusLabel4Attr(widget.pulseStatusValue,'li/ct/plc%d/Pulse_Status'%(number+3))
            self._setupTaurusLabel4Attr(widget.klystronVoltageValue,'li/ct/plc%d/Peak_V'%(number+3),'kV')
            self._setupTaurusLabel4Attr(widget.klystronCurrentValue,'li/ct/plc%d/Peak_I'%(number+3),'A')

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
        self._setupSpinBox4Attr(mainscreen_ui.rfA0OutputPowerValue,'li/ct/plc1/A0_OP',step=0.1)
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
            self._setupSpinBox4Attr(phaseShifters[shifter]['write'],attrName,step=0.1)
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
        magnets = {'sl1':{'state':mainscreen_ui.sl1Led,
                          'info':mainscreen_ui.sl1LedInfo,
                          'h':mainscreen_ui.sl1hValue,
                          'v':mainscreen_ui.sl1vValue,
                          'f':mainscreen_ui.sl1fValue,
                          'cmd':mainscreen_ui.sl1OnCheck,
                          'check':mainscreen_ui.sl1PopupCheck,
                          'widget':mainscreen_ui.sl1PopupWidget},
                   'sl2':{'state':mainscreen_ui.sl2Led,
                          'info':mainscreen_ui.sl2LedInfo,
                          'h':mainscreen_ui.sl2hValue,
                          'v':mainscreen_ui.sl2vValue,
                          'f':mainscreen_ui.sl2fValue,
                          'cmd':mainscreen_ui.sl2OnCheck,
                          'check':mainscreen_ui.sl2PopupCheck,
                          'widget':mainscreen_ui.sl2PopupWidget},
                   'sl3':{'state':mainscreen_ui.sl3Led,
                          'info':mainscreen_ui.sl3LedInfo,
                          'h':mainscreen_ui.sl3hValue,
                          'v':mainscreen_ui.sl3vValue,
                          'f':mainscreen_ui.sl3fValue,
                          'cmd':mainscreen_ui.sl3OnCheck,
                          'check':mainscreen_ui.sl3PopupCheck,
                          'widget':mainscreen_ui.sl3PopupWidget},
                   'sl4':{'state':mainscreen_ui.sl4Led,
                          'info':mainscreen_ui.sl4LedInfo,
                          'h':mainscreen_ui.sl4hValue,
                          'v':mainscreen_ui.sl4vValue,
                          'f':mainscreen_ui.sl4fValue,
                          'cmd':mainscreen_ui.sl4OnCheck,
                          'check':mainscreen_ui.sl4PopupCheck,
                          'widget':mainscreen_ui.sl4PopupWidget},
                   'bc1':{'state':mainscreen_ui.bc1Led,
                          'info':mainscreen_ui.bc1LedInfo,
                          'h':mainscreen_ui.bc1hValue,
                          'v':mainscreen_ui.bc1vValue,
                          'f':mainscreen_ui.bc1fValue,
                          'cmd':mainscreen_ui.bc1OnCheck,
                          'check':mainscreen_ui.bc1PopupCheck,
                          'widget':mainscreen_ui.bc1PopupWidget},
                   'bc2':{'state':mainscreen_ui.bc2Led,
                          'info':mainscreen_ui.bc2LedInfo,
                          'h':mainscreen_ui.bc2hValue,
                          'v':mainscreen_ui.bc2vValue,
                          'f':mainscreen_ui.bc2fValue,
                          'cmd':mainscreen_ui.bc2OnCheck,
                          'check':mainscreen_ui.bc2PopupCheck,
                          'widget':mainscreen_ui.bc2PopupWidget},
                   'gl': {'state':mainscreen_ui.glLed,
                          'info':mainscreen_ui.glLedInfo,
                          'h':mainscreen_ui.glhValue,
                          'v':mainscreen_ui.glvValue,
                          'f':mainscreen_ui.glfValue,
                          'cmd':mainscreen_ui.glOnCheck,
                          'check':mainscreen_ui.glPopupCheck,
                          'widget':mainscreen_ui.glPopupWidget},
                   'as1':{'state':mainscreen_ui.as1Led,
                          'info':mainscreen_ui.as1LedInfo,
                          'h':mainscreen_ui.as1hValue,
                          'v':mainscreen_ui.as1vValue,
                          'cmd':mainscreen_ui.as1OnCheck,
                          'check':mainscreen_ui.as1PopupCheck,
                          'widget':mainscreen_ui.as1PopupWidget},
                   'qt' :{'state':mainscreen_ui.qtLed,
                          'info':mainscreen_ui.qtLedInfo,
                          'cmd':mainscreen_ui.qt1OnCheck},
                   'qt1':{'h':mainscreen_ui.qt1hValue,
                          'v':mainscreen_ui.qt1vValue,
                          'f':mainscreen_ui.qt1fValue,
                          'check':mainscreen_ui.qt1PopupCheck,
                          'widget':mainscreen_ui.qt1PopupWidget},
                   'qt2':{'f':mainscreen_ui.qt2fValue,
                          'check':mainscreen_ui.qt2PopupCheck,
                          'widget':mainscreen_ui.qt2PopupWidget},
                   'as2':{'state':mainscreen_ui.as2Led,
                          'info':mainscreen_ui.as2LedInfo,
                          'h':mainscreen_ui.as2hValue,
                          'v':mainscreen_ui.as2vValue,
                          'cmd':mainscreen_ui.as2OnCheck,
                          'check':mainscreen_ui.as2PopupCheck,
                          'widget':mainscreen_ui.as2PopupWidget},
                   }
        self._magnets = {}
        for magnet in magnets.keys():
            deviceName = 'li/ct/plc3'
            if magnets[magnet].has_key('state'):
                attrName = '%s/%s_onc'%(deviceName,magnet)
                self._setupLed4Attr(magnets[magnet]['state'],attrName)
            if magnets[magnet].has_key('info'):
                attrName = '%s/%s_onc'%(deviceName,magnet)
                self._setupLed4Attr(magnets[magnet]['info'],attrName)
            if magnets[magnet].has_key('h'):
                attrName = '%s/%sh_I_setpoint'%(deviceName,magnet)
                self._setupSpinBox4Attr(magnets[magnet]['h'],attrName,step=0.01)
            if magnets[magnet].has_key('v'):
                attrName = '%s/%sv_I_setpoint'%(deviceName,magnet)
                self._setupSpinBox4Attr(magnets[magnet]['v'],attrName,step=0.01)
            if magnets[magnet].has_key('f'):
                attrName = '%s/%sf_I_setpoint'%(deviceName,magnet)
                #Special exception:
                if magnet in ['qt1','qt2']:
                    self._setupSpinBox4Attr(magnets[magnet]['f'],attrName,step=0.005)
                else:
                    self._setupSpinBox4Attr(magnets[magnet]['f'],attrName,step=0.01)
            if magnets[magnet].has_key('cmd'):
                attrName = '%s/%s_onc'%(deviceName,magnet)
                self._setupCheckbox4Attr(magnets[magnet]['cmd'],attrName)
            if magnets[magnet].has_key('check') and magnets[magnet].has_key('widget'):
                #magnets[magnet]['check'].setCheckState(False)
                magnets[magnet]['widget'].hide()
                self._magnets[magnet] = CheckboxManager(magnets[magnet]['check'],
                                                        magnets[magnet]['widget'],
                                                        "%s"%magnet)
                widget = magnets[magnet]['widget']._ui
                widget.magnetGroup.setTitle(magnet)
                #x,y,width,height = widget.x(),widget.y(),widget.width(),widget.height()
                #final_height = 25
                if magnets[magnet].has_key('h'):
                    self._setupTaurusLabel4Attr(widget.horizontalValue,'%s/%sh_I'%(deviceName,magnet),'A')
                    self._setupTaurusLabel4Attr(widget.horizontalStatus,'%s/%sh_Status'%(deviceName,magnet))
                    #final_height+=25
                else:
                    widget.horizontalLabel.hide()
                    widget.horizontalValue.hide()
                    widget.horizontalStatus.hide()
                if magnets[magnet].has_key('v'):
                    self._setupTaurusLabel4Attr(widget.verticalValue,'%s/%sv_I'%(deviceName,magnet),'A')
                    self._setupTaurusLabel4Attr(widget.verticalStatus,'%s/%sv_Status'%(deviceName,magnet))
                    #final_height+=25
                else:
                    widget.verticalLabel.hide()
                    widget.verticalValue.hide()
                    widget.verticalStatus.hide()
                if magnets[magnet].has_key('f'):
                    self._setupTaurusLabel4Attr(widget.focusValue,'%s/%sf_I'%(deviceName,magnet),'A')
                    self._setupTaurusLabel4Attr(widget.focusStatus,'%s/%sf_Status'%(deviceName,magnet))
                    #final_height+=25
                else:
                    widget.focusLabel.hide()
                    widget.focusValue.hide()
                    widget.focusStatus.hide()
                #wiget.setGeometry(Qt.QtCore.QRect(x,y,width,final_height))
        self._setupLed4Attr(mainscreen_ui.magnetsRstLed,'li/ct/plc3/MA_Interlock_RC',offColor='black')
        self._setupCheckbox4Attr(mainscreen_ui.magnetsRstCheck,
                                 'li/ct/plc3/MA_Interlock_RC')
        #FIXME: there is no attr to power on all magnets at once
        self._setupLed4UnknownAttr(mainscreen_ui.magnetsOnLed)
        self._setupCheckbox4UnknownAttr(mainscreen_ui.magnetsOnCheck)
        
    def _setMainscreen_hvs(self):
        mainscreen_ui = self.ui.linacMainscreenSynoptic._ui
        self._setupSpinBox4Attr(mainscreen_ui.hvsVoltageValue,'li/ct/plc1/GUN_HV_V_setpoint',step=0.1)
        self._setupTaurusLabel4Attr(mainscreen_ui.hvsCurrentValue,'li/ct/plc1/GUN_HV_I','uA')
        self._setupLed4Attr(mainscreen_ui.hvsOnLed,'li/ct/plc1/gun_hv_onc')
        self._setupCheckbox4Attr(mainscreen_ui.hvsOnCheck,'li/ct/plc1/gun_hv_onc')
        #mainscreen_ui.hvsPopupCheck.setCheckState(False)
        mainscreen_ui.hvsPopupWidget.hide()
        self._hvs = CheckboxManager(mainscreen_ui.hvsPopupCheck,
                                    mainscreen_ui.hvsPopupWidget,"HVS")
        widget = mainscreen_ui.hvsPopupWidget._ui
        self._setupLed4Attr(widget.doorInterlockLed,'li/ct/plc1/gm_di')
        self._setupTaurusLabel4Attr(widget.eGunHVStatus,'li/ct/plc1/Gun_HV_Status')
        self._setupTaurusLabel4Attr(widget.eGunHVValue,'li/ct/plc1/GUN_HV_V','kV')
        
    def _setMainscreen_vacuum(self):
        mainscreen_ui = self.ui.linacMainscreenSynoptic._ui
        self._setupLed4Attr(mainscreen_ui.vv1_oncLed,'li/ct/plc2/VV1_OC')
        self._setupCheckbox4Attr(mainscreen_ui.vv1_oncCheck,'li/ct/plc2/VV1_OC')
        
    def _setMainscreen_fs(self):
        mainscreen_ui = self.ui.linacMainscreenSynoptic._ui
        fluorescentScreens = {1:{'valve_led':mainscreen_ui.fluorescentScreen1ValveLed,
                                 'valve_cmd':mainscreen_ui.fluorescentScreen1ValveCheck,
                                 'valve_attrName':'li/ct/plc1/SCM1_DC',
                                 'light_led':mainscreen_ui.fluorescentScreen1LightLed,
                                 'light_cmd':mainscreen_ui.fluorescentScreen1LightCheck,
                                 'light_attrName':'li/ct/plc1/SCM1_LC',
                                 'status':mainscreen_ui.fluorescentScreen1Status,
                                 'status_attrName':'li/ct/plc1/SCM1_Status',
                                 'view':mainscreen_ui.fluorescentScreen1LightView,
                                 'screen':'li/di/fs-01'},
                              2:{'valve_led':mainscreen_ui.fluorescentScreen2ValveLed,
                                 'valve_cmd':mainscreen_ui.fluorescentScreen2ValveCheck,
                                 'valve_attrName':'li/ct/plc1/SCM2_DC',
                                 'light_led':mainscreen_ui.fluorescentScreen2LightLed,
                                 'light_cmd':mainscreen_ui.fluorescentScreen2LightCheck,
                                 'light_attrName':'li/ct/plc1/SCM2_LC',
                                 'status':mainscreen_ui.fluorescentScreen2Status,
                                 'status_attrName':'li/ct/plc1/SCM2_Status',
                                 'view':mainscreen_ui.fluorescentScreen2LightView,
                                 'screen':'li/di/fs-02'},
                              3:{'valve_led':mainscreen_ui.fluorescentScreen3ValveLed,
                                 'valve_cmd':mainscreen_ui.fluorescentScreen3ValveCheck,
                                 'valve_attrName':'li/ct/plc1/SCM3_DC',
                                 'light_led':mainscreen_ui.fluorescentScreen3LightLed,
                                 'light_cmd':mainscreen_ui.fluorescentScreen3LightCheck,
                                 'light_attrName':'li/ct/plc1/SCM3_LC',
                                 'status':mainscreen_ui.fluorescentScreen3Status,
                                 'status_attrName':'li/ct/plc1/SCM3_Status',
                                 'view':mainscreen_ui.fluorescentScreen3LightView,
                                 'screen':'li/di/fs-03'}}
        self._fluorescentScreensViewButtons = []
        for fs in fluorescentScreens.keys():
            self._setupLed4Attr(fluorescentScreens[fs]['valve_led'],
                                fluorescentScreens[fs]['valve_attrName'],
                                onColor='red',offColor='black')
            self._setupCheckbox4Attr(fluorescentScreens[fs]['valve_cmd'],
                                fluorescentScreens[fs]['valve_attrName'])
            self._setupLed4Attr(fluorescentScreens[fs]['light_led'],
                                fluorescentScreens[fs]['light_attrName'],
                                onColor='green',offColor='black')
            self._setupCheckbox4Attr(fluorescentScreens[fs]['light_cmd'],
                                fluorescentScreens[fs]['light_attrName'])
            self._setupTaurusLabel4Attr(fluorescentScreens[fs]['status'],
                                        fluorescentScreens[fs]['status_attrName'])
            listener = ViewButtonListener(fluorescentScreens[fs]['view'],
                                          fluorescentScreens[fs]['screen'])
            self._fluorescentScreensViewButtons.append(listener)

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
