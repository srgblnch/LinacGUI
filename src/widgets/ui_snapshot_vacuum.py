# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/snapshot_vacuum.ui'
#
# Created: Wed Mar 12 17:15:27 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_vacuumValveSnapshot(object):
    def setupUi(self, vacuumValveSnapshot):
        vacuumValveSnapshot.setObjectName(_fromUtf8("vacuumValveSnapshot"))
        vacuumValveSnapshot.resize(289, 83)
        font = QtGui.QFont()
        font.setPointSize(7)
        vacuumValveSnapshot.setFont(font)
        self.gridLayout = QtGui.QGridLayout(vacuumValveSnapshot)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.vacuumValveGroup = TaurusGroupBox(vacuumValveSnapshot)
        self.vacuumValveGroup.setObjectName(_fromUtf8("vacuumValveGroup"))
        self.gridLayout_2 = QtGui.QGridLayout(self.vacuumValveGroup)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.VaccumCollimatorValveRead = TaurusLed(self.vacuumValveGroup)
        self.VaccumCollimatorValveRead.setMinimumSize(QtCore.QSize(15, 15))
        self.VaccumCollimatorValveRead.setMaximumSize(QtCore.QSize(15, 15))
        self.VaccumCollimatorValveRead.setObjectName(_fromUtf8("VaccumCollimatorValveRead"))
        self.gridLayout_2.addWidget(self.VaccumCollimatorValveRead, 2, 1, 1, 1)
        self.VaccumCollimatorValveWrite = QtGui.QCheckBox(self.vacuumValveGroup)
        self.VaccumCollimatorValveWrite.setObjectName(_fromUtf8("VaccumCollimatorValveWrite"))
        self.gridLayout_2.addWidget(self.VaccumCollimatorValveWrite, 2, 2, 1, 2)
        self.VaccumCollimatorValveCheck = QtGui.QCheckBox(self.vacuumValveGroup)
        self.VaccumCollimatorValveCheck.setText(_fromUtf8(""))
        self.VaccumCollimatorValveCheck.setObjectName(_fromUtf8("VaccumCollimatorValveCheck"))
        self.gridLayout_2.addWidget(self.VaccumCollimatorValveCheck, 2, 5, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 4, 1, 1, 1)
        self.VaccumCollimatorValveLabel = QtGui.QLabel(self.vacuumValveGroup)
        self.VaccumCollimatorValveLabel.setObjectName(_fromUtf8("VaccumCollimatorValveLabel"))
        self.gridLayout_2.addWidget(self.VaccumCollimatorValveLabel, 2, 0, 1, 1)
        self.line = QtGui.QFrame(self.vacuumValveGroup)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 2, 4, 2, 1)
        self.PresentTitle = QtGui.QLabel(self.vacuumValveGroup)
        self.PresentTitle.setObjectName(_fromUtf8("PresentTitle"))
        self.gridLayout_2.addWidget(self.PresentTitle, 1, 1, 1, 1)
        self.SaveRetrieveTitle = QtGui.QLabel(self.vacuumValveGroup)
        self.SaveRetrieveTitle.setObjectName(_fromUtf8("SaveRetrieveTitle"))
        self.gridLayout_2.addWidget(self.SaveRetrieveTitle, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.vacuumValveGroup, 1, 0, 1, 1)

        self.retranslateUi(vacuumValveSnapshot)
        QtCore.QMetaObject.connectSlotsByName(vacuumValveSnapshot)

    def retranslateUi(self, vacuumValveSnapshot):
        vacuumValveSnapshot.setWindowTitle(QtGui.QApplication.translate("vacuumValveSnapshot", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.vacuumValveGroup.setTitle(QtGui.QApplication.translate("vacuumValveSnapshot", "Vacuum Valves", None, QtGui.QApplication.UnicodeUTF8))
        self.VaccumCollimatorValveWrite.setText(QtGui.QApplication.translate("vacuumValveSnapshot", "open/close", None, QtGui.QApplication.UnicodeUTF8))
        self.VaccumCollimatorValveLabel.setText(QtGui.QApplication.translate("vacuumValveSnapshot", "Collimator Valve", None, QtGui.QApplication.UnicodeUTF8))
        self.PresentTitle.setText(QtGui.QApplication.translate("vacuumValveSnapshot", "Present value", None, QtGui.QApplication.UnicodeUTF8))
        self.SaveRetrieveTitle.setText(QtGui.QApplication.translate("vacuumValveSnapshot", "Save/Retrieve", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.display import TaurusLed
from taurus.qt.qtgui.container import TaurusGroupBox
from taurus.qt.qtgui.panel import TaurusWidget
