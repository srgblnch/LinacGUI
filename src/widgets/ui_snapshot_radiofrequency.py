# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/ui/snapshot_radiofrequency.ui'
#
# Created: Wed Apr  9 13:20:46 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_radioFrequencySnapshot(object):
    def setupUi(self, radioFrequencySnapshot):
        radioFrequencySnapshot.setObjectName(_fromUtf8("radioFrequencySnapshot"))
        radioFrequencySnapshot.resize(299, 266)
        font = QtGui.QFont()
        font.setPointSize(7)
        radioFrequencySnapshot.setFont(font)
        self.gridLayout_2 = QtGui.QGridLayout(radioFrequencySnapshot)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.radioFrequencyGroup = TaurusGroupBox(radioFrequencySnapshot)
        self.radioFrequencyGroup.setObjectName(_fromUtf8("radioFrequencyGroup"))
        self.gridLayout = QtGui.QGridLayout(self.radioFrequencyGroup)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.PresentWriteTitle = QtGui.QLabel(self.radioFrequencyGroup)
        self.PresentWriteTitle.setObjectName(_fromUtf8("PresentWriteTitle"))
        self.gridLayout.addWidget(self.PresentWriteTitle, 0, 1, 1, 1)
        self.SaveRetrieveTitle = QtGui.QLabel(self.radioFrequencyGroup)
        self.SaveRetrieveTitle.setObjectName(_fromUtf8("SaveRetrieveTitle"))
        self.gridLayout.addWidget(self.SaveRetrieveTitle, 0, 2, 1, 1)
        self.TPS0PhaseLabel = QtGui.QLabel(self.radioFrequencyGroup)
        self.TPS0PhaseLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.TPS0PhaseLabel.setObjectName(_fromUtf8("TPS0PhaseLabel"))
        self.gridLayout.addWidget(self.TPS0PhaseLabel, 1, 0, 1, 1)
        self.TPS2PhaseWrite = QtGui.QDoubleSpinBox(self.radioFrequencyGroup)
        self.TPS2PhaseWrite.setMaximum(380.0)
        self.TPS2PhaseWrite.setSingleStep(0.1)
        self.TPS2PhaseWrite.setObjectName(_fromUtf8("TPS2PhaseWrite"))
        self.gridLayout.addWidget(self.TPS2PhaseWrite, 4, 2, 1, 1)
        self.PHS1Read = TaurusLabel(self.radioFrequencyGroup)
        self.PHS1Read.setObjectName(_fromUtf8("PHS1Read"))
        self.gridLayout.addWidget(self.PHS1Read, 8, 1, 1, 1)
        self.PHS2Read = TaurusLabel(self.radioFrequencyGroup)
        self.PHS2Read.setObjectName(_fromUtf8("PHS2Read"))
        self.gridLayout.addWidget(self.PHS2Read, 9, 1, 1, 1)
        self.A0OPWrite = QtGui.QDoubleSpinBox(self.radioFrequencyGroup)
        self.A0OPWrite.setMinimum(75.0)
        self.A0OPWrite.setMaximum(760.0)
        self.A0OPWrite.setObjectName(_fromUtf8("A0OPWrite"))
        self.gridLayout.addWidget(self.A0OPWrite, 5, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 10, 1, 1, 1)
        self.PHS2Write = QtGui.QDoubleSpinBox(self.radioFrequencyGroup)
        self.PHS2Write.setMaximum(380.0)
        self.PHS2Write.setObjectName(_fromUtf8("PHS2Write"))
        self.gridLayout.addWidget(self.PHS2Write, 9, 2, 1, 1)
        self.TPS0PhaseWrite = QtGui.QDoubleSpinBox(self.radioFrequencyGroup)
        self.TPS0PhaseWrite.setMaximum(380.0)
        self.TPS0PhaseWrite.setSingleStep(0.1)
        self.TPS0PhaseWrite.setObjectName(_fromUtf8("TPS0PhaseWrite"))
        self.gridLayout.addWidget(self.TPS0PhaseWrite, 1, 2, 1, 1)
        self.TPS1PhaseWrite = QtGui.QDoubleSpinBox(self.radioFrequencyGroup)
        self.TPS1PhaseWrite.setMaximum(380.0)
        self.TPS1PhaseWrite.setSingleStep(0.1)
        self.TPS1PhaseWrite.setObjectName(_fromUtf8("TPS1PhaseWrite"))
        self.gridLayout.addWidget(self.TPS1PhaseWrite, 3, 2, 1, 1)
        self.PHS1Write = QtGui.QDoubleSpinBox(self.radioFrequencyGroup)
        self.PHS1Write.setMaximum(160.0)
        self.PHS1Write.setObjectName(_fromUtf8("PHS1Write"))
        self.gridLayout.addWidget(self.PHS1Write, 8, 2, 1, 1)
        self.ATT2Read = TaurusLabel(self.radioFrequencyGroup)
        self.ATT2Read.setObjectName(_fromUtf8("ATT2Read"))
        self.gridLayout.addWidget(self.ATT2Read, 7, 1, 1, 1)
        self.ATT2Write = QtGui.QDoubleSpinBox(self.radioFrequencyGroup)
        self.ATT2Write.setMinimum(-10.0)
        self.ATT2Write.setMaximum(0.0)
        self.ATT2Write.setSingleStep(0.1)
        self.ATT2Write.setObjectName(_fromUtf8("ATT2Write"))
        self.gridLayout.addWidget(self.ATT2Write, 7, 2, 1, 1)
        self.A0OPRead = TaurusLabel(self.radioFrequencyGroup)
        self.A0OPRead.setObjectName(_fromUtf8("A0OPRead"))
        self.gridLayout.addWidget(self.A0OPRead, 5, 1, 1, 1)
        self.TPS2PhaseRead = TaurusLabel(self.radioFrequencyGroup)
        self.TPS2PhaseRead.setObjectName(_fromUtf8("TPS2PhaseRead"))
        self.gridLayout.addWidget(self.TPS2PhaseRead, 4, 1, 1, 1)
        self.TPSXPhaseRead = TaurusLabel(self.radioFrequencyGroup)
        self.TPSXPhaseRead.setObjectName(_fromUtf8("TPSXPhaseRead"))
        self.gridLayout.addWidget(self.TPSXPhaseRead, 2, 1, 1, 1)
        self.TPS1PhaseRead = TaurusLabel(self.radioFrequencyGroup)
        self.TPS1PhaseRead.setObjectName(_fromUtf8("TPS1PhaseRead"))
        self.gridLayout.addWidget(self.TPS1PhaseRead, 3, 1, 1, 1)
        self.TPS0PhaseCheck = QtGui.QCheckBox(self.radioFrequencyGroup)
        self.TPS0PhaseCheck.setText(_fromUtf8(""))
        self.TPS0PhaseCheck.setObjectName(_fromUtf8("TPS0PhaseCheck"))
        self.gridLayout.addWidget(self.TPS0PhaseCheck, 1, 4, 1, 1)
        self.PHS1Check = QtGui.QCheckBox(self.radioFrequencyGroup)
        self.PHS1Check.setText(_fromUtf8(""))
        self.PHS1Check.setObjectName(_fromUtf8("PHS1Check"))
        self.gridLayout.addWidget(self.PHS1Check, 8, 4, 1, 1)
        self.TPS1PhaseCheck = QtGui.QCheckBox(self.radioFrequencyGroup)
        self.TPS1PhaseCheck.setText(_fromUtf8(""))
        self.TPS1PhaseCheck.setObjectName(_fromUtf8("TPS1PhaseCheck"))
        self.gridLayout.addWidget(self.TPS1PhaseCheck, 3, 4, 1, 1)
        self.TPS0PhaseRead = TaurusLabel(self.radioFrequencyGroup)
        self.TPS0PhaseRead.setObjectName(_fromUtf8("TPS0PhaseRead"))
        self.gridLayout.addWidget(self.TPS0PhaseRead, 1, 1, 1, 1)
        self.TPSXPhaseWrite = QtGui.QDoubleSpinBox(self.radioFrequencyGroup)
        self.TPSXPhaseWrite.setMaximum(380.0)
        self.TPSXPhaseWrite.setSingleStep(0.1)
        self.TPSXPhaseWrite.setObjectName(_fromUtf8("TPSXPhaseWrite"))
        self.gridLayout.addWidget(self.TPSXPhaseWrite, 2, 2, 1, 1)
        self.TPS2PhaseCheck = QtGui.QCheckBox(self.radioFrequencyGroup)
        self.TPS2PhaseCheck.setText(_fromUtf8(""))
        self.TPS2PhaseCheck.setObjectName(_fromUtf8("TPS2PhaseCheck"))
        self.gridLayout.addWidget(self.TPS2PhaseCheck, 4, 4, 1, 1)
        self.TPSXPhaseCheck = QtGui.QCheckBox(self.radioFrequencyGroup)
        self.TPSXPhaseCheck.setText(_fromUtf8(""))
        self.TPSXPhaseCheck.setObjectName(_fromUtf8("TPSXPhaseCheck"))
        self.gridLayout.addWidget(self.TPSXPhaseCheck, 2, 4, 1, 1)
        self.A0OPCheck = QtGui.QCheckBox(self.radioFrequencyGroup)
        self.A0OPCheck.setText(_fromUtf8(""))
        self.A0OPCheck.setObjectName(_fromUtf8("A0OPCheck"))
        self.gridLayout.addWidget(self.A0OPCheck, 5, 4, 1, 1)
        self.TPSXPhaseLabel = QtGui.QLabel(self.radioFrequencyGroup)
        self.TPSXPhaseLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.TPSXPhaseLabel.setObjectName(_fromUtf8("TPSXPhaseLabel"))
        self.gridLayout.addWidget(self.TPSXPhaseLabel, 2, 0, 1, 1)
        self.TPS1PhaseLabel = QtGui.QLabel(self.radioFrequencyGroup)
        self.TPS1PhaseLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.TPS1PhaseLabel.setObjectName(_fromUtf8("TPS1PhaseLabel"))
        self.gridLayout.addWidget(self.TPS1PhaseLabel, 3, 0, 1, 1)
        self.TPS2PhaseLabel = QtGui.QLabel(self.radioFrequencyGroup)
        self.TPS2PhaseLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.TPS2PhaseLabel.setObjectName(_fromUtf8("TPS2PhaseLabel"))
        self.gridLayout.addWidget(self.TPS2PhaseLabel, 4, 0, 1, 1)
        self.A0OPLabel = QtGui.QLabel(self.radioFrequencyGroup)
        self.A0OPLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.A0OPLabel.setObjectName(_fromUtf8("A0OPLabel"))
        self.gridLayout.addWidget(self.A0OPLabel, 5, 0, 1, 1)
        self.PHS1Label = QtGui.QLabel(self.radioFrequencyGroup)
        self.PHS1Label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PHS1Label.setObjectName(_fromUtf8("PHS1Label"))
        self.gridLayout.addWidget(self.PHS1Label, 8, 0, 1, 1)
        self.ATT2Check = QtGui.QCheckBox(self.radioFrequencyGroup)
        self.ATT2Check.setText(_fromUtf8(""))
        self.ATT2Check.setObjectName(_fromUtf8("ATT2Check"))
        self.gridLayout.addWidget(self.ATT2Check, 7, 4, 1, 1)
        self.ATT2Label = QtGui.QLabel(self.radioFrequencyGroup)
        self.ATT2Label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ATT2Label.setObjectName(_fromUtf8("ATT2Label"))
        self.gridLayout.addWidget(self.ATT2Label, 7, 0, 1, 1)
        self.PHS2Label = QtGui.QLabel(self.radioFrequencyGroup)
        self.PHS2Label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PHS2Label.setObjectName(_fromUtf8("PHS2Label"))
        self.gridLayout.addWidget(self.PHS2Label, 9, 0, 1, 1)
        self.PHS2Check = QtGui.QCheckBox(self.radioFrequencyGroup)
        self.PHS2Check.setText(_fromUtf8(""))
        self.PHS2Check.setObjectName(_fromUtf8("PHS2Check"))
        self.gridLayout.addWidget(self.PHS2Check, 9, 4, 1, 1)
        self.line = QtGui.QFrame(self.radioFrequencyGroup)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 1, 3, 9, 1)
        self.gridLayout_2.addWidget(self.radioFrequencyGroup, 0, 0, 1, 1)

        self.retranslateUi(radioFrequencySnapshot)
        QtCore.QMetaObject.connectSlotsByName(radioFrequencySnapshot)

    def retranslateUi(self, radioFrequencySnapshot):
        radioFrequencySnapshot.setWindowTitle(QtGui.QApplication.translate("radioFrequencySnapshot", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.radioFrequencyGroup.setTitle(QtGui.QApplication.translate("radioFrequencySnapshot", "Radio Frequency", None, QtGui.QApplication.UnicodeUTF8))
        self.PresentWriteTitle.setText(QtGui.QApplication.translate("radioFrequencySnapshot", "Present value", None, QtGui.QApplication.UnicodeUTF8))
        self.SaveRetrieveTitle.setText(QtGui.QApplication.translate("radioFrequencySnapshot", "Save/Retrieve", None, QtGui.QApplication.UnicodeUTF8))
        self.TPS0PhaseLabel.setText(QtGui.QApplication.translate("radioFrequencySnapshot", "Time Phase Shifter 0", None, QtGui.QApplication.UnicodeUTF8))
        self.TPSXPhaseLabel.setText(QtGui.QApplication.translate("radioFrequencySnapshot", "Time Phase Shifter X", None, QtGui.QApplication.UnicodeUTF8))
        self.TPS1PhaseLabel.setText(QtGui.QApplication.translate("radioFrequencySnapshot", "Time Phase Shifter 1", None, QtGui.QApplication.UnicodeUTF8))
        self.TPS2PhaseLabel.setText(QtGui.QApplication.translate("radioFrequencySnapshot", "Time Phase Shifter 2", None, QtGui.QApplication.UnicodeUTF8))
        self.A0OPLabel.setText(QtGui.QApplication.translate("radioFrequencySnapshot", "A0 output power", None, QtGui.QApplication.UnicodeUTF8))
        self.PHS1Label.setText(QtGui.QApplication.translate("radioFrequencySnapshot", "Phase Shifter 1", None, QtGui.QApplication.UnicodeUTF8))
        self.ATT2Label.setText(QtGui.QApplication.translate("radioFrequencySnapshot", "Attenuator 2", None, QtGui.QApplication.UnicodeUTF8))
        self.PHS2Label.setText(QtGui.QApplication.translate("radioFrequencySnapshot", "Phase Shifter 2", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.display import TaurusLabel
from taurus.qt.qtgui.container import TaurusGroupBox
from taurus.qt.qtgui.panel import TaurusWidget
