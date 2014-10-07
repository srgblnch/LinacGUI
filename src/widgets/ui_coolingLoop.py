# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/ui/coolingLoop.ui'
#
# Created: Tue Oct  7 12:24:14 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_CoolingLoop(object):
    def setupUi(self, CoolingLoop):
        CoolingLoop.setObjectName(_fromUtf8("CoolingLoop"))
        CoolingLoop.resize(163, 167)
        self.gridLayout = QtGui.QGridLayout(CoolingLoop)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.coolingLoopGroup = TaurusGroupBox(CoolingLoop)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.coolingLoopGroup.setFont(font)
        self.coolingLoopGroup.setObjectName(_fromUtf8("coolingLoopGroup"))
        self.gridLayout_2 = QtGui.QGridLayout(self.coolingLoopGroup)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.epsTempLabel = QtGui.QLabel(self.coolingLoopGroup)
        self.epsTempLabel.setObjectName(_fromUtf8("epsTempLabel"))
        self.gridLayout_2.addWidget(self.epsTempLabel, 6, 0, 1, 1)
        self.epsTempValue = TaurusLabel(self.coolingLoopGroup)
        self.epsTempValue.setMinimumSize(QtCore.QSize(0, 20))
        self.epsTempValue.setObjectName(_fromUtf8("epsTempValue"))
        self.gridLayout_2.addWidget(self.epsTempValue, 6, 1, 1, 1)
        self.coolingLoopStatus = TaurusLabel(self.coolingLoopGroup)
        self.coolingLoopStatus.setMinimumSize(QtCore.QSize(0, 20))
        self.coolingLoopStatus.setObjectName(_fromUtf8("coolingLoopStatus"))
        self.gridLayout_2.addWidget(self.coolingLoopStatus, 0, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 8, 1, 1, 1)
        self.powerValue = TaurusLabel(self.coolingLoopGroup)
        self.powerValue.setMinimumSize(QtCore.QSize(0, 20))
        self.powerValue.setSuffixText(_fromUtf8(""))
        self.powerValue.setObjectName(_fromUtf8("powerValue"))
        self.gridLayout_2.addWidget(self.powerValue, 3, 1, 1, 1)
        self.temperatureValue = TaurusLabel(self.coolingLoopGroup)
        self.temperatureValue.setMinimumSize(QtCore.QSize(0, 20))
        self.temperatureValue.setSuffixText(_fromUtf8(""))
        self.temperatureValue.setObjectName(_fromUtf8("temperatureValue"))
        self.gridLayout_2.addWidget(self.temperatureValue, 1, 1, 1, 1)
        self.powerLabel = QtGui.QLabel(self.coolingLoopGroup)
        self.powerLabel.setObjectName(_fromUtf8("powerLabel"))
        self.gridLayout_2.addWidget(self.powerLabel, 3, 0, 1, 1)
        self.temperatureLabel = QtGui.QLabel(self.coolingLoopGroup)
        self.temperatureLabel.setObjectName(_fromUtf8("temperatureLabel"))
        self.gridLayout_2.addWidget(self.temperatureLabel, 1, 0, 1, 1)
        self.epsPressureLabel = QtGui.QLabel(self.coolingLoopGroup)
        self.epsPressureLabel.setObjectName(_fromUtf8("epsPressureLabel"))
        self.gridLayout_2.addWidget(self.epsPressureLabel, 4, 0, 1, 1)
        self.epsPressureValue = TaurusLabel(self.coolingLoopGroup)
        self.epsPressureValue.setMinimumSize(QtCore.QSize(0, 20))
        self.epsPressureValue.setObjectName(_fromUtf8("epsPressureValue"))
        self.gridLayout_2.addWidget(self.epsPressureValue, 4, 1, 1, 1)
        self.line = QtGui.QFrame(self.coolingLoopGroup)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 5, 0, 1, 2)
        self.gridLayout.addWidget(self.coolingLoopGroup, 0, 0, 1, 1)

        self.retranslateUi(CoolingLoop)
        QtCore.QMetaObject.connectSlotsByName(CoolingLoop)

    def retranslateUi(self, CoolingLoop):
        CoolingLoop.setWindowTitle(QtGui.QApplication.translate("CoolingLoop", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.coolingLoopGroup.setTitle(QtGui.QApplication.translate("CoolingLoop", "Cooling Loop #", None, QtGui.QApplication.UnicodeUTF8))
        self.epsTempLabel.setText(QtGui.QApplication.translate("CoolingLoop", "Temp Resistor", None, QtGui.QApplication.UnicodeUTF8))
        self.powerLabel.setText(QtGui.QApplication.translate("CoolingLoop", "Power drive", None, QtGui.QApplication.UnicodeUTF8))
        self.temperatureLabel.setText(QtGui.QApplication.translate("CoolingLoop", "Temp Water", None, QtGui.QApplication.UnicodeUTF8))
        self.epsPressureLabel.setText(QtGui.QApplication.translate("CoolingLoop", "Pressure", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.display import TaurusLabel
from taurus.qt.qtgui.container import TaurusGroupBox
from taurus.qt.qtgui.panel import TaurusWidget
