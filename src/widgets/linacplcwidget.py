#!/usr/bin/env python

# Code implementation generated from reading ui file 'linacPlcWidget.ui'
#
# Created: Mon Dec  9 11:14:33 2013 
#      by: Taurus UI code generator 3.0.0
#
# WARNING! All changes made in this file will be lost!

__docformat__ = 'restructuredtext'

import sys
import PyQt4.Qt as Qt
from ui_linacPlcWidget import Ui_linacPlcWidget
from taurus.qt.qtgui.container import TaurusWidget

class linacPlcWidget(TaurusWidget):

    def __init__(self, parent=None, designMode=False):
        TaurusWidget.__init__(self, parent, designMode=designMode)
        
        self._ui = Ui_linacPlcWidget()
        self._ui.setupUi(self)
        
    

def main():
    app = Qt.QApplication(sys.argv)
    w = linacPlcWidget()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
