# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/ui/linacConfigurationScreen.ui'
#
# Created: Mon Mar 16 10:40:53 2015
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
        linacConfigurationScreen.resize(950, 950)
        linacConfigurationScreen.setMinimumSize(QtCore.QSize(0, 0))
        self.gridLayout_3 = QtGui.QGridLayout(linacConfigurationScreen)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.centralFrame = QtGui.QFrame(linacConfigurationScreen)
        self.centralFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.centralFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.centralFrame.setObjectName(_fromUtf8("centralFrame"))
        self.gridLayout = QtGui.QGridLayout(self.centralFrame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.scrollArea = QtGui.QScrollArea(self.centralFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 922, 867))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.magnetSnapshot = magnetSnapshot(self.scrollAreaWidgetContents)
        self.magnetSnapshot.setObjectName(_fromUtf8("magnetSnapshot"))
        self.gridLayout_2.addWidget(self.magnetSnapshot, 0, 2, 6, 1)
        self.electronGunSnapshot = electronGunSnapshot(self.scrollAreaWidgetContents)
        self.electronGunSnapshot.setObjectName(_fromUtf8("electronGunSnapshot"))
        self.gridLayout_2.addWidget(self.electronGunSnapshot, 1, 0, 1, 1)
        self.klystronSnapshot = klystronSnapshot(self.scrollAreaWidgetContents)
        self.klystronSnapshot.setObjectName(_fromUtf8("klystronSnapshot"))
        self.gridLayout_2.addWidget(self.klystronSnapshot, 4, 0, 1, 1)
        self.radioFrequencySnapshot = radioFrequencySnapshot(self.scrollAreaWidgetContents)
        self.radioFrequencySnapshot.setObjectName(_fromUtf8("radioFrequencySnapshot"))
        self.gridLayout_2.addWidget(self.radioFrequencySnapshot, 0, 3, 1, 1)
        self.timingSnapshot = timingSnapshot(self.scrollAreaWidgetContents)
        self.timingSnapshot.setObjectName(_fromUtf8("timingSnapshot"))
        self.gridLayout_2.addWidget(self.timingSnapshot, 0, 0, 1, 1)
        self.coolingLoopSnapshot = coolingLoopSnapshot(self.scrollAreaWidgetContents)
        self.coolingLoopSnapshot.setObjectName(_fromUtf8("coolingLoopSnapshot"))
        self.gridLayout_2.addWidget(self.coolingLoopSnapshot, 3, 0, 1, 1)
        self.commentGroup = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.commentGroup.setMaximumSize(QtCore.QSize(350, 16777215))
        self.commentGroup.setObjectName(_fromUtf8("commentGroup"))
        self.gridLayout_4 = QtGui.QGridLayout(self.commentGroup)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.splitter = QtGui.QSplitter(self.commentGroup)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.textToSaveLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.textToSaveLayout.setMargin(0)
        self.textToSaveLayout.setObjectName(_fromUtf8("textToSaveLayout"))
        self.textToSaveLabel = QtGui.QLabel(self.layoutWidget)
        self.textToSaveLabel.setObjectName(_fromUtf8("textToSaveLabel"))
        self.textToSaveLayout.addWidget(self.textToSaveLabel)
        self.textToSave = QtGui.QTextEdit(self.layoutWidget)
        self.textToSave.setMaximumSize(QtCore.QSize(350, 16777215))
        self.textToSave.setObjectName(_fromUtf8("textToSave"))
        self.textToSaveLayout.addWidget(self.textToSave)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.textLoadedLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.textLoadedLayout.setMargin(0)
        self.textLoadedLayout.setObjectName(_fromUtf8("textLoadedLayout"))
        self.textLoadedLabel = QtGui.QLabel(self.layoutWidget1)
        self.textLoadedLabel.setObjectName(_fromUtf8("textLoadedLabel"))
        self.textLoadedLayout.addWidget(self.textLoadedLabel)
        self.textLoaded = QtGui.QTextEdit(self.layoutWidget1)
        self.textLoaded.setReadOnly(True)
        self.textLoaded.setObjectName(_fromUtf8("textLoaded"))
        self.textLoadedLayout.addWidget(self.textLoaded)
        self.gridLayout_4.addWidget(self.splitter, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.commentGroup, 1, 3, 5, 1)
        self.vacuumValveSnapshot = vacuumValveSnapshot(self.scrollAreaWidgetContents)
        self.vacuumValveSnapshot.setObjectName(_fromUtf8("vacuumValveSnapshot"))
        self.gridLayout_2.addWidget(self.vacuumValveSnapshot, 2, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(self.centralFrame)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Open|QtGui.QDialogButtonBox.Reset|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.progressBar = QtGui.QProgressBar(self.centralFrame)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout.addWidget(self.progressBar, 2, 0, 1, 1)
        self.gridLayout_3.addWidget(self.centralFrame, 0, 0, 1, 1)

        self.retranslateUi(linacConfigurationScreen)
        QtCore.QMetaObject.connectSlotsByName(linacConfigurationScreen)

    def retranslateUi(self, linacConfigurationScreen):
        linacConfigurationScreen.setWindowTitle(QtGui.QApplication.translate("linacConfigurationScreen", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.commentGroup.setTitle(QtGui.QApplication.translate("linacConfigurationScreen", "Comments", None, QtGui.QApplication.UnicodeUTF8))
        self.textToSaveLabel.setText(QtGui.QApplication.translate("linacConfigurationScreen", "Current comment:", None, QtGui.QApplication.UnicodeUTF8))
        self.textLoadedLabel.setText(QtGui.QApplication.translate("linacConfigurationScreen", "Old comment:", None, QtGui.QApplication.UnicodeUTF8))

from timingsnapshot import timingSnapshot
from vacuumvalvesnapshot import vacuumValveSnapshot
from electrongunsnapshot import electronGunSnapshot
from radiofrequencysnapshot import radioFrequencySnapshot
from taurus.qt.qtgui.panel import TaurusWidget
from klystronsnapshot import klystronSnapshot
from magnetsnapshot import magnetSnapshot
from coolingloopsnapshot import coolingLoopSnapshot
