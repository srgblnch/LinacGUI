# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/ui/klystronLV.ui'
#
# Created: Thu Nov 27 12:42:09 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_klystronLV(object):
    def setupUi(self, klystronLV):
        klystronLV.setObjectName(_fromUtf8("klystronLV"))
        klystronLV.resize(190, 255)
        self.gridLayout_3 = QtGui.QGridLayout(klystronLV)
        self.gridLayout_3.setMargin(1)
        self.gridLayout_3.setSpacing(2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.lowVoltageGroup = TaurusGroupBox(klystronLV)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.lowVoltageGroup.setFont(font)
        self.lowVoltageGroup.setObjectName(_fromUtf8("lowVoltageGroup"))
        self.verticalLayout = QtGui.QVBoxLayout(self.lowVoltageGroup)
        self.verticalLayout.setMargin(2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.LV_StatusLabel = QtGui.QLabel(self.lowVoltageGroup)
        self.LV_StatusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LV_StatusLabel.setObjectName(_fromUtf8("LV_StatusLabel"))
        self.verticalLayout.addWidget(self.LV_StatusLabel)
        self.LV_Status = TaurusLabel(self.lowVoltageGroup)
        self.LV_Status.setMinimumSize(QtCore.QSize(0, 20))
        self.LV_Status.setObjectName(_fromUtf8("LV_Status"))
        self.verticalLayout.addWidget(self.LV_Status)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.LV_TimeLabel = QtGui.QLabel(self.lowVoltageGroup)
        self.LV_TimeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LV_TimeLabel.setObjectName(_fromUtf8("LV_TimeLabel"))
        self.horizontalLayout_4.addWidget(self.LV_TimeLabel)
        self.LV_TimeValue = TaurusLabel(self.lowVoltageGroup)
        self.LV_TimeValue.setMinimumSize(QtCore.QSize(0, 20))
        self.LV_TimeValue.setObjectName(_fromUtf8("LV_TimeValue"))
        self.horizontalLayout_4.addWidget(self.LV_TimeValue)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout_3.addWidget(self.lowVoltageGroup, 0, 0, 1, 1)
        self.taurusGroupBox_2 = TaurusGroupBox(klystronLV)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.taurusGroupBox_2.setFont(font)
        self.taurusGroupBox_2.setObjectName(_fromUtf8("taurusGroupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.taurusGroupBox_2)
        self.gridLayout_2.setMargin(2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.heatStatus = TaurusLabel(self.taurusGroupBox_2)
        self.heatStatus.setMinimumSize(QtCore.QSize(0, 20))
        self.heatStatus.setObjectName(_fromUtf8("heatStatus"))
        self.gridLayout_2.addWidget(self.heatStatus, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.heatVLabel = QtGui.QLabel(self.taurusGroupBox_2)
        self.heatVLabel.setObjectName(_fromUtf8("heatVLabel"))
        self.horizontalLayout.addWidget(self.heatVLabel)
        self.heatVValue = TaurusLabel(self.taurusGroupBox_2)
        self.heatVValue.setMinimumSize(QtCore.QSize(0, 20))
        self.heatVValue.setObjectName(_fromUtf8("heatVValue"))
        self.horizontalLayout.addWidget(self.heatVValue)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.heatILabel = QtGui.QLabel(self.taurusGroupBox_2)
        self.heatILabel.setObjectName(_fromUtf8("heatILabel"))
        self.horizontalLayout_2.addWidget(self.heatILabel)
        self.heatIValue = TaurusLabel(self.taurusGroupBox_2)
        self.heatIValue.setMinimumSize(QtCore.QSize(0, 20))
        self.heatIValue.setObjectName(_fromUtf8("heatIValue"))
        self.horizontalLayout_2.addWidget(self.heatIValue)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.heatTLabel = QtGui.QLabel(self.taurusGroupBox_2)
        self.heatTLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.heatTLabel.setObjectName(_fromUtf8("heatTLabel"))
        self.horizontalLayout_3.addWidget(self.heatTLabel)
        self.heatTValue = TaurusLabel(self.taurusGroupBox_2)
        self.heatTValue.setMinimumSize(QtCore.QSize(0, 20))
        self.heatTValue.setObjectName(_fromUtf8("heatTValue"))
        self.horizontalLayout_3.addWidget(self.heatTValue)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.gridLayout_3.addWidget(self.taurusGroupBox_2, 2, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 3, 0, 1, 1)

        self.retranslateUi(klystronLV)
        QtCore.QMetaObject.connectSlotsByName(klystronLV)

    def retranslateUi(self, klystronLV):
        klystronLV.setWindowTitle(QtGui.QApplication.translate("klystronLV", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.lowVoltageGroup.setTitle(QtGui.QApplication.translate("klystronLV", "klystron low voltage", None, QtGui.QApplication.UnicodeUTF8))
        self.LV_StatusLabel.setText(QtGui.QApplication.translate("klystronLV", "General status", None, QtGui.QApplication.UnicodeUTF8))
        self.LV_TimeLabel.setText(QtGui.QApplication.translate("klystronLV", "Time cooling down", None, QtGui.QApplication.UnicodeUTF8))
        self.LV_TimeValue.setSuffixText(QtGui.QApplication.translate("klystronLV", " s", None, QtGui.QApplication.UnicodeUTF8))
        self.taurusGroupBox_2.setTitle(QtGui.QApplication.translate("klystronLV", "Heating", None, QtGui.QApplication.UnicodeUTF8))
        self.heatVLabel.setText(QtGui.QApplication.translate("klystronLV", "Voltage", None, QtGui.QApplication.UnicodeUTF8))
        self.heatVValue.setSuffixText(QtGui.QApplication.translate("klystronLV", " V", None, QtGui.QApplication.UnicodeUTF8))
        self.heatILabel.setText(QtGui.QApplication.translate("klystronLV", "Current", None, QtGui.QApplication.UnicodeUTF8))
        self.heatIValue.setSuffixText(QtGui.QApplication.translate("klystronLV", " A", None, QtGui.QApplication.UnicodeUTF8))
        self.heatTLabel.setText(QtGui.QApplication.translate("klystronLV", "Time cooling up", None, QtGui.QApplication.UnicodeUTF8))
        self.heatTValue.setSuffixText(QtGui.QApplication.translate("klystronLV", " min", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.display import TaurusLabel
from taurus.qt.qtgui.container import TaurusGroupBox
from taurus.qt.qtgui.panel import TaurusWidget
