#!/usr/bin/env python

# Code implementation generated from reading ui file 'widgets/ui/linacConfigurationScreen.ui'
#
# Created: Wed Mar 12 09:00:09 2014 
#      by: Taurus UI code generator 3.1.1
#
# WARNING! All changes made in this file will be lost!

__docformat__ = 'restructuredtext'

import sys
import PyQt4.Qt as Qt
from ui_linacConfigurationScreen import Ui_linacConfigurationScreen
from taurus.qt.qtgui.panel import TaurusWidget

class linacConfigurationScreen(TaurusWidget):

    def __init__(self, parent=None, designMode=False):
        TaurusWidget.__init__(self, parent, designMode=designMode)
        
        self._ui = Ui_linacConfigurationScreen()
        self._ui.setupUi(self)
        
    
    @classmethod
    def getQtDesignerPluginInfo(cls):
        ret = TaurusWidget.getQtDesignerPluginInfo()
        ret['module'] = 'linacconfigurationscreen'
        ret['group'] = 'Taurus Linac Main'
        ret['container'] = ':/designer/tabwidget.png'
        ret['container'] = False
        return ret


def main():
    app = Qt.QApplication(sys.argv)
    w = linacConfigurationScreen()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
