# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/ui/AttrRamps.ui'
#
# Created: Fri Nov 14 12:45:45 2014
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
        AttrRamps.resize(1024, 906)
        self.gridLayout_2 = QtGui.QGridLayout(AttrRamps)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.scrollArea = QtGui.QScrollArea(AttrRamps)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1010, 892))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter = QtGui.QSplitter(self.scrollAreaWidgetContents)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.Filament_LV_splitter = QtGui.QSplitter(self.splitter)
        self.Filament_LV_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.Filament_LV_splitter.setObjectName(_fromUtf8("Filament_LV_splitter"))
        self.Filament_LV = TaurusForm(self.Filament_LV_splitter)
        self.Filament_LV.setObjectName(_fromUtf8("Filament_LV"))
        self.Filament_LV_Setpoint = TaurusTrend(self.Filament_LV_splitter)
        self.Filament_LV_Setpoint.setObjectName(_fromUtf8("Filament_LV_Setpoint"))
        self.GUN_HV_splitter = QtGui.QSplitter(self.splitter)
        self.GUN_HV_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.GUN_HV_splitter.setObjectName(_fromUtf8("GUN_HV_splitter"))
        self.GUN_HV = TaurusForm(self.GUN_HV_splitter)
        self.GUN_HV.setObjectName(_fromUtf8("GUN_HV"))
        self.GUN_HV_Setpoint = TaurusTrend(self.GUN_HV_splitter)
        self.GUN_HV_Setpoint.setObjectName(_fromUtf8("GUN_HV_Setpoint"))
        self.KA1_HV_splitter = QtGui.QSplitter(self.splitter)
        self.KA1_HV_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.KA1_HV_splitter.setObjectName(_fromUtf8("KA1_HV_splitter"))
        self.KA1_HV = TaurusForm(self.KA1_HV_splitter)
        self.KA1_HV.setObjectName(_fromUtf8("KA1_HV"))
        self.KA1_HV_Setpoint = TaurusTrend(self.KA1_HV_splitter)
        self.KA1_HV_Setpoint.setObjectName(_fromUtf8("KA1_HV_Setpoint"))
        self.KA2_HV_splitter = QtGui.QSplitter(self.splitter)
        self.KA2_HV_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.KA2_HV_splitter.setObjectName(_fromUtf8("KA2_HV_splitter"))
        self.KA2_HV = TaurusForm(self.KA2_HV_splitter)
        self.KA2_HV.setObjectName(_fromUtf8("KA2_HV"))
        self.KA2_HV_Setpoint = TaurusTrend(self.KA2_HV_splitter)
        self.KA2_HV_Setpoint.setObjectName(_fromUtf8("KA2_HV_Setpoint"))
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(AttrRamps)
        QtCore.QMetaObject.connectSlotsByName(AttrRamps)

    def retranslateUi(self, AttrRamps):
        AttrRamps.setWindowTitle(QtGui.QApplication.translate("AttrRamps", "Configure ramps", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.panel import TaurusWidget, TaurusForm
from taurus.qt.qtgui.plot import TaurusTrend
