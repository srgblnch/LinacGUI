# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cavityVacuum.ui'
#
# Created: Wed Feb 12 10:56:02 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_cavityVacuum(object):
    def setupUi(self, cavityVacuum):
        cavityVacuum.setObjectName(_fromUtf8("cavityVacuum"))
        cavityVacuum.resize(159, 114)
        self.gridLayout = QtGui.QGridLayout(cavityVacuum)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.vacuumGroup = TaurusGroupBox(cavityVacuum)
        self.vacuumGroup.setObjectName(_fromUtf8("vacuumGroup"))
        self.gridLayout_2 = QtGui.QGridLayout(self.vacuumGroup)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.VacuuRange = QwtThermo(self.vacuumGroup)
        self.VacuuRange.setObjectName(_fromUtf8("VacuuRange"))
        self.gridLayout_2.addWidget(self.VacuuRange, 0, 0, 3, 1)
        self.HVGValue = TaurusLabel(self.vacuumGroup)
        self.HVGValue.setMinimumSize(QtCore.QSize(60, 15))
        self.HVGValue.setMaximumSize(QtCore.QSize(80, 15))
        self.HVGValue.setObjectName(_fromUtf8("HVGValue"))
        self.gridLayout_2.addWidget(self.HVGValue, 0, 1, 1, 2)
        self.IonPumpALabel = QtGui.QLabel(self.vacuumGroup)
        self.IonPumpALabel.setObjectName(_fromUtf8("IonPumpALabel"))
        self.gridLayout_2.addWidget(self.IonPumpALabel, 1, 1, 1, 1)
        self.IonPumpALed = TaurusLed(self.vacuumGroup)
        self.IonPumpALed.setMinimumSize(QtCore.QSize(15, 15))
        self.IonPumpALed.setMaximumSize(QtCore.QSize(15, 15))
        self.IonPumpALed.setObjectName(_fromUtf8("IonPumpALed"))
        self.gridLayout_2.addWidget(self.IonPumpALed, 1, 2, 1, 1)
        self.IonPumpBLabel = QtGui.QLabel(self.vacuumGroup)
        self.IonPumpBLabel.setObjectName(_fromUtf8("IonPumpBLabel"))
        self.gridLayout_2.addWidget(self.IonPumpBLabel, 2, 1, 1, 1)
        self.IonPumpBLed = TaurusLed(self.vacuumGroup)
        self.IonPumpBLed.setMinimumSize(QtCore.QSize(15, 15))
        self.IonPumpBLed.setMaximumSize(QtCore.QSize(15, 15))
        self.IonPumpBLed.setObjectName(_fromUtf8("IonPumpBLed"))
        self.gridLayout_2.addWidget(self.IonPumpBLed, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.vacuumGroup, 0, 0, 1, 1)

        self.retranslateUi(cavityVacuum)
        QtCore.QMetaObject.connectSlotsByName(cavityVacuum)

    def retranslateUi(self, cavityVacuum):
        cavityVacuum.setWindowTitle(QtGui.QApplication.translate("cavityVacuum", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.vacuumGroup.setTitle(QtGui.QApplication.translate("cavityVacuum", "cavity Vacuum", None, QtGui.QApplication.UnicodeUTF8))
        self.IonPumpALabel.setText(QtGui.QApplication.translate("cavityVacuum", "IP_A", None, QtGui.QApplication.UnicodeUTF8))
        self.IonPumpBLabel.setText(QtGui.QApplication.translate("cavityVacuum", "IP_B", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.display import TaurusLabel, TaurusLed
from taurus.qt.qtgui.container import TaurusGroupBox
from taurus.qt.qtgui.panel import TaurusWidget
from qwt_thermo import QwtThermo
