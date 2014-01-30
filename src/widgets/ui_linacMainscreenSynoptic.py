# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'linacMainscreenSynoptic.ui'
#
# Created: Wed Jan 22 14:44:42 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_linacMainscreenSynoptic(object):
    def setupUi(self, linacMainscreenSynoptic):
        linacMainscreenSynoptic.setObjectName(_fromUtf8("linacMainscreenSynoptic"))
        linacMainscreenSynoptic.resize(1235, 821)
        linacMainscreenSynoptic.setMinimumSize(QtCore.QSize(1235, 821))
        linacMainscreenSynoptic.setMaximumSize(QtCore.QSize(1235, 821))
        self.MainScreenSchematic = TaurusJDrawSynopticsView(linacMainscreenSynoptic)
        self.MainScreenSchematic.setGeometry(QtCore.QRect(0, 0, 1250, 825))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.MainScreenSchematic.setForegroundBrush(brush)
        self.MainScreenSchematic.setObjectName(_fromUtf8("MainScreenSchematic"))

        self.retranslateUi(linacMainscreenSynoptic)
        QtCore.QMetaObject.connectSlotsByName(linacMainscreenSynoptic)

    def retranslateUi(self, linacMainscreenSynoptic):
        linacMainscreenSynoptic.setWindowTitle(QtGui.QApplication.translate("linacMainscreenSynoptic", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.MainScreenSchematic.setModel(QtGui.QApplication.translate("linacMainscreenSynoptic", "jdraw/linac_mainscreen_synoptic.jdw", None, QtGui.QApplication.UnicodeUTF8))

from taurus.qt.qtgui.container import TaurusWidget
from taurus.qt.qtgui.graphic.jdraw import TaurusJDrawSynopticsView
