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
from taurus.external.qt import QtGui
from taurus.qt.qtgui.container import TaurusWidget
from taurus.qt.qtgui.util.ui import UILoadable
import traceback


@UILoadable(with_ui="ui")
class EVR300(TaurusWidget):
    def __init__(self, parent=None, name=None, designMode=False):
        try:
            self.__name = name.__name__
        except:
            self.__name = "ERV300"
        try:
            super(EVR300, self).__init__()
        except Exception as e:
            self.warning("[%s]__init__(): Parent exception!\n%s"
                         % (self.__name, e))
            self.traceback()
        try:
            self.debug("[%s]__init__()" % (self.__name))
            self.__model = ""
            basePath = os.path.dirname(__file__)
            if len(basePath) == 0:
                basePath = '.'
            self.loadUi(filename="evr300.ui",
                        path=basePath+"/ui")
        except Exception as e:
            self.warning("[%s]__init__(): Widget exception! %s"
                         % (self.__name, e))
            traceback.print_exc()
            self.traceback()
    # __init__

    def setModel(self, devName):
        devName = str(devName)
        if not self.__model == devName:
            attributes = {'PulseDelay0': [self.ui.ch0PulseValue,
                                          self.ui.ch0PulseUnit],
                          'FineDelay0': [self.ui.ch0FineValue,
                                         self.ui.ch0FineUnit],
                          'PulseDelay1': [self.ui.ch1PulseValue,
                                          self.ui.ch1PulseUnit],
                          'FineDelay1': [self.ui.ch1FineValue,
                                         self.ui.ch1FineUnit],
                          'PulseDelay2': [self.ui.ch2PulseValue,
                                          self.ui.ch2PulseUnit],
                          'FineDelay2': [self.ui.ch2FineValue,
                                         self.ui.ch2FineUnit],
                          }
            for attrName in attributes.keys():
                fullName = devName+'/'+attrName
                self.info("setting %s model" % (fullName))
                attributes[attrName][0].setModel(fullName)
                attributes[attrName][1].setModel(fullName +
                                                 '?configuration=unit')
                attributes[attrName][1].bgRole = ''
            self.__model = devName

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    evr300 = EVR300()
    evr300.setModel('li/ti/evr300-cli0302-a')
    evr300.show()
#     if not sys.argv[1] is None:
#         ibaWidget.setModel(sys.argv[1])
    sys.exit(app.exec_())
