#!/usr/bin/env python

# Code implementation generated from reading ui file 'klystron2ictk.ui'
#
# Created: Wed Feb 12 12:35:40 2014 
#      by: Taurus UI code generator 3.1.1
#
# WARNING! All changes made in this file will be lost!

__docformat__ = 'restructuredtext'

import sys
import PyQt4.Qt as Qt
from ui_klystron2ictk import Ui_klystron2itck
from taurus.qt.qtgui.panel import TaurusWidget

class klystron2itck(TaurusWidget):

    def __init__(self, parent=None, designMode=False):
        TaurusWidget.__init__(self, parent, designMode=designMode)
        
        self._ui = Ui_klystron2itck()
        self._ui.setupUi(self)
        
    
    @classmethod
    def getQtDesignerPluginInfo(cls):
        ret = TaurusWidget.getQtDesignerPluginInfo()
        ret['module'] = 'klystron2itck'
        ret['group'] = 'Taurus Linac Widgets'
        ret['icon'] = ':/designer/widgetstack.png'
        ret['container'] = False
        return ret


def main():
    app = Qt.QApplication(sys.argv)
    w = klystron2itck()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
