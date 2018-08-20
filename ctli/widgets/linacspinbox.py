# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 3
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; If not, see <http://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####

from taurus.core.units import Quantity
from taurus.external.qt import Qt
from taurus.qt.qtgui.base import TaurusBaseWritableWidget
from taurus.qt.qtgui.input import TaurusValueSpinBox, TaurusValueLineEdit
from taurus.qt.qtgui.util import PintValidator
from time import time
import traceback

__author__ = "Sergi Blanch-Torne"
__copyright__ = "Copyright 2018, CELLS / ALBA Synchrotron"
__license__ = "GPLv3+"

"""
This module provides an specialisation of the TaurusValueSpinBox to include
experimental features that would be later integrated in taurus.
Also another non-taurus widget used in the save/retrieve.
"""

__all__ = ["LinacValueSpinBox", "SaveRetrieveSpinBox"]


class LinacValueLineEdit(TaurusValueLineEdit):

    _dangerOperation_OkReceived = None
    _dangerOperation_ConfirmationRequested = None
    _dangerMessage = None
    _dangerAbove = None
    _dangerBelow = None

    def __init__(self, *args, **kwargs):
        TaurusValueLineEdit.__init__(self, *args, **kwargs)
        self._dangerOperation_ConfirmationRequested = False

    def _my_debug(self, msg):
        '''FIXME: this is a hackish method to be removed after the development
           It's used to print some information, about the behaviour of the
           widget, filtering by an specific model to simplify and get readable
           the tracing logs.
        '''
        monitoredAttrs = [
            'li/ct/plc4/hvps_v_setpoint',
            'li/ct/plc5/hvps_v_setpoint'
        ]
        model = self.getModelName().lower().split('#')[0]
        if len(model.split('/')) == 5:
            model = model.split('/', 1)[1]
        if model in monitoredAttrs:
            self.info(msg)

    def _reviewIsDangerous(self):
        if self._dangerAbove is not None or self._dangerBelow is not None:
            self._isDangerous = len(self._dangerMessage) > 0
            self.info("Dangerous operation feature active")
        else:
            self._isDangerous = False
            self.info("Dangerous operation feature INactive")

    def setDangerMessage(self, dangerMessage=""):
        """Sets the danger message when applying an operation.
           In this widget, setting a danger message is not enough to define
           a dangerous operation, because it must be defined the thresholds
           where the danger operation applies.
           If dangerMessage is None, the apply operation is considered safe

        :param dangerMessage: (str or None) the danger message.
                              If None is given (default) the apply operation
                              is considered safe.
        """
        self._dangerMessage = dangerMessage
        self.info("setting a danger message %r" % (self._dangerMessage))
        self._reviewIsDangerous()

    DangerMessage = Qt.pyqtProperty("QString",
                                    TaurusBaseWritableWidget.getDangerMessage,
                                    setDangerMessage,
                                    TaurusBaseWritableWidget.
                                    resetDangerMessage)

    def getDangerAbove(self):
        return self._dangerAbove or float('Inf')

    def setDangerAbove(self, value):
        self._dangerAbove = value
        self.info("setting dangerous setpoint above %g" % value)
        self._reviewIsDangerous()

    def resetDangerAbove(self):
        self.setDangerAbove(None)

    DangerAbove = Qt.pyqtProperty('int', getDangerAbove, setDangerAbove,
                                  resetDangerAbove)

    def getDangerBelow(self):
        return self._dangerBelow or float('-Inf')

    def setDangerBelow(self, value):
        self._dangerBelow = value
        self.info("setting dangerous setpoint below %g" % value)
        self._reviewIsDangerous()

    def resetDangerBelow(self):
        self.setDangerBelow(None)

    DangerBelow = Qt.pyqtProperty('int', getDangerBelow, setDangerBelow,
                                  resetDangerBelow)

    def getMagnitudeValue(self):
        value = self.getValue()
        if isinstance(value, Quantity):
            value = value.magnitude
        return value

    def isDangerAbove(self):
        if self._dangerAbove is not None:
            value = self.getMagnitudeValue()
            if value > self._dangerAbove:
                self._my_debug("Value %g is above danger threshold" % (value))
                return True
            self._my_debug("Value %g is NOT above danger threshold" % (value))
        return False

    def isDangerBelow(self):
        if self._dangerBelow is not None:
            value = self.getMagnitudeValue()
            if value < self._dangerBelow:
                self._my_debug("Value %g is below danger threshold" % (value))
                return True
            self._my_debug("Value %g is NOT below danger threshold" % (value))
        return False

    def isDangerousAction(self):
        if self.isDangerAbove() or self.isDangerBelow():
            if self._dangerOperation_OkReceived is not None:
                t = time()-self._dangerOperation_OkReceived
                if t < 3.0:  # FIXME adapt this time
                    self._my_debug("Still confirmed the ok (%fs), "
                                   "renew it" % (t))
                    self._dangerOperation_OkReceived = time()
                    return False
                else:
                    self._my_debug("Timeout, required to ask again (%fs)"
                                   % (t))
                    self._dangerOperation_OkReceived = None
            return True
        if self._dangerOperation_OkReceived is not None:
            self._my_debug("Pass Outside the danger operations, "
                           "clean the confirmation")
            self._dangerOperation_OkReceived = None
        return False

    # PendingOperations area



    # def hasPendingOperations(self):
    #     self._my_debug("hasPendingOperations()")
    #     return TaurusValueLineEdit.hasPendingOperations(self)

    # def getPendingOperations(self):
    #     self._my_debug("getPendingOperations()")
    #     return TaurusValueLineEdit.getPendingOperations(self)

    # def resetPendingOperations(self):
    #     answer = TaurusValueLineEdit.resetPendingOperations(self)
    #     self._my_debug("resetPendingOperations() -> %s" % (answer))
    #     return answer
    #
    # def setForceDangerousOperations(self, yesno):
    #     answer = TaurusValueLineEdit.setForceDangerousOperations(self, yesno)
    #     self._my_debug("setForceDangerousOperations(%s) -> " % (yesno, answer))
    #     return answer
    #
    # def getForceDangerousOperations(self):
    #     answer = TaurusValueLineEdit.getForceDangerousOperations(self)
    #     self._my_debug("getForceDangerousOperations() -> %s" % (answer))
    #     return answer
    #
    # def resetForceDangerousOperations(self):
    #     answer = TaurusValueLineEdit.resetForceDangerousOperations(self)
    #     self._my_debug("resetForceDangerousOperations() -> %s" % (answer))
    #     return answer
    #
    # def resetAutoProtectOperation(self):
    #     answer = TaurusValueLineEdit.resetAutoProtectOperation(self)
    #     self._my_debug("resetAutoProtectOperation() -> %s" % (answer))
    #     return answer
    #
    # def isAutoProtectOperation(self):
    #     answer = TaurusValueLineEdit.isAutoProtectOperation(self)
    #     self._my_debug("isAutoProtectOperation() -> %s" % (answer))
    #     return answer
    #
    # def setAutoProtectOperation(self, protect):
    #     answer = TaurusValueLineEdit.setAutoProtectOperation(self)
    #     self._my_debug("setAutoProtectOperation() -> %s" % (answer))
    #     return answer
    #
    # def updatePendingOperations(self):
    #     answer = TaurusValueLineEdit.updatePendingOperations(self)
    #     self._my_debug("updatePendingOperations() -> %s" % (answer))
    #     return answer
    #
    # def getOperationCallbacks(self):
    #     answer = TaurusValueLineEdit.getOperationCallbacks(self)
    #     self._my_debug("getOperationCallbacks() -> %s" % (answer))
    #     return answer

    def safeApplyOperations(self, ops=None):
        '''Modify the behaviour of the DangerMessage because in this case,
           different than a button, we may distinguish between set action and
           unset action.
           It seems that Taurus will someday support multiple Danger messages,
           but this widget did not copy this feature.
        '''
        if ops is None:
            ops = self.getPendingOperations()
        self._my_debug("safeApplyOperations(ops=%s)" % (ops))
        # Check if we need to take care of dangerous operations
        if self.getForceDangerousOperations():
            dangerMsgs = []
        else:
            dangerMsgs = [op.getDangerMessage() for op in ops
                          if len(op.getDangerMessage()) > 0]
        # warn the user if need be
        if self.isDangerousAction() and len(dangerMsgs) > 0:
            if self._dangerOperation_ConfirmationRequested is False:
                self._dangerOperation_ConfirmationRequested = True
                WarnTitle = "Potentially dangerous action"
                WarnMsg = "%s\nProceed?" % (dangerMsgs[0])
                self._my_debug("%s. %s"
                               % (WarnTitle, WarnMsg.replace('\n',' ')))
                Buttons = Qt.QMessageBox.Ok | Qt.QMessageBox.Cancel
                Default = Qt.QMessageBox.Cancel
                result = Qt.QMessageBox.warning(self, WarnTitle, WarnMsg,
                                                Buttons, Default)
                # Important default behaviour shall be the Cancel ---
                if result == Qt.QMessageBox.Cancel:
                    self._my_debug("safeApplyOperations(...) answer = Cancel")
                    self._dangerOperation_OkReceived = None
                    self._OperationCancelled()
                else:
                    self._my_debug("safeApplyOperations(...) answer = Ok")
                    self._dangerOperation_OkReceived = time()
                    self.applyPendingOperations(ops)
                self._my_debug("Confirmation request answered, "
                               "cleaning the flag")
                self._dangerOperation_ConfirmationRequested = False
            else:
                self._my_debug("Confirmation request already send, "
                               "waiting for the answer")
        else:
            self._my_debug("It is NOT a dangerous action")
            self.applyPendingOperations(ops)

    def _onEditingFinished(self):
        if self._autoApply:
            self.writeValue()

    def _OperationCancelled(self):
        self.resetPendingOperations()
        self.setValue(self.getValue())

    # def applyPendingOperations(self, ops=None):
    #     if not self._dangerOperationQuestion:
    #         TaurusValueLineEdit.applyPendingOperations(self)
    #     else:
    #         self.getTaurusManager().applyPendingOperations(ops)


class LinacValueSpinBox(TaurusValueSpinBox):

    def __init__(self, qt_parent=None, designMode=False):
        TaurusValueSpinBox.__init__(self, qt_parent, designMode)

        # recreate the lineEdit object for a instance prepared here
        lineEdit = LinacValueLineEdit(designMode=designMode)
        lineEdit.setValidator(PintValidator(self))
        self.setLineEdit(lineEdit)

        self.setEnableWheelEvent(False)

    def wheelEvent(self, evt):
        """Wheel event handler"""
        if self.getEnableWheelEvent() or \
                TaurusValueSpinBox.isReadOnly(self):
            return TaurusValueSpinBox.wheelEvent(self, evt)

    def setEnableWheelEvent(self, value):
        self.lineEdit().setEnableWheelEvent(value)

    def getEnableWheelEvent(self):
        return self.lineEdit().getEnableWheelEvent()

    def resetEnableWheelEvent(self):
        self.setEnableWheelEvent(False)

    enableWheelEvent = Qt.pyqtProperty("bool", getEnableWheelEvent,
                                       setEnableWheelEvent,
                                       resetEnableWheelEvent)

    def getDangerMessage(self):
        return self.lineEdit().getDangerMessage()

    def setDangerMessage(self, dangerMessage=""):
        self.lineEdit().setDangerMessage(dangerMessage)

    def resetDangerMessage(self):
        self.lineEdit().resetDangerMessage()

    DangerMessage = Qt.pyqtProperty("QString", getDangerMessage,
                                    setDangerMessage, resetDangerMessage)

    def getDangerAbove(self):
        return self.lineEdit().getDangerAbove()

    def setDangerAbove(self, value):
        self.lineEdit().setDangerAbove(value)

    def resetDangerAbove(self):
        self.lineEdit().resetDangerAbove()

    DangerAbove = Qt.pyqtProperty('int', getDangerAbove, setDangerAbove,
                                  resetDangerAbove)

    def getDangerBelow(self):
        return self.lineEdit().getDangerBelow()

    def setDangerBelow(self, value):
        self.lineEdit().setDangerBelow(value)

    def resetDangerBelow(self):
        self.lineEdit().resetDangerBelow()

    DangerBelow = Qt.pyqtProperty('int', getDangerBelow, setDangerBelow,
                                  resetDangerBelow)


class SaveRetrieveSpinBox(Qt.QSpinBox):

    _enableWheelEvent = None

    def __init__(self, qt_parent=None, designMode=False):
        Qt.QSpinBox.__init__(self, qt_parent)
        self.setEnableWheelEvent(False)

    def wheelEvent(self, evt):
        """Wheel event handler"""
        if self.getEnableWheelEvent() or \
                Qt.QSpinBox.isReadOnly(self):
            return Qt.QSpinBox.wheelEvent(self, evt)

    def setEnableWheelEvent(self, value):
        self._enableWheelEvent = value

    def getEnableWheelEvent(self):
        return self._enableWheelEvent

    def resetEnableWheelEvent(self):
        self.setEnableWheelEvent(False)

    enableWheelEvent = Qt.pyqtProperty("bool", getEnableWheelEvent,
                                       setEnableWheelEvent,
                                       resetEnableWheelEvent)


class SaveRetrieveDoubleSpinBox(Qt.QDoubleSpinBox):

    _enableWheelEvent = None

    def __init__(self, qt_parent=None, designMode=False):
        Qt.QDoubleSpinBox.__init__(self, qt_parent)
        self.setEnableWheelEvent(False)

    def wheelEvent(self, evt):
        """Wheel event handler"""
        print("handle wheel event")
        if self.getEnableWheelEvent() or \
                Qt.QDoubleSpinBox.isReadOnly(self):
            return Qt.QDoubleSpinBox.wheelEvent(self, evt)

    def setEnableWheelEvent(self, value):
        self._enableWheelEvent = value

    def getEnableWheelEvent(self):
        return self._enableWheelEvent

    def resetEnableWheelEvent(self):
        self.setEnableWheelEvent(False)

    enableWheelEvent = Qt.pyqtProperty("bool", getEnableWheelEvent,
                                       setEnableWheelEvent,
                                       resetEnableWheelEvent)


class _Test_(object):

    _widgets = None

    def __init__(self, layout, model, column):
        super(_Test_, self).__init__()
        self._widgets = []
        self._layout = layout
        self._checkbox = Qt.QCheckBox("Enable Wheel Event")
        self._layout.addWidget(self._checkbox, 0, column)
        self._taurusSpinBox = LinacValueSpinBox()
        self._taurusSpinBox.setModel(model)
        self._layout.addWidget(self._taurusSpinBox, 1, column)
        self._widgets.append(self._taurusSpinBox)
        self._saveRetrieve = SaveRetrieveSpinBox()
        self._layout.addWidget(self._saveRetrieve, 2, column)
        self._widgets.append(self._saveRetrieve)
        self._doubleSaveRetrieve = SaveRetrieveDoubleSpinBox()
        self._layout.addWidget(self._doubleSaveRetrieve, 3, column)
        self._widgets.append(self._doubleSaveRetrieve)
        self._checkbox.stateChanged.connect(
            lambda: self.enable(self._checkbox))

    def enable(self, checkbox):
        value = checkbox.isChecked()
        print("%s Wheel Event" % ("Enable" if value else "Disable"))
        for widget in self._widgets:
            widget.setEnableWheelEvent(value)


def main():
    import sys
    import taurus.qt.qtgui.application
    Application = taurus.qt.qtgui.application.TaurusApplication

    app = Application.instance()
    owns_app = app is None

    if owns_app:
        import taurus.core.util.argparse
        parser = taurus.core.util.argparse.get_taurus_parser()
        parser.usage = "%prog [options] <full_attribute_name(s)>"
        app = Application(sys.argv, cmd_line_parser=parser,
                          app_name="Linac's Taurus spinbox demo",
                          app_version="1.0", org_domain="Alba",
                          org_name="Alba")

    args = app.get_command_line_args()

    w = Qt.QWidget()
    layout = Qt.QGridLayout()
    w.setLayout(layout)

    if len(args) == 0:
        models = ['sys/tg_test/1/double_scalar']
    else:
        models = args
    for i, model in enumerate(models):
        _Test_(layout, model, i)
    w.resize(300, 50)
    w.show()

    if owns_app:
        sys.exit(app.exec_())
    else:
        return w


if __name__ == "__main__":
    main()
