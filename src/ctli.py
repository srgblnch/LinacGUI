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
from taurus.qt import Qt

from ui_ctli import Ui_linacGui

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
        self.initComponents()
        #kill splash screen
        self.splashScreen().finish(self)
        
    def initComponents(self):
        self.centralwidget = self.ui.linacTabs
        self.setCentralWidget(self.centralwidget)
        self.setModels_Communications()
        self.setModels_StartUp()
        
    def setModels_Communications(self):
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
    
    def setModels_StartUp(self):
        #following the synoptic regions from left to right and from top to bottom
        startup_ui = self.ui.linacStartupSynoptic._ui
        #The square of the Interlock Unit
        
        #Klystrons low voltage
        klystrons = {1:{'plc':4,
                        'on':[startup_ui.k1onLed,startup_ui.k1onCheck],
                        'rst':[startup_ui.k1rstLed,startup_ui.k1rstCheck],
                        'check':startup_ui.k1Popup,
                        'popup':startup_ui.klystron1LV},
                     2:{'plc':5,
                        'on':[startup_ui.k2onLed,startup_ui.k2onCheck],
                        'rst':[startup_ui.k2rstLed,startup_ui.k2rstCheck],
                        'check':startup_ui.k2Popup,
                        'popup':startup_ui.klystron2LV}}
        for number in klystrons.keys():
            for widget in klystrons[number]['on']:
                widget.setModel('li/ct/plc%d/LV_ONC'%(klystrons[number]['plc']))
            for widget in klystrons[number]['rst']:
                widget.setModel('li/ct/plc%d/LV_Interlock_RC'%(klystrons[number]['plc']))
            widget = klystrons[number]['check']
            #TODO:
            #self.connect(widget, Qt.SIGNAL('stateChanged(int)'),klystrons[number]['popup'],Qt.SLOT('setVisible(bool)'))
            
            widget = klystrons[number]['popup']
            #TODO:#widget.setVisible(False)
            #widget.setWindowOpacity(0)
            #print "!"*20,widget.windowOpacity()
            widget._ui.lowVoltageGroup.setTitle('klystron%d low voltage'%(number))
            widget._ui.LV_Status.setModel('li/ct/plc%d/LV_Status'%(klystrons[number]['plc']))
            widget._ui.LV_TimeValue.setModel('li/ct/plc%d/LV_Time'%(klystrons[number]['plc']))
            widget._ui.heatStatus.setModel('li/ct/plc%d/Heat_Status'%(klystrons[number]['plc']))
            widget._ui.heatVValue.setModel('li/ct/plc%d/Heat_V'%(klystrons[number]['plc']))
            widget._ui.heatIValue.setModel('li/ct/plc%d/Heat_I'%(klystrons[number]['plc']))
            widget._ui.heatTValue.setModel('li/ct/plc%d/Heat_Time'%(klystrons[number]['plc']))
        #e- gun
        startup_ui.eGunLV._ui.cathodeValue.setModel('li/ct/plc1/GUN_Kathode_V')
        startup_ui.eGunLV._ui.cathodeSetpoint.setModel('li/ct/plc1/GUN_Kathode_V')
        startup_ui.eGunLV._ui.temperatureValue.setModel('li/ct/plc1/GUN_Kathode_T')
        startup_ui.eGunLV._ui.filamentValue.setModel('li/ct/plc1/GUN_Filament_V')
        startup_ui.eGunLV._ui.filamentSetpoint.setModel('li/ct/plc1/GUN_Filament_V')
        startup_ui.eGunLV._ui.filamentCurrent.setModel('li/ct/plc1/GUN_Filament_I')
        startup_ui.eGunLV._ui.onLed.setModel('li/ct/plc1/GUN_LV_ONC')
        startup_ui.eGunLV._ui.onCheck.setModel('li/ct/plc1/GUN_LV_ONC')
        startup_ui.eGunLV._ui.eGunStatus.setModel('li/ct/plc1/Gun_Status')
        #Cooling area
        startup_ui.cl1onCheck.setModel('li/ct/plc2/CL1_ONC')
        startup_ui.cl1TemperatureValue.setModel('li/ct/plc2/CL1_T')
        startup_ui.coolingLoop1._ui.coolingLoopGroup.setTitle('Cooling Loop 1')
        startup_ui.coolingLoop1._ui.coolingLoopStatus.setModel('li/ct/plc2/CL1_Status')
        startup_ui.coolingLoop1._ui.temperatureValue.setModel('li/ct/plc2/CL1_T')
        startup_ui.coolingLoop1._ui.powerValue.setModel('li/ct/plc2/CL1_PWD')
        startup_ui.cl2onCheck.setModel('li/ct/plc2/CL2_ONC')
        startup_ui.cl2TemperatureValue.setModel('li/ct/plc2/CL2_T')
        startup_ui.coolingLoop2._ui.coolingLoopGroup.setTitle('Cooling Loop 2')
        startup_ui.coolingLoop2._ui.coolingLoopStatus.setModel('li/ct/plc2/CL2_Status')
        startup_ui.coolingLoop2._ui.temperatureValue.setModel('li/ct/plc2/CL2_T')
        startup_ui.coolingLoop2._ui.powerValue.setModel('li/ct/plc2/CL2_PWD')
        startup_ui.cl3onCheck.setModel('li/ct/plc2/CL3_ONC')
        startup_ui.cl3TemperatureValue.setModel('li/ct/plc2/CL3_T')
        startup_ui.coolingLoop3._ui.coolingLoopGroup.setTitle('Cooling Loop 3')
        startup_ui.coolingLoop3._ui.coolingLoopStatus.setModel('li/ct/plc2/CL3_Status')
        startup_ui.coolingLoop3._ui.temperatureValue.setModel('li/ct/plc2/CL3_T')
        startup_ui.coolingLoop3._ui.powerValue.setModel('li/ct/plc2/CL3_PWD')
        #Magnets area
        startup_ui.sl1Led.setModel('li/ct/plc3/SL1_ONC')
        startup_ui.sl2Led.setModel('li/ct/plc3/SL2_ONC')
        startup_ui.sl3Led.setModel('li/ct/plc3/SL3_ONC')
        startup_ui.sl4Led.setModel('li/ct/plc3/SL4_ONC')
        startup_ui.bc1Led.setModel('li/ct/plc3/BC1_ONC')
        startup_ui.bc2Led.setModel('li/ct/plc3/BC2_ONC')
        startup_ui.glLed.setModel('li/ct/plc3/GL_ONC')
        startup_ui.as1Led.setModel('li/ct/plc3/AS1_ONC')
        startup_ui.qtLed.setModel('li/ct/plc3/QT_ONC')
        startup_ui.as2Led.setModel('li/ct/plc3/AS2_ONC')
        #vacuum area
        startup_ui.vv1Led.setModel('li/ct/plc2/VV1_OC')
        startup_ui.vv1Status.setModel('li/ct/plc2/VV1_Status')
        startup_ui.vv1_oncCheck.setModel('li/ct/plc2/VV1_OC')
        startup_ui.vv2Led.setModel('li/ct/plc2/VV2_OC')
        startup_ui.vv2Status.setModel('li/ct/plc2/VV2_Status')
        startup_ui.vv2_oncCheck.setModel('li/ct/plc2/VV2_OC')
        startup_ui.vv3Led.setModel('li/ct/plc2/VV3_OC')
        startup_ui.vv3Status.setModel('li/ct/plc2/VV3_Status')
        startup_ui.vv3_oncCheck.setModel('li/ct/plc2/VV3_OC')
        startup_ui.vv4Led.setModel('li/ct/plc2/VV4_OC')
        startup_ui.vv4Status.setModel('li/ct/plc2/VV4_Status')
        startup_ui.vv4_oncCheck.setModel('li/ct/plc2/VV4_OC')
        startup_ui.vv5Led.setModel('li/ct/plc2/VV5_OC')
        startup_ui.vv5Status.setModel('li/ct/plc2/VV5_Status')
        startup_ui.vv5_oncCheck.setModel('li/ct/plc2/VV5_OC')
        startup_ui.vv6Led.setModel('li/ct/plc2/VV6_OC')
        startup_ui.vv6Status.setModel('li/ct/plc2/VV6_Status')
        startup_ui.vv6_oncCheck.setModel('li/ct/plc2/VV6_OC')
        startup_ui.vv7Led.setModel('li/ct/plc2/VV7_OC')
        startup_ui.vv7Status.setModel('li/ct/plc2/VV7_Status')
        startup_ui.vv7_oncCheck.setModel('li/ct/plc2/VV7_OC')
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

#     def popupcheckBoxes(self,qstate):
#         pass

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
