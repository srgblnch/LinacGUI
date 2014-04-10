# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/ui/snapshot_klystrons.ui'
#
# Created: Thu Apr 10 16:31:42 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_klystronSnapshot(object):
    def setupUi(self, klystronSnapshot):
        klystronSnapshot.setObjectName(_fromUtf8("klystronSnapshot"))
        klystronSnapshot.resize(297, 114)
        font = QtGui.QFont()
        font.setPointSize(7)
        klystronSnapshot.setFont(font)
        self.gridLayout_3 = QtGui.QGridLayout(klystronSnapshot)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.klystronGroup = TaurusGroupBox(klystronSnapshot)
        self.klystronGroup.setObjectName(_fromUtf8("klystronGroup"))
        self.gridLayout = QtGui.QGridLayout(self.klystronGroup)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.ka2HVPSLabel = QtGui.QLabel(self.klystronGroup)
        self.ka2HVPSLabel.setObjectName(_fromUtf8("ka2HVPSLabel"))
        self.gridLayout.addWidget(self.ka2HVPSLabel, 3, 0, 1, 1)
        self.ka1HVPSLabel = QtGui.QLabel(self.klystronGroup)
        self.ka1HVPSLabel.setObjectName(_fromUtf8("ka1HVPSLabel"))
        self.gridLayout.addWidget(self.ka1HVPSLabel, 2, 0, 1, 1)
        self.PresentWriteTitle = QtGui.QLabel(self.klystronGroup)
        self.PresentWriteTitle.setObjectName(_fromUtf8("PresentWriteTitle"))
        self.gridLayout.addWidget(self.PresentWriteTitle, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)
        self.ka1HVPSCheck = QtGui.QCheckBox(self.klystronGroup)
        self.ka1HVPSCheck.setText(_fromUtf8(""))
        self.ka1HVPSCheck.setObjectName(_fromUtf8("ka1HVPSCheck"))
        self.gridLayout.addWidget(self.ka1HVPSCheck, 2, 4, 1, 1)
        self.ka1HVPSWrite = QtGui.QDoubleSpinBox(self.klystronGroup)
        self.ka1HVPSWrite.setObjectName(_fromUtf8("ka1HVPSWrite"))
        self.gridLayout.addWidget(self.ka1HVPSWrite, 2, 2, 1, 1)
        self.SaveRetrieveTitle = QtGui.QLabel(self.klystronGroup)
        self.SaveRetrieveTitle.setObjectName(_fromUtf8("SaveRetrieveTitle"))
        self.gridLayout.addWidget(self.SaveRetrieveTitle, 0, 2, 1, 1)
        self.ka1HVPSRead = TaurusLabel(self.klystronGroup)
        self.ka1HVPSRead.setObjectName(_fromUtf8("ka1HVPSRead"))
        self.gridLayout.addWidget(self.ka1HVPSRead, 2, 1, 1, 1)
        self.ka2HVPSRead = TaurusLabel(self.klystronGroup)
        self.ka2HVPSRead.setObjectName(_fromUtf8("ka2HVPSRead"))
        self.gridLayout.addWidget(self.ka2HVPSRead, 3, 1, 1, 1)
        self.ka2HVPSWrite = QtGui.QDoubleSpinBox(self.klystronGroup)
        self.ka2HVPSWrite.setObjectName(_fromUtf8("ka2HVPSWrite"))
        self.gridLayout.addWidget(self.ka2HVPSWrite, 3, 2, 1, 1)
        self.ka2HVPSCheck = QtGui.QCheckBox(self.klystronGroup)
        self.ka2HVPSCheck.setText(_fromUtf8(""))
        self.ka2HVPSCheck.setObjectName(_fromUtf8("ka2HVPSCheck"))
        self.gridLayout.addWidget(self.ka2HVPSCheck, 3, 4, 1, 1)
        self.line = QtGui.QFrame(self.klystronGroup)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 1, 3, 4, 1)
        self.gridLayout_3.addWidget(self.klystronGroup, 0, 0, 1, 1)

        self.retranslateUi(klystronSnapshot)
        QtCore.QMetaObject.connectSlotsByName(klystronSnapshot)

    def retranslateUi(self, klystronSnapshot):
        klystronSnapshot.setWindowTitle(QtGui.QApplication.translate("klystronSnapshot", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.klystronGroup.setTitle(QtGui.QApplication.translate("klystronSnapshot", "Klystrons", None, QtGui.QApplication.UnicodeUTF8))
        self.ka2HVPSLabel.setText(QtGui.QApplication.translate("klystronSnapshot", "KA2 High Voltage PS", None, QtGui.QApplication.UnicodeUTF8))
        self.ka1HVPSLabel.setText(QtGui.QApplication.translate("klystronSnapshot", "KA1 High Voltage PS", None, QtGui.QApplication.UnicodeUTF8))
        self.PresentWriteTitle.setText(QtGui.QApplication.translate("klystronSnapshot", "Present value", None, QtGui.QApplication.UnicodeUTF8))
        self.SaveRetrieveTitle.setText(QtGui.QApplication.translate("klystronSnapshot", "Save/Retrieve", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.display import TaurusLabel
from taurus.qt.qtgui.container import TaurusGroupBox
from taurus.qt.qtgui.panel import TaurusWidget
