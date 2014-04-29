# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/ui/klystronHV.ui'
#
# Created: Tue Apr 29 13:17:19 2014
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
        klystronHV.resize(172, 265)
        self.gridLayout = QtGui.QGridLayout(klystronHV)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.highVoltageGroup = TaurusGroupBox(klystronHV)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.highVoltageGroup.setFont(font)
        self.highVoltageGroup.setObjectName(_fromUtf8("highVoltageGroup"))
        self.gridLayout_2 = QtGui.QGridLayout(self.highVoltageGroup)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
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
        font = QtGui.QFont()
        font.setPointSize(7)
        self.hvVoltageValue.setFont(font)
        self.hvVoltageValue.setObjectName(_fromUtf8("hvVoltageValue"))
        self.gridLayout_2.addWidget(self.hvVoltageValue, 2, 1, 1, 2)
        self.hvRampStepLabel_2 = QtGui.QLabel(self.highVoltageGroup)
        self.hvRampStepLabel_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.hvRampStepLabel_2.setObjectName(_fromUtf8("hvRampStepLabel_2"))
        self.gridLayout_2.addWidget(self.hvRampStepLabel_2, 3, 0, 1, 1)
        self.hvSetpointValue = TaurusLabel(self.highVoltageGroup)
        self.hvSetpointValue.setObjectName(_fromUtf8("hvSetpointValue"))
        self.gridLayout_2.addWidget(self.hvSetpointValue, 3, 1, 1, 2)
        self.hvRamp = QtGui.QLabel(self.highVoltageGroup)
        self.hvRamp.setMaximumSize(QtCore.QSize(60, 16777215))
        self.hvRamp.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.hvRamp.setObjectName(_fromUtf8("hvRamp"))
        self.gridLayout_2.addWidget(self.hvRamp, 4, 0, 1, 1)
        self.hvRampEnableLed = TaurusLed(self.highVoltageGroup)
        self.hvRampEnableLed.setMinimumSize(QtCore.QSize(15, 15))
        self.hvRampEnableLed.setMaximumSize(QtCore.QSize(15, 15))
        self.hvRampEnableLed.setObjectName(_fromUtf8("hvRampEnableLed"))
        self.gridLayout_2.addWidget(self.hvRampEnableLed, 4, 1, 1, 1)
        self.hvRampEnableCheck = TaurusValueCheckBox(self.highVoltageGroup)
        self.hvRampEnableCheck.setShowText(False)
        self.hvRampEnableCheck.setAutoApply(True)
        self.hvRampEnableCheck.setForcedApply(True)
        self.hvRampEnableCheck.setObjectName(_fromUtf8("hvRampEnableCheck"))
        self.gridLayout_2.addWidget(self.hvRampEnableCheck, 4, 2, 1, 1)
        self.hvRampStepLabel = QtGui.QLabel(self.highVoltageGroup)
        self.hvRampStepLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.hvRampStepLabel.setObjectName(_fromUtf8("hvRampStepLabel"))
        self.gridLayout_2.addWidget(self.hvRampStepLabel, 5, 0, 1, 1)
        self.hvRampStepValue = TaurusLabel(self.highVoltageGroup)
        self.hvRampStepValue.setObjectName(_fromUtf8("hvRampStepValue"))
        self.gridLayout_2.addWidget(self.hvRampStepValue, 5, 1, 1, 2)
        self.hvRampStepTimeLabel = QtGui.QLabel(self.highVoltageGroup)
        self.hvRampStepTimeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.hvRampStepTimeLabel.setObjectName(_fromUtf8("hvRampStepTimeLabel"))
        self.gridLayout_2.addWidget(self.hvRampStepTimeLabel, 6, 0, 1, 1)
        self.hvRampStepTimeValue = TaurusLabel(self.highVoltageGroup)
        self.hvRampStepTimeValue.setObjectName(_fromUtf8("hvRampStepTimeValue"))
        self.gridLayout_2.addWidget(self.hvRampStepTimeValue, 6, 1, 1, 2)
        self.hvRampThresholdLabel = QtGui.QLabel(self.highVoltageGroup)
        self.hvRampThresholdLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.hvRampThresholdLabel.setObjectName(_fromUtf8("hvRampThresholdLabel"))
        self.gridLayout_2.addWidget(self.hvRampThresholdLabel, 7, 0, 1, 1)
        self.hvRampThresholdValue = TaurusLabel(self.highVoltageGroup)
        self.hvRampThresholdValue.setObjectName(_fromUtf8("hvRampThresholdValue"))
        self.gridLayout_2.addWidget(self.hvRampThresholdValue, 7, 1, 1, 2)
        self.line = QtGui.QFrame(self.highVoltageGroup)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 8, 0, 1, 3)
        self.pulseStatusValue = TaurusLabel(self.highVoltageGroup)
        self.pulseStatusValue.setMinimumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pulseStatusValue.setFont(font)
        self.pulseStatusValue.setObjectName(_fromUtf8("pulseStatusValue"))
        self.gridLayout_2.addWidget(self.pulseStatusValue, 9, 1, 1, 2)
        self.klystronVoltageValue = TaurusLabel(self.highVoltageGroup)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.klystronVoltageValue.setFont(font)
        self.klystronVoltageValue.setObjectName(_fromUtf8("klystronVoltageValue"))
        self.gridLayout_2.addWidget(self.klystronVoltageValue, 10, 1, 1, 2)
        self.klystronCurrentValue = TaurusLabel(self.highVoltageGroup)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.klystronCurrentValue.setFont(font)
        self.klystronCurrentValue.setObjectName(_fromUtf8("klystronCurrentValue"))
        self.gridLayout_2.addWidget(self.klystronCurrentValue, 11, 1, 1, 2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 12, 1, 1, 1)
        self.klystronLabel = QtGui.QLabel(self.highVoltageGroup)
        self.klystronLabel.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.klystronLabel.setFont(font)
        self.klystronLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.klystronLabel.setWordWrap(True)
        self.klystronLabel.setObjectName(_fromUtf8("klystronLabel"))
        self.gridLayout_2.addWidget(self.klystronLabel, 9, 0, 3, 1)
        self.gridLayout.addWidget(self.highVoltageGroup, 0, 0, 1, 1)

        self.retranslateUi(klystronHV)
        QtCore.QMetaObject.connectSlotsByName(klystronHV)

    def retranslateUi(self, klystronHV):
        klystronHV.setWindowTitle(QtGui.QApplication.translate("klystronHV", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.highVoltageGroup.setTitle(QtGui.QApplication.translate("klystronHV", "klystron high voltage", None, QtGui.QApplication.UnicodeUTF8))
        self.hvLabel.setText(QtGui.QApplication.translate("klystronHV", "Power Supply", None, QtGui.QApplication.UnicodeUTF8))
        self.hvCurrentLabel.setText(QtGui.QApplication.translate("klystronHV", "readback", None, QtGui.QApplication.UnicodeUTF8))
        self.hvRampStepLabel_2.setText(QtGui.QApplication.translate("klystronHV", "setpoint", None, QtGui.QApplication.UnicodeUTF8))
        self.hvRamp.setText(QtGui.QApplication.translate("klystronHV", "HV Ramp", None, QtGui.QApplication.UnicodeUTF8))
        self.hvRampStepLabel.setText(QtGui.QApplication.translate("klystronHV", "step", None, QtGui.QApplication.UnicodeUTF8))
        self.hvRampStepTimeLabel.setText(QtGui.QApplication.translate("klystronHV", "time", None, QtGui.QApplication.UnicodeUTF8))
        self.hvRampThresholdLabel.setText(QtGui.QApplication.translate("klystronHV", "threshold", None, QtGui.QApplication.UnicodeUTF8))
        self.klystronLabel.setText(QtGui.QApplication.translate("klystronHV", "klystron electron pulse", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.display import TaurusLabel, TaurusLed
from taurus.qt.qtgui.container import TaurusGroupBox
from taurus.qt.qtgui.panel import TaurusWidget
from taurus.qt.qtgui.input import TaurusValueCheckBox
