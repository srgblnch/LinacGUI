# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/ui/snapshot_vacuum.ui'
#
# Created: Wed Mar 12 14:28:14 2014
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
        vacuumValveSnapshot.resize(301, 265)
        font = QtGui.QFont()
        font.setPointSize(7)
        vacuumValveSnapshot.setFont(font)
        self.gridLayout = QtGui.QGridLayout(vacuumValveSnapshot)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.vacuumValveGroup = TaurusGroupBox(vacuumValveSnapshot)
        self.vacuumValveGroup.setObjectName(_fromUtf8("vacuumValveGroup"))
        self.gridLayout_2 = QtGui.QGridLayout(self.vacuumValveGroup)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.VaccumValve3Read = TaurusLed(self.vacuumValveGroup)
        self.VaccumValve3Read.setMinimumSize(QtCore.QSize(15, 15))
        self.VaccumValve3Read.setMaximumSize(QtCore.QSize(15, 15))
        self.VaccumValve3Read.setObjectName(_fromUtf8("VaccumValve3Read"))
        self.gridLayout_2.addWidget(self.VaccumValve3Read, 5, 1, 1, 1)
        self.VaccumValve3Write = QtGui.QCheckBox(self.vacuumValveGroup)
        self.VaccumValve3Write.setObjectName(_fromUtf8("VaccumValve3Write"))
        self.gridLayout_2.addWidget(self.VaccumValve3Write, 5, 2, 1, 2)
        self.VaccumValve4Check = QtGui.QCheckBox(self.vacuumValveGroup)
        self.VaccumValve4Check.setText(_fromUtf8(""))
        self.VaccumValve4Check.setObjectName(_fromUtf8("VaccumValve4Check"))
        self.gridLayout_2.addWidget(self.VaccumValve4Check, 6, 5, 1, 1)
        self.VaccumValve5Label = QtGui.QLabel(self.vacuumValveGroup)
        self.VaccumValve5Label.setObjectName(_fromUtf8("VaccumValve5Label"))
        self.gridLayout_2.addWidget(self.VaccumValve5Label, 7, 0, 1, 1)
        self.VaccumValve5Read = TaurusLed(self.vacuumValveGroup)
        self.VaccumValve5Read.setMinimumSize(QtCore.QSize(15, 15))
        self.VaccumValve5Read.setMaximumSize(QtCore.QSize(15, 15))
        self.VaccumValve5Read.setObjectName(_fromUtf8("VaccumValve5Read"))
        self.gridLayout_2.addWidget(self.VaccumValve5Read, 7, 1, 1, 1)
        self.VaccumCollimatorValveRead = TaurusLed(self.vacuumValveGroup)
        self.VaccumCollimatorValveRead.setMinimumSize(QtCore.QSize(15, 15))
        self.VaccumCollimatorValveRead.setMaximumSize(QtCore.QSize(15, 15))
        self.VaccumCollimatorValveRead.setObjectName(_fromUtf8("VaccumCollimatorValveRead"))
        self.gridLayout_2.addWidget(self.VaccumCollimatorValveRead, 2, 1, 1, 1)
        self.VaccumValve1Read = TaurusLed(self.vacuumValveGroup)
        self.VaccumValve1Read.setMinimumSize(QtCore.QSize(15, 15))
        self.VaccumValve1Read.setMaximumSize(QtCore.QSize(15, 15))
        self.VaccumValve1Read.setObjectName(_fromUtf8("VaccumValve1Read"))
        self.gridLayout_2.addWidget(self.VaccumValve1Read, 3, 1, 1, 1)
        self.VaccumValve1Write = QtGui.QCheckBox(self.vacuumValveGroup)
        self.VaccumValve1Write.setObjectName(_fromUtf8("VaccumValve1Write"))
        self.gridLayout_2.addWidget(self.VaccumValve1Write, 3, 2, 1, 2)
        self.VaccumValve1Check = QtGui.QCheckBox(self.vacuumValveGroup)
        self.VaccumValve1Check.setText(_fromUtf8(""))
        self.VaccumValve1Check.setObjectName(_fromUtf8("VaccumValve1Check"))
        self.gridLayout_2.addWidget(self.VaccumValve1Check, 3, 5, 1, 1)
        self.VaccumValve2Label = QtGui.QLabel(self.vacuumValveGroup)
        self.VaccumValve2Label.setObjectName(_fromUtf8("VaccumValve2Label"))
        self.gridLayout_2.addWidget(self.VaccumValve2Label, 4, 0, 1, 1)
        self.VaccumValve6Write = QtGui.QCheckBox(self.vacuumValveGroup)
        self.VaccumValve6Write.setObjectName(_fromUtf8("VaccumValve6Write"))
        self.gridLayout_2.addWidget(self.VaccumValve6Write, 8, 2, 1, 2)
        self.VaccumValve2Read = TaurusLed(self.vacuumValveGroup)
        self.VaccumValve2Read.setMinimumSize(QtCore.QSize(15, 15))
        self.VaccumValve2Read.setMaximumSize(QtCore.QSize(15, 15))
        self.VaccumValve2Read.setObjectName(_fromUtf8("VaccumValve2Read"))
        self.gridLayout_2.addWidget(self.VaccumValve2Read, 4, 1, 1, 1)
        self.VaccumValve2Write = QtGui.QCheckBox(self.vacuumValveGroup)
        self.VaccumValve2Write.setObjectName(_fromUtf8("VaccumValve2Write"))
        self.gridLayout_2.addWidget(self.VaccumValve2Write, 4, 2, 1, 2)
        self.VaccumCollimatorValveWrite = QtGui.QCheckBox(self.vacuumValveGroup)
        self.VaccumCollimatorValveWrite.setObjectName(_fromUtf8("VaccumCollimatorValveWrite"))
        self.gridLayout_2.addWidget(self.VaccumCollimatorValveWrite, 2, 2, 1, 2)
        self.VaccumValve5Write = QtGui.QCheckBox(self.vacuumValveGroup)
        self.VaccumValve5Write.setObjectName(_fromUtf8("VaccumValve5Write"))
        self.gridLayout_2.addWidget(self.VaccumValve5Write, 7, 2, 1, 2)
        self.VaccumValve5Check = QtGui.QCheckBox(self.vacuumValveGroup)
        self.VaccumValve5Check.setText(_fromUtf8(""))
        self.VaccumValve5Check.setObjectName(_fromUtf8("VaccumValve5Check"))
        self.gridLayout_2.addWidget(self.VaccumValve5Check, 7, 5, 1, 1)
        self.VaccumValve2Check = QtGui.QCheckBox(self.vacuumValveGroup)
        self.VaccumValve2Check.setText(_fromUtf8(""))
        self.VaccumValve2Check.setObjectName(_fromUtf8("VaccumValve2Check"))
        self.gridLayout_2.addWidget(self.VaccumValve2Check, 4, 5, 1, 1)
        self.VaccumValve3Label = QtGui.QLabel(self.vacuumValveGroup)
        self.VaccumValve3Label.setObjectName(_fromUtf8("VaccumValve3Label"))
        self.gridLayout_2.addWidget(self.VaccumValve3Label, 5, 0, 1, 1)
        self.VaccumValve4Read = TaurusLed(self.vacuumValveGroup)
        self.VaccumValve4Read.setMinimumSize(QtCore.QSize(15, 15))
        self.VaccumValve4Read.setMaximumSize(QtCore.QSize(15, 15))
        self.VaccumValve4Read.setObjectName(_fromUtf8("VaccumValve4Read"))
        self.gridLayout_2.addWidget(self.VaccumValve4Read, 6, 1, 1, 1)
        self.VaccumValve4Write = QtGui.QCheckBox(self.vacuumValveGroup)
        self.VaccumValve4Write.setObjectName(_fromUtf8("VaccumValve4Write"))
        self.gridLayout_2.addWidget(self.VaccumValve4Write, 6, 2, 1, 2)
        self.VaccumCollimatorValveCheck = QtGui.QCheckBox(self.vacuumValveGroup)
        self.VaccumCollimatorValveCheck.setText(_fromUtf8(""))
        self.VaccumCollimatorValveCheck.setObjectName(_fromUtf8("VaccumCollimatorValveCheck"))
        self.gridLayout_2.addWidget(self.VaccumCollimatorValveCheck, 2, 5, 1, 1)
        self.VaccumValve1Label = QtGui.QLabel(self.vacuumValveGroup)
        self.VaccumValve1Label.setObjectName(_fromUtf8("VaccumValve1Label"))
        self.gridLayout_2.addWidget(self.VaccumValve1Label, 3, 0, 1, 1)
        self.VaccumValve7Read = TaurusLed(self.vacuumValveGroup)
        self.VaccumValve7Read.setMinimumSize(QtCore.QSize(15, 15))
        self.VaccumValve7Read.setMaximumSize(QtCore.QSize(15, 15))
        self.VaccumValve7Read.setObjectName(_fromUtf8("VaccumValve7Read"))
        self.gridLayout_2.addWidget(self.VaccumValve7Read, 9, 1, 1, 1)
        self.VaccumValve7Write = QtGui.QCheckBox(self.vacuumValveGroup)
        self.VaccumValve7Write.setObjectName(_fromUtf8("VaccumValve7Write"))
        self.gridLayout_2.addWidget(self.VaccumValve7Write, 9, 2, 1, 2)
        self.VaccumValve7Check = QtGui.QCheckBox(self.vacuumValveGroup)
        self.VaccumValve7Check.setText(_fromUtf8(""))
        self.VaccumValve7Check.setObjectName(_fromUtf8("VaccumValve7Check"))
        self.gridLayout_2.addWidget(self.VaccumValve7Check, 9, 5, 1, 1)
        self.VaccumValve6Read = TaurusLed(self.vacuumValveGroup)
        self.VaccumValve6Read.setMinimumSize(QtCore.QSize(15, 15))
        self.VaccumValve6Read.setMaximumSize(QtCore.QSize(15, 15))
        self.VaccumValve6Read.setObjectName(_fromUtf8("VaccumValve6Read"))
        self.gridLayout_2.addWidget(self.VaccumValve6Read, 8, 1, 1, 1)
        self.VaccumValve6Check = QtGui.QCheckBox(self.vacuumValveGroup)
        self.VaccumValve6Check.setText(_fromUtf8(""))
        self.VaccumValve6Check.setObjectName(_fromUtf8("VaccumValve6Check"))
        self.gridLayout_2.addWidget(self.VaccumValve6Check, 8, 5, 1, 1)
        self.VaccumValve7Label = QtGui.QLabel(self.vacuumValveGroup)
        self.VaccumValve7Label.setObjectName(_fromUtf8("VaccumValve7Label"))
        self.gridLayout_2.addWidget(self.VaccumValve7Label, 9, 0, 1, 1)
        self.VaccumValve6Label = QtGui.QLabel(self.vacuumValveGroup)
        self.VaccumValve6Label.setObjectName(_fromUtf8("VaccumValve6Label"))
        self.gridLayout_2.addWidget(self.VaccumValve6Label, 8, 0, 1, 1)
        self.VaccumValve3Check = QtGui.QCheckBox(self.vacuumValveGroup)
        self.VaccumValve3Check.setText(_fromUtf8(""))
        self.VaccumValve3Check.setObjectName(_fromUtf8("VaccumValve3Check"))
        self.gridLayout_2.addWidget(self.VaccumValve3Check, 5, 5, 1, 1)
        self.VaccumValve4Label = QtGui.QLabel(self.vacuumValveGroup)
        self.VaccumValve4Label.setObjectName(_fromUtf8("VaccumValve4Label"))
        self.gridLayout_2.addWidget(self.VaccumValve4Label, 6, 0, 1, 1)
        self.VaccumCollimatorValveLabel = QtGui.QLabel(self.vacuumValveGroup)
        self.VaccumCollimatorValveLabel.setObjectName(_fromUtf8("VaccumCollimatorValveLabel"))
        self.gridLayout_2.addWidget(self.VaccumCollimatorValveLabel, 2, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 10, 1, 1, 1)
        self.PresentTitle = QtGui.QLabel(self.vacuumValveGroup)
        self.PresentTitle.setObjectName(_fromUtf8("PresentTitle"))
        self.gridLayout_2.addWidget(self.PresentTitle, 1, 1, 1, 1)
        self.SaveRetrieveTitle = QtGui.QLabel(self.vacuumValveGroup)
        self.SaveRetrieveTitle.setObjectName(_fromUtf8("SaveRetrieveTitle"))
        self.gridLayout_2.addWidget(self.SaveRetrieveTitle, 1, 2, 1, 1)
        self.line = QtGui.QFrame(self.vacuumValveGroup)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 2, 4, 8, 1)
        self.ToApplyTitle = QtGui.QCheckBox(self.vacuumValveGroup)
        self.ToApplyTitle.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.ToApplyTitle.setObjectName(_fromUtf8("ToApplyTitle"))
        self.gridLayout_2.addWidget(self.ToApplyTitle, 1, 5, 1, 1)
        self.gridLayout.addWidget(self.vacuumValveGroup, 1, 0, 1, 1)

        self.retranslateUi(vacuumValveSnapshot)
        QtCore.QMetaObject.connectSlotsByName(vacuumValveSnapshot)

    def retranslateUi(self, vacuumValveSnapshot):
        vacuumValveSnapshot.setWindowTitle(QtGui.QApplication.translate("vacuumValveSnapshot", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.vacuumValveGroup.setTitle(QtGui.QApplication.translate("vacuumValveSnapshot", "Vacuum Valves", None, QtGui.QApplication.UnicodeUTF8))
        self.VaccumValve3Write.setText(QtGui.QApplication.translate("vacuumValveSnapshot", "open/close", None, QtGui.QApplication.UnicodeUTF8))
        self.VaccumValve5Label.setText(QtGui.QApplication.translate("vacuumValveSnapshot", "Valve 5", None, QtGui.QApplication.UnicodeUTF8))
        self.VaccumValve1Write.setText(QtGui.QApplication.translate("vacuumValveSnapshot", "open/close", None, QtGui.QApplication.UnicodeUTF8))
        self.VaccumValve2Label.setText(QtGui.QApplication.translate("vacuumValveSnapshot", "Valve 2", None, QtGui.QApplication.UnicodeUTF8))
        self.VaccumValve6Write.setText(QtGui.QApplication.translate("vacuumValveSnapshot", "open/close", None, QtGui.QApplication.UnicodeUTF8))
        self.VaccumValve2Write.setText(QtGui.QApplication.translate("vacuumValveSnapshot", "open/close", None, QtGui.QApplication.UnicodeUTF8))
        self.VaccumCollimatorValveWrite.setText(QtGui.QApplication.translate("vacuumValveSnapshot", "open/close", None, QtGui.QApplication.UnicodeUTF8))
        self.VaccumValve5Write.setText(QtGui.QApplication.translate("vacuumValveSnapshot", "open/close", None, QtGui.QApplication.UnicodeUTF8))
        self.VaccumValve3Label.setText(QtGui.QApplication.translate("vacuumValveSnapshot", "Valve 3", None, QtGui.QApplication.UnicodeUTF8))
        self.VaccumValve4Write.setText(QtGui.QApplication.translate("vacuumValveSnapshot", "open/close", None, QtGui.QApplication.UnicodeUTF8))
        self.VaccumValve1Label.setText(QtGui.QApplication.translate("vacuumValveSnapshot", "Valve 1", None, QtGui.QApplication.UnicodeUTF8))
        self.VaccumValve7Write.setText(QtGui.QApplication.translate("vacuumValveSnapshot", "open/close", None, QtGui.QApplication.UnicodeUTF8))
        self.VaccumValve7Label.setText(QtGui.QApplication.translate("vacuumValveSnapshot", "Valve 7", None, QtGui.QApplication.UnicodeUTF8))
        self.VaccumValve6Label.setText(QtGui.QApplication.translate("vacuumValveSnapshot", "Valve 6", None, QtGui.QApplication.UnicodeUTF8))
        self.VaccumValve4Label.setText(QtGui.QApplication.translate("vacuumValveSnapshot", "Valve 4", None, QtGui.QApplication.UnicodeUTF8))
        self.VaccumCollimatorValveLabel.setText(QtGui.QApplication.translate("vacuumValveSnapshot", "Collimator Valve", None, QtGui.QApplication.UnicodeUTF8))
        self.PresentTitle.setText(QtGui.QApplication.translate("vacuumValveSnapshot", "Present value", None, QtGui.QApplication.UnicodeUTF8))
        self.SaveRetrieveTitle.setText(QtGui.QApplication.translate("vacuumValveSnapshot", "Save/Retrieve", None, QtGui.QApplication.UnicodeUTF8))
        self.ToApplyTitle.setText(QtGui.QApplication.translate("vacuumValveSnapshot", "All", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.display import TaurusLed
from taurus.qt.qtgui.container import TaurusGroupBox
from taurus.qt.qtgui.panel import TaurusWidget