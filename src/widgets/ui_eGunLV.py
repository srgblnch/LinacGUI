# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/ui/eGunLV.ui'
#
# Created: Thu Nov 27 12:41:27 2014
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
        eGunLV.resize(158, 95)
        self.gridLayout_2 = QtGui.QGridLayout(eGunLV)
        self.gridLayout_2.setMargin(1)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.eGunGroup = TaurusGroupBox(eGunLV)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.eGunGroup.setFont(font)
        self.eGunGroup.setObjectName(_fromUtf8("eGunGroup"))
        self.gridLayout = QtGui.QGridLayout(self.eGunGroup)
        self.gridLayout.setMargin(2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.filamentValue = TaurusLabel(self.eGunGroup)
        self.filamentValue.setSuffixText(_fromUtf8(""))
        self.filamentValue.setObjectName(_fromUtf8("filamentValue"))
        self.verticalLayout.addWidget(self.filamentValue)
        self.filamentLabel = QtGui.QLabel(self.eGunGroup)
        self.filamentLabel.setObjectName(_fromUtf8("filamentLabel"))
        self.verticalLayout.addWidget(self.filamentLabel)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.cathodeValue = TaurusLabel(self.eGunGroup)
        self.cathodeValue.setSuffixText(_fromUtf8(""))
        self.cathodeValue.setObjectName(_fromUtf8("cathodeValue"))
        self.verticalLayout_2.addWidget(self.cathodeValue)
        self.cathodeLabel = QtGui.QLabel(self.eGunGroup)
        self.cathodeLabel.setObjectName(_fromUtf8("cathodeLabel"))
        self.verticalLayout_2.addWidget(self.cathodeLabel)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.eGunStatus = TaurusLabel(self.eGunGroup)
        self.eGunStatus.setObjectName(_fromUtf8("eGunStatus"))
        self.horizontalLayout.addWidget(self.eGunStatus)
        self.RampConfigurator = QtGui.QToolButton(self.eGunGroup)
        self.RampConfigurator.setObjectName(_fromUtf8("RampConfigurator"))
        self.horizontalLayout.addWidget(self.RampConfigurator)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.gridLayout_2.addWidget(self.eGunGroup, 0, 0, 1, 1)

        self.retranslateUi(eGunLV)
        QtCore.QMetaObject.connectSlotsByName(eGunLV)

    def retranslateUi(self, eGunLV):
        eGunLV.setWindowTitle(QtGui.QApplication.translate("eGunLV", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.eGunGroup.setTitle(QtGui.QApplication.translate("eGunLV", "e- gun status", None, QtGui.QApplication.UnicodeUTF8))
        self.filamentLabel.setText(QtGui.QApplication.translate("eGunLV", "Filament V", None, QtGui.QApplication.UnicodeUTF8))
        self.cathodeLabel.setText(QtGui.QApplication.translate("eGunLV", "Cathode V", None, QtGui.QApplication.UnicodeUTF8))
        self.RampConfigurator.setText(QtGui.QApplication.translate("eGunLV", "Ramp", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.display import TaurusLabel
from taurus.qt.qtgui.container import TaurusGroupBox
from taurus.qt.qtgui.panel import TaurusWidget
