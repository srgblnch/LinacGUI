# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/ui/eGunHV.ui'
#
# Created: Thu Mar 13 15:04:23 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_eGunHV(object):
    def setupUi(self, eGunHV):
        eGunHV.setObjectName(_fromUtf8("eGunHV"))
        eGunHV.resize(109, 55)
        self.gridLayout = QtGui.QGridLayout(eGunHV)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.taurusGroupBox = TaurusGroupBox(eGunHV)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.taurusGroupBox.setFont(font)
        self.taurusGroupBox.setObjectName(_fromUtf8("taurusGroupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.taurusGroupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.doorInterlockLabel = QtGui.QLabel(self.taurusGroupBox)
        self.doorInterlockLabel.setObjectName(_fromUtf8("doorInterlockLabel"))
        self.gridLayout_2.addWidget(self.doorInterlockLabel, 0, 0, 1, 1)
        self.doorInterlockLed = TaurusLed(self.taurusGroupBox)
        self.doorInterlockLed.setMinimumSize(QtCore.QSize(15, 15))
        self.doorInterlockLed.setMaximumSize(QtCore.QSize(15, 15))
        self.doorInterlockLed.setObjectName(_fromUtf8("doorInterlockLed"))
        self.gridLayout_2.addWidget(self.doorInterlockLed, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.taurusGroupBox, 0, 0, 1, 1)

        self.retranslateUi(eGunHV)
        QtCore.QMetaObject.connectSlotsByName(eGunHV)

    def retranslateUi(self, eGunHV):
        eGunHV.setWindowTitle(QtGui.QApplication.translate("eGunHV", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.taurusGroupBox.setTitle(QtGui.QApplication.translate("eGunHV", "e-gun status", None, QtGui.QApplication.UnicodeUTF8))
        self.doorInterlockLabel.setText(QtGui.QApplication.translate("eGunHV", "door interlock", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.display import TaurusLed
from taurus.qt.qtgui.container import TaurusGroupBox
from taurus.qt.qtgui.panel import TaurusWidget
