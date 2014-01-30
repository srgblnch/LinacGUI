# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eGunLV.ui'
#
# Created: Thu Jan 23 12:35:17 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_eGunLV(object):
    def setupUi(self, eGunLV):
        eGunLV.setObjectName(_fromUtf8("eGunLV"))
        eGunLV.resize(157, 98)
        self.gridLayout_2 = QtGui.QGridLayout(eGunLV)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.eGunGroup = TaurusGroupBox(eGunLV)
        self.eGunGroup.setObjectName(_fromUtf8("eGunGroup"))
        self.gridLayout = QtGui.QGridLayout(self.eGunGroup)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.filamentValue = TaurusLabel(self.eGunGroup)
        self.filamentValue.setSuffixText(_fromUtf8(""))
        self.filamentValue.setObjectName(_fromUtf8("filamentValue"))
        self.gridLayout.addWidget(self.filamentValue, 1, 1, 1, 1)
        self.filamentLabel = QtGui.QLabel(self.eGunGroup)
        self.filamentLabel.setObjectName(_fromUtf8("filamentLabel"))
        self.gridLayout.addWidget(self.filamentLabel, 2, 1, 1, 1)
        self.cathodeValue = TaurusLabel(self.eGunGroup)
        self.cathodeValue.setSuffixText(_fromUtf8(""))
        self.cathodeValue.setObjectName(_fromUtf8("cathodeValue"))
        self.gridLayout.addWidget(self.cathodeValue, 1, 2, 1, 1)
        self.cathodeLabel = QtGui.QLabel(self.eGunGroup)
        self.cathodeLabel.setObjectName(_fromUtf8("cathodeLabel"))
        self.gridLayout.addWidget(self.cathodeLabel, 2, 2, 1, 1)
        self.eGunStatus = TaurusLabel(self.eGunGroup)
        self.eGunStatus.setObjectName(_fromUtf8("eGunStatus"))
        self.gridLayout.addWidget(self.eGunStatus, 0, 1, 1, 2)
        self.gridLayout_2.addWidget(self.eGunGroup, 0, 0, 1, 1)

        self.retranslateUi(eGunLV)
        QtCore.QMetaObject.connectSlotsByName(eGunLV)

    def retranslateUi(self, eGunLV):
        eGunLV.setWindowTitle(QtGui.QApplication.translate("eGunLV", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.eGunGroup.setTitle(QtGui.QApplication.translate("eGunLV", "e- gun status", None, QtGui.QApplication.UnicodeUTF8))
        self.filamentLabel.setText(QtGui.QApplication.translate("eGunLV", "Filament V", None, QtGui.QApplication.UnicodeUTF8))
        self.cathodeLabel.setText(QtGui.QApplication.translate("eGunLV", "Cathode V", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.display import TaurusLabel
from taurus.qt.qtgui.container import TaurusWidget, TaurusGroupBox
