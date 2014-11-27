# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/ui/klystronHV.ui'
#
# Created: Wed Nov 26 12:55:59 2014
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
        klystronHV.resize(172, 215)
        self.gridLayout = QtGui.QGridLayout(klystronHV)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.highVoltageGroup = TaurusGroupBox(klystronHV)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.highVoltageGroup.setFont(font)
        self.highVoltageGroup.setObjectName(_fromUtf8("highVoltageGroup"))
        self.gridLayout_2 = QtGui.QGridLayout(self.highVoltageGroup)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.RampConfigurator = QtGui.QToolButton(self.highVoltageGroup)
        self.RampConfigurator.setObjectName(_fromUtf8("RampConfigurator"))
        self.gridLayout_2.addWidget(self.RampConfigurator, 3, 2, 1, 1)
        self.hvLabel = QtGui.QLabel(self.highVoltageGroup)
        self.hvLabel.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.hvLabel.setFont(font)
        self.hvLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.hvLabel.setWordWrap(True)
        self.hvLabel.setObjectName(_fromUtf8("hvLabel"))
        self.gridLayout_2.addWidget(self.hvLabel, 0, 0, 2, 1)
        self.hvStatusValue = TaurusLabel(self.highVoltageGroup)
        self.hvStatusValue.setMinimumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.hvStatusValue.setFont(font)
        self.hvStatusValue.setObjectName(_fromUtf8("hvStatusValue"))
        self.gridLayout_2.addWidget(self.hvStatusValue, 0, 1, 1, 2)
        self.hvCurrentValue = TaurusLabel(self.highVoltageGroup)
        self.hvCurrentValue.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.hvCurrentValue.setFont(font)
        self.hvCurrentValue.setObjectName(_fromUtf8("hvCurrentValue"))
        self.gridLayout_2.addWidget(self.hvCurrentValue, 1, 1, 1, 2)
        self.hvCurrentLabel = QtGui.QLabel(self.highVoltageGroup)
        self.hvCurrentLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.hvCurrentLabel.setObjectName(_fromUtf8("hvCurrentLabel"))
        self.gridLayout_2.addWidget(self.hvCurrentLabel, 2, 0, 1, 1)
        self.hvVoltageValue = TaurusLabel(self.highVoltageGroup)
        self.hvVoltageValue.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.hvVoltageValue.setFont(font)
        self.hvVoltageValue.setObjectName(_fromUtf8("hvVoltageValue"))
        self.gridLayout_2.addWidget(self.hvVoltageValue, 2, 1, 1, 2)
        self.hvRampStepLabel_2 = QtGui.QLabel(self.highVoltageGroup)
        self.hvRampStepLabel_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.hvRampStepLabel_2.setObjectName(_fromUtf8("hvRampStepLabel_2"))
        self.gridLayout_2.addWidget(self.hvRampStepLabel_2, 3, 0, 1, 1)
        self.line = QtGui.QFrame(self.highVoltageGroup)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 4, 0, 1, 3)
        self.pulseStatusValue = TaurusLabel(self.highVoltageGroup)
        self.pulseStatusValue.setMinimumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pulseStatusValue.setFont(font)
        self.pulseStatusValue.setObjectName(_fromUtf8("pulseStatusValue"))
        self.gridLayout_2.addWidget(self.pulseStatusValue, 5, 1, 1, 2)
        self.klystronVoltageValue = TaurusLabel(self.highVoltageGroup)
        self.klystronVoltageValue.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.klystronVoltageValue.setFont(font)
        self.klystronVoltageValue.setObjectName(_fromUtf8("klystronVoltageValue"))
        self.gridLayout_2.addWidget(self.klystronVoltageValue, 6, 1, 1, 2)
        self.klystronCurrentValue = TaurusLabel(self.highVoltageGroup)
        self.klystronCurrentValue.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.klystronCurrentValue.setFont(font)
        self.klystronCurrentValue.setObjectName(_fromUtf8("klystronCurrentValue"))
        self.gridLayout_2.addWidget(self.klystronCurrentValue, 7, 1, 1, 2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 8, 1, 1, 1)
        self.klystronLabel = QtGui.QLabel(self.highVoltageGroup)
        self.klystronLabel.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.klystronLabel.setFont(font)
        self.klystronLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.klystronLabel.setWordWrap(True)
        self.klystronLabel.setObjectName(_fromUtf8("klystronLabel"))
        self.gridLayout_2.addWidget(self.klystronLabel, 5, 0, 3, 1)
        self.hvSetpointValue = TaurusLabel(self.highVoltageGroup)
        self.hvSetpointValue.setMinimumSize(QtCore.QSize(0, 20))
        self.hvSetpointValue.setObjectName(_fromUtf8("hvSetpointValue"))
        self.gridLayout_2.addWidget(self.hvSetpointValue, 3, 1, 1, 1)
        self.gridLayout.addWidget(self.highVoltageGroup, 0, 0, 1, 1)

        self.retranslateUi(klystronHV)
        QtCore.QMetaObject.connectSlotsByName(klystronHV)

    def retranslateUi(self, klystronHV):
        klystronHV.setWindowTitle(QtGui.QApplication.translate("klystronHV", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.highVoltageGroup.setTitle(QtGui.QApplication.translate("klystronHV", "klystron high voltage", None, QtGui.QApplication.UnicodeUTF8))
        self.RampConfigurator.setText(QtGui.QApplication.translate("klystronHV", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.hvLabel.setText(QtGui.QApplication.translate("klystronHV", "Power Supply", None, QtGui.QApplication.UnicodeUTF8))
        self.hvCurrentLabel.setText(QtGui.QApplication.translate("klystronHV", "readback", None, QtGui.QApplication.UnicodeUTF8))
        self.hvRampStepLabel_2.setText(QtGui.QApplication.translate("klystronHV", "setpoint", None, QtGui.QApplication.UnicodeUTF8))
        self.klystronLabel.setText(QtGui.QApplication.translate("klystronHV", "klystron electron pulse", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.display import TaurusLabel
from taurus.qt.qtgui.container import TaurusGroupBox
from taurus.qt.qtgui.panel import TaurusWidget
