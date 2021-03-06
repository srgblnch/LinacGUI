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
from taurus.external.qt import Qt, QtCore, QtGui
from taurus.qt.qtgui.container import TaurusWidget
from taurus.qt.qtgui.util.ui import UILoadable
import traceback


@UILoadable(with_ui="_ui")
class LinacStartupSynoptic(TaurusWidget):

    def __init__(self, parent=None, name=None, designMode=False):
        try:
            self.__name = name.__name__
        except:
            self.__name = "LinacStartupSynoptic"
        super(LinacStartupSynoptic, self).__init__(parent,
                                                   designMode=designMode)
        try:
            self.debug("[%s]__init__()" % (self.__name))
            basePath = os.path.dirname(__file__)
            if len(basePath) == 0:
                basePath = '.'
            self.loadUi(filename="LinacStartupSynoptic.ui",
                        path=basePath+"/ui")
        except Exception as e:
            self.warning("[%s]__init__(): Widget exception! %s"
                         % (self.__name, e))
            traceback.print_exc()
            self.traceback()
            raise e
        self._loadBackGroundImage()

    @classmethod
    def getQtDesignerPluginInfo(cls):
        ret = TaurusWidget.getQtDesignerPluginInfo()
        ret['module'] = 'linacstartupsynoptic'
        ret['group'] = 'Taurus Linac Main'
        ret['icon'] = ':/designer/tabwidget.png'
        ret['container'] = False
        return ret

    def _loadBackGroundImage(self):
        try:
            fileName = self._getImageFileName()
            # print("%s%s%s" % ("\n"*10, fileName, "\n"*10))
            img = QtGui.QPixmap(fileName)
            self._ui.StartUpSchematic.setPixmap(img)
        except Exception as e:
            self.warning("[%s]__init__(): background image exception! %s"
                         % (self.__name, e))
            traceback.print_exc()
            self.traceback()

    def _getImageFileName(self):
        fileName = "jdraw/linac_startup_synoptic.png"
        if os.path.isfile(fileName):
            return fileName
        basePath = os.path.dirname(__file__)
        if os.path.isfile(basePath+"/"+fileName):
            return basePath+"/"+fileName
        if os.path.isfile(basePath+"/../"+fileName):
            return basePath+"/../"+fileName


def main():
    app = Qt.QApplication(sys.argv)
    w = LinacStartupSynoptic()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
