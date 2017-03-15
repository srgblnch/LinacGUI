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
from taurus.external.qt import Qt, Qwt5
from taurus.qt.qtgui.container import TaurusWidget
from taurus.qt.qtgui.util.ui import UILoadable
import traceback


@UILoadable(with_ui="_ui")
class DeviceEvents(TaurusWidget):

    def __init__(self, parent=None, name=None, designMode=False):
        try:
            self.__name = name.__name__
        except:
            self.__name = "DeviceEvents"
        super(DeviceEvents, self).__init__(parent, designMode=designMode)
        try:
            self.debug("[%s]__init__()" % (self.__name))
            basePath = os.path.dirname(__file__)
            if len(basePath) == 0:
                basePath = '.'
            self.loadUi(filename="DeviceEvents.ui",
                        path=basePath+"/ui")
            
        except Exception as e:
            self.warning("[%s]__init__(): Widget exception! %s"
                         % (self.__name, e))
            traceback.print_exc()
            self.traceback()

    def setModel(self, model):
        if model != self.model:
            attributes = ['EventsNumber', 'EventsTime']
            self.info("%s" % (model))
            self._ui.plot.setModel(["%s/%s" % (model, attr)
                                    for attr in attributes])
            self._ui.plot.showLegend(False)
            toY2 = self._ui.plot.getCurve("%s/%s"
                                                % (model, attributes[1]))
            toY2.setYAxis(Qwt5.QwtPlot.Axis(1))  # move time to axis2
            self._ui.plot.autoShowYAxes()
            for attribute in attributes:
                for suffix in ['Max', 'Mean', 'Std', 'Min']:
                    widget = getattr(self._ui, '%s%s' % (attribute, suffix))
                    widget.setModel('%s/%s%s' % (model, attribute, suffix))
            self.model = model

    @classmethod
    def getQtDesignerPluginInfo(cls):
        ret = TaurusWidget.getQtDesignerPluginInfo()
        ret['module'] = 'deviceevents'
        ret['group'] = 'Taurus Linac Widgets'
        ret['container'] = ':/designer/frame.png'
        ret['container'] = False
        return ret


def main():
    app = Qt.QApplication(sys.argv)
    w = DeviceEvents()
    if len(sys.argv) > 1:
        w.setModel(sys.argv[1])
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
