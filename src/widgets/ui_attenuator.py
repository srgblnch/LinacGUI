# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'attenuator.ui'
#
# Created: Thu Jan 30 15:33:13 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Attenuator(object):
    def setupUi(self, Attenuator):
        Attenuator.setObjectName(_fromUtf8("Attenuator"))
        Attenuator.resize(108, 78)
        self.gridLayout = QtGui.QGridLayout(Attenuator)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.attenuatorGroup = TaurusGroupBox(Attenuator)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.attenuatorGroup.setFont(font)
        self.attenuatorGroup.setObjectName(_fromUtf8("attenuatorGroup"))
        self.gridLayout_2 = QtGui.QGridLayout(self.attenuatorGroup)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.statusValue = TaurusLabel(self.attenuatorGroup)
        self.statusValue.setObjectName(_fromUtf8("statusValue"))
        self.gridLayout_2.addWidget(self.statusValue, 0, 0, 1, 1)
        self.AttrValue = TaurusLabel(self.attenuatorGroup)
        self.AttrValue.setObjectName(_fromUtf8("AttrValue"))
        self.gridLayout_2.addWidget(self.AttrValue, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.attenuatorGroup, 0, 0, 1, 1)

        self.retranslateUi(Attenuator)
        QtCore.QMetaObject.connectSlotsByName(Attenuator)

    def retranslateUi(self, Attenuator):
        Attenuator.setWindowTitle(QtGui.QApplication.translate("Attenuator", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.attenuatorGroup.setTitle(QtGui.QApplication.translate("Attenuator", "Attenuator #", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.display import TaurusLabel
from taurus.qt.qtgui.container import TaurusWidget, TaurusGroupBox

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Attenuator = QtGui.TaurusWidget()
    ui = Ui_Attenuator()
    ui.setupUi(Attenuator)
    Attenuator.show()
    sys.exit(app.exec_())
