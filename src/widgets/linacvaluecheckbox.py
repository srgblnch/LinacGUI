#!/usr/bin/env python

#############################################################################
##
## This file is part of Taurus, a Tango User Interface Library
##
## http://www.tango-controls.org/static/taurus/latest/doc/html/index.html
##
## Copyright 2011 CELLS / ALBA Synchrotron, Bellaterra, Spain
##
## Taurus is free software: you can redistribute it and/or modify
## it under the terms of the GNU Lesser General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## Taurus is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU Lesser General Public License for more details.
##
## You should have received a copy of the GNU Lesser General Public License
## along with Taurus.  If not, see <http://www.gnu.org/licenses/>.
##
#############################################################################

"""This module provides an specialization of the TaurusValueCheckBox to include
   two new requested features for this linac control"""
   
__all__ = ["LinacValueCheckBox"]

__docformat__ = 'restructuredtext'

import sys
from taurus.qt import Qt
from taurus.qt.qtgui.base import TaurusBaseComponent,TaurusBaseWritableWidget


class LinacValueCheckBox(Qt.QCheckBox, TaurusBaseWritableWidget):
    """Clone the TaurusValueCheckBox that connects a boolean writable 
       attribute model, with two extra features:
       - uncheck when a reset is cleaned.
       - DangerMessage to warn the user when it will do a danger action.
    """

    __pyqtSignals__ = ("modelChanged(const QString &)",)

    def __init__(self, qt_parent = None, designMode = False):
        name = "LinacValueCheckBox"
        #this part is the copy from the TaurusValueCheckBox
        try:
            self.call__init__wo_kw(Qt.QCheckBox, qt_parent)
            self.call__init__(TaurusBaseWritableWidget, name, designMode=designMode)
            self.setObjectName(name)
            self.updateStyle()
            self.connect(self, Qt.SIGNAL('stateChanged(int)'),self.valueChanged)
        except Exception,e:
            print("Uou! Exception: %s"%(e))
            raise Exception(e)

        #This is the part with the changes related with the TaurusValueCheckBox
        try:
            self._dangerRiseEdge = False
            self._dangerFallingEdge = False
            self._isResetCheckBox = False
        except Exception,e:
            print("Uou! Exception: %s"%(e))
            raise Exception(e)

    def keyPressEvent(self, event):
        if event.key() in (Qt.Qt.Key_Return, Qt.Qt.Key_Enter):
            self.writeValue()
            event.accept()
        else:
            Qt.QCheckBox.keyPressEvent(self,event)
            event.ignore()

    def minimumSizeHint(self):
        return Qt.QSize(20, 20)

    #-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-
    # TaurusValueCheckBox overwriting
    #-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-

    def updateStyle(self):
        TaurusBaseWritableWidget.updateStyle(self)
        # Show text only if it is not specifically hidden
        if self._showText:
            try:
                self.setText(str(self.getModelObj().getConfig().getLabel()))
            except:
                self.setText('----')
        else:
            self.setText('')
        #Update pending operations style
        
        if self.hasPendingOperations():
            if self._isResetCheckBox:
                #This behalves different than the original TaurusValueCheckBox
                pass
            else:
                #If it is not a resetCheckBox, proceed like the TaurusValueCheckBox
                txt = str(self.text()).strip()
                if len(txt) == 0:
                    self.setText("!")
                self.setStyleSheet('TaurusValueCheckBox {color: blue;}')
        else:
            if str(self.text()) == "!":
                self.setText(" ")
            self.setStyleSheet('TaurusValueCheckBox {}')
        self.update()

    def setValue(self, v):
        self.setChecked(bool(v))

    def getValue(self):
        return self.isChecked()

    @classmethod
    def getQtDesignerPluginInfo(cls):
        ret = TaurusBaseWritableWidget.getQtDesignerPluginInfo()
        ret['module'] = 'linacvaluecheckbox'
        ret['group'] = 'Taurus Linac'
        ret['icon'] = ":/designer/checkbox.png"
        return ret

    #---- TODO: when a value change is received, the setChecked() must change 
    #           the same way

    #-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-
    # TaurusBaseComponent overwriting
    #-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-

    #---- TODO: if it's necessary to modify the behaviour of the DangerMessage
    #           because in this case, different than a button, we may 
    #           distinguish between set action and unset action

    #-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-
    # QT properties
    #-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-

    model = Qt.pyqtProperty("QString", TaurusBaseWritableWidget.getModel,
                            TaurusBaseWritableWidget.setModel,
                            TaurusBaseWritableWidget.resetModel)

    showText = Qt.pyqtProperty("bool", TaurusBaseWritableWidget.getShowText,
                               TaurusBaseWritableWidget.setShowText,
                               TaurusBaseWritableWidget.resetShowText)

    useParentModel = Qt.pyqtProperty("bool", TaurusBaseWritableWidget.getUseParentModel,
                                     TaurusBaseWritableWidget.setUseParentModel,
                                     TaurusBaseWritableWidget.resetUseParentModel)

    autoApply = Qt.pyqtProperty("bool", TaurusBaseWritableWidget.getAutoApply,
                                TaurusBaseWritableWidget.setAutoApply,
                                TaurusBaseWritableWidget.resetAutoApply)

    forcedApply = Qt.pyqtProperty("bool", TaurusBaseWritableWidget.getForcedApply,
                                  TaurusBaseWritableWidget.setForcedApply,
                                  TaurusBaseWritableWidget.resetForcedApply)

    #New feature different than the TaurusValueCheckBox, 
    #but similar to the one that is implemented in the TaurusCommandButton:
    DangerMessage = Qt.pyqtProperty("QString", TaurusBaseComponent.getDangerMessage, 
                                    TaurusBaseComponent.setDangerMessage, 
                                    TaurusBaseComponent.resetDangerMessage)

    #---- TDOD: extra Qt properties to configure which of the operations can 
    #           be dangerous (set, unset, or both).
    def getDangerRiseEdge(self):
        return self._dangerRiseEdge
    def setDangerRiseEdge(self,riseEdge):
        self._dangerRiseEdge = riseEdge
    def resetDangerRiseEdge(self):
        self.setDangerRiseEdge(False)
    DangerOnRiseEdge = Qt.pyqtProperty('bool',getDangerRiseEdge,
                                       setDangerRiseEdge,
                                       resetDangerRiseEdge)

    def getDangerFallingEdge(self):
        return self._dangerFallingEdge
    def setDangerFallingEdge(self,FallingEdge):
        self._dangerFallingEdge = FallingEdge
    def resetDangerFallingEdge(self):
        self.setDangerFallingEdge(False)

    DangerOnFallingEdge = Qt.pyqtProperty('bool',getDangerFallingEdge,
                                   setDangerFallingEdge,
                                   resetDangerFallingEdge)
    
    #another QT property to define the reset behaviour
    def getResetCheckBox(self):
        return self._isResetCheckBox
    def setResetCheckBox(self,hasReset):
        self._isResetCheckBox = hasReset
    def resetResetCheckBox(self):
        self.setResetBehaviour(False)
    
    ResetCheckBox = Qt.pyqtProperty("bool",getResetCheckBox,
                                     setResetCheckBox,
                                     resetResetCheckBox)

def main():
    app = Qt.QApplication(sys.argv)
    w = LinacValueCheckBox()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
