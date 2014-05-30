# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/ui/linacPlcWidget.ui'
#
# Created: Fri May 30 12:22:27 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_linacPlcWidget(object):
    def setupUi(self, linacPlcWidget):
        linacPlcWidget.setObjectName(_fromUtf8("linacPlcWidget"))
        linacPlcWidget.resize(300, 335)
        self.gridLayout_5 = QtGui.QGridLayout(linacPlcWidget)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.splitter = QtGui.QSplitter(linacPlcWidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.plcGroup = TaurusGroupBox(self.splitter)
        self.plcGroup.setObjectName(_fromUtf8("plcGroup"))
        self.gridLayout_2 = QtGui.QGridLayout(self.plcGroup)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.stateRead = TaurusLed(self.plcGroup)
        self.stateRead.setMinimumSize(QtCore.QSize(25, 25))
        self.stateRead.setMaximumSize(QtCore.QSize(25, 25))
        self.stateRead.setUseParentModel(True)
        self.stateRead.setObjectName(_fromUtf8("stateRead"))
        self.gridLayout.addWidget(self.stateRead, 3, 1, 1, 1)
        self.statusLabel = QtGui.QLabel(self.plcGroup)
        self.statusLabel.setObjectName(_fromUtf8("statusLabel"))
        self.gridLayout.addWidget(self.statusLabel, 4, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lockingRead = TaurusLed(self.plcGroup)
        self.lockingRead.setMinimumSize(QtCore.QSize(25, 25))
        self.lockingRead.setMaximumSize(QtCore.QSize(25, 25))
        self.lockingRead.setUseParentModel(True)
        self.lockingRead.setObjectName(_fromUtf8("lockingRead"))
        self.horizontalLayout.addWidget(self.lockingRead)
        self.lockingWrite = LinacValueCheckBox(self.plcGroup)
        self.lockingWrite.setMinimumSize(QtCore.QSize(0, 0))
        self.lockingWrite.setMaximumSize(QtCore.QSize(25, 20))
        self.lockingWrite.setUseParentModel(True)
        self.lockingWrite.setAutoApply(True)
        self.lockingWrite.setForcedApply(True)
        self.lockingWrite.setObjectName(_fromUtf8("lockingWrite"))
        self.horizontalLayout.addWidget(self.lockingWrite)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        self.lockingLabel = QtGui.QLabel(self.plcGroup)
        self.lockingLabel.setObjectName(_fromUtf8("lockingLabel"))
        self.gridLayout.addWidget(self.lockingLabel, 2, 0, 1, 1)
        self.stateLabel = QtGui.QLabel(self.plcGroup)
        self.stateLabel.setObjectName(_fromUtf8("stateLabel"))
        self.gridLayout.addWidget(self.stateLabel, 3, 0, 1, 1)
        self.statusRead = TaurusLabel(self.plcGroup)
        self.statusRead.setMinimumSize(QtCore.QSize(200, 50))
        self.statusRead.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.statusRead.setUseParentModel(True)
        self.statusRead.setObjectName(_fromUtf8("statusRead"))
        self.gridLayout.addWidget(self.statusRead, 4, 1, 1, 1)
        self.heartbeatRead = TaurusLed(self.plcGroup)
        self.heartbeatRead.setMinimumSize(QtCore.QSize(25, 25))
        self.heartbeatRead.setMaximumSize(QtCore.QSize(25, 25))
        self.heartbeatRead.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignVCenter)
        self.heartbeatRead.setUseParentModel(True)
        self.heartbeatRead.setObjectName(_fromUtf8("heartbeatRead"))
        self.gridLayout.addWidget(self.heartbeatRead, 0, 1, 1, 1)
        self.heartbeatLabel = QtGui.QLabel(self.plcGroup)
        self.heartbeatLabel.setObjectName(_fromUtf8("heartbeatLabel"))
        self.gridLayout.addWidget(self.heartbeatLabel, 0, 0, 1, 1)
        self.lockerLabel = QtGui.QLabel(self.plcGroup)
        self.lockerLabel.setObjectName(_fromUtf8("lockerLabel"))
        self.gridLayout.addWidget(self.lockerLabel, 1, 0, 1, 1)
        self.lockerRead = TaurusLabel(self.plcGroup)
        self.lockerRead.setMinimumSize(QtCore.QSize(0, 25))
        self.lockerRead.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lockerRead.setUseParentModel(True)
        self.lockerRead.setObjectName(_fromUtf8("lockerRead"))
        self.gridLayout.addWidget(self.lockerRead, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.ResetState = TaurusCommandButton(self.plcGroup)
        self.ResetState.setMinimumSize(QtCore.QSize(0, 20))
        self.ResetState.setObjectName(_fromUtf8("ResetState"))
        self.gridLayout_2.addWidget(self.ResetState, 1, 0, 1, 1)
        self.instanceGroup = TaurusGroupBox(self.splitter)
        self.instanceGroup.setObjectName(_fromUtf8("instanceGroup"))
        self.gridLayout_4 = QtGui.QGridLayout(self.instanceGroup)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.instanceLayout = QtGui.QGridLayout()
        self.instanceLayout.setObjectName(_fromUtf8("instanceLayout"))
        self.instanceLocationLabel = QtGui.QLabel(self.instanceGroup)
        self.instanceLocationLabel.setObjectName(_fromUtf8("instanceLocationLabel"))
        self.instanceLayout.addWidget(self.instanceLocationLabel, 1, 0, 1, 1)
        self.moveLocal = TaurusCommandButton(self.instanceGroup)
        self.moveLocal.setMinimumSize(QtCore.QSize(0, 20))
        self.moveLocal.setObjectName(_fromUtf8("moveLocal"))
        self.instanceLayout.addWidget(self.moveLocal, 2, 1, 1, 1)
        self.instanceLocationRead = TaurusLabel(self.instanceGroup)
        self.instanceLocationRead.setMinimumSize(QtCore.QSize(25, 25))
        self.instanceLocationRead.setMaximumSize(QtCore.QSize(16777215, 25))
        self.instanceLocationRead.setObjectName(_fromUtf8("instanceLocationRead"))
        self.instanceLayout.addWidget(self.instanceLocationRead, 1, 1, 1, 2)
        self.instanceStateRead = TaurusLed(self.instanceGroup)
        self.instanceStateRead.setMinimumSize(QtCore.QSize(25, 25))
        self.instanceStateRead.setMaximumSize(QtCore.QSize(25, 25))
        self.instanceStateRead.setObjectName(_fromUtf8("instanceStateRead"))
        self.instanceLayout.addWidget(self.instanceStateRead, 0, 1, 1, 2)
        self.instanceStateLabel = QtGui.QLabel(self.instanceGroup)
        self.instanceStateLabel.setObjectName(_fromUtf8("instanceStateLabel"))
        self.instanceLayout.addWidget(self.instanceStateLabel, 0, 0, 1, 1)
        self.moveRemote = TaurusCommandButton(self.instanceGroup)
        self.moveRemote.setMinimumSize(QtCore.QSize(0, 20))
        self.moveRemote.setObjectName(_fromUtf8("moveRemote"))
        self.instanceLayout.addWidget(self.moveRemote, 2, 2, 1, 1)
        self.resetInstance = TaurusCommandButton(self.instanceGroup)
        self.resetInstance.setMinimumSize(QtCore.QSize(0, 20))
        self.resetInstance.setObjectName(_fromUtf8("resetInstance"))
        self.instanceLayout.addWidget(self.resetInstance, 2, 0, 1, 1)
        self.gridLayout_4.addLayout(self.instanceLayout, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.splitter, 0, 0, 1, 1)

        self.retranslateUi(linacPlcWidget)
        QtCore.QMetaObject.connectSlotsByName(linacPlcWidget)

    def retranslateUi(self, linacPlcWidget):
        linacPlcWidget.setWindowTitle(QtGui.QApplication.translate("linacPlcWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.plcGroup.setTitle(QtGui.QApplication.translate("linacPlcWidget", "PLC #", None, QtGui.QApplication.UnicodeUTF8))
        self.stateRead.setModel(QtGui.QApplication.translate("linacPlcWidget", "/state", None, QtGui.QApplication.UnicodeUTF8))
        self.statusLabel.setText(QtGui.QApplication.translate("linacPlcWidget", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.lockingRead.setModel(QtGui.QApplication.translate("linacPlcWidget", "/Locking", None, QtGui.QApplication.UnicodeUTF8))
        self.lockingWrite.setModel(QtGui.QApplication.translate("linacPlcWidget", "/Locking", None, QtGui.QApplication.UnicodeUTF8))
        self.lockingLabel.setText(QtGui.QApplication.translate("linacPlcWidget", "Locking", None, QtGui.QApplication.UnicodeUTF8))
        self.stateLabel.setText(QtGui.QApplication.translate("linacPlcWidget", "State", None, QtGui.QApplication.UnicodeUTF8))
        self.statusRead.setText(QtGui.QApplication.translate("linacPlcWidget", " 99.99", None, QtGui.QApplication.UnicodeUTF8))
        self.statusRead.setModel(QtGui.QApplication.translate("linacPlcWidget", "/status", None, QtGui.QApplication.UnicodeUTF8))
        self.statusRead.setBgRole(QtGui.QApplication.translate("linacPlcWidget", "state", None, QtGui.QApplication.UnicodeUTF8))
        self.heartbeatRead.setModel(QtGui.QApplication.translate("linacPlcWidget", "/HeartBeat", None, QtGui.QApplication.UnicodeUTF8))
        self.heartbeatLabel.setText(QtGui.QApplication.translate("linacPlcWidget", "Heartbeat", None, QtGui.QApplication.UnicodeUTF8))
        self.lockerLabel.setText(QtGui.QApplication.translate("linacPlcWidget", "Locker", None, QtGui.QApplication.UnicodeUTF8))
        self.lockerRead.setText(QtGui.QApplication.translate("linacPlcWidget", " 99.99", None, QtGui.QApplication.UnicodeUTF8))
        self.lockerRead.setModel(QtGui.QApplication.translate("linacPlcWidget", "/Lock_Status", None, QtGui.QApplication.UnicodeUTF8))
        self.instanceLocationLabel.setText(QtGui.QApplication.translate("linacPlcWidget", "Instance location", None, QtGui.QApplication.UnicodeUTF8))
        self.moveLocal.setText(QtGui.QApplication.translate("linacPlcWidget", "---", None, QtGui.QApplication.UnicodeUTF8))
        self.moveLocal.setCommand(QtGui.QApplication.translate("linacPlcWidget", "MoveInstance", None, QtGui.QApplication.UnicodeUTF8))
        self.instanceLocationRead.setText(QtGui.QApplication.translate("linacPlcWidget", " 99.99", None, QtGui.QApplication.UnicodeUTF8))
        self.instanceStateLabel.setText(QtGui.QApplication.translate("linacPlcWidget", "Instance state", None, QtGui.QApplication.UnicodeUTF8))
        self.moveRemote.setText(QtGui.QApplication.translate("linacPlcWidget", "---", None, QtGui.QApplication.UnicodeUTF8))
        self.moveRemote.setCommand(QtGui.QApplication.translate("linacPlcWidget", "MoveInstance", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.display import TaurusLed, TaurusLabel
from taurus.qt.qtgui.container import TaurusGroupBox
from taurus.qt.qtgui.panel import TaurusWidget
from taurus.qt.qtgui.button import TaurusCommandButton
from linacvaluecheckbox import LinacValueCheckBox
