# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/ui/magnet.ui'
#
# Created: Thu Nov 27 12:42:27 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_magnet(object):
    def setupUi(self, magnet):
        magnet.setObjectName(_fromUtf8("magnet"))
        magnet.resize(208, 104)
        self.gridLayout = QtGui.QGridLayout(magnet)
        self.gridLayout.setMargin(1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.magnetGroup = TaurusGroupBox(magnet)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.magnetGroup.setFont(font)
        self.magnetGroup.setObjectName(_fromUtf8("magnetGroup"))
        self.gridLayout_2 = QtGui.QGridLayout(self.magnetGroup)
        self.gridLayout_2.setMargin(2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLabel = QtGui.QLabel(self.magnetGroup)
        self.horizontalLabel.setMinimumSize(QtCore.QSize(30, 0))
        self.horizontalLabel.setObjectName(_fromUtf8("horizontalLabel"))
        self.gridLayout_2.addWidget(self.horizontalLabel, 0, 0, 1, 1)
        self.horizontalStatus = TaurusLabel(self.magnetGroup)
        self.horizontalStatus.setMinimumSize(QtCore.QSize(100, 15))
        self.horizontalStatus.setObjectName(_fromUtf8("horizontalStatus"))
        self.gridLayout_2.addWidget(self.horizontalStatus, 0, 2, 1, 1)
        self.focusValue = TaurusLabel(self.magnetGroup)
        self.focusValue.setMinimumSize(QtCore.QSize(60, 15))
        self.focusValue.setObjectName(_fromUtf8("focusValue"))
        self.gridLayout_2.addWidget(self.focusValue, 2, 1, 1, 1)
        self.focusLabel = QtGui.QLabel(self.magnetGroup)
        self.focusLabel.setMinimumSize(QtCore.QSize(25, 0))
        self.focusLabel.setObjectName(_fromUtf8("focusLabel"))
        self.gridLayout_2.addWidget(self.focusLabel, 2, 0, 1, 1)
        self.verticalLabel = QtGui.QLabel(self.magnetGroup)
        self.verticalLabel.setMinimumSize(QtCore.QSize(30, 0))
        self.verticalLabel.setObjectName(_fromUtf8("verticalLabel"))
        self.gridLayout_2.addWidget(self.verticalLabel, 1, 0, 1, 1)
        self.verticalValue = TaurusLabel(self.magnetGroup)
        self.verticalValue.setMinimumSize(QtCore.QSize(60, 15))
        self.verticalValue.setObjectName(_fromUtf8("verticalValue"))
        self.gridLayout_2.addWidget(self.verticalValue, 1, 1, 1, 1)
        self.focusStatus = TaurusLabel(self.magnetGroup)
        self.focusStatus.setMinimumSize(QtCore.QSize(100, 15))
        self.focusStatus.setObjectName(_fromUtf8("focusStatus"))
        self.gridLayout_2.addWidget(self.focusStatus, 2, 2, 1, 1)
        self.horizontalValue = TaurusLabel(self.magnetGroup)
        self.horizontalValue.setMinimumSize(QtCore.QSize(60, 15))
        self.horizontalValue.setObjectName(_fromUtf8("horizontalValue"))
        self.gridLayout_2.addWidget(self.horizontalValue, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 4, 1, 1, 1)
        self.verticalStatus = TaurusLabel(self.magnetGroup)
        self.verticalStatus.setMinimumSize(QtCore.QSize(100, 15))
        self.verticalStatus.setObjectName(_fromUtf8("verticalStatus"))
        self.gridLayout_2.addWidget(self.verticalStatus, 1, 2, 1, 1)
        self.focus2Label = QtGui.QLabel(self.magnetGroup)
        self.focus2Label.setMinimumSize(QtCore.QSize(25, 0))
        self.focus2Label.setObjectName(_fromUtf8("focus2Label"))
        self.gridLayout_2.addWidget(self.focus2Label, 3, 0, 1, 1)
        self.focus2Value = TaurusLabel(self.magnetGroup)
        self.focus2Value.setMinimumSize(QtCore.QSize(60, 15))
        self.focus2Value.setObjectName(_fromUtf8("focus2Value"))
        self.gridLayout_2.addWidget(self.focus2Value, 3, 1, 1, 1)
        self.focus2Status = TaurusLabel(self.magnetGroup)
        self.focus2Status.setMinimumSize(QtCore.QSize(100, 15))
        self.focus2Status.setObjectName(_fromUtf8("focus2Status"))
        self.gridLayout_2.addWidget(self.focus2Status, 3, 2, 1, 1)
        self.gridLayout.addWidget(self.magnetGroup, 0, 0, 1, 1)

        self.retranslateUi(magnet)
        QtCore.QMetaObject.connectSlotsByName(magnet)

    def retranslateUi(self, magnet):
        magnet.setWindowTitle(QtGui.QApplication.translate("magnet", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.magnetGroup.setTitle(QtGui.QApplication.translate("magnet", "magnet", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalLabel.setText(QtGui.QApplication.translate("magnet", "__NH", None, QtGui.QApplication.UnicodeUTF8))
        self.focusLabel.setText(QtGui.QApplication.translate("magnet", "__NF", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLabel.setText(QtGui.QApplication.translate("magnet", "__NV", None, QtGui.QApplication.UnicodeUTF8))
        self.focus2Label.setText(QtGui.QApplication.translate("magnet", "__NF", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.display import TaurusLabel
from taurus.qt.qtgui.container import TaurusGroupBox
from taurus.qt.qtgui.panel import TaurusWidget
