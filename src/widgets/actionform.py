#!/usr/bin/env python

# Code implementation generated from reading ui file 'ui/actionWidget.ui'
#
# Created: Fri Mar 14 13:21:51 2014
#      by: Taurus UI code generator 3.1.1
#
# WARNING! All changes made in this file will be lost!

__docformat__ = 'restructuredtext'

import sys
import PyQt4.Qt as Qt
from ui_actionWidget import Ui_actionForm
from taurus.qt.qtgui.panel import TaurusWidget


class actionForm(TaurusWidget):

    def __init__(self, parent=None, designMode=False):
        TaurusWidget.__init__(self, parent, designMode=designMode)
        self._ui = Ui_actionForm()
        self._ui.setupUi(self)

    @classmethod
    def getQtDesignerPluginInfo(cls):
        ret = TaurusWidget.getQtDesignerPluginInfo()
        ret['module'] = 'actionform'
        ret['group'] = 'Taurus Linac Widgets'
        ret['container'] = ':/designer/dialogbuttonbox.png'
        ret['container'] = False
        return ret


def main():
    app = Qt.QApplication(sys.argv)
    w = actionForm()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
