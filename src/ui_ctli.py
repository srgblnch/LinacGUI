# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ctli.ui'
#
# Created: Wed Mar 12 09:00:59 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_linacGui(object):
    def setupUi(self, linacGui):
        linacGui.setObjectName(_fromUtf8("linacGui"))
        linacGui.resize(1325, 1000)
        self.gridLayout = QtGui.QGridLayout(linacGui)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.linacTabs = QtGui.QTabWidget(linacGui)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.linacTabs.setFont(font)
        self.linacTabs.setAutoFillBackground(False)
        self.linacTabs.setTabPosition(QtGui.QTabWidget.South)
        self.linacTabs.setTabShape(QtGui.QTabWidget.Rounded)
        self.linacTabs.setElideMode(QtCore.Qt.ElideMiddle)
        self.linacTabs.setObjectName(_fromUtf8("linacTabs"))
        self.communicationTab = QtGui.QWidget()
        self.communicationTab.setObjectName(_fromUtf8("communicationTab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.communicationTab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.communicationsScrollArea = QtGui.QScrollArea(self.communicationTab)
        self.communicationsScrollArea.setWidgetResizable(True)
        self.communicationsScrollArea.setObjectName(_fromUtf8("communicationsScrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 666, 676))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_3 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 1)
        self.plc1 = linacPlcWidget(self.scrollAreaWidgetContents)
        self.plc1.setObjectName(_fromUtf8("plc1"))
        self.gridLayout_3.addWidget(self.plc1, 1, 2, 1, 1)
        self.linacOverview = linacOverview(self.scrollAreaWidgetContents)
        self.linacOverview.setObjectName(_fromUtf8("linacOverview"))
        self.gridLayout_3.addWidget(self.linacOverview, 1, 1, 1, 1)
        self.plc4 = linacPlcWidget(self.scrollAreaWidgetContents)
        self.plc4.setObjectName(_fromUtf8("plc4"))
        self.gridLayout_3.addWidget(self.plc4, 2, 2, 1, 1)
        self.plc5 = linacPlcWidget(self.scrollAreaWidgetContents)
        self.plc5.setObjectName(_fromUtf8("plc5"))
        self.gridLayout_3.addWidget(self.plc5, 2, 3, 1, 1)
        self.plc2 = linacPlcWidget(self.scrollAreaWidgetContents)
        self.plc2.setObjectName(_fromUtf8("plc2"))
        self.gridLayout_3.addWidget(self.plc2, 1, 3, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 4, 1, 1)
        self.plc3 = linacPlcWidget(self.scrollAreaWidgetContents)
        self.plc3.setObjectName(_fromUtf8("plc3"))
        self.gridLayout_3.addWidget(self.plc3, 2, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 3, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem3, 0, 2, 1, 1)
        self.communicationsScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.communicationsScrollArea, 0, 0, 1, 1)
        self.linacTabs.addTab(self.communicationTab, _fromUtf8(""))
        self.startupTab = QtGui.QWidget()
        self.startupTab.setObjectName(_fromUtf8("startupTab"))
        self.gridLayout_4 = QtGui.QGridLayout(self.startupTab)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.startupScrollArea = QtGui.QScrollArea(self.startupTab)
        self.startupScrollArea.setWidgetResizable(True)
        self.startupScrollArea.setObjectName(_fromUtf8("startupScrollArea"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1266, 841))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.gridLayout_5 = QtGui.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        spacerItem4 = QtGui.QSpacerItem(20, 6, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem4, 0, 1, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(601, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem5, 1, 0, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(601, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem6, 1, 2, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(20, 6, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem7, 2, 1, 1, 1)
        self.linacStartupSynoptic = linacStartupSynoptic(self.scrollAreaWidgetContents_2)
        self.linacStartupSynoptic.setObjectName(_fromUtf8("linacStartupSynoptic"))
        self.gridLayout_5.addWidget(self.linacStartupSynoptic, 1, 1, 1, 1)
        self.startupScrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.addWidget(self.startupScrollArea, 1, 0, 1, 1)
        self.linacTabs.addTab(self.startupTab, _fromUtf8(""))
        self.mainscreenTab = QtGui.QWidget()
        self.mainscreenTab.setObjectName(_fromUtf8("mainscreenTab"))
        self.gridLayout_6 = QtGui.QGridLayout(self.mainscreenTab)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.mainscreenScrollArea = QtGui.QScrollArea(self.mainscreenTab)
        self.mainscreenScrollArea.setWidgetResizable(True)
        self.mainscreenScrollArea.setObjectName(_fromUtf8("mainscreenScrollArea"))
        self.scrollAreaWidgetContents_3 = QtGui.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 1266, 841))
        self.scrollAreaWidgetContents_3.setObjectName(_fromUtf8("scrollAreaWidgetContents_3"))
        self.gridLayout_7 = QtGui.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem8, 2, 1, 1, 1)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem9, 1, 0, 1, 1)
        self.linacMainscreenSynoptic = linacMainscreenSynoptic(self.scrollAreaWidgetContents_3)
        self.linacMainscreenSynoptic.setObjectName(_fromUtf8("linacMainscreenSynoptic"))
        self.gridLayout_7.addWidget(self.linacMainscreenSynoptic, 1, 1, 1, 1)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem10, 1, 2, 1, 1)
        spacerItem11 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem11, 0, 1, 1, 1)
        self.mainscreenScrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_6.addWidget(self.mainscreenScrollArea, 0, 0, 1, 1)
        self.linacTabs.addTab(self.mainscreenTab, _fromUtf8(""))
        self.configurationTab = QtGui.QWidget()
        self.configurationTab.setObjectName(_fromUtf8("configurationTab"))
        self.gridLayout_8 = QtGui.QGridLayout(self.configurationTab)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.linacConfigurationScreen = linacConfigurationScreen(self.configurationTab)
        self.linacConfigurationScreen.setObjectName(_fromUtf8("linacConfigurationScreen"))
        self.gridLayout_8.addWidget(self.linacConfigurationScreen, 0, 0, 1, 1)
        self.linacTabs.addTab(self.configurationTab, _fromUtf8(""))
        self.gridLayout.addWidget(self.linacTabs, 0, 0, 1, 1)

        self.retranslateUi(linacGui)
        self.linacTabs.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(linacGui)

    def retranslateUi(self, linacGui):
        linacGui.setWindowTitle(QtGui.QApplication.translate("linacGui", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.plc1.setModel(QtGui.QApplication.translate("linacGui", "li/ct/plc1", None, QtGui.QApplication.UnicodeUTF8))
        self.plc4.setModel(QtGui.QApplication.translate("linacGui", "li/ct/plc4", None, QtGui.QApplication.UnicodeUTF8))
        self.plc5.setModel(QtGui.QApplication.translate("linacGui", "li/ct/plc5", None, QtGui.QApplication.UnicodeUTF8))
        self.plc2.setModel(QtGui.QApplication.translate("linacGui", "li/ct/plc2", None, QtGui.QApplication.UnicodeUTF8))
        self.plc3.setModel(QtGui.QApplication.translate("linacGui", "li/ct/plc3", None, QtGui.QApplication.UnicodeUTF8))
        self.linacTabs.setTabText(self.linacTabs.indexOf(self.communicationTab), QtGui.QApplication.translate("linacGui", "Communication", None, QtGui.QApplication.UnicodeUTF8))
        self.linacTabs.setTabText(self.linacTabs.indexOf(self.startupTab), QtGui.QApplication.translate("linacGui", "Start up", None, QtGui.QApplication.UnicodeUTF8))
        self.linacTabs.setTabText(self.linacTabs.indexOf(self.mainscreenTab), QtGui.QApplication.translate("linacGui", "Main Screen", None, QtGui.QApplication.UnicodeUTF8))
        self.linacTabs.setTabText(self.linacTabs.indexOf(self.configurationTab), QtGui.QApplication.translate("linacGui", "Configuration", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.container import TaurusFrame
from linacplcwidget import linacPlcWidget
from linacstartupsynoptic import linacStartupSynoptic
from linacmainscreensynoptic import linacMainscreenSynoptic
from linacoverview import linacOverview
from linacconfigurationscreen import linacConfigurationScreen
