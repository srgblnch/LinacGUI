#!/usr/bin/env python

# Code implementation generated from reading ui file 'ui/beamChargeMonitors.ui'
#
# Created: Thu Mar 13 12:45:27 2014 
#      by: Taurus UI code generator 3.1.1
#
# WARNING! All changes made in this file will be lost!

__docformat__ = 'restructuredtext'

import sys
import PyQt4.Qt as Qt
from ui_beamChargeMonitors import Ui_beamChargeMonitors
from taurus.qt.qtgui.panel import TaurusWidget

class beamChargeMonitors(TaurusWidget):

    def __init__(self, parent=None, designMode=False):
        TaurusWidget.__init__(self, parent, designMode=designMode)
        
        self._ui = Ui_beamChargeMonitors()
        self._ui.setupUi(self)
        
    
    @classmethod
    def getQtDesignerPluginInfo(cls):
        ret = TaurusWidget.getQtDesignerPluginInfo()
        ret['module'] = 'beamchargemonitors'
        ret['group'] = 'Taurus Linac Widgets'
        ret['container'] = ':/designer/widgetstack.png'
        ret['container'] = False
        return ret


def main():
    app = Qt.QApplication(sys.argv)
    w = beamChargeMonitors()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
