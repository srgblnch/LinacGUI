#!/usr/bin/env python

# Code implementation generated from reading ui file 'linacOverview.ui'
#
# Created: Wed Dec  4 12:54:15 2013 
#      by: Taurus UI code generator 3.0.0
#
# WARNING! All changes made in this file will be lost!

__docformat__ = 'restructuredtext'

import sys
import PyQt4.Qt as Qt
from ui_linacOverview import Ui_linacOverview
from taurus.qt.qtgui.container import TaurusWidget

class linacOverview(TaurusWidget):

    def __init__(self, parent=None, designMode=False):
        TaurusWidget.__init__(self, parent, designMode=designMode)
        
        self._ui = Ui_linacOverview()
        self._ui.setupUi(self)
        
    
    @classmethod
    def getQtDesignerPluginInfo(cls):
        ret = TaurusWidget.getQtDesignerPluginInfo()
        ret['module'] = 'linacoverview'
        ret['group'] = 'Taurus Display'
        ret['container'] = ':/designer/frame.png'
        ret['container'] = False
        return ret


def main():
    app = Qt.QApplication(sys.argv)
    w = linacOverview()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
