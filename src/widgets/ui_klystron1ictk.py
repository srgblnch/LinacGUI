# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/ui/klystron1ictk.ui'
#
# Created: Thu Nov 27 12:41:40 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_klystron1itck(object):
    def setupUi(self, klystron1itck):
        klystron1itck.setObjectName(_fromUtf8("klystron1itck"))
        klystron1itck.resize(155, 144)
        self.gridLayout = QtGui.QGridLayout(klystron1itck)
        self.gridLayout.setMargin(1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.ictkGroup = TaurusGroupBox(klystron1itck)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ictkGroup.setFont(font)
        self.ictkGroup.setObjectName(_fromUtf8("ictkGroup"))
        self.gridLayout_2 = QtGui.QGridLayout(self.ictkGroup)
        self.gridLayout_2.setMargin(2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.rfl2Label = QtGui.QLabel(self.ictkGroup)
        self.rfl2Label.setObjectName(_fromUtf8("rfl2Label"))
        self.gridLayout_2.addWidget(self.rfl2Label, 4, 0, 1, 1)
        self.rfw2Label = QtGui.QLabel(self.ictkGroup)
        self.rfw2Label.setObjectName(_fromUtf8("rfw2Label"))
        self.gridLayout_2.addWidget(self.rfw2Label, 2, 0, 1, 1)
        self.sf6p1Label = QtGui.QLabel(self.ictkGroup)
        self.sf6p1Label.setObjectName(_fromUtf8("sf6p1Label"))
        self.gridLayout_2.addWidget(self.sf6p1Label, 0, 0, 1, 1)
        self.rfl1Label = QtGui.QLabel(self.ictkGroup)
        self.rfl1Label.setObjectName(_fromUtf8("rfl1Label"))
        self.gridLayout_2.addWidget(self.rfl1Label, 3, 0, 1, 1)
        self.rfw1Label = QtGui.QLabel(self.ictkGroup)
        self.rfw1Label.setObjectName(_fromUtf8("rfw1Label"))
        self.gridLayout_2.addWidget(self.rfw1Label, 1, 0, 1, 1)
        self.sf6p1Led = TaurusLed(self.ictkGroup)
        self.sf6p1Led.setMinimumSize(QtCore.QSize(15, 15))
        self.sf6p1Led.setMaximumSize(QtCore.QSize(15, 15))
        self.sf6p1Led.setObjectName(_fromUtf8("sf6p1Led"))
        self.gridLayout_2.addWidget(self.sf6p1Led, 0, 1, 1, 1)
        self.rfw1Led = TaurusLed(self.ictkGroup)
        self.rfw1Led.setMinimumSize(QtCore.QSize(15, 15))
        self.rfw1Led.setMaximumSize(QtCore.QSize(15, 15))
        self.rfw1Led.setObjectName(_fromUtf8("rfw1Led"))
        self.gridLayout_2.addWidget(self.rfw1Led, 1, 1, 1, 1)
        self.rfw2Led = TaurusLed(self.ictkGroup)
        self.rfw2Led.setMinimumSize(QtCore.QSize(15, 15))
        self.rfw2Led.setMaximumSize(QtCore.QSize(15, 15))
        self.rfw2Led.setObjectName(_fromUtf8("rfw2Led"))
        self.gridLayout_2.addWidget(self.rfw2Led, 2, 1, 1, 1)
        self.rfl1Led = TaurusLed(self.ictkGroup)
        self.rfl1Led.setMinimumSize(QtCore.QSize(15, 15))
        self.rfl1Led.setMaximumSize(QtCore.QSize(15, 15))
        self.rfl1Led.setObjectName(_fromUtf8("rfl1Led"))
        self.gridLayout_2.addWidget(self.rfl1Led, 3, 1, 1, 1)
        self.rfl2Led = TaurusLed(self.ictkGroup)
        self.rfl2Led.setMinimumSize(QtCore.QSize(15, 15))
        self.rfl2Led.setMaximumSize(QtCore.QSize(15, 15))
        self.rfl2Led.setObjectName(_fromUtf8("rfl2Led"))
        self.gridLayout_2.addWidget(self.rfl2Led, 4, 1, 1, 1)
        self.gridLayout.addWidget(self.ictkGroup, 0, 0, 1, 1)

        self.retranslateUi(klystron1itck)
        QtCore.QMetaObject.connectSlotsByName(klystron1itck)

    def retranslateUi(self, klystron1itck):
        klystron1itck.setWindowTitle(QtGui.QApplication.translate("klystron1itck", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.ictkGroup.setTitle(QtGui.QApplication.translate("klystron1itck", "klystron 1 interlock", None, QtGui.QApplication.UnicodeUTF8))
        self.rfl2Label.setText(QtGui.QApplication.translate("klystron1itck", "RF load 2 underflow", None, QtGui.QApplication.UnicodeUTF8))
        self.rfw2Label.setText(QtGui.QApplication.translate("klystron1itck", "RF window 2 underflow", None, QtGui.QApplication.UnicodeUTF8))
        self.sf6p1Label.setText(QtGui.QApplication.translate("klystron1itck", "SF6 Pressure 1", None, QtGui.QApplication.UnicodeUTF8))
        self.rfl1Label.setText(QtGui.QApplication.translate("klystron1itck", "RF load 1 underflow", None, QtGui.QApplication.UnicodeUTF8))
        self.rfw1Label.setText(QtGui.QApplication.translate("klystron1itck", "RF window 1 underflow", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.display import TaurusLed
from taurus.qt.qtgui.container import TaurusGroupBox
from taurus.qt.qtgui.panel import TaurusWidget
