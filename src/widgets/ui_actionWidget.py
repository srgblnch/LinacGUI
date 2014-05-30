# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/ui/actionWidget.ui'
#
# Created: Thu May 29 15:11:49 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_actionForm(object):
    def setupUi(self, actionForm):
        actionForm.setObjectName(_fromUtf8("actionForm"))
        actionForm.resize(86, 41)
        self.gridLayout_2 = QtGui.QGridLayout(actionForm)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.actionFrame = QtGui.QFrame(actionForm)
        self.actionFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.actionFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.actionFrame.setObjectName(_fromUtf8("actionFrame"))
        self.gridLayout = QtGui.QGridLayout(self.actionFrame)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Check = LinacValueCheckBox(self.actionFrame)
        self.Check.setMinimumSize(QtCore.QSize(30, 0))
        self.Check.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Check.setShowText(True)
        self.Check.setObjectName(_fromUtf8("Check"))
        self.gridLayout.addWidget(self.Check, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.Led = TaurusLed(self.actionFrame)
        self.Led.setMinimumSize(QtCore.QSize(15, 15))
        self.Led.setMaximumSize(QtCore.QSize(15, 15))
        self.Led.setObjectName(_fromUtf8("Led"))
        self.gridLayout.addWidget(self.Led, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.Label = QtGui.QLabel(self.actionFrame)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.Label.setFont(font)
        self.Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Label.setObjectName(_fromUtf8("Label"))
        self.gridLayout.addWidget(self.Label, 1, 0, 1, 4)
        self.gridLayout_2.addWidget(self.actionFrame, 0, 0, 1, 1)

        self.retranslateUi(actionForm)
        QtCore.QMetaObject.connectSlotsByName(actionForm)

    def retranslateUi(self, actionForm):
        actionForm.setWindowTitle(QtGui.QApplication.translate("actionForm", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.Label.setText(QtGui.QApplication.translate("actionForm", "true/false", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.display import TaurusLed
from taurus.qt.qtgui.panel import TaurusWidget
from linacvaluecheckbox import LinacValueCheckBox
