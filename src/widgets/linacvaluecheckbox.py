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
#from taurus.qt.qtgui.input import TaurusValueCheckBox
from taurus.qt.qtgui.base import TaurusBaseWritableWidget#,\
#                                 TaurusBaseWidget,\
#                                 TaurusBaseComponent


#class LinacValueCheckBox(TaurusValueCheckBox):
class LinacValueCheckBox(Qt.QCheckBox, TaurusBaseWritableWidget):
    """Clone the TaurusValueCheckBox that connects a boolean writable 
       attribute model, with two extra features:
       - uncheck when a reset is cleaned.
       - DangerMessage to warn the user when it will do a danger action.
    """

    __pyqtSignals__ = ("modelChanged(const QString &)",)

    def __init__(self, qt_parent = None, designMode = False):
        name = "LinacValueCheckBox"
        try:
            #self.call__init__(TaurusValueCheckBox,name,designMode=designMode)
            self.call__init__wo_kw(Qt.QCheckBox, qt_parent)
            self.call__init__(TaurusBaseWritableWidget, name, designMode=designMode)
        
            self.setObjectName(name)
            self.updateStyle()
            self.connect(self, Qt.SIGNAL('stateChanged(int)'),self.valueChanged)
            #End the copy of the TaurusValueCheckBox constructor
            self._dangerRiseEdge = False
            self._dangerFallingEdge = False
            self._isResetCheckBox = False
            #The superclass connect the event 'stateChanged(int)' with
            #the method valueChanged.
        except Exception,e:
            self.error("Uou! Exception: %s"%(e))
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

    def _my_debug(self,msg):
        '''FIXME: this is a hackish method to be removed after the development
           It's used to print some information, about the behaviour of the 
           widget, filtering by an specific model to simplify and get readable
           the tracing logs.
        '''
        pass
#        if self.getModelName() in ['li/ct/plc1/SCM1_DC',
#                                   'li/ct/plc4/HVPS_Interlock_RC']:
#            self.info(msg)

    def isResetCheckBox(self):
        return hasattr(self,'_isResetCheckBox') and self._isResetCheckBox
    
    def isDangerRiseEdge(self):
        return self.getValue() and self._dangerRiseEdge
    
    def isDangerFallingEdge(self):
        return not self.getValue() and self._dangerFallingEdge
    
    def isDangerousAction(self):
        return self.isDangerRiseEdge() or self.isDangerFallingEdge()
    
    def _OperationCancelled(self):
        self._my_debug("_OperationCancelled() ops="%(self._operations))
        #self.setValue(not self.getValue())

    def getDangerRiseEdge(self):
        return self._dangerRiseEdge
    def setDangerRiseEdge(self,riseEdge):
        self._dangerRiseEdge = riseEdge
        self._isDangerous = len(self._dangerMessage) > 0
    def resetDangerRiseEdge(self):
        self.setDangerRiseEdge(False)

    def getDangerFallingEdge(self):
        return self._dangerFallingEdge
    def setDangerFallingEdge(self,FallingEdge):
        self._dangerFallingEdge = FallingEdge
        self._isDangerous = len(self._dangerMessage) > 0
    def resetDangerFallingEdge(self):
        self.setDangerFallingEdge(False)

    def getResetCheckBox(self):
        return self._isResetCheckBox
    def setResetCheckBox(self,hasReset):
        self._isResetCheckBox = hasReset
    def resetResetCheckBox(self):
        self.setResetBehaviour(False)

    #-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-
    # TaurusValueCheckBox overwriting
    #-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-

    def updateStyle(self):
        self._my_debug("updateStyle()")
        try:
            #TaurusValueCheckBox.updateStyle(self)
            TaurusBaseWritableWidget.updateStyle(self)
            # Show text only if it is not specifically hidden
            if self._showText and self.isResetCheckBox():
                try:
                    self.setText(str(self.getModelObj().getConfig().getLabel()))
                except:
                    self.setText('----')
            else:
                self.setText('')
            #Update pending operations style
            
            if not self.isResetCheckBox():
                #If it is not a resetCheckBox, proceed like the TaurusValueCheckBox
                if self.hasPendingOperations():
                    txt = str(self.text()).strip()
                    if len(txt) == 0:
                        self.setText("!")
                    self.setStyleSheet('TaurusValueCheckBox {color: blue;}')
                else:
                    if str(self.text()) == "!":
                        self.setText(" ")
                    self.setStyleSheet('TaurusValueCheckBox {}')
                self.update()
        except Exception,e:
            self.error("Cannot updateStyle: %s"%(e))

    def setValue(self, v):
        self._my_debug("setValue(v=%s)"%(v))
        #TaurusValueCheckBox.setChecked(self,bool(v))
        self.setChecked(bool(v))

    def getValue(self):
        #value = TaurusValueCheckBox.getValue(self)
        value = self.isChecked()
        self._my_debug("getValue(): %s"%(value))
        return value

    @classmethod
    def getQtDesignerPluginInfo(cls):
        #ret = TaurusValueCheckBox.getQtDesignerPluginInfo()
        ret = TaurusBaseWritableWidget.getQtDesignerPluginInfo()
        ret['module'] = 'linacvaluecheckbox'
        ret['group'] = 'Taurus Linac'
        ret['icon'] = ":/designer/checkbox.png"
        return ret

    #-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-
    # TaurusBaseWritableWidget overwriting
    #-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-

    #---- TODO: when a value change is received, the setChecked() must change 
    #           the same way
    def valueChanged(self, *args):
        self._my_debug("valueChanged(*args=%s) isChecked=%s"%(args,self.isChecked()))
        if not self.isChecked() and self.isResetCheckBox():
            #when it's a reset checkbox, ignore when is unchecked because it is
            #cause by handleEvent() and the write to the attr must be avoided.
            return
        #TaurusValueCheckBox.valueChanged(self, *args)
        TaurusBaseWritableWidget.valueChanged(self, *args)
    
    def handleEvent(self, src, evt_type, evt_value):
        #self._my_debug("handleEvent(src=%s,value=%s)"%(src,evt_value))
        if hasattr(evt_value,'value'):
            self._my_debug("received from %s: %s"%(src,evt_value.value))
            if self.isResetCheckBox():
                if self.getValue() and evt_value.value ==False:
                    self.setValue(False)
#            else:
#                self.setChecked(evt_value.w_value)
        #TaurusValueCheckBox.handleEvent(self,src,evt_type,evt_value)
        TaurusBaseWritableWidget.handleEvent(self,src,evt_type,evt_value)
        
#    def writeValue(self, forceApply=False):
#        self._my_debug("writeValue(forceApply=%s)"%(forceApply))
#        #TaurusValueCheckBox.writeValue(self,forceApply)
#        TaurusBaseWritableWidget.writeValue(self,forceApply)

    #-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-
    # TaurusBaseWidget overwriting
    #-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-

    def safeApplyOperations(self, ops = None):
        '''Modify the behaviour of the DangerMessage because in this case, 
           different than a button, we may distinguish between set action and 
           unset action.
           It seems that Taurus will someday support multiple Danger messages,
           but this widget did not copy this feature.
        '''
        if ops is None: ops = self.getPendingOperations()
        
        self._my_debug("safeApplyOperations(ops=%s)"%(ops))
        
        #Check if we need to take care of dangerous operations
        if self.getForceDangerousOperations(): dangerMsgs = []
        else: dangerMsgs = [op.getDangerMessage() for op in ops \
                                              if len(op.getDangerMessage()) > 0]
        #warn the user if need be
        if self.isDangerousAction():
            WarnTitle = "Potentially dangerous action"
            WarnMsg = "%s\nProceed?"%dangerMsgs[0]
            Buttons = Qt.QMessageBox.Ok|Qt.QMessageBox.Cancel
            Default = Qt.QMessageBox.Cancel
            result = Qt.QMessageBox.warning(self,WarnTitle,WarnMsg,
                                            Buttons,Default)
            #---- Important default behaviour shall be the Cancel
            self._my_debug("safeApplyOperations(...) answer = %s"%result)
            if result == Qt.QMessageBox.Cancel:
                self._OperationCancelled()
            else:
                self.applyPendingOperations(ops)
        else:
            self.applyPendingOperations(ops)

#    def emitValueChanged(self, *args):
#        self._my_debug("emitValueChanged(args=%s)"%(str(args)))
#        #TaurusValueCheckBox.emitValueChanged(self,*args)
#        TaurusBaseWritableWidget.emitValueChanged(self,*args)

    #-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-
    # TaurusBaseComponent overwriting
    #-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-

    def setDangerMessage(self, dangerMessage=""):
        """Sets the danger message when applying an operation.
           In this widget, setting a danger message is not enough to define
           a dangerous operation, because it must be defined if the danger is
           on setting true or false, or both.
           If dangerMessage is None, the apply operation is considered safe
        
        :param dangerMessage: (str or None) the danger message. 
                              If None is given (default) the apply operation 
                              is considered safe.
        """
        self._dangerMessage = dangerMessage
        if self._dangerRiseEdge or self._dangerFallingEdge:
            self._isDangerous = len(dangerMessage) > 0
        else:
            self._isDangerous = False

#    def hasPendingOperations(self):
#        #value = TaurusValueCheckBox.hasPendingOperations(self)
#        value = TaurusBaseWritableWidget.hasPendingOperations(self)
#        self._my_debug("hasPendingOperations(): %s"%(value))
#        return value

#    def getPendingOperations(self):
#        #value = TaurusValueCheckBox.getPendingOperations(self)
#        value = TaurusBaseWritableWidget.getPendingOperations(self)
#        self._my_debug("getPendingOperations(): %s"%(value))
#        return value
    
#    def applyPendingOperations(self,ops=None):
#        self._my_debug("applyPendingOperations(ops=%s)"%(ops))
#        #TaurusValueCheckBox.applyPendingOperations(self,ops)
#        TaurusBaseWritableWidget.applyPendingOperations(self,ops)

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
    DangerMessage = Qt.pyqtProperty("QString", TaurusBaseWritableWidget.getDangerMessage, 
                                    setDangerMessage, 
                                    TaurusBaseWritableWidget.resetDangerMessage)

    #extra Qt properties to configure which of the operations can 
    #be dangerous (set, unset, or both).
    DangerOnRiseEdge = Qt.pyqtProperty('bool',getDangerRiseEdge,
                                       setDangerRiseEdge,
                                       resetDangerRiseEdge)

    DangerOnFallingEdge = Qt.pyqtProperty('bool',getDangerFallingEdge,
                                   setDangerFallingEdge,
                                   resetDangerFallingEdge)
    
    #another QT property to define the reset behaviour
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
