#!/usr/bin/env python

# Code implementation generated from reading ui file 'phaseShifter.ui'
#
# Created: Mon Jan 27 15:58:30 2014 
#      by: Taurus UI code generator 3.0.0
#
# WARNING! All changes made in this file will be lost!

__docformat__ = 'restructuredtext'

import sys
import PyQt4.Qt as Qt
from ui_phaseShifter import Ui_phaseShifter
from taurus.qt.qtgui.container import TaurusWidget

class phaseShifter(TaurusWidget):

    def __init__(self, parent=None, designMode=False):
        TaurusWidget.__init__(self, parent, designMode=designMode)
        
        self._ui = Ui_phaseShifter()
        self._ui.setupUi(self)
        
    
    @classmethod
    def getQtDesignerPluginInfo(cls):
        ret = TaurusWidget.getQtDesignerPluginInfo()
        ret['module'] = 'phaseshifter'
        ret['group'] = 'Taurus Linac'
        ret['container'] = ':/designer/frame.png'
        ret['container'] = False
        return ret


def main():
    app = Qt.QApplication(sys.argv)
    w = phaseShifter()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()