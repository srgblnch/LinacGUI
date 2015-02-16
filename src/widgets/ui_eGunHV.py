# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/ui/eGunHV.ui'
#
# Created: Mon Feb 16 11:15:50 2015
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
        eGunHV.resize(120, 95)
        self.gridLayout = QtGui.QGridLayout(eGunHV)
        self.gridLayout.setMargin(1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.taurusGroupBox = TaurusGroupBox(eGunHV)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.taurusGroupBox.setFont(font)
        self.taurusGroupBox.setObjectName(_fromUtf8("taurusGroupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.taurusGroupBox)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.doorInterlockLed = TaurusLed(self.taurusGroupBox)
        self.doorInterlockLed.setMinimumSize(QtCore.QSize(15, 15))
        self.doorInterlockLed.setMaximumSize(QtCore.QSize(15, 15))
        self.doorInterlockLed.setObjectName(_fromUtf8("doorInterlockLed"))
        self.gridLayout_2.addWidget(self.doorInterlockLed, 0, 1, 1, 1)
        self.doorInterlockLabel = QtGui.QLabel(self.taurusGroupBox)
        self.doorInterlockLabel.setObjectName(_fromUtf8("doorInterlockLabel"))
        self.gridLayout_2.addWidget(self.doorInterlockLabel, 0, 0, 1, 1)
        self.AutostopperTriggerLabel = QtGui.QLabel(self.taurusGroupBox)
        self.AutostopperTriggerLabel.setObjectName(_fromUtf8("AutostopperTriggerLabel"))
        self.gridLayout_2.addWidget(self.AutostopperTriggerLabel, 1, 0, 1, 1)
        self.AutostopperTriggerLed = TaurusLed(self.taurusGroupBox)
        self.AutostopperTriggerLed.setMinimumSize(QtCore.QSize(15, 15))
        self.AutostopperTriggerLed.setMaximumSize(QtCore.QSize(15, 15))
        self.AutostopperTriggerLed.setObjectName(_fromUtf8("AutostopperTriggerLed"))
        self.gridLayout_2.addWidget(self.AutostopperTriggerLed, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.RampConfigurator = QtGui.QToolButton(self.taurusGroupBox)
        self.RampConfigurator.setObjectName(_fromUtf8("RampConfigurator"))
        self.horizontalLayout_2.addWidget(self.RampConfigurator)
        self.AutoStopConfiguration = QtGui.QToolButton(self.taurusGroupBox)
        self.AutoStopConfiguration.setObjectName(_fromUtf8("AutoStopConfiguration"))
        self.horizontalLayout_2.addWidget(self.AutoStopConfiguration)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.taurusGroupBox, 0, 0, 1, 1)

        self.retranslateUi(eGunHV)
        QtCore.QMetaObject.connectSlotsByName(eGunHV)

    def retranslateUi(self, eGunHV):
        eGunHV.setWindowTitle(QtGui.QApplication.translate("eGunHV", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.taurusGroupBox.setTitle(QtGui.QApplication.translate("eGunHV", "e-gun status", None, QtGui.QApplication.UnicodeUTF8))
        self.doorInterlockLabel.setText(QtGui.QApplication.translate("eGunHV", "door interlock", None, QtGui.QApplication.UnicodeUTF8))
        self.AutostopperTriggerLabel.setText(QtGui.QApplication.translate("eGunHV", "Autostop Trigger", None, QtGui.QApplication.UnicodeUTF8))
        self.RampConfigurator.setText(QtGui.QApplication.translate("eGunHV", "Ramp", None, QtGui.QApplication.UnicodeUTF8))
        self.AutoStopConfiguration.setText(QtGui.QApplication.translate("eGunHV", "Stopper", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.display import TaurusLed
from taurus.qt.qtgui.container import TaurusGroupBox
from taurus.qt.qtgui.panel import TaurusWidget
