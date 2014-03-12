# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/ui/linacConfigurationScreen.ui'
#
# Created: Wed Mar 12 08:59:44 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_linacConfigurationScreen(object):
    def setupUi(self, linacConfigurationScreen):
        linacConfigurationScreen.setObjectName(_fromUtf8("linacConfigurationScreen"))
        linacConfigurationScreen.resize(1250, 825)
        self.gridLayout = QtGui.QGridLayout(linacConfigurationScreen)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonBox = QtGui.QDialogButtonBox(linacConfigurationScreen)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Open|QtGui.QDialogButtonBox.Reset|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.scrollArea = QtGui.QScrollArea(linacConfigurationScreen)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1445, 816))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.timingSnapshot = timingSnapshot(self.scrollAreaWidgetContents)
        self.timingSnapshot.setObjectName(_fromUtf8("timingSnapshot"))
        self.gridLayout_2.addWidget(self.timingSnapshot, 1, 2, 1, 1)
        self.magnetSnapshot = magnetSnapshot(self.scrollAreaWidgetContents)
        self.magnetSnapshot.setObjectName(_fromUtf8("magnetSnapshot"))
        self.gridLayout_2.addWidget(self.magnetSnapshot, 0, 1, 5, 1)
        self.coolingLoopSnapshot = coolingLoopSnapshot(self.scrollAreaWidgetContents)
        self.coolingLoopSnapshot.setObjectName(_fromUtf8("coolingLoopSnapshot"))
        self.gridLayout_2.addWidget(self.coolingLoopSnapshot, 1, 0, 1, 1)
        self.radioFrequencySnapshot = radioFrequencySnapshot(self.scrollAreaWidgetContents)
        self.radioFrequencySnapshot.setObjectName(_fromUtf8("radioFrequencySnapshot"))
        self.gridLayout_2.addWidget(self.radioFrequencySnapshot, 0, 2, 1, 1)
        self.electronGunSnapshot = electronGunSnapshot(self.scrollAreaWidgetContents)
        self.electronGunSnapshot.setObjectName(_fromUtf8("electronGunSnapshot"))
        self.gridLayout_2.addWidget(self.electronGunSnapshot, 0, 0, 1, 1)
        self.klystronSnapshot = klystronSnapshot(self.scrollAreaWidgetContents)
        self.klystronSnapshot.setObjectName(_fromUtf8("klystronSnapshot"))
        self.gridLayout_2.addWidget(self.klystronSnapshot, 2, 2, 1, 1)
        self.vacuumValveSnapshot = vacuumValveSnapshot(self.scrollAreaWidgetContents)
        self.vacuumValveSnapshot.setObjectName(_fromUtf8("vacuumValveSnapshot"))
        self.gridLayout_2.addWidget(self.vacuumValveSnapshot, 2, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)

        self.retranslateUi(linacConfigurationScreen)
        QtCore.QMetaObject.connectSlotsByName(linacConfigurationScreen)

    def retranslateUi(self, linacConfigurationScreen):
        linacConfigurationScreen.setWindowTitle(QtGui.QApplication.translate("linacConfigurationScreen", "Form", None, QtGui.QApplication.UnicodeUTF8))

from timingsnapshot import timingSnapshot
from vacuumvalvesnapshot import vacuumValveSnapshot
from electrongunsnapshot import electronGunSnapshot
from radiofrequencysnapshot import radioFrequencySnapshot
from taurus.qt.qtgui.panel import TaurusWidget
from magnetsnapshot import magnetSnapshot
from klystronsnapshot import klystronSnapshot
from coolingloopsnapshot import coolingLoopSnapshot
