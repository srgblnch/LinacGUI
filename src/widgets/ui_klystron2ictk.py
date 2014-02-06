# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'klystron2ictk.ui'
#
# Created: Thu Feb  6 08:52:39 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_klystron2itck(object):
    def setupUi(self, klystron2itck):
        klystron2itck.setObjectName(_fromUtf8("klystron2itck"))
        klystron2itck.resize(156, 100)
        self.gridLayout = QtGui.QGridLayout(klystron2itck)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.ictkGroup = TaurusGroupBox(klystron2itck)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ictkGroup.setFont(font)
        self.ictkGroup.setObjectName(_fromUtf8("ictkGroup"))
        self.gridLayout_2 = QtGui.QGridLayout(self.ictkGroup)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.rfw3Label = QtGui.QLabel(self.ictkGroup)
        self.rfw3Label.setObjectName(_fromUtf8("rfw3Label"))
        self.gridLayout_2.addWidget(self.rfw3Label, 1, 0, 1, 1)
        self.sf6p2Label = QtGui.QLabel(self.ictkGroup)
        self.sf6p2Label.setObjectName(_fromUtf8("sf6p2Label"))
        self.gridLayout_2.addWidget(self.sf6p2Label, 0, 0, 1, 1)
        self.rfl3Label = QtGui.QLabel(self.ictkGroup)
        self.rfl3Label.setObjectName(_fromUtf8("rfl3Label"))
        self.gridLayout_2.addWidget(self.rfl3Label, 2, 0, 1, 1)
        self.sf6p2Led = TaurusLed(self.ictkGroup)
        self.sf6p2Led.setMinimumSize(QtCore.QSize(15, 15))
        self.sf6p2Led.setMaximumSize(QtCore.QSize(15, 15))
        self.sf6p2Led.setObjectName(_fromUtf8("sf6p2Led"))
        self.gridLayout_2.addWidget(self.sf6p2Led, 0, 1, 1, 1)
        self.rfw3Led = TaurusLed(self.ictkGroup)
        self.rfw3Led.setMinimumSize(QtCore.QSize(15, 15))
        self.rfw3Led.setMaximumSize(QtCore.QSize(15, 15))
        self.rfw3Led.setObjectName(_fromUtf8("rfw3Led"))
        self.gridLayout_2.addWidget(self.rfw3Led, 1, 1, 1, 1)
        self.rfl3Led = TaurusLed(self.ictkGroup)
        self.rfl3Led.setMinimumSize(QtCore.QSize(15, 15))
        self.rfl3Led.setMaximumSize(QtCore.QSize(15, 15))
        self.rfl3Led.setObjectName(_fromUtf8("rfl3Led"))
        self.gridLayout_2.addWidget(self.rfl3Led, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.ictkGroup, 0, 0, 1, 1)

        self.retranslateUi(klystron2itck)
        QtCore.QMetaObject.connectSlotsByName(klystron2itck)

    def retranslateUi(self, klystron2itck):
        klystron2itck.setWindowTitle(QtGui.QApplication.translate("klystron2itck", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.ictkGroup.setTitle(QtGui.QApplication.translate("klystron2itck", "klystron 2 interlock", None, QtGui.QApplication.UnicodeUTF8))
        self.rfw3Label.setText(QtGui.QApplication.translate("klystron2itck", "RF window 3 underflow", None, QtGui.QApplication.UnicodeUTF8))
        self.sf6p2Label.setText(QtGui.QApplication.translate("klystron2itck", "SF6 Pressure 2", None, QtGui.QApplication.UnicodeUTF8))
        self.rfl3Label.setText(QtGui.QApplication.translate("klystron2itck", "RF load 3 underflow", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.display import TaurusLed
from taurus.qt.qtgui.container import TaurusWidget, TaurusGroupBox
