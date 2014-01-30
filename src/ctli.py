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

    ######
    #---- Auxiliar methods to configure widgets
    def _setupLed4UnknownAttr(self,widget):
        widget.setLedPatternName(":leds/images256/led_{color}_{status}.png")
        widget.setOnColor('green')
        widget.setOffColor('white')

    def _setupLed4Attr(self,widget,attrName,inverted=False):
        widget.setModel(attrName)
        widget.setLedPatternName(":leds/images256/led_{color}_on.png")
        widget.setOnColor('green')
        widget.setOffColor('red')
        if inverted:
            widget.setLedInverted(True)

    def _setupCheckbox4Attr(self,widget,attrName):
        widget.setModel(attrName)
        widget.setAutoApply(True)
        widget.setForcedApply(True)

    def _setupSpinBox4Attr(self,widget,attrName):
        widget.setModel(attrName)
        widget.setAutoApply(True)
        widget.setForcedApply(True)

    def _setupTaurusLabel4Attr(self,widget,attrName,unit=None):
        widget.setModel(attrName)
        if unit:
            widget.setSuffixText(' %s'%unit)
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

    def _setStartup_InterlockUnit(self):
        startup_ui = self.ui.linacStartupSynoptic._ui
        #---- configure the widgets in the top left corner diagram
        self._setupLed4UnknownAttr(startup_ui.klystronAmplifierEnabledLed)                      #KA_ENB
        self._setupLed4UnknownAttr(startup_ui.magnetInterlockStateLed)                          #MI_IS
        self._setupCheckbox4Attr(startup_ui.interlockUnitResetCheck,'li/ct/plc1/interlock_rc')  #Rst
        self._setupLed4UnknownAttr(startup_ui.utilitiesInterlockStateLed)                       #UI_IS
        self._setupLed4Attr(startup_ui.compressedAirStateLed,'li/ct/plc2/ac_is')                #AC_IS
        self._setupLed4UnknownAttr(startup_ui.transferlineVacuumStateLed)                       #TL_VOK
        self._setupLed4Attr(startup_ui.linacVacuumStateLed,'li/ct/plc2/vc_ok')                  #LI_VOK
        self._setupLed4UnknownAttr(startup_ui.electronGunEnabledLed)                            #EG_ENB
        self._setupLed4UnknownAttr(startup_ui.gmdiLed)                                          #GM_DI FIXME!!! This was not well documented in the Labview
        self._setupLed4UnknownAttr(startup_ui.interlockUnitReadyStateLed)                       #UI
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
                        'rfw_attrName':['',''],
                        'rfl':[startup_ui.klystron1InterlockPopupWidget._ui.rfl1Led,
                               startup_ui.klystron1InterlockPopupWidget._ui.rfl2Led],
                        'rfl_attrName':['',''],
                       },
                     2:{'check':startup_ui.klystron2InterlockPopupCheck,
                        'widget':startup_ui.klystron2InterlockPopupWidget,
                        'sf6':startup_ui.klystron2InterlockPopupWidget._ui.sf6p2Led,
                        'sf6_attrName':'li/ct/plc1/sf6_p2_st',
                        'rfw':[startup_ui.klystron2InterlockPopupWidget._ui.rfw3Led],
                        'rfw_attrName':[''],
                        'rfl':[startup_ui.klystron2InterlockPopupWidget._ui.rfl3Led],
                        'rfl_attrName':[''],
                       }
                    }
        self._klystronsInterlocks = {}#to avoid garbage collection on the CkechboxManagers
        #Using the previous structure configure each of the klystrons interlock widgets
        for number in klystrons.keys():
            klystron = klystrons[number]
            klystron['check'].setCheckState(False)
            klystron['widget'].hide()
            self._klystronsInterlocks[number] = CheckboxManager(klystron['check'],
                                                                klystron['widget'],
                                                                'klystron%dInterlock'%number)
            self._setupLed4Attr(klystron['sf6'],klystron['sf6_attrName'])
            for i in range(len(klystron['rfw'])):
                self._setupLed4UnknownAttr(klystron['rfw'][i])
            for i in range(len(klystron['rfl'])):
                self._setupLed4UnknownAttr(klystron['rfl'][i])

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
            klystrons[number]['check'].setCheckState(False)
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
        startup_ui.kdeGunLVPopupCheck.setCheckState(False)
        startup_ui.kdeGunLVWidget.hide()
        self._egunManager = CheckboxManager(startup_ui.kdeGunLVPopupCheck,
                                            startup_ui.kdeGunLVWidget,
                                            "EGunPopup")
        self._setupSpinBox4Attr(startup_ui.filamentSetpoint,'li/ct/plc1/GUN_Filament_V')
        self._setupSpinBox4Attr(startup_ui.cathodeSetpoint,'li/ct/plc1/GUN_Kathode_V')
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
                           'power_attrName':'li/ct/plc2/CL1_PWD'},
                        2:{'cmdCheck':startup_ui.coolingLoop2OnCheck,
                           'cmdLed':startup_ui.coolingLoop2OnLed,
                           'cmd_attrName':'li/ct/plc2/CL2_ONC',
                           'Temperature':startup_ui.coolingLoop2TemperatureValue,
                           'Temperature_attrName':'li/ct/plc2/CL2_T',
                           'check':startup_ui.coolingLoop2PopupCheck,
                           'widget':startup_ui.coolingLoop2Widget,
                           'status_attrName':'li/ct/plc2/CL2_Status',
                           'power_attrName':'li/ct/plc2/CL2_PWD'},
                        3:{'cmdCheck':startup_ui.coolingLoop3OnCheck,
                           'cmdLed':startup_ui.coolingLoop3OnLed,
                           'cmd_attrName':'li/ct/plc2/CL3_ONC',
                           'Temperature':startup_ui.coolingLoop3TemperatureValue,
                           'Temperature_attrName':'li/ct/plc2/CL3_T',
                           'check':startup_ui.coolingLoop3PopupCheck,
                           'widget':startup_ui.coolingLoop3Widget,
                           'status_attrName':'li/ct/plc2/CL3_Status',
                           'power_attrName':'li/ct/plc2/CL3_PWD'}
                       }
        self._coolingLoopManagers = {}
        for number in coolingLoops.keys():
            #command area
            self._setupCheckbox4Attr(coolingLoops[number]['cmdCheck'],coolingLoops[number]['cmd_attrName'])
            self._setupLed4Attr(coolingLoops[number]['cmdLed'],coolingLoops[number]['cmd_attrName'])
            #information area
            self._setupSpinBox4Attr(coolingLoops[number]['Temperature'],coolingLoops[number]['Temperature_attrName'])
            coolingLoops[number]['check'].setCheckState(False)
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

    def _setStartup_magnets(self):
        startup_ui = self.ui.linacStartupSynoptic._ui
        self._setupLed4Attr(startup_ui.sl1Led,'li/ct/plc3/SL1_ONC',inverted=True)
        self._setupLed4Attr(startup_ui.sl2Led,'li/ct/plc3/SL2_ONC',inverted=True)
        self._setupLed4Attr(startup_ui.sl3Led,'li/ct/plc3/SL3_ONC',inverted=True)
        self._setupLed4Attr(startup_ui.sl4Led,'li/ct/plc3/SL4_ONC',inverted=True)
        self._setupLed4Attr(startup_ui.bc1Led,'li/ct/plc3/BC1_ONC',inverted=True)
        self._setupLed4Attr(startup_ui.bc2Led,'li/ct/plc3/BC2_ONC',inverted=True)
        self._setupLed4Attr(startup_ui.glLed,'li/ct/plc3/GL_ONC',inverted=True)
        self._setupLed4Attr(startup_ui.as1Led,'li/ct/plc3/AS1_ONC',inverted=True)
        self._setupLed4Attr(startup_ui.qtLed,'li/ct/plc3/QT_ONC',inverted=True)
        self._setupLed4Attr(startup_ui.as2Led,'li/ct/plc3/AS2_ONC',inverted=True)

    def _setStartup_vacuum(self):
        startup_ui = self.ui.linacStartupSynoptic._ui
        vacuumValves = {1:{'cmdCheck':startup_ui.vacuumValve1OnCheck,
                           'cmdLed':startup_ui.vacuumValve1OnLed,
                           'cmd_attrName':'li/ct/plc2/VV1_OC',
                           'status':startup_ui.vacuumValve1OnStatus,
                           'status_attrName':'li/ct/plc2/VV1_Status'},
                        2:{'cmdCheck':startup_ui.vacuumValve2OnCheck,
                           'cmdLed':startup_ui.vacuumValve2OnLed,
                           'cmd_attrName':'li/ct/plc2/VV2_OC',
                           'status':startup_ui.vacuumValve2OnStatus,
                           'status_attrName':'li/ct/plc2/VV2_Status'},
                        3:{'cmdCheck':startup_ui.vacuumValve3OnCheck,
                           'cmdLed':startup_ui.vacuumValve3OnLed,
                           'cmd_attrName':'li/ct/plc2/VV3_OC',
                           'status':startup_ui.vacuumValve3OnStatus,
                           'status_attrName':'li/ct/plc2/VV3_Status'},
                        4:{'cmdCheck':startup_ui.vacuumValve4OnCheck,
                           'cmdLed':startup_ui.vacuumValve4OnLed,
                           'cmd_attrName':'li/ct/plc2/VV4_OC',
                           'status':startup_ui.vacuumValve4OnStatus,
                           'status_attrName':'li/ct/plc2/VV4_Status'},
                        5:{'cmdCheck':startup_ui.vacuumValve5OnCheck,
                           'cmdLed':startup_ui.vacuumValve5OnLed,
                           'cmd_attrName':'li/ct/plc2/VV5_OC',
                           'status':startup_ui.vacuumValve5OnStatus,
                           'status_attrName':'li/ct/plc2/VV5_Status'},
                        6:{'cmdCheck':startup_ui.vacuumValve6OnCheck,
                           'cmdLed':startup_ui.vacuumValve6OnLed,
                           'cmd_attrName':'li/ct/plc2/VV6_OC',
                           'status':startup_ui.vacuumValve6OnStatus,
                           'status_attrName':'li/ct/plc2/VV6_Status'},
                        7:{'cmdCheck':startup_ui.vacuumValve7OnCheck,
                           'cmdLed':startup_ui.vacuumValve7OnLed,
                           'cmd_attrName':'li/ct/plc2/VV7_OC',
                           'status':startup_ui.vacuumValve7OnStatus,
                           'status_attrName':'li/ct/plc2/VV7_Status'},
                       }
        #TODO: there is an OPEN all valves not implemented in the device
        #TODO: there is a reset vacuum interlocks to check if it is in the device
        for number in vacuumValves.keys():
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
        startup_ui.hvg1Value.setModel('li/ct/plc2/HVG1_P')
        startup_ui.hvg2Led.setModel('li/ct/plc2/HVG2_IS')
        startup_ui.hvg2Value.setModel('li/ct/plc2/HVG2_P')
        startup_ui.hvg3Led.setModel('li/ct/plc2/HVG3_IS')
        startup_ui.hvg3Value.setModel('li/ct/plc2/HVG3_P')
        startup_ui.hvg4Led.setModel('li/ct/plc2/HVG4_IS')
        startup_ui.hvg4Value.setModel('li/ct/plc2/HVG4_P')
        startup_ui.hvg5Led.setModel('li/ct/plc2/HVG5_IS')
        startup_ui.hvg5Value.setModel('li/ct/plc2/HVG5_P')
        startup_ui.ipc1Value1.setModel('li/ct/plc2/IP1_P')
        startup_ui.ipc1Value2.setModel('li/ct/plc2/IP2_P')
        startup_ui.ipc2Value1.setModel('li/ct/plc2/IP3_P')
        startup_ui.ipc2Value2.setModel('li/ct/plc2/IP4_P')
        startup_ui.ipc3Value1.setModel('li/ct/plc2/IP5_P')
        startup_ui.ipc3Value2.setModel('li/ct/plc2/IP6_P')
        startup_ui.ipc4Value1.setModel('li/ct/plc2/IP7_P')
        startup_ui.ipc4Value2.setModel('li/ct/plc2/IP8_P')
        startup_ui.ipc5Value1.setModel('li/ct/plc2/IP9_P')
        #TODO:
        #startup_ui.vv_rstCheck.setmodel('')
        #startup_ui.vv_oncCheck.setmodel('')

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
        #self.connect(self._checker,Qt.SIGNAL('stateChanged(int)'),self._checkboxChanged)
        Qt.QObject.connect(self._checker,Qt.SIGNAL('stateChanged(int)'),self._checkboxChanged)
        self.debug("Build the checkbox manager")

    def _checkboxChanged(self,qstate):
        if self._checker.isChecked():
            self._widget.show()
        else:
            self._widget.hide()

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
