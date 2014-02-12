# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'klystronHV.ui'
#
# Created: Wed Feb 12 12:36:05 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_klystronHV(object):
    def setupUi(self, klystronHV):
        klystronHV.setObjectName(_fromUtf8("klystronHV"))
        klystronHV.resize(185, 165)
        self.gridLayout = QtGui.QGridLayout(klystronHV)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.highVoltageGroup = TaurusGroupBox(klystronHV)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.highVoltageGroup.setFont(font)
        self.highVoltageGroup.setObjectName(_fromUtf8("highVoltageGroup"))
        self.gridLayout_2 = QtGui.QGridLayout(self.highVoltageGroup)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.klystronVoltageValue = TaurusLabel(self.highVoltageGroup)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.klystronVoltageValue.setFont(font)
        self.klystronVoltageValue.setObjectName(_fromUtf8("klystronVoltageValue"))
        self.gridLayout_2.addWidget(self.klystronVoltageValue, 4, 1, 1, 1)
        self.klystronLabel = QtGui.QLabel(self.highVoltageGroup)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.klystronLabel.setFont(font)
        self.klystronLabel.setObjectName(_fromUtf8("klystronLabel"))
        self.gridLayout_2.addWidget(self.klystronLabel, 4, 0, 1, 1)
        self.hvVoltageValue = TaurusLabel(self.highVoltageGroup)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.hvVoltageValue.setFont(font)
        self.hvVoltageValue.setObjectName(_fromUtf8("hvVoltageValue"))
        self.gridLayout_2.addWidget(self.hvVoltageValue, 2, 1, 1, 1)
        self.hvCurrentValue = TaurusLabel(self.highVoltageGroup)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.hvCurrentValue.setFont(font)
        self.hvCurrentValue.setObjectName(_fromUtf8("hvCurrentValue"))
        self.gridLayout_2.addWidget(self.hvCurrentValue, 3, 1, 1, 1)
        self.hvLabel = QtGui.QLabel(self.highVoltageGroup)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.hvLabel.setFont(font)
        self.hvLabel.setObjectName(_fromUtf8("hvLabel"))
        self.gridLayout_2.addWidget(self.hvLabel, 2, 0, 1, 1)
        self.klystronCurrentValue = TaurusLabel(self.highVoltageGroup)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.klystronCurrentValue.setFont(font)
        self.klystronCurrentValue.setObjectName(_fromUtf8("klystronCurrentValue"))
        self.gridLayout_2.addWidget(self.klystronCurrentValue, 5, 1, 1, 1)
        self.pulseStatusValue = TaurusLabel(self.highVoltageGroup)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pulseStatusValue.setFont(font)
        self.pulseStatusValue.setObjectName(_fromUtf8("pulseStatusValue"))
        self.gridLayout_2.addWidget(self.pulseStatusValue, 1, 0, 1, 2)
        self.hvStatusValue = TaurusLabel(self.highVoltageGroup)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.hvStatusValue.setFont(font)
        self.hvStatusValue.setObjectName(_fromUtf8("hvStatusValue"))
        self.gridLayout_2.addWidget(self.hvStatusValue, 0, 0, 1, 2)
        self.gridLayout.addWidget(self.highVoltageGroup, 0, 0, 1, 1)

        self.retranslateUi(klystronHV)
        QtCore.QMetaObject.connectSlotsByName(klystronHV)

    def retranslateUi(self, klystronHV):
        klystronHV.setWindowTitle(QtGui.QApplication.translate("klystronHV", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.highVoltageGroup.setTitle(QtGui.QApplication.translate("klystronHV", "klystron high voltage", None, QtGui.QApplication.UnicodeUTF8))
        self.klystronLabel.setText(QtGui.QApplication.translate("klystronHV", "klystron", None, QtGui.QApplication.UnicodeUTF8))
        self.hvLabel.setText(QtGui.QApplication.translate("klystronHV", "High Voltage", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.display import TaurusLabel
from taurus.qt.qtgui.container import TaurusGroupBox
from taurus.qt.qtgui.panel import TaurusWidget
