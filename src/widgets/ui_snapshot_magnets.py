# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/ui/snapshot_magnets.ui'
#
# Created: Thu Apr 10 14:20:39 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_magnetSnapshot(object):
    def setupUi(self, magnetSnapshot):
        magnetSnapshot.setObjectName(_fromUtf8("magnetSnapshot"))
        magnetSnapshot.resize(272, 808)
        font = QtGui.QFont()
        font.setPointSize(7)
        magnetSnapshot.setFont(font)
        self.gridLayout_2 = QtGui.QGridLayout(magnetSnapshot)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.magnetsGroup = TaurusGroupBox(magnetSnapshot)
        self.magnetsGroup.setObjectName(_fromUtf8("magnetsGroup"))
        self.gridLayout = QtGui.QGridLayout(self.magnetsGroup)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.as1HLabel = QtGui.QLabel(self.magnetsGroup)
        self.as1HLabel.setObjectName(_fromUtf8("as1HLabel"))
        self.gridLayout.addWidget(self.as1HLabel, 22, 0, 1, 1)
        self.qt1HCheck = QtGui.QCheckBox(self.magnetsGroup)
        self.qt1HCheck.setText(_fromUtf8(""))
        self.qt1HCheck.setObjectName(_fromUtf8("qt1HCheck"))
        self.gridLayout.addWidget(self.qt1HCheck, 24, 5, 1, 1)
        self.as2VCheck = QtGui.QCheckBox(self.magnetsGroup)
        self.as2VCheck.setText(_fromUtf8(""))
        self.as2VCheck.setObjectName(_fromUtf8("as2VCheck"))
        self.gridLayout.addWidget(self.as2VCheck, 29, 5, 1, 1)
        self.qt1FWrite = QtGui.QDoubleSpinBox(self.magnetsGroup)
        self.qt1FWrite.setMaximum(6.0)
        self.qt1FWrite.setSingleStep(0.005)
        self.qt1FWrite.setObjectName(_fromUtf8("qt1FWrite"))
        self.gridLayout.addWidget(self.qt1FWrite, 26, 2, 1, 1)
        self.bc2HRead = TaurusLabel(self.magnetsGroup)
        self.bc2HRead.setObjectName(_fromUtf8("bc2HRead"))
        self.gridLayout.addWidget(self.bc2HRead, 16, 1, 1, 1)
        self.glHWrite = QtGui.QDoubleSpinBox(self.magnetsGroup)
        self.glHWrite.setMinimum(-2.0)
        self.glHWrite.setMaximum(2.0)
        self.glHWrite.setSingleStep(0.01)
        self.glHWrite.setObjectName(_fromUtf8("glHWrite"))
        self.gridLayout.addWidget(self.glHWrite, 19, 2, 1, 1)
        self.glHRead = TaurusLabel(self.magnetsGroup)
        self.glHRead.setObjectName(_fromUtf8("glHRead"))
        self.gridLayout.addWidget(self.glHRead, 19, 1, 1, 1)
        self.as2VWrite = QtGui.QDoubleSpinBox(self.magnetsGroup)
        self.as2VWrite.setMinimum(-2.0)
        self.as2VWrite.setMaximum(2.0)
        self.as2VWrite.setSingleStep(0.01)
        self.as2VWrite.setObjectName(_fromUtf8("as2VWrite"))
        self.gridLayout.addWidget(self.as2VWrite, 29, 2, 1, 1)
        self.glVCheck = QtGui.QCheckBox(self.magnetsGroup)
        self.glVCheck.setText(_fromUtf8(""))
        self.glVCheck.setObjectName(_fromUtf8("glVCheck"))
        self.gridLayout.addWidget(self.glVCheck, 20, 5, 1, 1)
        self.bc2FWrite = QtGui.QDoubleSpinBox(self.magnetsGroup)
        self.bc2FWrite.setMaximum(200.0)
        self.bc2FWrite.setSingleStep(0.01)
        self.bc2FWrite.setObjectName(_fromUtf8("bc2FWrite"))
        self.gridLayout.addWidget(self.bc2FWrite, 18, 2, 1, 1)
        self.qt1VCheck = QtGui.QCheckBox(self.magnetsGroup)
        self.qt1VCheck.setText(_fromUtf8(""))
        self.qt1VCheck.setObjectName(_fromUtf8("qt1VCheck"))
        self.gridLayout.addWidget(self.qt1VCheck, 25, 5, 1, 1)
        self.as2VRead = TaurusLabel(self.magnetsGroup)
        self.as2VRead.setObjectName(_fromUtf8("as2VRead"))
        self.gridLayout.addWidget(self.as2VRead, 29, 1, 1, 1)
        self.glVRead = TaurusLabel(self.magnetsGroup)
        self.glVRead.setObjectName(_fromUtf8("glVRead"))
        self.gridLayout.addWidget(self.glVRead, 20, 1, 1, 1)
        self.bc2HLabel = QtGui.QLabel(self.magnetsGroup)
        self.bc2HLabel.setObjectName(_fromUtf8("bc2HLabel"))
        self.gridLayout.addWidget(self.bc2HLabel, 16, 0, 1, 1)
        self.qt1VRead = TaurusLabel(self.magnetsGroup)
        self.qt1VRead.setObjectName(_fromUtf8("qt1VRead"))
        self.gridLayout.addWidget(self.qt1VRead, 25, 1, 1, 1)
        self.qt1FCheck = QtGui.QCheckBox(self.magnetsGroup)
        self.qt1FCheck.setText(_fromUtf8(""))
        self.qt1FCheck.setObjectName(_fromUtf8("qt1FCheck"))
        self.gridLayout.addWidget(self.qt1FCheck, 26, 5, 1, 1)
        self.glHCheck = QtGui.QCheckBox(self.magnetsGroup)
        self.glHCheck.setText(_fromUtf8(""))
        self.glHCheck.setObjectName(_fromUtf8("glHCheck"))
        self.gridLayout.addWidget(self.glHCheck, 19, 5, 1, 1)
        self.as2HCheck = QtGui.QCheckBox(self.magnetsGroup)
        self.as2HCheck.setText(_fromUtf8(""))
        self.as2HCheck.setObjectName(_fromUtf8("as2HCheck"))
        self.gridLayout.addWidget(self.as2HCheck, 28, 5, 1, 1)
        self.qt2FRead = TaurusLabel(self.magnetsGroup)
        self.qt2FRead.setObjectName(_fromUtf8("qt2FRead"))
        self.gridLayout.addWidget(self.qt2FRead, 27, 1, 1, 1)
        self.as1HCheck = QtGui.QCheckBox(self.magnetsGroup)
        self.as1HCheck.setText(_fromUtf8(""))
        self.as1HCheck.setObjectName(_fromUtf8("as1HCheck"))
        self.gridLayout.addWidget(self.as1HCheck, 22, 5, 1, 1)
        self.as1VWrite = QtGui.QDoubleSpinBox(self.magnetsGroup)
        self.as1VWrite.setMinimum(-2.0)
        self.as1VWrite.setMaximum(2.0)
        self.as1VWrite.setSingleStep(0.01)
        self.as1VWrite.setObjectName(_fromUtf8("as1VWrite"))
        self.gridLayout.addWidget(self.as1VWrite, 23, 2, 1, 1)
        self.glFCheck = QtGui.QCheckBox(self.magnetsGroup)
        self.glFCheck.setText(_fromUtf8(""))
        self.glFCheck.setObjectName(_fromUtf8("glFCheck"))
        self.gridLayout.addWidget(self.glFCheck, 21, 5, 1, 1)
        self.qt1HLabel = QtGui.QLabel(self.magnetsGroup)
        self.qt1HLabel.setObjectName(_fromUtf8("qt1HLabel"))
        self.gridLayout.addWidget(self.qt1HLabel, 24, 0, 1, 1)
        self.glVWrite = QtGui.QDoubleSpinBox(self.magnetsGroup)
        self.glVWrite.setMinimum(-2.0)
        self.glVWrite.setMaximum(2.0)
        self.glVWrite.setSingleStep(0.01)
        self.glVWrite.setObjectName(_fromUtf8("glVWrite"))
        self.gridLayout.addWidget(self.glVWrite, 20, 2, 1, 1)
        self.bc2VRead = TaurusLabel(self.magnetsGroup)
        self.bc2VRead.setObjectName(_fromUtf8("bc2VRead"))
        self.gridLayout.addWidget(self.bc2VRead, 17, 1, 1, 1)
        self.as1VCheck = QtGui.QCheckBox(self.magnetsGroup)
        self.as1VCheck.setText(_fromUtf8(""))
        self.as1VCheck.setObjectName(_fromUtf8("as1VCheck"))
        self.gridLayout.addWidget(self.as1VCheck, 23, 5, 1, 1)
        self.as1HRead = TaurusLabel(self.magnetsGroup)
        self.as1HRead.setObjectName(_fromUtf8("as1HRead"))
        self.gridLayout.addWidget(self.as1HRead, 22, 1, 1, 1)
        self.bc2FCheck = QtGui.QCheckBox(self.magnetsGroup)
        self.bc2FCheck.setText(_fromUtf8(""))
        self.bc2FCheck.setObjectName(_fromUtf8("bc2FCheck"))
        self.gridLayout.addWidget(self.bc2FCheck, 18, 5, 1, 1)
        self.bc2HCheck = QtGui.QCheckBox(self.magnetsGroup)
        self.bc2HCheck.setText(_fromUtf8(""))
        self.bc2HCheck.setObjectName(_fromUtf8("bc2HCheck"))
        self.gridLayout.addWidget(self.bc2HCheck, 16, 5, 1, 1)
        self.glFLabel = QtGui.QLabel(self.magnetsGroup)
        self.glFLabel.setObjectName(_fromUtf8("glFLabel"))
        self.gridLayout.addWidget(self.glFLabel, 21, 0, 1, 1)
        self.bc2FRead = TaurusLabel(self.magnetsGroup)
        self.bc2FRead.setObjectName(_fromUtf8("bc2FRead"))
        self.gridLayout.addWidget(self.bc2FRead, 18, 1, 1, 1)
        self.qt2FCheck = QtGui.QCheckBox(self.magnetsGroup)
        self.qt2FCheck.setText(_fromUtf8(""))
        self.qt2FCheck.setObjectName(_fromUtf8("qt2FCheck"))
        self.gridLayout.addWidget(self.qt2FCheck, 27, 5, 1, 1)
        self.as2VLabel = QtGui.QLabel(self.magnetsGroup)
        self.as2VLabel.setObjectName(_fromUtf8("as2VLabel"))
        self.gridLayout.addWidget(self.as2VLabel, 29, 0, 1, 1)
        self.as2HLabel = QtGui.QLabel(self.magnetsGroup)
        self.as2HLabel.setObjectName(_fromUtf8("as2HLabel"))
        self.gridLayout.addWidget(self.as2HLabel, 28, 0, 1, 1)
        self.glHLabel = QtGui.QLabel(self.magnetsGroup)
        self.glHLabel.setObjectName(_fromUtf8("glHLabel"))
        self.gridLayout.addWidget(self.glHLabel, 19, 0, 1, 1)
        self.qt1VWrite = QtGui.QDoubleSpinBox(self.magnetsGroup)
        self.qt1VWrite.setMinimum(-16.0)
        self.qt1VWrite.setMaximum(16.0)
        self.qt1VWrite.setSingleStep(0.01)
        self.qt1VWrite.setObjectName(_fromUtf8("qt1VWrite"))
        self.gridLayout.addWidget(self.qt1VWrite, 25, 2, 1, 1)
        self.qt2FLabel = QtGui.QLabel(self.magnetsGroup)
        self.qt2FLabel.setObjectName(_fromUtf8("qt2FLabel"))
        self.gridLayout.addWidget(self.qt2FLabel, 27, 0, 1, 1)
        self.bc2HWrite = QtGui.QDoubleSpinBox(self.magnetsGroup)
        self.bc2HWrite.setMinimum(-2.0)
        self.bc2HWrite.setMaximum(2.0)
        self.bc2HWrite.setSingleStep(0.01)
        self.bc2HWrite.setProperty("value", 0.0)
        self.bc2HWrite.setObjectName(_fromUtf8("bc2HWrite"))
        self.gridLayout.addWidget(self.bc2HWrite, 16, 2, 1, 1)
        self.qt1FRead = TaurusLabel(self.magnetsGroup)
        self.qt1FRead.setObjectName(_fromUtf8("qt1FRead"))
        self.gridLayout.addWidget(self.qt1FRead, 26, 1, 1, 1)
        self.glVLabel = QtGui.QLabel(self.magnetsGroup)
        self.glVLabel.setObjectName(_fromUtf8("glVLabel"))
        self.gridLayout.addWidget(self.glVLabel, 20, 0, 1, 1)
        self.bc2FLabel = QtGui.QLabel(self.magnetsGroup)
        self.bc2FLabel.setObjectName(_fromUtf8("bc2FLabel"))
        self.gridLayout.addWidget(self.bc2FLabel, 18, 0, 1, 1)
        self.glFRead = TaurusLabel(self.magnetsGroup)
        self.glFRead.setObjectName(_fromUtf8("glFRead"))
        self.gridLayout.addWidget(self.glFRead, 21, 1, 1, 1)
        self.as2HRead = TaurusLabel(self.magnetsGroup)
        self.as2HRead.setObjectName(_fromUtf8("as2HRead"))
        self.gridLayout.addWidget(self.as2HRead, 28, 1, 1, 1)
        self.glFWrite = QtGui.QDoubleSpinBox(self.magnetsGroup)
        self.glFWrite.setMaximum(130.0)
        self.glFWrite.setSingleStep(0.01)
        self.glFWrite.setObjectName(_fromUtf8("glFWrite"))
        self.gridLayout.addWidget(self.glFWrite, 21, 2, 1, 1)
        self.qt1HWrite = QtGui.QDoubleSpinBox(self.magnetsGroup)
        self.qt1HWrite.setMinimum(-16.0)
        self.qt1HWrite.setMaximum(16.0)
        self.qt1HWrite.setSingleStep(0.01)
        self.qt1HWrite.setObjectName(_fromUtf8("qt1HWrite"))
        self.gridLayout.addWidget(self.qt1HWrite, 24, 2, 1, 1)
        self.bc2VLabel = QtGui.QLabel(self.magnetsGroup)
        self.bc2VLabel.setObjectName(_fromUtf8("bc2VLabel"))
        self.gridLayout.addWidget(self.bc2VLabel, 17, 0, 1, 1)
        self.bc2VCheck = QtGui.QCheckBox(self.magnetsGroup)
        self.bc2VCheck.setText(_fromUtf8(""))
        self.bc2VCheck.setObjectName(_fromUtf8("bc2VCheck"))
        self.gridLayout.addWidget(self.bc2VCheck, 17, 5, 1, 1)
        self.as1VLabel = QtGui.QLabel(self.magnetsGroup)
        self.as1VLabel.setObjectName(_fromUtf8("as1VLabel"))
        self.gridLayout.addWidget(self.as1VLabel, 23, 0, 1, 1)
        self.qt1HRead = TaurusLabel(self.magnetsGroup)
        self.qt1HRead.setObjectName(_fromUtf8("qt1HRead"))
        self.gridLayout.addWidget(self.qt1HRead, 24, 1, 1, 1)
        self.qt1FLabel = QtGui.QLabel(self.magnetsGroup)
        self.qt1FLabel.setObjectName(_fromUtf8("qt1FLabel"))
        self.gridLayout.addWidget(self.qt1FLabel, 26, 0, 1, 1)
        self.qt2FWrite = QtGui.QDoubleSpinBox(self.magnetsGroup)
        self.qt2FWrite.setMaximum(6.0)
        self.qt2FWrite.setSingleStep(0.005)
        self.qt2FWrite.setObjectName(_fromUtf8("qt2FWrite"))
        self.gridLayout.addWidget(self.qt2FWrite, 27, 2, 1, 1)
        self.as1VRead = TaurusLabel(self.magnetsGroup)
        self.as1VRead.setObjectName(_fromUtf8("as1VRead"))
        self.gridLayout.addWidget(self.as1VRead, 23, 1, 1, 1)
        self.as1HWrite = QtGui.QDoubleSpinBox(self.magnetsGroup)
        self.as1HWrite.setMinimum(-2.0)
        self.as1HWrite.setMaximum(2.0)
        self.as1HWrite.setSingleStep(0.01)
        self.as1HWrite.setObjectName(_fromUtf8("as1HWrite"))
        self.gridLayout.addWidget(self.as1HWrite, 22, 2, 1, 1)
        self.bc2VWrite = QtGui.QDoubleSpinBox(self.magnetsGroup)
        self.bc2VWrite.setMinimum(-2.0)
        self.bc2VWrite.setMaximum(2.0)
        self.bc2VWrite.setSingleStep(0.01)
        self.bc2VWrite.setObjectName(_fromUtf8("bc2VWrite"))
        self.gridLayout.addWidget(self.bc2VWrite, 17, 2, 1, 1)
        self.sl2HRead = TaurusLabel(self.magnetsGroup)
        self.sl2HRead.setObjectName(_fromUtf8("sl2HRead"))
        self.gridLayout.addWidget(self.sl2HRead, 4, 1, 1, 1)
        self.as2HWrite = QtGui.QDoubleSpinBox(self.magnetsGroup)
        self.as2HWrite.setMinimum(-2.0)
        self.as2HWrite.setMaximum(2.0)
        self.as2HWrite.setSingleStep(0.01)
        self.as2HWrite.setObjectName(_fromUtf8("as2HWrite"))
        self.gridLayout.addWidget(self.as2HWrite, 28, 2, 1, 1)
        self.qt1VLabel = QtGui.QLabel(self.magnetsGroup)
        self.qt1VLabel.setObjectName(_fromUtf8("qt1VLabel"))
        self.gridLayout.addWidget(self.qt1VLabel, 25, 0, 1, 1)
        self.sl4VLabel = QtGui.QLabel(self.magnetsGroup)
        self.sl4VLabel.setObjectName(_fromUtf8("sl4VLabel"))
        self.gridLayout.addWidget(self.sl4VLabel, 11, 0, 1, 1)
        self.sl4FWrite = QtGui.QDoubleSpinBox(self.magnetsGroup)
        self.sl4FWrite.setMaximum(1.0)
        self.sl4FWrite.setSingleStep(0.01)
        self.sl4FWrite.setObjectName(_fromUtf8("sl4FWrite"))
        self.gridLayout.addWidget(self.sl4FWrite, 12, 2, 1, 1)
        self.sl4HRead = TaurusLabel(self.magnetsGroup)
        self.sl4HRead.setObjectName(_fromUtf8("sl4HRead"))
        self.gridLayout.addWidget(self.sl4HRead, 10, 1, 1, 1)
        self.sl4FRead = TaurusLabel(self.magnetsGroup)
        self.sl4FRead.setObjectName(_fromUtf8("sl4FRead"))
        self.gridLayout.addWidget(self.sl4FRead, 12, 1, 1, 1)
        self.sl4HLabel = QtGui.QLabel(self.magnetsGroup)
        self.sl4HLabel.setObjectName(_fromUtf8("sl4HLabel"))
        self.gridLayout.addWidget(self.sl4HLabel, 10, 0, 1, 1)
        self.sl4VCheck = QtGui.QCheckBox(self.magnetsGroup)
        self.sl4VCheck.setText(_fromUtf8(""))
        self.sl4VCheck.setObjectName(_fromUtf8("sl4VCheck"))
        self.gridLayout.addWidget(self.sl4VCheck, 11, 5, 1, 1)
        self.sl4HCheck = QtGui.QCheckBox(self.magnetsGroup)
        self.sl4HCheck.setText(_fromUtf8(""))
        self.sl4HCheck.setObjectName(_fromUtf8("sl4HCheck"))
        self.gridLayout.addWidget(self.sl4HCheck, 10, 5, 1, 1)
        self.sl4VRead = TaurusLabel(self.magnetsGroup)
        self.sl4VRead.setObjectName(_fromUtf8("sl4VRead"))
        self.gridLayout.addWidget(self.sl4VRead, 11, 1, 1, 1)
        self.sl4VWrite = QtGui.QDoubleSpinBox(self.magnetsGroup)
        self.sl4VWrite.setMinimum(-2.0)
        self.sl4VWrite.setMaximum(2.0)
        self.sl4VWrite.setSingleStep(0.01)
        self.sl4VWrite.setObjectName(_fromUtf8("sl4VWrite"))
        self.gridLayout.addWidget(self.sl4VWrite, 11, 2, 1, 1)
        self.sl4FLabel = QtGui.QLabel(self.magnetsGroup)
        self.sl4FLabel.setObjectName(_fromUtf8("sl4FLabel"))
        self.gridLayout.addWidget(self.sl4FLabel, 12, 0, 1, 1)
        self.sl3VRead = TaurusLabel(self.magnetsGroup)
        self.sl3VRead.setObjectName(_fromUtf8("sl3VRead"))
        self.gridLayout.addWidget(self.sl3VRead, 8, 1, 1, 1)
        self.sl3VCheck = QtGui.QCheckBox(self.magnetsGroup)
        self.sl3VCheck.setText(_fromUtf8(""))
        self.sl3VCheck.setObjectName(_fromUtf8("sl3VCheck"))
        self.gridLayout.addWidget(self.sl3VCheck, 8, 5, 1, 1)
        self.SaveRetrieveTitle = QtGui.QLabel(self.magnetsGroup)
        self.SaveRetrieveTitle.setObjectName(_fromUtf8("SaveRetrieveTitle"))
        self.gridLayout.addWidget(self.SaveRetrieveTitle, 0, 2, 1, 1)
        self.sl3HWrite = QtGui.QDoubleSpinBox(self.magnetsGroup)
        self.sl3HWrite.setMinimum(-2.0)
        self.sl3HWrite.setMaximum(2.0)
        self.sl3HWrite.setSingleStep(0.01)
        self.sl3HWrite.setObjectName(_fromUtf8("sl3HWrite"))
        self.gridLayout.addWidget(self.sl3HWrite, 7, 2, 1, 1)
        self.sl1HCheck = QtGui.QCheckBox(self.magnetsGroup)
        self.sl1HCheck.setText(_fromUtf8(""))
        self.sl1HCheck.setObjectName(_fromUtf8("sl1HCheck"))
        self.gridLayout.addWidget(self.sl1HCheck, 1, 5, 1, 1)
        self.sl3VWrite = QtGui.QDoubleSpinBox(self.magnetsGroup)
        self.sl3VWrite.setMinimum(-2.0)
        self.sl3VWrite.setMaximum(2.0)
        self.sl3VWrite.setSingleStep(0.01)
        self.sl3VWrite.setObjectName(_fromUtf8("sl3VWrite"))
        self.gridLayout.addWidget(self.sl3VWrite, 8, 2, 1, 1)
        self.sl2VCheck = QtGui.QCheckBox(self.magnetsGroup)
        self.sl2VCheck.setText(_fromUtf8(""))
        self.sl2VCheck.setObjectName(_fromUtf8("sl2VCheck"))
        self.gridLayout.addWidget(self.sl2VCheck, 5, 5, 1, 1)
        self.sl3HCheck = QtGui.QCheckBox(self.magnetsGroup)
        self.sl3HCheck.setText(_fromUtf8(""))
        self.sl3HCheck.setObjectName(_fromUtf8("sl3HCheck"))
        self.gridLayout.addWidget(self.sl3HCheck, 7, 5, 1, 1)
        self.sl3FLabel = QtGui.QLabel(self.magnetsGroup)
        self.sl3FLabel.setObjectName(_fromUtf8("sl3FLabel"))
        self.gridLayout.addWidget(self.sl3FLabel, 9, 0, 1, 1)
        self.sl2HWrite = QtGui.QDoubleSpinBox(self.magnetsGroup)
        self.sl2HWrite.setMinimum(-2.0)
        self.sl2HWrite.setMaximum(2.0)
        self.sl2HWrite.setSingleStep(0.01)
        self.sl2HWrite.setObjectName(_fromUtf8("sl2HWrite"))
        self.gridLayout.addWidget(self.sl2HWrite, 4, 2, 1, 1)
        self.sl2VWrite = QtGui.QDoubleSpinBox(self.magnetsGroup)
        self.sl2VWrite.setMinimum(-2.0)
        self.sl2VWrite.setMaximum(2.0)
        self.sl2VWrite.setSingleStep(0.01)
        self.sl2VWrite.setProperty("value", 0.0)
        self.sl2VWrite.setObjectName(_fromUtf8("sl2VWrite"))
        self.gridLayout.addWidget(self.sl2VWrite, 5, 2, 1, 1)
        self.sl1HRead = TaurusLabel(self.magnetsGroup)
        self.sl1HRead.setObjectName(_fromUtf8("sl1HRead"))
        self.gridLayout.addWidget(self.sl1HRead, 1, 1, 1, 1)
        self.sl1FLabel = QtGui.QLabel(self.magnetsGroup)
        self.sl1FLabel.setObjectName(_fromUtf8("sl1FLabel"))
        self.gridLayout.addWidget(self.sl1FLabel, 3, 0, 1, 1)
        self.PresentWriteTitle = QtGui.QLabel(self.magnetsGroup)
        self.PresentWriteTitle.setObjectName(_fromUtf8("PresentWriteTitle"))
        self.gridLayout.addWidget(self.PresentWriteTitle, 0, 1, 1, 1)
        self.sl2FRead = TaurusLabel(self.magnetsGroup)
        self.sl2FRead.setObjectName(_fromUtf8("sl2FRead"))
        self.gridLayout.addWidget(self.sl2FRead, 6, 1, 1, 1)
        self.sl1VCheck = QtGui.QCheckBox(self.magnetsGroup)
        self.sl1VCheck.setText(_fromUtf8(""))
        self.sl1VCheck.setObjectName(_fromUtf8("sl1VCheck"))
        self.gridLayout.addWidget(self.sl1VCheck, 2, 5, 1, 1)
        self.sl2HCheck = QtGui.QCheckBox(self.magnetsGroup)
        self.sl2HCheck.setText(_fromUtf8(""))
        self.sl2HCheck.setObjectName(_fromUtf8("sl2HCheck"))
        self.gridLayout.addWidget(self.sl2HCheck, 4, 5, 1, 1)
        self.sl2HLabel = QtGui.QLabel(self.magnetsGroup)
        self.sl2HLabel.setObjectName(_fromUtf8("sl2HLabel"))
        self.gridLayout.addWidget(self.sl2HLabel, 4, 0, 1, 1)
        self.sl3HLabel = QtGui.QLabel(self.magnetsGroup)
        self.sl3HLabel.setObjectName(_fromUtf8("sl3HLabel"))
        self.gridLayout.addWidget(self.sl3HLabel, 7, 0, 1, 1)
        self.sl2VLabel = QtGui.QLabel(self.magnetsGroup)
        self.sl2VLabel.setObjectName(_fromUtf8("sl2VLabel"))
        self.gridLayout.addWidget(self.sl2VLabel, 5, 0, 1, 1)
        self.sl3FCheck = QtGui.QCheckBox(self.magnetsGroup)
        self.sl3FCheck.setText(_fromUtf8(""))
        self.sl3FCheck.setObjectName(_fromUtf8("sl3FCheck"))
        self.gridLayout.addWidget(self.sl3FCheck, 9, 5, 1, 1)
        self.sl2FCheck = QtGui.QCheckBox(self.magnetsGroup)
        self.sl2FCheck.setText(_fromUtf8(""))
        self.sl2FCheck.setObjectName(_fromUtf8("sl2FCheck"))
        self.gridLayout.addWidget(self.sl2FCheck, 6, 5, 1, 1)
        self.sl2FLabel = QtGui.QLabel(self.magnetsGroup)
        self.sl2FLabel.setObjectName(_fromUtf8("sl2FLabel"))
        self.gridLayout.addWidget(self.sl2FLabel, 6, 0, 1, 1)
        self.sl3FRead = TaurusLabel(self.magnetsGroup)
        self.sl3FRead.setObjectName(_fromUtf8("sl3FRead"))
        self.gridLayout.addWidget(self.sl3FRead, 9, 1, 1, 1)
        self.sl1FRead = TaurusLabel(self.magnetsGroup)
        self.sl1FRead.setObjectName(_fromUtf8("sl1FRead"))
        self.gridLayout.addWidget(self.sl1FRead, 3, 1, 1, 1)
        self.sl1HWrite = QtGui.QDoubleSpinBox(self.magnetsGroup)
        self.sl1HWrite.setMinimum(-2.0)
        self.sl1HWrite.setMaximum(2.0)
        self.sl1HWrite.setSingleStep(0.01)
        self.sl1HWrite.setObjectName(_fromUtf8("sl1HWrite"))
        self.gridLayout.addWidget(self.sl1HWrite, 1, 2, 1, 1)
        self.sl2VRead = TaurusLabel(self.magnetsGroup)
        self.sl2VRead.setObjectName(_fromUtf8("sl2VRead"))
        self.gridLayout.addWidget(self.sl2VRead, 5, 1, 1, 1)
        self.sl3VLabel = QtGui.QLabel(self.magnetsGroup)
        self.sl3VLabel.setObjectName(_fromUtf8("sl3VLabel"))
        self.gridLayout.addWidget(self.sl3VLabel, 8, 0, 1, 1)
        self.sl1VLabel = QtGui.QLabel(self.magnetsGroup)
        self.sl1VLabel.setObjectName(_fromUtf8("sl1VLabel"))
        self.gridLayout.addWidget(self.sl1VLabel, 2, 0, 1, 1)
        self.sl3HRead = TaurusLabel(self.magnetsGroup)
        self.sl3HRead.setObjectName(_fromUtf8("sl3HRead"))
        self.gridLayout.addWidget(self.sl3HRead, 7, 1, 1, 1)
        self.sl3FWrite = QtGui.QDoubleSpinBox(self.magnetsGroup)
        self.sl3FWrite.setMaximum(1.0)
        self.sl3FWrite.setSingleStep(0.01)
        self.sl3FWrite.setObjectName(_fromUtf8("sl3FWrite"))
        self.gridLayout.addWidget(self.sl3FWrite, 9, 2, 1, 1)
        self.sl1HLabel = QtGui.QLabel(self.magnetsGroup)
        self.sl1HLabel.setObjectName(_fromUtf8("sl1HLabel"))
        self.gridLayout.addWidget(self.sl1HLabel, 1, 0, 1, 1)
        self.sl1VWrite = QtGui.QDoubleSpinBox(self.magnetsGroup)
        self.sl1VWrite.setMinimum(-2.0)
        self.sl1VWrite.setMaximum(2.0)
        self.sl1VWrite.setSingleStep(0.01)
        self.sl1VWrite.setObjectName(_fromUtf8("sl1VWrite"))
        self.gridLayout.addWidget(self.sl1VWrite, 2, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 38, 1, 1, 1)
        self.sl1FCheck = QtGui.QCheckBox(self.magnetsGroup)
        self.sl1FCheck.setText(_fromUtf8(""))
        self.sl1FCheck.setObjectName(_fromUtf8("sl1FCheck"))
        self.gridLayout.addWidget(self.sl1FCheck, 3, 5, 1, 1)
        self.sl2FWrite = QtGui.QDoubleSpinBox(self.magnetsGroup)
        self.sl2FWrite.setMaximum(1.0)
        self.sl2FWrite.setSingleStep(0.01)
        self.sl2FWrite.setObjectName(_fromUtf8("sl2FWrite"))
        self.gridLayout.addWidget(self.sl2FWrite, 6, 2, 1, 1)
        self.sl1FWrite = QtGui.QDoubleSpinBox(self.magnetsGroup)
        self.sl1FWrite.setMaximum(1.0)
        self.sl1FWrite.setSingleStep(0.01)
        self.sl1FWrite.setObjectName(_fromUtf8("sl1FWrite"))
        self.gridLayout.addWidget(self.sl1FWrite, 3, 2, 1, 1)
        self.sl1VRead = TaurusLabel(self.magnetsGroup)
        self.sl1VRead.setObjectName(_fromUtf8("sl1VRead"))
        self.gridLayout.addWidget(self.sl1VRead, 2, 1, 1, 1)
        self.sl4HWrite = QtGui.QDoubleSpinBox(self.magnetsGroup)
        self.sl4HWrite.setMinimum(-2.0)
        self.sl4HWrite.setMaximum(2.0)
        self.sl4HWrite.setSingleStep(0.01)
        self.sl4HWrite.setObjectName(_fromUtf8("sl4HWrite"))
        self.gridLayout.addWidget(self.sl4HWrite, 10, 2, 1, 1)
        self.bc1HRead = TaurusLabel(self.magnetsGroup)
        self.bc1HRead.setObjectName(_fromUtf8("bc1HRead"))
        self.gridLayout.addWidget(self.bc1HRead, 13, 1, 1, 1)
        self.sl4FCheck = QtGui.QCheckBox(self.magnetsGroup)
        self.sl4FCheck.setText(_fromUtf8(""))
        self.sl4FCheck.setObjectName(_fromUtf8("sl4FCheck"))
        self.gridLayout.addWidget(self.sl4FCheck, 12, 5, 1, 1)
        self.bc1HLabel = QtGui.QLabel(self.magnetsGroup)
        self.bc1HLabel.setObjectName(_fromUtf8("bc1HLabel"))
        self.gridLayout.addWidget(self.bc1HLabel, 13, 0, 1, 1)
        self.bc1HWrite = QtGui.QDoubleSpinBox(self.magnetsGroup)
        self.bc1HWrite.setMinimum(-2.0)
        self.bc1HWrite.setMaximum(2.0)
        self.bc1HWrite.setSingleStep(0.01)
        self.bc1HWrite.setObjectName(_fromUtf8("bc1HWrite"))
        self.gridLayout.addWidget(self.bc1HWrite, 13, 2, 1, 1)
        self.bc1HCheck = QtGui.QCheckBox(self.magnetsGroup)
        self.bc1HCheck.setText(_fromUtf8(""))
        self.bc1HCheck.setObjectName(_fromUtf8("bc1HCheck"))
        self.gridLayout.addWidget(self.bc1HCheck, 13, 5, 1, 1)
        self.bc1VLabel = QtGui.QLabel(self.magnetsGroup)
        self.bc1VLabel.setObjectName(_fromUtf8("bc1VLabel"))
        self.gridLayout.addWidget(self.bc1VLabel, 14, 0, 1, 1)
        self.bc1VRead = TaurusLabel(self.magnetsGroup)
        self.bc1VRead.setObjectName(_fromUtf8("bc1VRead"))
        self.gridLayout.addWidget(self.bc1VRead, 14, 1, 1, 1)
        self.bc1VWrite = QtGui.QDoubleSpinBox(self.magnetsGroup)
        self.bc1VWrite.setMinimum(-2.0)
        self.bc1VWrite.setMaximum(2.0)
        self.bc1VWrite.setSingleStep(0.01)
        self.bc1VWrite.setObjectName(_fromUtf8("bc1VWrite"))
        self.gridLayout.addWidget(self.bc1VWrite, 14, 2, 1, 1)
        self.bc1VCheck = QtGui.QCheckBox(self.magnetsGroup)
        self.bc1VCheck.setText(_fromUtf8(""))
        self.bc1VCheck.setObjectName(_fromUtf8("bc1VCheck"))
        self.gridLayout.addWidget(self.bc1VCheck, 14, 5, 1, 1)
        self.bc1FLabel = QtGui.QLabel(self.magnetsGroup)
        self.bc1FLabel.setObjectName(_fromUtf8("bc1FLabel"))
        self.gridLayout.addWidget(self.bc1FLabel, 15, 0, 1, 1)
        self.bc1FRead = TaurusLabel(self.magnetsGroup)
        self.bc1FRead.setObjectName(_fromUtf8("bc1FRead"))
        self.gridLayout.addWidget(self.bc1FRead, 15, 1, 1, 1)
        self.bc1FWrite = QtGui.QDoubleSpinBox(self.magnetsGroup)
        self.bc1FWrite.setMaximum(200.0)
        self.bc1FWrite.setSingleStep(0.01)
        self.bc1FWrite.setObjectName(_fromUtf8("bc1FWrite"))
        self.gridLayout.addWidget(self.bc1FWrite, 15, 2, 1, 1)
        self.bc1FCheck = QtGui.QCheckBox(self.magnetsGroup)
        self.bc1FCheck.setText(_fromUtf8(""))
        self.bc1FCheck.setObjectName(_fromUtf8("bc1FCheck"))
        self.gridLayout.addWidget(self.bc1FCheck, 15, 5, 1, 1)
        self.line_1 = QtGui.QFrame(self.magnetsGroup)
        self.line_1.setFrameShape(QtGui.QFrame.VLine)
        self.line_1.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_1.setObjectName(_fromUtf8("line_1"))
        self.gridLayout.addWidget(self.line_1, 1, 4, 29, 1)
        self.gridLayout_2.addWidget(self.magnetsGroup, 0, 0, 1, 1)

        self.retranslateUi(magnetSnapshot)
        QtCore.QMetaObject.connectSlotsByName(magnetSnapshot)

    def retranslateUi(self, magnetSnapshot):
        magnetSnapshot.setWindowTitle(QtGui.QApplication.translate("magnetSnapshot", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.magnetsGroup.setTitle(QtGui.QApplication.translate("magnetSnapshot", "Magnets", None, QtGui.QApplication.UnicodeUTF8))
        self.as1HLabel.setText(QtGui.QApplication.translate("magnetSnapshot", "AS1 Horizontal", None, QtGui.QApplication.UnicodeUTF8))
        self.bc2HLabel.setText(QtGui.QApplication.translate("magnetSnapshot", "BC2 Horizontal", None, QtGui.QApplication.UnicodeUTF8))
        self.qt1HLabel.setText(QtGui.QApplication.translate("magnetSnapshot", "QT1 Horizontal", None, QtGui.QApplication.UnicodeUTF8))
        self.glFLabel.setText(QtGui.QApplication.translate("magnetSnapshot", "GLFocus", None, QtGui.QApplication.UnicodeUTF8))
        self.as2VLabel.setText(QtGui.QApplication.translate("magnetSnapshot", "AS2 Vertical", None, QtGui.QApplication.UnicodeUTF8))
        self.as2HLabel.setText(QtGui.QApplication.translate("magnetSnapshot", "AS2 Horizontal", None, QtGui.QApplication.UnicodeUTF8))
        self.glHLabel.setText(QtGui.QApplication.translate("magnetSnapshot", "GL Horizontal", None, QtGui.QApplication.UnicodeUTF8))
        self.qt2FLabel.setText(QtGui.QApplication.translate("magnetSnapshot", "QT2 Focus", None, QtGui.QApplication.UnicodeUTF8))
        self.glVLabel.setText(QtGui.QApplication.translate("magnetSnapshot", "GL Vertical", None, QtGui.QApplication.UnicodeUTF8))
        self.bc2FLabel.setText(QtGui.QApplication.translate("magnetSnapshot", "BC2 Focus", None, QtGui.QApplication.UnicodeUTF8))
        self.bc2VLabel.setText(QtGui.QApplication.translate("magnetSnapshot", "BC2 Vertical", None, QtGui.QApplication.UnicodeUTF8))
        self.as1VLabel.setText(QtGui.QApplication.translate("magnetSnapshot", "AS1 Vertical", None, QtGui.QApplication.UnicodeUTF8))
        self.qt1FLabel.setText(QtGui.QApplication.translate("magnetSnapshot", "QT1 Focus", None, QtGui.QApplication.UnicodeUTF8))
        self.qt1VLabel.setText(QtGui.QApplication.translate("magnetSnapshot", "QT1 Vertical", None, QtGui.QApplication.UnicodeUTF8))
        self.sl4VLabel.setText(QtGui.QApplication.translate("magnetSnapshot", "SL4 Vertical", None, QtGui.QApplication.UnicodeUTF8))
        self.sl4HLabel.setText(QtGui.QApplication.translate("magnetSnapshot", "SL4 Horizontal", None, QtGui.QApplication.UnicodeUTF8))
        self.sl4FLabel.setText(QtGui.QApplication.translate("magnetSnapshot", "SL4 Focus", None, QtGui.QApplication.UnicodeUTF8))
        self.SaveRetrieveTitle.setText(QtGui.QApplication.translate("magnetSnapshot", "Save/Retrieve", None, QtGui.QApplication.UnicodeUTF8))
        self.sl3FLabel.setText(QtGui.QApplication.translate("magnetSnapshot", "SL3 Focus", None, QtGui.QApplication.UnicodeUTF8))
        self.sl1FLabel.setText(QtGui.QApplication.translate("magnetSnapshot", "SL1 Focus", None, QtGui.QApplication.UnicodeUTF8))
        self.PresentWriteTitle.setText(QtGui.QApplication.translate("magnetSnapshot", "Present value", None, QtGui.QApplication.UnicodeUTF8))
        self.sl2HLabel.setText(QtGui.QApplication.translate("magnetSnapshot", "SL2 Horizontal", None, QtGui.QApplication.UnicodeUTF8))
        self.sl3HLabel.setText(QtGui.QApplication.translate("magnetSnapshot", "SL3 Horizontal", None, QtGui.QApplication.UnicodeUTF8))
        self.sl2VLabel.setText(QtGui.QApplication.translate("magnetSnapshot", "SL2 Vertical", None, QtGui.QApplication.UnicodeUTF8))
        self.sl2FLabel.setText(QtGui.QApplication.translate("magnetSnapshot", "SL2 Focus", None, QtGui.QApplication.UnicodeUTF8))
        self.sl3VLabel.setText(QtGui.QApplication.translate("magnetSnapshot", "SL3 Vertical", None, QtGui.QApplication.UnicodeUTF8))
        self.sl1VLabel.setText(QtGui.QApplication.translate("magnetSnapshot", "SL1 Vertical", None, QtGui.QApplication.UnicodeUTF8))
        self.sl1HLabel.setText(QtGui.QApplication.translate("magnetSnapshot", "SL1 Horizontal", None, QtGui.QApplication.UnicodeUTF8))
        self.bc1HLabel.setText(QtGui.QApplication.translate("magnetSnapshot", "BC1 Horizontal", None, QtGui.QApplication.UnicodeUTF8))
        self.bc1VLabel.setText(QtGui.QApplication.translate("magnetSnapshot", "BC1 Vertical", None, QtGui.QApplication.UnicodeUTF8))
        self.bc1FLabel.setText(QtGui.QApplication.translate("magnetSnapshot", "BC1 Focus", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.display import TaurusLabel
from taurus.qt.qtgui.container import TaurusGroupBox
from taurus.qt.qtgui.panel import TaurusWidget
