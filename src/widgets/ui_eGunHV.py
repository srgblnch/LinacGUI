# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/ui/eGunHV.ui'
#
# Created: Wed Nov 26 14:58:14 2014
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
        eGunHV.resize(109, 78)
        self.gridLayout = QtGui.QGridLayout(eGunHV)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.taurusGroupBox = TaurusGroupBox(eGunHV)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.taurusGroupBox.setFont(font)
        self.taurusGroupBox.setObjectName(_fromUtf8("taurusGroupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.taurusGroupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.doorInterlockLabel = QtGui.QLabel(self.taurusGroupBox)
        self.doorInterlockLabel.setObjectName(_fromUtf8("doorInterlockLabel"))
        self.horizontalLayout.addWidget(self.doorInterlockLabel)
        self.doorInterlockLed = TaurusLed(self.taurusGroupBox)
        self.doorInterlockLed.setMinimumSize(QtCore.QSize(15, 15))
        self.doorInterlockLed.setMaximumSize(QtCore.QSize(15, 15))
        self.doorInterlockLed.setObjectName(_fromUtf8("doorInterlockLed"))
        self.horizontalLayout.addWidget(self.doorInterlockLed)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.RampConfigurator = QtGui.QToolButton(self.taurusGroupBox)
        self.RampConfigurator.setObjectName(_fromUtf8("RampConfigurator"))
        self.horizontalLayout_2.addWidget(self.RampConfigurator)
        self.AutoStopConfiguration = QtGui.QToolButton(self.taurusGroupBox)
        self.AutoStopConfiguration.setObjectName(_fromUtf8("AutoStopConfiguration"))
        self.horizontalLayout_2.addWidget(self.AutoStopConfiguration)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.taurusGroupBox, 0, 0, 1, 1)

        self.retranslateUi(eGunHV)
        QtCore.QMetaObject.connectSlotsByName(eGunHV)

    def retranslateUi(self, eGunHV):
        eGunHV.setWindowTitle(QtGui.QApplication.translate("eGunHV", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.taurusGroupBox.setTitle(QtGui.QApplication.translate("eGunHV", "e-gun status", None, QtGui.QApplication.UnicodeUTF8))
        self.doorInterlockLabel.setText(QtGui.QApplication.translate("eGunHV", "door interlock", None, QtGui.QApplication.UnicodeUTF8))
        self.RampConfigurator.setText(QtGui.QApplication.translate("eGunHV", "Ramp", None, QtGui.QApplication.UnicodeUTF8))
        self.AutoStopConfiguration.setText(QtGui.QApplication.translate("eGunHV", "Stopper", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.display import TaurusLed
from taurus.qt.qtgui.container import TaurusGroupBox
from taurus.qt.qtgui.panel import TaurusWidget
