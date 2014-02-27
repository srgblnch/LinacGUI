# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/cavityVacuum.ui'
#
# Created: Thu Feb 27 19:07:41 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_CavityVacuum(object):
    def setupUi(self, CavityVacuum):
        CavityVacuum.setObjectName(_fromUtf8("CavityVacuum"))
        CavityVacuum.resize(116, 100)
        self.gridLayout = QtGui.QGridLayout(CavityVacuum)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.vacuumGroup = TaurusGroupBox(CavityVacuum)
        self.vacuumGroup.setObjectName(_fromUtf8("vacuumGroup"))
        self.gridLayout_2 = QtGui.QGridLayout(self.vacuumGroup)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.HVGValue = TaurusLabel(self.vacuumGroup)
        self.HVGValue.setMinimumSize(QtCore.QSize(60, 15))
        self.HVGValue.setMaximumSize(QtCore.QSize(80, 15))
        self.HVGValue.setObjectName(_fromUtf8("HVGValue"))
        self.gridLayout_2.addWidget(self.HVGValue, 0, 0, 1, 2)
        self.IonPumpALabel = QtGui.QLabel(self.vacuumGroup)
        self.IonPumpALabel.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.IonPumpALabel.setFont(font)
        self.IonPumpALabel.setObjectName(_fromUtf8("IonPumpALabel"))
        self.gridLayout_2.addWidget(self.IonPumpALabel, 1, 0, 1, 1)
        self.IonPumpALed = TaurusLed(self.vacuumGroup)
        self.IonPumpALed.setMinimumSize(QtCore.QSize(15, 15))
        self.IonPumpALed.setMaximumSize(QtCore.QSize(15, 15))
        self.IonPumpALed.setObjectName(_fromUtf8("IonPumpALed"))
        self.gridLayout_2.addWidget(self.IonPumpALed, 1, 1, 1, 1)
        self.IonPumpBLabel = QtGui.QLabel(self.vacuumGroup)
        self.IonPumpBLabel.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.IonPumpBLabel.setFont(font)
        self.IonPumpBLabel.setObjectName(_fromUtf8("IonPumpBLabel"))
        self.gridLayout_2.addWidget(self.IonPumpBLabel, 2, 0, 1, 1)
        self.IonPumpBLed = TaurusLed(self.vacuumGroup)
        self.IonPumpBLed.setMinimumSize(QtCore.QSize(15, 15))
        self.IonPumpBLed.setMaximumSize(QtCore.QSize(15, 15))
        self.IonPumpBLed.setObjectName(_fromUtf8("IonPumpBLed"))
        self.gridLayout_2.addWidget(self.IonPumpBLed, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.vacuumGroup, 0, 0, 1, 1)

        self.retranslateUi(CavityVacuum)
        QtCore.QMetaObject.connectSlotsByName(CavityVacuum)

    def retranslateUi(self, CavityVacuum):
        CavityVacuum.setWindowTitle(QtGui.QApplication.translate("CavityVacuum", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.vacuumGroup.setTitle(QtGui.QApplication.translate("CavityVacuum", "cavity Vacuum", None, QtGui.QApplication.UnicodeUTF8))
        self.IonPumpALabel.setText(QtGui.QApplication.translate("CavityVacuum", "IP_A", None, QtGui.QApplication.UnicodeUTF8))
        self.IonPumpBLabel.setText(QtGui.QApplication.translate("CavityVacuum", "IP_B", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.display import TaurusLabel, TaurusLed
from taurus.qt.qtgui.container import TaurusGroupBox
from taurus.qt.qtgui.panel import TaurusWidget
