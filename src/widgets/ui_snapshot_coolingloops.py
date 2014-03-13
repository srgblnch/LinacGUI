# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/snapshot_coolingloops.ui'
#
# Created: Wed Mar 12 17:15:20 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_coolingLoopSnapshot(object):
    def setupUi(self, coolingLoopSnapshot):
        coolingLoopSnapshot.setObjectName(_fromUtf8("coolingLoopSnapshot"))
        coolingLoopSnapshot.resize(277, 136)
        font = QtGui.QFont()
        font.setPointSize(7)
        coolingLoopSnapshot.setFont(font)
        self.gridLayout = QtGui.QGridLayout(coolingLoopSnapshot)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.coolingLoopGroup = TaurusGroupBox(coolingLoopSnapshot)
        self.coolingLoopGroup.setObjectName(_fromUtf8("coolingLoopGroup"))
        self.gridLayout_2 = QtGui.QGridLayout(self.coolingLoopGroup)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.coolingLoop1SetpointCheck = QtGui.QCheckBox(self.coolingLoopGroup)
        self.coolingLoop1SetpointCheck.setText(_fromUtf8(""))
        self.coolingLoop1SetpointCheck.setObjectName(_fromUtf8("coolingLoop1SetpointCheck"))
        self.gridLayout_2.addWidget(self.coolingLoop1SetpointCheck, 1, 4, 1, 1)
        self.coolingLoop1SetpointLabel = QtGui.QLabel(self.coolingLoopGroup)
        self.coolingLoop1SetpointLabel.setObjectName(_fromUtf8("coolingLoop1SetpointLabel"))
        self.gridLayout_2.addWidget(self.coolingLoop1SetpointLabel, 1, 0, 1, 1)
        self.coolingLoop1SetpointWrite = QtGui.QDoubleSpinBox(self.coolingLoopGroup)
        self.coolingLoop1SetpointWrite.setObjectName(_fromUtf8("coolingLoop1SetpointWrite"))
        self.gridLayout_2.addWidget(self.coolingLoop1SetpointWrite, 1, 2, 1, 1)
        self.coolingLoop1SetpointRead = TaurusLabel(self.coolingLoopGroup)
        self.coolingLoop1SetpointRead.setObjectName(_fromUtf8("coolingLoop1SetpointRead"))
        self.gridLayout_2.addWidget(self.coolingLoop1SetpointRead, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 5, 1, 1, 1)
        self.PresentWriteTitle = QtGui.QLabel(self.coolingLoopGroup)
        self.PresentWriteTitle.setObjectName(_fromUtf8("PresentWriteTitle"))
        self.gridLayout_2.addWidget(self.PresentWriteTitle, 0, 1, 1, 1)
        self.SaveRetrieveTitle = QtGui.QLabel(self.coolingLoopGroup)
        self.SaveRetrieveTitle.setObjectName(_fromUtf8("SaveRetrieveTitle"))
        self.gridLayout_2.addWidget(self.SaveRetrieveTitle, 0, 2, 1, 1)
        self.coolingLoop3SetpointLabel = QtGui.QLabel(self.coolingLoopGroup)
        self.coolingLoop3SetpointLabel.setObjectName(_fromUtf8("coolingLoop3SetpointLabel"))
        self.gridLayout_2.addWidget(self.coolingLoop3SetpointLabel, 3, 0, 1, 1)
        self.coolingLoop2SetpointLabel = QtGui.QLabel(self.coolingLoopGroup)
        self.coolingLoop2SetpointLabel.setObjectName(_fromUtf8("coolingLoop2SetpointLabel"))
        self.gridLayout_2.addWidget(self.coolingLoop2SetpointLabel, 2, 0, 1, 1)
        self.coolingLoop2SetpointRead = TaurusLabel(self.coolingLoopGroup)
        self.coolingLoop2SetpointRead.setObjectName(_fromUtf8("coolingLoop2SetpointRead"))
        self.gridLayout_2.addWidget(self.coolingLoop2SetpointRead, 2, 1, 1, 1)
        self.coolingLoop3SetpointRead = TaurusLabel(self.coolingLoopGroup)
        self.coolingLoop3SetpointRead.setObjectName(_fromUtf8("coolingLoop3SetpointRead"))
        self.gridLayout_2.addWidget(self.coolingLoop3SetpointRead, 3, 1, 1, 1)
        self.coolingLoop2SetpointWrite = QtGui.QDoubleSpinBox(self.coolingLoopGroup)
        self.coolingLoop2SetpointWrite.setObjectName(_fromUtf8("coolingLoop2SetpointWrite"))
        self.gridLayout_2.addWidget(self.coolingLoop2SetpointWrite, 2, 2, 1, 1)
        self.coolingLoop3SetpointWrite = QtGui.QDoubleSpinBox(self.coolingLoopGroup)
        self.coolingLoop3SetpointWrite.setObjectName(_fromUtf8("coolingLoop3SetpointWrite"))
        self.gridLayout_2.addWidget(self.coolingLoop3SetpointWrite, 3, 2, 1, 1)
        self.coolingLoop2SetpointCheck = QtGui.QCheckBox(self.coolingLoopGroup)
        self.coolingLoop2SetpointCheck.setText(_fromUtf8(""))
        self.coolingLoop2SetpointCheck.setObjectName(_fromUtf8("coolingLoop2SetpointCheck"))
        self.gridLayout_2.addWidget(self.coolingLoop2SetpointCheck, 2, 4, 1, 1)
        self.coolingLoop3SetpointCheck = QtGui.QCheckBox(self.coolingLoopGroup)
        self.coolingLoop3SetpointCheck.setText(_fromUtf8(""))
        self.coolingLoop3SetpointCheck.setObjectName(_fromUtf8("coolingLoop3SetpointCheck"))
        self.gridLayout_2.addWidget(self.coolingLoop3SetpointCheck, 3, 4, 1, 1)
        self.line = QtGui.QFrame(self.coolingLoopGroup)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 1, 3, 4, 1)
        self.gridLayout.addWidget(self.coolingLoopGroup, 0, 0, 1, 1)

        self.retranslateUi(coolingLoopSnapshot)
        QtCore.QMetaObject.connectSlotsByName(coolingLoopSnapshot)

    def retranslateUi(self, coolingLoopSnapshot):
        coolingLoopSnapshot.setWindowTitle(QtGui.QApplication.translate("coolingLoopSnapshot", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.coolingLoopGroup.setTitle(QtGui.QApplication.translate("coolingLoopSnapshot", "Cooling Loops", None, QtGui.QApplication.UnicodeUTF8))
        self.coolingLoop1SetpointLabel.setText(QtGui.QApplication.translate("coolingLoopSnapshot", "cl1 Temperature", None, QtGui.QApplication.UnicodeUTF8))
        self.PresentWriteTitle.setText(QtGui.QApplication.translate("coolingLoopSnapshot", "Present value", None, QtGui.QApplication.UnicodeUTF8))
        self.SaveRetrieveTitle.setText(QtGui.QApplication.translate("coolingLoopSnapshot", "Save/Retrieve", None, QtGui.QApplication.UnicodeUTF8))
        self.coolingLoop3SetpointLabel.setText(QtGui.QApplication.translate("coolingLoopSnapshot", "cl3 Temperature", None, QtGui.QApplication.UnicodeUTF8))
        self.coolingLoop2SetpointLabel.setText(QtGui.QApplication.translate("coolingLoopSnapshot", "cl2 Temperature", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.display import TaurusLabel
from taurus.qt.qtgui.container import TaurusGroupBox
from taurus.qt.qtgui.panel import TaurusWidget
