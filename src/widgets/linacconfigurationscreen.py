#!/usr/bin/env python

# Code implementation generated from reading ui file 'ui/linacConfigurationScreen.ui'
#
# Created: Thu Nov 19 15:37:44 2015 
#      by: Taurus UI code generator 3.4.0
#
# WARNING! All changes made in this file will be lost!

__docformat__ = 'restructuredtext'

import sys
import PyQt4.Qt as Qt
from ui_linacConfigurationScreen import Ui_linacConfigurationScreen
from taurus.qt.qtgui.container import TaurusWidget

class linacConfigurationScreen(TaurusWidget):

    def __init__(self, parent=None, designMode=False):
        TaurusWidget.__init__(self, parent, designMode=designMode)
        
        self._ui = Ui_linacConfigurationScreen()
        self._ui.setupUi(self)
        
    

def main():
    app = Qt.QApplication(sys.argv)
    w = linacConfigurationScreen()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
