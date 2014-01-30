# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'linacOverview.ui'
#
# Created: Mon Jan 27 17:17:07 2014
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
        linacOverview.resize(300, 332)
        self.gridLayout_2 = QtGui.QGridLayout(linacOverview)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.overviewLayout = QtGui.QGridLayout()
        self.overviewLayout.setObjectName(_fromUtf8("overviewLayout"))
        self.klystron2Label = QtGui.QLabel(linacOverview)
        self.klystron2Label.setObjectName(_fromUtf8("klystron2Label"))
        self.overviewLayout.addWidget(self.klystron2Label, 6, 0, 1, 1)
        self.linacLabel = QtGui.QLabel(linacOverview)
        self.linacLabel.setObjectName(_fromUtf8("linacLabel"))
        self.overviewLayout.addWidget(self.linacLabel, 7, 0, 1, 1)
        self.HVPSRead = TaurusLed(linacOverview)
        self.HVPSRead.setMinimumSize(QtCore.QSize(25, 25))
        self.HVPSRead.setMaximumSize(QtCore.QSize(25, 25))
        self.HVPSRead.setObjectName(_fromUtf8("HVPSRead"))
        self.overviewLayout.addWidget(self.HVPSRead, 1, 1, 1, 1)
        self.VCLabel = QtGui.QLabel(linacOverview)
        self.VCLabel.setObjectName(_fromUtf8("VCLabel"))
        self.overviewLayout.addWidget(self.VCLabel, 3, 0, 1, 1)
        self.RFLabel = QtGui.QLabel(linacOverview)
        self.RFLabel.setObjectName(_fromUtf8("RFLabel"))
        self.overviewLayout.addWidget(self.RFLabel, 2, 0, 1, 1)
        self.HVPSLabel = QtGui.QLabel(linacOverview)
        self.HVPSLabel.setObjectName(_fromUtf8("HVPSLabel"))
        self.overviewLayout.addWidget(self.HVPSLabel, 1, 0, 1, 1)
        self.klystron1Label = QtGui.QLabel(linacOverview)
        self.klystron1Label.setObjectName(_fromUtf8("klystron1Label"))
        self.overviewLayout.addWidget(self.klystron1Label, 5, 0, 1, 1)
        self.gunLowVoltageRead = TaurusLed(linacOverview)
        self.gunLowVoltageRead.setMinimumSize(QtCore.QSize(25, 25))
        self.gunLowVoltageRead.setMaximumSize(QtCore.QSize(25, 25))
        self.gunLowVoltageRead.setObjectName(_fromUtf8("gunLowVoltageRead"))
        self.overviewLayout.addWidget(self.gunLowVoltageRead, 0, 1, 1, 1)
        self.gunLowVoltageLabel = QtGui.QLabel(linacOverview)
        self.gunLowVoltageLabel.setObjectName(_fromUtf8("gunLowVoltageLabel"))
        self.overviewLayout.addWidget(self.gunLowVoltageLabel, 0, 0, 1, 1)
        self.ACLabel = QtGui.QLabel(linacOverview)
        self.ACLabel.setObjectName(_fromUtf8("ACLabel"))
        self.overviewLayout.addWidget(self.ACLabel, 4, 0, 1, 1)
        self.gunLowVoltageWrite = TaurusValueCheckBox(linacOverview)
        self.gunLowVoltageWrite.setShowText(False)
        self.gunLowVoltageWrite.setObjectName(_fromUtf8("gunLowVoltageWrite"))
        self.overviewLayout.addWidget(self.gunLowVoltageWrite, 0, 2, 1, 1)
        self.HVPSWrite = TaurusValueCheckBox(linacOverview)
        self.HVPSWrite.setShowText(False)
        self.HVPSWrite.setObjectName(_fromUtf8("HVPSWrite"))
        self.overviewLayout.addWidget(self.HVPSWrite, 1, 2, 1, 1)
        self.RFRead = TaurusLed(linacOverview)
        self.RFRead.setMinimumSize(QtCore.QSize(25, 25))
        self.RFRead.setMaximumSize(QtCore.QSize(25, 25))
        self.RFRead.setObjectName(_fromUtf8("RFRead"))
        self.overviewLayout.addWidget(self.RFRead, 2, 1, 1, 2)
        self.VCRead = TaurusLed(linacOverview)
        self.VCRead.setMinimumSize(QtCore.QSize(25, 25))
        self.VCRead.setMaximumSize(QtCore.QSize(25, 25))
        self.VCRead.setObjectName(_fromUtf8("VCRead"))
        self.overviewLayout.addWidget(self.VCRead, 3, 1, 1, 2)
        self.ACRead = TaurusLed(linacOverview)
        self.ACRead.setMinimumSize(QtCore.QSize(25, 25))
        self.ACRead.setMaximumSize(QtCore.QSize(25, 25))
        self.ACRead.setObjectName(_fromUtf8("ACRead"))
        self.overviewLayout.addWidget(self.ACRead, 4, 1, 1, 2)
        self.klystron1Read = TaurusLed(linacOverview)
        self.klystron1Read.setMinimumSize(QtCore.QSize(25, 25))
        self.klystron1Read.setMaximumSize(QtCore.QSize(25, 25))
        self.klystron1Read.setObjectName(_fromUtf8("klystron1Read"))
        self.overviewLayout.addWidget(self.klystron1Read, 5, 1, 1, 2)
        self.klystron2Read = TaurusLed(linacOverview)
        self.klystron2Read.setMinimumSize(QtCore.QSize(25, 25))
        self.klystron2Read.setMaximumSize(QtCore.QSize(25, 25))
        self.klystron2Read.setObjectName(_fromUtf8("klystron2Read"))
        self.overviewLayout.addWidget(self.klystron2Read, 6, 1, 1, 2)
        self.linacRead = TaurusLed(linacOverview)
        self.linacRead.setMinimumSize(QtCore.QSize(25, 25))
        self.linacRead.setMaximumSize(QtCore.QSize(25, 25))
        self.linacRead.setObjectName(_fromUtf8("linacRead"))
        self.overviewLayout.addWidget(self.linacRead, 7, 1, 1, 2)
        self.gridLayout_2.addLayout(self.overviewLayout, 0, 0, 1, 1)

        self.retranslateUi(linacOverview)
        QtCore.QMetaObject.connectSlotsByName(linacOverview)

    def retranslateUi(self, linacOverview):
        linacOverview.setWindowTitle(QtGui.QApplication.translate("linacOverview", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.klystron2Label.setText(QtGui.QApplication.translate("linacOverview", "Klystron 2 Ready", None, QtGui.QApplication.UnicodeUTF8))
        self.linacLabel.setText(QtGui.QApplication.translate("linacOverview", "Linac Ready", None, QtGui.QApplication.UnicodeUTF8))
        self.VCLabel.setText(QtGui.QApplication.translate("linacOverview", "Vacuum Ready", None, QtGui.QApplication.UnicodeUTF8))
        self.RFLabel.setText(QtGui.QApplication.translate("linacOverview", "RF Ready", None, QtGui.QApplication.UnicodeUTF8))
        self.HVPSLabel.setText(QtGui.QApplication.translate("linacOverview", "High Voltage PS", None, QtGui.QApplication.UnicodeUTF8))
        self.klystron1Label.setText(QtGui.QApplication.translate("linacOverview", "Klystron 1 Ready", None, QtGui.QApplication.UnicodeUTF8))
        self.gunLowVoltageRead.setOffColor(QtGui.QApplication.translate("linacOverview", "black", None, QtGui.QApplication.UnicodeUTF8))
        self.gunLowVoltageLabel.setText(QtGui.QApplication.translate("linacOverview", "Gun Low Voltage", None, QtGui.QApplication.UnicodeUTF8))
        self.ACLabel.setText(QtGui.QApplication.translate("linacOverview", "Compressed Air Ready", None, QtGui.QApplication.UnicodeUTF8))
        self.RFRead.setOffColor(QtGui.QApplication.translate("linacOverview", "red", None, QtGui.QApplication.UnicodeUTF8))
        self.VCRead.setOffColor(QtGui.QApplication.translate("linacOverview", "red", None, QtGui.QApplication.UnicodeUTF8))
        self.ACRead.setOffColor(QtGui.QApplication.translate("linacOverview", "red", None, QtGui.QApplication.UnicodeUTF8))
        self.klystron1Read.setOffColor(QtGui.QApplication.translate("linacOverview", "red", None, QtGui.QApplication.UnicodeUTF8))
        self.klystron2Read.setOffColor(QtGui.QApplication.translate("linacOverview", "red", None, QtGui.QApplication.UnicodeUTF8))
        self.linacRead.setOffColor(QtGui.QApplication.translate("linacOverview", "red", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.display import TaurusLed
from taurus.qt.qtgui.container import TaurusWidget
from taurus.qt.qtgui.input import TaurusValueCheckBox

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    linacOverview = QtGui.TaurusWidget()
    ui = Ui_linacOverview()
    ui.setupUi(linacOverview)
    linacOverview.show()
    sys.exit(app.exec_())

