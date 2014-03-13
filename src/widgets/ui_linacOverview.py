# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/linacOverview.ui'
#
# Created: Thu Mar 13 11:21:00 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_linacOverview(object):
    def setupUi(self, linacOverview):
        linacOverview.setObjectName(_fromUtf8("linacOverview"))
        linacOverview.resize(308, 330)
        self.gridLayout_2 = QtGui.QGridLayout(linacOverview)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.moveLocal = TaurusCommandButton(linacOverview)
        self.moveLocal.setObjectName(_fromUtf8("moveLocal"))
        self.gridLayout_2.addWidget(self.moveLocal, 3, 1, 1, 1)
        self.moveRemote = TaurusCommandButton(linacOverview)
        self.moveRemote.setObjectName(_fromUtf8("moveRemote"))
        self.gridLayout_2.addWidget(self.moveRemote, 3, 2, 1, 1)
        self.resetInstance = TaurusCommandButton(linacOverview)
        self.resetInstance.setObjectName(_fromUtf8("resetInstance"))
        self.gridLayout_2.addWidget(self.resetInstance, 4, 1, 1, 2)
        self.AllInstancesLocationLabel = QtGui.QLabel(linacOverview)
        self.AllInstancesLocationLabel.setObjectName(_fromUtf8("AllInstancesLocationLabel"))
        self.gridLayout_2.addWidget(self.AllInstancesLocationLabel, 3, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.plcLastUpdateTrend = TaurusTrend(linacOverview)
        self.plcLastUpdateTrend.setObjectName(_fromUtf8("plcLastUpdateTrend"))
        self.gridLayout_2.addWidget(self.plcLastUpdateTrend, 2, 0, 1, 3)
        self.plcLastUpdateLabel = QtGui.QLabel(linacOverview)
        self.plcLastUpdateLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.plcLastUpdateLabel.setObjectName(_fromUtf8("plcLastUpdateLabel"))
        self.gridLayout_2.addWidget(self.plcLastUpdateLabel, 1, 0, 1, 3)

        self.retranslateUi(linacOverview)
        QtCore.QMetaObject.connectSlotsByName(linacOverview)

    def retranslateUi(self, linacOverview):
        linacOverview.setWindowTitle(QtGui.QApplication.translate("linacOverview", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.AllInstancesLocationLabel.setText(QtGui.QApplication.translate("linacOverview", "All instances:", None, QtGui.QApplication.UnicodeUTF8))
        self.plcLastUpdateLabel.setText(QtGui.QApplication.translate("linacOverview", "PLCs update time", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.plot import TaurusTrend
from taurus.qt.qtgui.panel import TaurusWidget
from taurus.qt.qtgui.button import TaurusCommandButton
