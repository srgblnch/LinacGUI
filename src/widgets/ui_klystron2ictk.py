# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'klystron2ictk.ui'
#
# Created: Tue Jan 21 10:18:29 2014
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
        klystron2itck.resize(183, 100)
        self.gridLayout = QtGui.QGridLayout(klystron2itck)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.ictkGroup = TaurusGroupBox(klystron2itck)
        self.ictkGroup.setObjectName(_fromUtf8("ictkGroup"))
        self.gridLayout_2 = QtGui.QGridLayout(self.ictkGroup)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.sf6p2Label = QtGui.QLabel(self.ictkGroup)
        self.sf6p2Label.setObjectName(_fromUtf8("sf6p2Label"))
        self.gridLayout_2.addWidget(self.sf6p2Label, 0, 0, 1, 1)
        self.sf6p2Led = TaurusLed(self.ictkGroup)
        self.sf6p2Led.setMinimumSize(QtCore.QSize(16, 16))
        self.sf6p2Led.setMaximumSize(QtCore.QSize(16, 16))
        self.sf6p2Led.setLedStatus(False)
        self.sf6p2Led.setObjectName(_fromUtf8("sf6p2Led"))
        self.gridLayout_2.addWidget(self.sf6p2Led, 0, 1, 1, 1)
        self.w3Label = QtGui.QLabel(self.ictkGroup)
        self.w3Label.setObjectName(_fromUtf8("w3Label"))
        self.gridLayout_2.addWidget(self.w3Label, 1, 0, 1, 1)
        self.w3Led = TaurusLed(self.ictkGroup)
        self.w3Led.setMinimumSize(QtCore.QSize(16, 16))
        self.w3Led.setMaximumSize(QtCore.QSize(16, 16))
        self.w3Led.setLedStatus(False)
        self.w3Led.setObjectName(_fromUtf8("w3Led"))
        self.gridLayout_2.addWidget(self.w3Led, 1, 1, 1, 1)
        self.rl3Label = QtGui.QLabel(self.ictkGroup)
        self.rl3Label.setObjectName(_fromUtf8("rl3Label"))
        self.gridLayout_2.addWidget(self.rl3Label, 2, 0, 1, 1)
        self.rl3Led = TaurusLed(self.ictkGroup)
        self.rl3Led.setMinimumSize(QtCore.QSize(16, 16))
        self.rl3Led.setMaximumSize(QtCore.QSize(16, 16))
        self.rl3Led.setLedStatus(False)
        self.rl3Led.setObjectName(_fromUtf8("rl3Led"))
        self.gridLayout_2.addWidget(self.rl3Led, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.ictkGroup, 0, 0, 1, 1)

        self.retranslateUi(klystron2itck)
        QtCore.QMetaObject.connectSlotsByName(klystron2itck)

    def retranslateUi(self, klystron2itck):
        klystron2itck.setWindowTitle(QtGui.QApplication.translate("klystron2itck", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.ictkGroup.setTitle(QtGui.QApplication.translate("klystron2itck", "klystron 2 interlock", None, QtGui.QApplication.UnicodeUTF8))
        self.sf6p2Label.setText(QtGui.QApplication.translate("klystron2itck", "SF6 Pressure 2", None, QtGui.QApplication.UnicodeUTF8))
        self.sf6p2Led.setProperty("ledPattern", QtGui.QApplication.translate("klystron2itck", ":leds/images256/led_{color}_on.png", None, QtGui.QApplication.UnicodeUTF8))
        self.sf6p2Led.setModel(QtGui.QApplication.translate("klystron2itck", "li/ct/plc1/sf6_p2_st", None, QtGui.QApplication.UnicodeUTF8))
        self.sf6p2Led.setOffColor(QtGui.QApplication.translate("klystron2itck", "red", None, QtGui.QApplication.UnicodeUTF8))
        self.w3Label.setText(QtGui.QApplication.translate("klystron2itck", "RF window 3 underflow", None, QtGui.QApplication.UnicodeUTF8))
        self.w3Led.setProperty("ledPattern", QtGui.QApplication.translate("klystron2itck", ":leds/images256/led_{color}_{status}.png", None, QtGui.QApplication.UnicodeUTF8))
        self.w3Led.setOffColor(QtGui.QApplication.translate("klystron2itck", "white", None, QtGui.QApplication.UnicodeUTF8))
        self.rl3Label.setText(QtGui.QApplication.translate("klystron2itck", "RF load 3 underflow", None, QtGui.QApplication.UnicodeUTF8))
        self.rl3Led.setProperty("ledPattern", QtGui.QApplication.translate("klystron2itck", ":leds/images256/led_{color}_{status}.png", None, QtGui.QApplication.UnicodeUTF8))
        self.rl3Led.setOffColor(QtGui.QApplication.translate("klystron2itck", "white", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.display import TaurusLed
from taurus.qt.qtgui.container import TaurusWidget, TaurusGroupBox
