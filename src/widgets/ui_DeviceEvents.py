# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/ui/DeviceEvents.ui'
#
# Created: Wed Nov 12 11:23:34 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_deviceEvents(object):
    def setupUi(self, deviceEvents):
        deviceEvents.setObjectName(_fromUtf8("deviceEvents"))
        deviceEvents.resize(1024, 224)
        self.gridLayout = QtGui.QGridLayout(deviceEvents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.scrollArea = QtGui.QScrollArea(deviceEvents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 995, 1020))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.splitter = QtGui.QSplitter(self.scrollAreaWidgetContents)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.eventsplc1 = TaurusPlot(self.splitter)
        self.eventsplc1.setObjectName(_fromUtf8("eventsplc1"))
        self.eventsplc2 = TaurusPlot(self.splitter)
        self.eventsplc2.setObjectName(_fromUtf8("eventsplc2"))
        self.eventsplc3 = TaurusPlot(self.splitter)
        self.eventsplc3.setObjectName(_fromUtf8("eventsplc3"))
        self.eventsplc4 = TaurusPlot(self.splitter)
        self.eventsplc4.setObjectName(_fromUtf8("eventsplc4"))
        self.eventsplc5 = TaurusPlot(self.splitter)
        self.eventsplc5.setObjectName(_fromUtf8("eventsplc5"))
        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(deviceEvents)
        QtCore.QMetaObject.connectSlotsByName(deviceEvents)

    def retranslateUi(self, deviceEvents):
        deviceEvents.setWindowTitle(QtGui.QApplication.translate("deviceEvents", "Plc Devices Events", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.panel import TaurusWidget
from taurus.qt.qtgui.plot import TaurusPlot
