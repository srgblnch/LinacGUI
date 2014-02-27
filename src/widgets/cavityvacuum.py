#!/usr/bin/env python

# Code implementation generated from reading ui file 'cavityVacuum.ui'
#
# Created: Thu Feb 27 18:26:28 2014 
#      by: Taurus UI code generator 3.1.1
#
# WARNING! All changes made in this file will be lost!

__docformat__ = 'restructuredtext'

import sys
import PyQt4.Qt as Qt
from ui_cavityVacuum import Ui_CavityVacuum
from taurus.qt.qtgui.panel import TaurusWidget

class CavityVacuum(TaurusWidget):

    def __init__(self, parent=None, designMode=False):
        TaurusWidget.__init__(self, parent, designMode=designMode)
        
        self._ui = Ui_CavityVacuum()
        self._ui.setupUi(self)
        
    
    @classmethod
    def getQtDesignerPluginInfo(cls):
        ret = TaurusWidget.getQtDesignerPluginInfo()
        ret['module'] = 'cavityvacuum'
        ret['group'] = 'Taurus Linac'
        ret['container'] = ':/designer/frame.png'
        ret['container'] = False
        return ret


def main():
    app = Qt.QApplication(sys.argv)
    w = cavityVacuum()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
