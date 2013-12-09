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
