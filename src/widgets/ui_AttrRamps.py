# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/ui/AttrRamps.ui'
#
# Created: Wed Nov 26 15:06:21 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AttrRamps(object):
    def setupUi(self, AttrRamps):
        AttrRamps.setObjectName(_fromUtf8("AttrRamps"))
        AttrRamps.resize(510, 250)
        self.gridLayout_2 = QtGui.QGridLayout(AttrRamps)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.scrollArea = QtGui.QScrollArea(AttrRamps)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 496, 236))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter = QtGui.QSplitter(self.scrollAreaWidgetContents)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.AttributesForm = TaurusForm(self.splitter)
        self.AttributesForm.setObjectName(_fromUtf8("AttributesForm"))
        self.AttributesPlot = TaurusTrend(self.splitter)
        self.AttributesPlot.setObjectName(_fromUtf8("AttributesPlot"))
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(AttrRamps)
        QtCore.QMetaObject.connectSlotsByName(AttrRamps)

    def retranslateUi(self, AttrRamps):
        AttrRamps.setWindowTitle(QtGui.QApplication.translate("AttrRamps", "Configure ramps", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.panel import TaurusWidget, TaurusForm
from taurus.qt.qtgui.plot import TaurusTrend
