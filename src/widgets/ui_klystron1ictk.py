# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'klystron1ictk.ui'
#
# Created: Tue Jan 21 10:18:27 2014
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
        klystron1itck.resize(183, 144)
        self.gridLayout = QtGui.QGridLayout(klystron1itck)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.ictkGroup = TaurusGroupBox(klystron1itck)
        self.ictkGroup.setObjectName(_fromUtf8("ictkGroup"))
        self.gridLayout_2 = QtGui.QGridLayout(self.ictkGroup)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.sf6p1Led = TaurusLed(self.ictkGroup)
        self.sf6p1Led.setMinimumSize(QtCore.QSize(16, 16))
        self.sf6p1Led.setMaximumSize(QtCore.QSize(16, 16))
        self.sf6p1Led.setLedStatus(False)
        self.sf6p1Led.setObjectName(_fromUtf8("sf6p1Led"))
        self.gridLayout_2.addWidget(self.sf6p1Led, 0, 1, 1, 1)
        self.w1Led = TaurusLed(self.ictkGroup)
        self.w1Led.setMinimumSize(QtCore.QSize(16, 16))
        self.w1Led.setMaximumSize(QtCore.QSize(16, 16))
        self.w1Led.setLedStatus(False)
        self.w1Led.setObjectName(_fromUtf8("w1Led"))
        self.gridLayout_2.addWidget(self.w1Led, 1, 1, 1, 1)
        self.w2Label = QtGui.QLabel(self.ictkGroup)
        self.w2Label.setObjectName(_fromUtf8("w2Label"))
        self.gridLayout_2.addWidget(self.w2Label, 2, 0, 1, 1)
        self.w2Led = TaurusLed(self.ictkGroup)
        self.w2Led.setMinimumSize(QtCore.QSize(16, 16))
        self.w2Led.setMaximumSize(QtCore.QSize(16, 16))
        self.w2Led.setLedStatus(False)
        self.w2Led.setObjectName(_fromUtf8("w2Led"))
        self.gridLayout_2.addWidget(self.w2Led, 2, 1, 1, 1)
        self.w1Label = QtGui.QLabel(self.ictkGroup)
        self.w1Label.setObjectName(_fromUtf8("w1Label"))
        self.gridLayout_2.addWidget(self.w1Label, 1, 0, 1, 1)
        self.rl1Led = TaurusLed(self.ictkGroup)
        self.rl1Led.setMinimumSize(QtCore.QSize(16, 16))
        self.rl1Led.setMaximumSize(QtCore.QSize(16, 16))
        self.rl1Led.setLedStatus(False)
        self.rl1Led.setObjectName(_fromUtf8("rl1Led"))
        self.gridLayout_2.addWidget(self.rl1Led, 3, 1, 1, 1)
        self.sf6p1Label = QtGui.QLabel(self.ictkGroup)
        self.sf6p1Label.setObjectName(_fromUtf8("sf6p1Label"))
        self.gridLayout_2.addWidget(self.sf6p1Label, 0, 0, 1, 1)
        self.rl2Led = TaurusLed(self.ictkGroup)
        self.rl2Led.setMinimumSize(QtCore.QSize(16, 16))
        self.rl2Led.setMaximumSize(QtCore.QSize(16, 16))
        self.rl2Led.setLedStatus(False)
        self.rl2Led.setObjectName(_fromUtf8("rl2Led"))
        self.gridLayout_2.addWidget(self.rl2Led, 4, 1, 1, 1)
        self.rl1Label = QtGui.QLabel(self.ictkGroup)
        self.rl1Label.setObjectName(_fromUtf8("rl1Label"))
        self.gridLayout_2.addWidget(self.rl1Label, 3, 0, 1, 1)
        self.rl2Label = QtGui.QLabel(self.ictkGroup)
        self.rl2Label.setObjectName(_fromUtf8("rl2Label"))
        self.gridLayout_2.addWidget(self.rl2Label, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.ictkGroup, 0, 0, 1, 1)

        self.retranslateUi(klystron1itck)
        QtCore.QMetaObject.connectSlotsByName(klystron1itck)

    def retranslateUi(self, klystron1itck):
        klystron1itck.setWindowTitle(QtGui.QApplication.translate("klystron1itck", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.ictkGroup.setTitle(QtGui.QApplication.translate("klystron1itck", "klystron 1 interlock", None, QtGui.QApplication.UnicodeUTF8))
        self.sf6p1Led.setProperty("ledPattern", QtGui.QApplication.translate("klystron1itck", ":leds/images256/led_{color}_on.png", None, QtGui.QApplication.UnicodeUTF8))
        self.sf6p1Led.setModel(QtGui.QApplication.translate("klystron1itck", "li/ct/plc1/sf6_p1_st", None, QtGui.QApplication.UnicodeUTF8))
        self.sf6p1Led.setOffColor(QtGui.QApplication.translate("klystron1itck", "red", None, QtGui.QApplication.UnicodeUTF8))
        self.w1Led.setProperty("ledPattern", QtGui.QApplication.translate("klystron1itck", ":leds/images256/led_{color}_{status}.png", None, QtGui.QApplication.UnicodeUTF8))
        self.w1Led.setOffColor(QtGui.QApplication.translate("klystron1itck", "white", None, QtGui.QApplication.UnicodeUTF8))
        self.w2Label.setText(QtGui.QApplication.translate("klystron1itck", "RF window 2 underflow", None, QtGui.QApplication.UnicodeUTF8))
        self.w2Led.setProperty("ledPattern", QtGui.QApplication.translate("klystron1itck", ":leds/images256/led_{color}_{status}.png", None, QtGui.QApplication.UnicodeUTF8))
        self.w2Led.setOffColor(QtGui.QApplication.translate("klystron1itck", "white", None, QtGui.QApplication.UnicodeUTF8))
        self.w1Label.setText(QtGui.QApplication.translate("klystron1itck", "RF window 1 underflow", None, QtGui.QApplication.UnicodeUTF8))
        self.rl1Led.setProperty("ledPattern", QtGui.QApplication.translate("klystron1itck", ":leds/images256/led_{color}_{status}.png", None, QtGui.QApplication.UnicodeUTF8))
        self.rl1Led.setOffColor(QtGui.QApplication.translate("klystron1itck", "white", None, QtGui.QApplication.UnicodeUTF8))
        self.sf6p1Label.setText(QtGui.QApplication.translate("klystron1itck", "SF6 Pressure 1", None, QtGui.QApplication.UnicodeUTF8))
        self.rl2Led.setProperty("ledPattern", QtGui.QApplication.translate("klystron1itck", ":leds/images256/led_{color}_{status}.png", None, QtGui.QApplication.UnicodeUTF8))
        self.rl2Led.setOffColor(QtGui.QApplication.translate("klystron1itck", "white", None, QtGui.QApplication.UnicodeUTF8))
        self.rl1Label.setText(QtGui.QApplication.translate("klystron1itck", "RF load 1 underflow", None, QtGui.QApplication.UnicodeUTF8))
        self.rl2Label.setText(QtGui.QApplication.translate("klystron1itck", "RF load 2 underflow", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.display import TaurusLed
from taurus.qt.qtgui.container import TaurusWidget, TaurusGroupBox
