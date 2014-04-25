# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/ui/phaseShifter.ui'
#
# Created: Fri Apr 25 11:29:57 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_phaseShifter(object):
    def setupUi(self, phaseShifter):
        phaseShifter.setObjectName(_fromUtf8("phaseShifter"))
        phaseShifter.resize(108, 78)
        self.gridLayout = QtGui.QGridLayout(phaseShifter)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.phaseShifterGroup = TaurusGroupBox(phaseShifter)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.phaseShifterGroup.setFont(font)
        self.phaseShifterGroup.setObjectName(_fromUtf8("phaseShifterGroup"))
        self.gridLayout_2 = QtGui.QGridLayout(self.phaseShifterGroup)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.statusValue = TaurusLabel(self.phaseShifterGroup)
        self.statusValue.setObjectName(_fromUtf8("statusValue"))
        self.gridLayout_2.addWidget(self.statusValue, 0, 0, 1, 1)
        self.attrValue = TaurusLabel(self.phaseShifterGroup)
        self.attrValue.setObjectName(_fromUtf8("attrValue"))
        self.gridLayout_2.addWidget(self.attrValue, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.phaseShifterGroup, 0, 0, 1, 1)

        self.retranslateUi(phaseShifter)
        QtCore.QMetaObject.connectSlotsByName(phaseShifter)

    def retranslateUi(self, phaseShifter):
        phaseShifter.setWindowTitle(QtGui.QApplication.translate("phaseShifter", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.phaseShifterGroup.setTitle(QtGui.QApplication.translate("phaseShifter", "Phase Shifter #", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.display import TaurusLabel
from taurus.qt.qtgui.container import TaurusGroupBox
from taurus.qt.qtgui.panel import TaurusWidget
