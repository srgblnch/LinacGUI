#!/usr/bin/env python

# Code implementation generated from reading ui file 'klystronLV.ui'
#
# Created: Wed Feb 12 12:36:22 2014 
#      by: Taurus UI code generator 3.1.1
#
# WARNING! All changes made in this file will be lost!

__docformat__ = 'restructuredtext'

import sys
import PyQt4.Qt as Qt
from ui_klystronLV import Ui_klystronLV
from taurus.qt.qtgui.panel import TaurusWidget

class klystronLV(TaurusWidget):

    def __init__(self, parent=None, designMode=False):
        TaurusWidget.__init__(self, parent, designMode=designMode)
        
        self._ui = Ui_klystronLV()
        self._ui.setupUi(self)
        
    
    @classmethod
    def getQtDesignerPluginInfo(cls):
        ret = TaurusWidget.getQtDesignerPluginInfo()
        ret['module'] = 'klystronlv'
        ret['group'] = 'Taurus Linac'
        ret['icon'] = ':/designer/widgetstack.png'
        ret['container'] = False
        return ret


def main():
    app = Qt.QApplication(sys.argv)
    w = klystronLV()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
