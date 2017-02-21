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

from ctliaux import defaultConfigurations
from ctlienums import doSave
import os
from taurus.external.qt import QtGui, Qt
from taurus.qt.qtgui.container import TaurusWidget
from taurus.qt.qtgui.util.ui import UILoadable
import traceback


@UILoadable(with_ui="ui")
class CompomentsWindow(TaurusWidget):

    _attrSet = {'1': ['ATT2_u', 'GUN_Cathode_u', 'GUN_CDB_u', 'TU_u', 'A0_u',
                      'LLRF_u'],
                '2': ['IP1_u', 'IP2_u', 'IP3_u', 'IP4_u', 'IP5_u', 'IP6_u',
                      'IP7_u', 'IP8_u', 'IP9_u', 'HVG1_u', 'HVG2_u', 'HVG3_u',
                      'HVG4_u', 'HVG5_u', 'IPC1_u', 'IPC2_u', 'IPC3_u',
                      'IPC4_u', 'IPC5_u'],
                '3': ['BC1F_u', 'BC2F_u', 'GL_u', 'SL1F_u', 'SL2F_u',
                      'SL3F_u', 'SL4F_u', 'QT1F_u', 'QT2F_u', 'QT1H_u',
                      'QT2V_u'],
                'k': ['ka_tube_u', 'ka_thyratron_u', 'ka_3GHz_RFampli_u',
                      'ka_DCps_thyratron_u', 'ka_HVps_u', 'ka_IP_controller',
                      'ka_fcoil1_u', 'ka_fcoil2_u', 'ka_fcoil3_u']}

    def __init__(self, parent=None, name=None, designMode=False):
        try:
            self.__name = name.__name__
        except:
            self.__name = "CompomentsWindow"
        try:
            super(CompomentsWindow, self).__init__()
        except Exception as e:
            self.warning("[%s]__init__(): Parent exception!\n%s"
                         % (self.__name, e))
            self.traceback()
        try:
            self.debug("[%s]__init__()" % (self.__name))
            basePath = os.path.dirname(__file__)
            if len(basePath) == 0:
                basePath = '.'
            self.loadUi(filename="compomentsWindow.ui",
                        path=basePath+"/ui")
            self.showActiveAttrs()
            self.setupConfigurationAttrs()
        except Exception as e:
            self.warning("[%s]__init__(): Widget exception! %s"
                         % (self.__name, e))
            traceback.print_exc()
            self.traceback()
    # __init__

    def showActiveAttrs(self):
        self.ui.activeAttributes.setWithButtons(False)
        modelLst = []
        plcs = self._attrSet.keys()
        plcs.sort()
        for plc in plcs:
            if plc == 'k':
                modelLst += self.buildActiveAttrList4Device(4,
                                                            self._attrSet[plc])
                modelLst += self.buildActiveAttrList4Device(5,
                                                            self._attrSet[plc])
            else:
                modelLst += self.buildActiveAttrList4Device(int(plc),
                                                            self._attrSet[plc])
        self.ui.activeAttributes.setModel(modelLst)
        Qt.QObject.connect(self.ui.saveButton, Qt.SIGNAL("clicked(bool)"),
                           self._saveAction)

    def buildActiveAttrList4Device(self, number, lst):
        argout = []
        for element in lst:
            argout.append('li/ct/plc%d/%s_meaning' % (number, element))
        return argout

    def setupConfigurationAttrs(self):
        self.ui.componentSelection.addItems(self.buildComboBoxList())
        Qt.QObject.connect(self.ui.componentSelection,
                           Qt.SIGNAL("currentIndexChanged(QString)"),
                           self.configurationChange)
        self.configurationChange(self.ui.componentSelection.currentText())

    def buildComboBoxList(self):
        lst = []
        plcs = self._attrSet.keys()
        plcs.sort()
        for plc in plcs:
            if plc == 'k':
                lst += self._attrSet[plc]
            else:
                lst += self._attrSet[plc]
        return lst

    def configurationChange(self, newSelection):
        modelsLst = []
        for plc in self._attrSet.keys():
            if newSelection in self._attrSet[plc]:
                if plc == 'k':
                    modelsLst = self.buildConfigurationSet(4, newSelection)
                    modelsLst += self.buildConfigurationSet(5, newSelection)
                else:
                    modelsLst = self.buildConfigurationSet(int(plc),
                                                           newSelection)
        self.ui.componentAttributes.setModel(modelsLst)

    def buildConfigurationSet(self, number, element):
        return ['li/ct/plc%d/%s_active' % (number, element),
                'li/ct/plc%d/%s_options' % (number, element),
                'li/ct/plc%d/%s_numeric' % (number, element),
                'li/ct/plc%d/%s_meaning' % (number, element)]

    def _saveAction(self):
        fileName = str(QtGui.QFileDialog.getSaveFileName(self, "Select File",
                                                         defaultConfigurations,
                                                         "CSV (*.csv)"))
        doSave(fileName)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    compomentsWindow = CompomentsWindow()
    compomentsWindow.show()
    sys.exit(app.exec_())
