#!/usr/bin/env python

# Code implementation generated from reading ui file 'widgets/ui/snapshot_radiofrequency.ui'
#
# Created: Wed Mar 12 08:56:08 2014 
#      by: Taurus UI code generator 3.1.1
#
# WARNING! All changes made in this file will be lost!

__docformat__ = 'restructuredtext'

import sys
import PyQt4.Qt as Qt
from ui_snapshot_radiofrequency import Ui_radioFrequencySnapshot
from taurus.qt.qtgui.panel import TaurusWidget

class radioFrequencySnapshot(TaurusWidget):

    def __init__(self, parent=None, designMode=False):
        TaurusWidget.__init__(self, parent, designMode=designMode)
        
        self._ui = Ui_radioFrequencySnapshot()
        self._ui.setupUi(self)
        
    
    @classmethod
    def getQtDesignerPluginInfo(cls):
        ret = TaurusWidget.getQtDesignerPluginInfo()
        ret['module'] = 'radiofrequencysnapshot'
        ret['group'] = 'Taurus Linac Snapshot'
        ret['container'] = ':/designer/frame.png'
        ret['container'] = False
        return ret


def main():
    app = Qt.QApplication(sys.argv)
    w = radioFrequencySnapshot()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
