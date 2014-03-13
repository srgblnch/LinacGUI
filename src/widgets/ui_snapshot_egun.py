# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/snapshot_egun.ui'
#
# Created: Wed Mar 12 17:15:21 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_electronGunSnapshot(object):
    def setupUi(self, electronGunSnapshot):
        electronGunSnapshot.setObjectName(_fromUtf8("electronGunSnapshot"))
        electronGunSnapshot.resize(301, 135)
        font = QtGui.QFont()
        font.setPointSize(7)
        electronGunSnapshot.setFont(font)
        self.gridLayout = QtGui.QGridLayout(electronGunSnapshot)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.electronGunGroup = TaurusGroupBox(electronGunSnapshot)
        self.electronGunGroup.setObjectName(_fromUtf8("electronGunGroup"))
        self.gridLayout_2 = QtGui.QGridLayout(self.electronGunGroup)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.PresentWriteTitle = QtGui.QLabel(self.electronGunGroup)
        self.PresentWriteTitle.setObjectName(_fromUtf8("PresentWriteTitle"))
        self.gridLayout_2.addWidget(self.PresentWriteTitle, 0, 1, 1, 1)
        self.GunFilamentLowVoltageCheck = QtGui.QCheckBox(self.electronGunGroup)
        self.GunFilamentLowVoltageCheck.setText(_fromUtf8(""))
        self.GunFilamentLowVoltageCheck.setObjectName(_fromUtf8("GunFilamentLowVoltageCheck"))
        self.gridLayout_2.addWidget(self.GunFilamentLowVoltageCheck, 1, 4, 1, 1)
        self.SaveRetrieveTitle = QtGui.QLabel(self.electronGunGroup)
        self.SaveRetrieveTitle.setObjectName(_fromUtf8("SaveRetrieveTitle"))
        self.gridLayout_2.addWidget(self.SaveRetrieveTitle, 0, 2, 1, 1)
        self.GunFilamentLowVoltageLabel = QtGui.QLabel(self.electronGunGroup)
        self.GunFilamentLowVoltageLabel.setObjectName(_fromUtf8("GunFilamentLowVoltageLabel"))
        self.gridLayout_2.addWidget(self.GunFilamentLowVoltageLabel, 1, 0, 1, 1)
        self.GunFilamentLowVoltageRead = TaurusLabel(self.electronGunGroup)
        self.GunFilamentLowVoltageRead.setObjectName(_fromUtf8("GunFilamentLowVoltageRead"))
        self.gridLayout_2.addWidget(self.GunFilamentLowVoltageRead, 1, 1, 1, 1)
        self.GunFilamentLowVoltageWrite = QtGui.QDoubleSpinBox(self.electronGunGroup)
        self.GunFilamentLowVoltageWrite.setObjectName(_fromUtf8("GunFilamentLowVoltageWrite"))
        self.gridLayout_2.addWidget(self.GunFilamentLowVoltageWrite, 1, 2, 1, 1)
        self.line = QtGui.QFrame(self.electronGunGroup)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 1, 3, 5, 1)
        self.GunKathodeLowVoltageRead = TaurusLabel(self.electronGunGroup)
        self.GunKathodeLowVoltageRead.setObjectName(_fromUtf8("GunKathodeLowVoltageRead"))
        self.gridLayout_2.addWidget(self.GunKathodeLowVoltageRead, 2, 1, 2, 1)
        self.GunKathodeLowVoltageWrite = QtGui.QDoubleSpinBox(self.electronGunGroup)
        self.GunKathodeLowVoltageWrite.setObjectName(_fromUtf8("GunKathodeLowVoltageWrite"))
        self.gridLayout_2.addWidget(self.GunKathodeLowVoltageWrite, 2, 2, 2, 1)
        self.GunKathodeLowVoltageLabel = QtGui.QLabel(self.electronGunGroup)
        self.GunKathodeLowVoltageLabel.setObjectName(_fromUtf8("GunKathodeLowVoltageLabel"))
        self.gridLayout_2.addWidget(self.GunKathodeLowVoltageLabel, 3, 0, 1, 1)
        self.GunKathodeLowVoltageCheck = QtGui.QCheckBox(self.electronGunGroup)
        self.GunKathodeLowVoltageCheck.setText(_fromUtf8(""))
        self.GunKathodeLowVoltageCheck.setObjectName(_fromUtf8("GunKathodeLowVoltageCheck"))
        self.gridLayout_2.addWidget(self.GunKathodeLowVoltageCheck, 3, 4, 1, 1)
        self.GunHighVoltagePowerSupplyLabel = QtGui.QLabel(self.electronGunGroup)
        self.GunHighVoltagePowerSupplyLabel.setObjectName(_fromUtf8("GunHighVoltagePowerSupplyLabel"))
        self.gridLayout_2.addWidget(self.GunHighVoltagePowerSupplyLabel, 4, 0, 1, 1)
        self.GunHighVoltagePowerSupplyRead = TaurusLabel(self.electronGunGroup)
        self.GunHighVoltagePowerSupplyRead.setObjectName(_fromUtf8("GunHighVoltagePowerSupplyRead"))
        self.gridLayout_2.addWidget(self.GunHighVoltagePowerSupplyRead, 4, 1, 1, 1)
        self.GunHighVoltagePowerSupplyWrite = QtGui.QDoubleSpinBox(self.electronGunGroup)
        self.GunHighVoltagePowerSupplyWrite.setObjectName(_fromUtf8("GunHighVoltagePowerSupplyWrite"))
        self.gridLayout_2.addWidget(self.GunHighVoltagePowerSupplyWrite, 4, 2, 1, 1)
        self.GunHighVoltagePowerSupplyCheck = QtGui.QCheckBox(self.electronGunGroup)
        self.GunHighVoltagePowerSupplyCheck.setText(_fromUtf8(""))
        self.GunHighVoltagePowerSupplyCheck.setObjectName(_fromUtf8("GunHighVoltagePowerSupplyCheck"))
        self.gridLayout_2.addWidget(self.GunHighVoltagePowerSupplyCheck, 4, 4, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 5, 1, 1, 1)
        self.gridLayout.addWidget(self.electronGunGroup, 0, 0, 1, 1)

        self.retranslateUi(electronGunSnapshot)
        QtCore.QMetaObject.connectSlotsByName(electronGunSnapshot)

    def retranslateUi(self, electronGunSnapshot):
        electronGunSnapshot.setWindowTitle(QtGui.QApplication.translate("electronGunSnapshot", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.electronGunGroup.setTitle(QtGui.QApplication.translate("electronGunSnapshot", "Electron Gun", None, QtGui.QApplication.UnicodeUTF8))
        self.PresentWriteTitle.setText(QtGui.QApplication.translate("electronGunSnapshot", "Present value", None, QtGui.QApplication.UnicodeUTF8))
        self.SaveRetrieveTitle.setText(QtGui.QApplication.translate("electronGunSnapshot", "Save/Retrieve", None, QtGui.QApplication.UnicodeUTF8))
        self.GunFilamentLowVoltageLabel.setText(QtGui.QApplication.translate("electronGunSnapshot", "Filament Low Voltage", None, QtGui.QApplication.UnicodeUTF8))
        self.GunKathodeLowVoltageLabel.setText(QtGui.QApplication.translate("electronGunSnapshot", "Kathode Low Voltage", None, QtGui.QApplication.UnicodeUTF8))
        self.GunHighVoltagePowerSupplyLabel.setText(QtGui.QApplication.translate("electronGunSnapshot", "High Voltage PS", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.display import TaurusLabel
from taurus.qt.qtgui.container import TaurusGroupBox
from taurus.qt.qtgui.panel import TaurusWidget
