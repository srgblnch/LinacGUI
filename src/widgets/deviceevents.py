#!/usr/bin/env python

# Code implementation generated from reading ui file 'widgets/ui/DeviceEvents.ui'
#
# Created: Thu Oct 30 16:58:17 2014 
#      by: Taurus UI code generator 3.3.0
#
# WARNING! All changes made in this file will be lost!

__docformat__ = 'restructuredtext'

import sys
import PyQt4.Qt as Qt
from ui_DeviceEvents import Ui_deviceEvents
from taurus.qt.qtgui.panel import TaurusWidget

class deviceEvents(TaurusWidget):

    def __init__(self, parent=None, designMode=False):
        TaurusWidget.__init__(self, parent, designMode=designMode)
        
        self._ui = Ui_deviceEvents()
        self._ui.setupUi(self)
        
    
    @classmethod
    def getQtDesignerPluginInfo(cls):
        ret = TaurusWidget.getQtDesignerPluginInfo()
        ret['module'] = 'widgets.deviceevents'
        ret['group'] = 'Taurus Linac Widgets'
        ret['container'] = ':/designer/frame.png'
        ret['container'] = False
        return ret


def main():
    app = Qt.QApplication(sys.argv)
    w = deviceEvents()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
