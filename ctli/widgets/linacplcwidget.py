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
from taurus.external.qt import Qt
from taurus.qt.qtgui.container import TaurusWidget
from taurus.qt.qtgui.util.ui import UILoadable
import traceback


@UILoadable(with_ui="_ui")
class LinacPlcWidget(TaurusWidget):

    def __init__(self, parent=None, name=None, designMode=False):
        try:
            self.__name = name.__name__
        except:
            self.__name = "LinacPlcWidget"
        # super(LinacPlcWidget, self).__init__(parent, designMode=designMode)
        TaurusWidget.__init__(self, parent, designMode)
        try:
            self.debug("[%s]__init__()" % (self.__name))
            basePath = os.path.dirname(__file__)
            if len(basePath) == 0:
                basePath = '.'
            self.loadUi(filename="LinacPlcWidget.ui",
                        path=basePath+"/ui")
        except Exception as e:
            self.warning("[%s]__init__(): Widget exception! %s"
                         % (self.__name, e))
            traceback.print_exc()
            self.traceback()

    @classmethod
    def getQtDesignerPluginInfo(cls):
        ret = TaurusWidget.getQtDesignerPluginInfo()
        ret['module'] = 'linacplcwidget'
        ret['group'] = 'Taurus Linac Widgets'
        ret['icon'] = ':/designer/groupbox.png'
        ret['container'] = False
        return ret

    def setModel(self, model):
        TaurusWidget.setModel(self, model)
        self._ui.heartbeatRead.setModel("%s/HeartBeat" % (self.model))
        self._ui.lockerRead.setModel("%s/Lock_Status" % (self.model))
        self._ui.lockingRead.setModel("%s/Locking" % (self.model))
        self._ui.lockingWrite.setModel("%s/Locking" % (self.model))
        self._ui.lockingWrite.setAutoApply(True)
        self._ui.lockingWrite.setForcedApply(False)
        self._ui.stateRead.setModel("%s/state" % (self.model))
        self._ui.statusRead.setModel("%s/status" % (self.model))
        self._ui.statusRead.setBgRole(None)
        self._ui.ResetState.setModel(model)
        self._ui.ResetState.setCommand('ResetState')
        self._ui.RestoreReadDB.setModel(model)
        self._ui.RestoreReadDB.setCommand('RestoreReadDB')
        self._ui.RestoreReadDB.setDangerMessage("This is an experimental "
                                                "feature! Use with caution and"
                                                " under your responsability.")
        self._ui.forceWriteDB.setModel("%s/forceWriteDB" % (self.model))

    def setRelocator(self, relocator, idx):
        self._ui.instanceStateRead.setModel('%s/LinacData.plc%d_state'
                                           % (relocator, idx+1))
        self._ui.instanceLocationRead.setModel('%s/LinacData.plc%d_location'
                                              % (relocator, idx+1))
        self._ui.moveLocal.setModel(relocator)
        self._ui.moveLocal.setCommand('MoveInstance')
        self._ui.moveLocal.setParameters(['LinacData/plc%d' % (idx+1),
                                         'local'])
        self._ui.moveLocal.setCustomText('Local')
        self._ui.moveLocal.setDangerMessage("Be sure Labview is not link "
                                           "to this PLC!")
        self._ui.moveRemote.setModel(relocator)
        self._ui.moveRemote.setCommand('MoveInstance')
        self._ui.moveRemote.setParameters(['LinacData/plc%d' % (idx+1),
                                          'remote'])
        self._ui.moveRemote.setCustomText('Remote')
        self._ui.moveRemote.setDangerMessage("After this action you will "
                                            "lose write access.")
        self._ui.resetInstance.setModel(relocator)
        self._ui.resetInstance.setCommand('RestartInstance')
        self._ui.resetInstance.setParameters(['LinacData/plc%d' % (idx+1)])
        self._ui.resetInstance.setCustomText('Restart')
        self._ui.resetInstance.setDangerMessage("This will stop the "
                                               "control temporally.")


def main():
    import sys
    import taurus.qt.qtgui.application
    Application = taurus.qt.qtgui.application.TaurusApplication
    
    app = Application.instance()
    owns_app = app is None

    if owns_app:
        import taurus.core.util.argparse
        parser = taurus.core.util.argparse.get_taurus_parser()
        parser.usage = "%prog [options] <full_attribute_name(s)>"
        app = Application(sys.argv, cmd_line_parser=parser,
                          app_name="Taurus ctli plc demo", app_version="1.0",
                          org_domain="Taurus", org_name="Tango community")

    args = app.get_command_line_args()

    if len(args) == 0:
        w = LinacPlcWidget()
        w.setModel('li/ct/plc1')
        w.setRelocator('li/ct/linacDataRelocator-01', 1)
        w.resize(300, 50)
    else:
        w = Qt.QWidget()
        layout = Qt.QGridLayout()
        w.setLayout(layout)
        for model in args:
            plc = LinacPlcWidget()
            plc.setModel(model)
            plc.setRelocator('li/ct/linacDataRelocator-01', model[-1])
            layout.addWidget(plc)
        w.resize(300, 50)
    w.show()

    if owns_app:
        sys.exit(app.exec_())
    else:
        return w


if __name__ == "__main__":
    main()
