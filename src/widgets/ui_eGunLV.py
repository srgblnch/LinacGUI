# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eGunLV.ui'
#
# Created: Thu Dec 19 16:12:39 2013
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
        eGunLV.resize(122, 259)
        self.gridLayout = QtGui.QGridLayout(eGunLV)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.eGunGroup = TaurusGroupBox(eGunLV)
        self.eGunGroup.setObjectName(_fromUtf8("eGunGroup"))
        self.gridLayout_2 = QtGui.QGridLayout(self.eGunGroup)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.onLed = TaurusLed(self.eGunGroup)
        self.onLed.setMinimumSize(QtCore.QSize(15, 15))
        self.onLed.setMaximumSize(QtCore.QSize(15, 15))
        self.onLed.setObjectName(_fromUtf8("onLed"))
        self.gridLayout_2.addWidget(self.onLed, 9, 0, 1, 1)
        self.onCheck = TaurusValueCheckBox(self.eGunGroup)
        self.onCheck.setShowText(False)
        self.onCheck.setAutoApply(True)
        self.onCheck.setForcedApply(False)
        self.onCheck.setObjectName(_fromUtf8("onCheck"))
        self.gridLayout_2.addWidget(self.onCheck, 9, 1, 1, 1)
        self.eGunStatus = TaurusLabel(self.eGunGroup)
        self.eGunStatus.setObjectName(_fromUtf8("eGunStatus"))
        self.gridLayout_2.addWidget(self.eGunStatus, 11, 0, 1, 2)
        self.filamentCurrent = TaurusLabel(self.eGunGroup)
        self.filamentCurrent.setObjectName(_fromUtf8("filamentCurrent"))
        self.gridLayout_2.addWidget(self.filamentCurrent, 8, 0, 1, 2)
        self.filamentSetpoint = TaurusValueSpinBox(self.eGunGroup)
        self.filamentSetpoint.setAutoApply(True)
        self.filamentSetpoint.setObjectName(_fromUtf8("filamentSetpoint"))
        self.gridLayout_2.addWidget(self.filamentSetpoint, 7, 0, 1, 2)
        self.filamentValue = TaurusLabel(self.eGunGroup)
        self.filamentValue.setObjectName(_fromUtf8("filamentValue"))
        self.gridLayout_2.addWidget(self.filamentValue, 6, 0, 1, 2)
        self.filamentLabel = QtGui.QLabel(self.eGunGroup)
        self.filamentLabel.setObjectName(_fromUtf8("filamentLabel"))
        self.gridLayout_2.addWidget(self.filamentLabel, 5, 0, 1, 2)
        self.temperatureValue = TaurusLabel(self.eGunGroup)
        self.temperatureValue.setObjectName(_fromUtf8("temperatureValue"))
        self.gridLayout_2.addWidget(self.temperatureValue, 4, 0, 1, 2)
        self.temperatureLabel = QtGui.QLabel(self.eGunGroup)
        self.temperatureLabel.setObjectName(_fromUtf8("temperatureLabel"))
        self.gridLayout_2.addWidget(self.temperatureLabel, 3, 0, 1, 2)
        self.cathodeSetpoint = TaurusValueSpinBox(self.eGunGroup)
        self.cathodeSetpoint.setAutoApply(True)
        self.cathodeSetpoint.setObjectName(_fromUtf8("cathodeSetpoint"))
        self.gridLayout_2.addWidget(self.cathodeSetpoint, 2, 0, 1, 2)
        self.cathodeValue = TaurusLabel(self.eGunGroup)
        self.cathodeValue.setObjectName(_fromUtf8("cathodeValue"))
        self.gridLayout_2.addWidget(self.cathodeValue, 1, 0, 1, 2)
        self.cathodeLabel = QtGui.QLabel(self.eGunGroup)
        self.cathodeLabel.setObjectName(_fromUtf8("cathodeLabel"))
        self.gridLayout_2.addWidget(self.cathodeLabel, 0, 0, 1, 2)
        self.gridLayout.addWidget(self.eGunGroup, 0, 0, 1, 1)

        self.retranslateUi(eGunLV)
        QtCore.QMetaObject.connectSlotsByName(eGunLV)

    def retranslateUi(self, eGunLV):
        eGunLV.setWindowTitle(QtGui.QApplication.translate("eGunLV", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.filamentCurrent.setSuffixText(QtGui.QApplication.translate("eGunLV", " A", None, QtGui.QApplication.UnicodeUTF8))
        self.filamentValue.setSuffixText(QtGui.QApplication.translate("eGunLV", " V", None, QtGui.QApplication.UnicodeUTF8))
        self.filamentLabel.setText(QtGui.QApplication.translate("eGunLV", "Filament", None, QtGui.QApplication.UnicodeUTF8))
        self.temperatureValue.setSuffixText(QtGui.QApplication.translate("eGunLV", " C", None, QtGui.QApplication.UnicodeUTF8))
        self.temperatureLabel.setText(QtGui.QApplication.translate("eGunLV", "Temperature", None, QtGui.QApplication.UnicodeUTF8))
        self.cathodeValue.setSuffixText(QtGui.QApplication.translate("eGunLV", " V", None, QtGui.QApplication.UnicodeUTF8))
        self.cathodeLabel.setText(QtGui.QApplication.translate("eGunLV", "Cathode", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.display import TaurusLed, TaurusLabel
from taurus.qt.qtgui.container import TaurusWidget, TaurusGroupBox
from taurus.qt.qtgui.input import TaurusValueSpinBox, TaurusValueCheckBox
