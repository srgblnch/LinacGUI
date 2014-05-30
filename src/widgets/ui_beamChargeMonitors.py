# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/ui/beamChargeMonitors.ui'
#
# Created: Fri May 30 15:03:11 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_beamChargeMonitors(object):
    def setupUi(self, beamChargeMonitors):
        beamChargeMonitors.setObjectName(_fromUtf8("beamChargeMonitors"))
        beamChargeMonitors.resize(170, 104)
        self.gridLayout_2 = QtGui.QGridLayout(beamChargeMonitors)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.beamChargeMonitorsGroup = TaurusGroupBox(beamChargeMonitors)
        self.beamChargeMonitorsGroup.setObjectName(_fromUtf8("beamChargeMonitorsGroup"))
        self.gridLayout = QtGui.QGridLayout(self.beamChargeMonitorsGroup)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.liLabel = QtGui.QLabel(self.beamChargeMonitorsGroup)
        self.liLabel.setMaximumSize(QtCore.QSize(40, 16777215))
        self.liLabel.setObjectName(_fromUtf8("liLabel"))
        self.gridLayout.addWidget(self.liLabel, 0, 0, 1, 1)
        self.liValue = TaurusLabel(self.beamChargeMonitorsGroup)
        self.liValue.setObjectName(_fromUtf8("liValue"))
        self.gridLayout.addWidget(self.liValue, 0, 1, 1, 1)
        self.lt01Label = QtGui.QLabel(self.beamChargeMonitorsGroup)
        self.lt01Label.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lt01Label.setObjectName(_fromUtf8("lt01Label"))
        self.gridLayout.addWidget(self.lt01Label, 1, 0, 1, 1)
        self.lt01Value = TaurusLabel(self.beamChargeMonitorsGroup)
        self.lt01Value.setObjectName(_fromUtf8("lt01Value"))
        self.gridLayout.addWidget(self.lt01Value, 1, 1, 1, 1)
        self.lt02Label = QtGui.QLabel(self.beamChargeMonitorsGroup)
        self.lt02Label.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lt02Label.setObjectName(_fromUtf8("lt02Label"))
        self.gridLayout.addWidget(self.lt02Label, 2, 0, 1, 1)
        self.lt02Value = TaurusLabel(self.beamChargeMonitorsGroup)
        self.lt02Value.setObjectName(_fromUtf8("lt02Value"))
        self.gridLayout.addWidget(self.lt02Value, 2, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        self.gridLayout_2.addWidget(self.beamChargeMonitorsGroup, 0, 0, 1, 1)

        self.retranslateUi(beamChargeMonitors)
        QtCore.QMetaObject.connectSlotsByName(beamChargeMonitors)

    def retranslateUi(self, beamChargeMonitors):
        beamChargeMonitors.setWindowTitle(QtGui.QApplication.translate("beamChargeMonitors", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.beamChargeMonitorsGroup.setTitle(QtGui.QApplication.translate("beamChargeMonitors", "Beam Charge Monitors", None, QtGui.QApplication.UnicodeUTF8))
        self.liLabel.setText(QtGui.QApplication.translate("beamChargeMonitors", "Linac", None, QtGui.QApplication.UnicodeUTF8))
        self.lt01Label.setText(QtGui.QApplication.translate("beamChargeMonitors", "LT01", None, QtGui.QApplication.UnicodeUTF8))
        self.lt02Label.setText(QtGui.QApplication.translate("beamChargeMonitors", "LT02", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.display import TaurusLabel
from taurus.qt.qtgui.container import TaurusGroupBox
from taurus.qt.qtgui.panel import TaurusWidget
