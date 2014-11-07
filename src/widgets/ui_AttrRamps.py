# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/ui/AttrRamps.ui'
#
# Created: Fri Nov  7 09:35:06 2014
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
        AttrRamps.resize(765, 810)
        self.gridLayout_2 = QtGui.QGridLayout(AttrRamps)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.scrollArea = QtGui.QScrollArea(AttrRamps)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 751, 796))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.KA2_HV = TaurusForm(self.scrollAreaWidgetContents)
        self.KA2_HV.setObjectName(_fromUtf8("KA2_HV"))
        self.gridLayout.addWidget(self.KA2_HV, 2, 0, 1, 1)
        self.GUN_HV = TaurusForm(self.scrollAreaWidgetContents)
        self.GUN_HV.setObjectName(_fromUtf8("GUN_HV"))
        self.gridLayout.addWidget(self.GUN_HV, 0, 0, 1, 1)
        self.KA1_HV = TaurusForm(self.scrollAreaWidgetContents)
        self.KA1_HV.setObjectName(_fromUtf8("KA1_HV"))
        self.gridLayout.addWidget(self.KA1_HV, 1, 0, 1, 1)
        self.GUN_HV_Setpoint = TaurusTrend(self.scrollAreaWidgetContents)
        self.GUN_HV_Setpoint.setObjectName(_fromUtf8("GUN_HV_Setpoint"))
        self.gridLayout.addWidget(self.GUN_HV_Setpoint, 0, 1, 1, 1)
        self.KA1_HV_Setpoint = TaurusTrend(self.scrollAreaWidgetContents)
        self.KA1_HV_Setpoint.setObjectName(_fromUtf8("KA1_HV_Setpoint"))
        self.gridLayout.addWidget(self.KA1_HV_Setpoint, 1, 1, 1, 1)
        self.KA2_HV_Setpoint = TaurusTrend(self.scrollAreaWidgetContents)
        self.KA2_HV_Setpoint.setObjectName(_fromUtf8("KA2_HV_Setpoint"))
        self.gridLayout.addWidget(self.KA2_HV_Setpoint, 2, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(AttrRamps)
        QtCore.QMetaObject.connectSlotsByName(AttrRamps)

    def retranslateUi(self, AttrRamps):
        AttrRamps.setWindowTitle(QtGui.QApplication.translate("AttrRamps", "Configure ramps", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.panel import TaurusWidget, TaurusForm
from taurus.qt.qtgui.plot import TaurusTrend
