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
import sys
from taurus.external.qt import Qt
from taurus.qt.qtgui.panel import TaurusWidget
from taurus.qt.qtgui.util.ui import UILoadable
import traceback


# The widgets are stored in a subdirectory and needs to be added to the
# pythonpath
linacWidgetsPath = os.environ['PWD']
if linacWidgetsPath not in sys.path:
    sys.path.append(linacWidgetsPath)


@UILoadable(with_ui="_ui")
class DevicesEvents(TaurusWidget):

    def __init__(self, parent=None, name=None, designMode=False):
        try:
            self.__name = name.__name__
        except:
            self.__name = "DevicesEvents"
        super(DevicesEvents, self).__init__(parent, designMode=designMode)
        try:
            self.debug("[%s]__init__()" % (self.__name))
            basePath = os.path.dirname(__file__)
            if len(basePath) == 0:
                basePath = '.'
            self.loadUi(filename="DevicesEvents.ui",
                        path=basePath+"/ui")
        except Exception as e:
            self.warning("[%s]__init__(): Widget exception! %s"
                         % (self.__name, e))
            traceback.print_exc()
            self.traceback()

    def setModel(self, model):
        print(">> %s" % model)
        if not isinstance(self.model, list):
            self.warning("Previous model is not a list: %r (%s)"
                         % (self.model, type(self.model)))
            self.model = [None]*5
        if len(model) == 5:
            for i in range(len(model)):
                if model[i] != self.model[i]:
                    widget = getattr(self._ui, 'eventsplc%d' % (i+1))
                    widget.setModel(model[i])
            self.model = model

    @classmethod
    def getQtDesignerPluginInfo(cls):
        ret = TaurusWidget.getQtDesignerPluginInfo()
        ret['module'] = 'widgets.devicesevents'
        ret['group'] = 'Taurus Linac Widgets'
        ret['container'] = ':/designer/frame.png'
        ret['container'] = False
        return ret


def main():
    app = Qt.QApplication(sys.argv)
    w = DevicesEvents()
    if len(sys.argv) == 6:
        print("> %s" % sys.argv)
        w.setModel(sys.argv[1:])
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
