# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'klystron1interlocks.ui'
#
# Created: Mon Jan 20 15:03:14 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_k1itck(object):
    def setupUi(self, k1itck):
        k1itck.setObjectName(_fromUtf8("k1itck"))
        k1itck.resize(183, 144)
        self.gridLayout = QtGui.QGridLayout(k1itck)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.taurusGroupBox = TaurusGroupBox(k1itck)
        self.taurusGroupBox.setObjectName(_fromUtf8("taurusGroupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.taurusGroupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.taurusLed = TaurusLed(self.taurusGroupBox)
        self.taurusLed.setMinimumSize(QtCore.QSize(16, 16))
        self.taurusLed.setMaximumSize(QtCore.QSize(16, 16))
        self.taurusLed.setObjectName(_fromUtf8("taurusLed"))
        self.gridLayout_2.addWidget(self.taurusLed, 0, 1, 1, 1)
        self.taurusLed_2 = TaurusLed(self.taurusGroupBox)
        self.taurusLed_2.setMinimumSize(QtCore.QSize(16, 16))
        self.taurusLed_2.setMaximumSize(QtCore.QSize(16, 16))
        self.taurusLed_2.setObjectName(_fromUtf8("taurusLed_2"))
        self.gridLayout_2.addWidget(self.taurusLed_2, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.taurusGroupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.taurusLed_3 = TaurusLed(self.taurusGroupBox)
        self.taurusLed_3.setMinimumSize(QtCore.QSize(16, 16))
        self.taurusLed_3.setMaximumSize(QtCore.QSize(16, 16))
        self.taurusLed_3.setObjectName(_fromUtf8("taurusLed_3"))
        self.gridLayout_2.addWidget(self.taurusLed_3, 2, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.taurusGroupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.taurusLed_4 = TaurusLed(self.taurusGroupBox)
        self.taurusLed_4.setMinimumSize(QtCore.QSize(16, 16))
        self.taurusLed_4.setMaximumSize(QtCore.QSize(16, 16))
        self.taurusLed_4.setObjectName(_fromUtf8("taurusLed_4"))
        self.gridLayout_2.addWidget(self.taurusLed_4, 3, 1, 1, 1)
        self.label = QtGui.QLabel(self.taurusGroupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.taurusLed_5 = TaurusLed(self.taurusGroupBox)
        self.taurusLed_5.setMinimumSize(QtCore.QSize(16, 16))
        self.taurusLed_5.setMaximumSize(QtCore.QSize(16, 16))
        self.taurusLed_5.setObjectName(_fromUtf8("taurusLed_5"))
        self.gridLayout_2.addWidget(self.taurusLed_5, 4, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.taurusGroupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.taurusGroupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.taurusGroupBox, 0, 0, 1, 1)

        self.retranslateUi(k1itck)
        QtCore.QMetaObject.connectSlotsByName(k1itck)

    def retranslateUi(self, k1itck):
        k1itck.setWindowTitle(QtGui.QApplication.translate("k1itck", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.taurusGroupBox.setTitle(QtGui.QApplication.translate("k1itck", "klystron 1 interlock", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("k1itck", "RF window 2 underflow", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("k1itck", "RF window 1 underflow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("k1itck", "SF6 Pressure 1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("k1itck", "RF load 1 underflow", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("k1itck", "RF load 2 underflow", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.display import TaurusLed
from taurus.qt.qtgui.container import TaurusWidget, TaurusGroupBox
