#!/usr/bin/env python

# Code implementation generated from reading ui file 'snapshot_timing.ui'
#
# Created: Wed Mar 12 08:39:24 2014 
#      by: Taurus UI code generator 3.1.1
#
# WARNING! All changes made in this file will be lost!

__docformat__ = 'restructuredtext'

import sys
import PyQt4.Qt as Qt
from ui_snapshot_timing import Ui_timingSnapshot
from taurus.qt.qtgui.panel import TaurusWidget

class timingSnapshot(TaurusWidget):

    def __init__(self, parent=None, designMode=False):
        TaurusWidget.__init__(self, parent, designMode=designMode)
        
        self._ui = Ui_timingSnapshot()
        self._ui.setupUi(self)
        
    
    @classmethod
    def getQtDesignerPluginInfo(cls):
        ret = TaurusWidget.getQtDesignerPluginInfo()
        ret['module'] = 'timingsnapshot'
        ret['group'] = 'Taurus Linac Snapshot'
        ret['container'] = ':/designer/frame.png'
        ret['container'] = False
        return ret


def main():
    app = Qt.QApplication(sys.argv)
    w = timingSnapshot()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
