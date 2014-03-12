#!/usr/bin/env python

# Code implementation generated from reading ui file 'widgets/ui/snapshot_vacuum.ui'
#
# Created: Wed Mar 12 08:57:09 2014 
#      by: Taurus UI code generator 3.1.1
#
# WARNING! All changes made in this file will be lost!

__docformat__ = 'restructuredtext'

import sys
import PyQt4.Qt as Qt
from ui_snapshot_vacuum import Ui_vacuumValveSnapshot
from taurus.qt.qtgui.panel import TaurusWidget

class vacuumValveSnapshot(TaurusWidget):

    def __init__(self, parent=None, designMode=False):
        TaurusWidget.__init__(self, parent, designMode=designMode)
        
        self._ui = Ui_vacuumValveSnapshot()
        self._ui.setupUi(self)
        
    
    @classmethod
    def getQtDesignerPluginInfo(cls):
        ret = TaurusWidget.getQtDesignerPluginInfo()
        ret['module'] = 'vacuumvalvesnapshot'
        ret['group'] = 'Taurus Linac Snapshot'
        ret['container'] = ':/designer/frame.png'
        ret['container'] = False
        return ret


def main():
    app = Qt.QApplication(sys.argv)
    w = vacuumValveSnapshot()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
