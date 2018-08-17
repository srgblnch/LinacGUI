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

from taurus.qt.qtgui.input import TaurusValueSpinBox
from taurus.external.qt import Qt
from taurus.qt.qtgui.base import TaurusBaseWritableWidget

__author__ = "Sergi Blanch-Torne"
__copyright__ = "Copyright 2018, CELLS / ALBA Synchrotron"
__license__ = "GPLv3+"

"""
This module provides an specialisation of the TaurusValueSpinBox to include
experimental features that would be later integrated in taurus.
Also another non-taurus widget used in the save/retrieve.
"""

__all__ = ["LinacValueSpinBox", "SaveRetrieveSpinBox"]


class LinacValueSpinBox(TaurusValueSpinBox):

    _dangerMessage = None
    _dangerAbove = None
    _dangerBelow = None

    def __init__(self, qt_parent=None, designMode=False):
        TaurusValueSpinBox.__init__(self, qt_parent, designMode)
        self.setEnableWheelEvent(False)
        self._dangerMessage = ""

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

    def isDangerAbove(self):
        return self._dangerAbove is not None and \
               self.getValue() > self._dangerAbove

    def isDangerBelow(self):
        return self._dangerBelow is not None and \
               self.getValue() < self._dangerBelow

    def isDangerousAction(self):
        return self.isDangerAbove() or self.isDangerBelow()

    def safeApplyOperations(self, ops=None):
        '''Modify the behaviour of the DangerMessage because in this case,
           different than a button, we may distinguish between set action and
           unset action.
           It seems that Taurus will someday support multiple Danger messages,
           but this widget did not copy this feature.
        '''
        if ops is None:
            ops = self.getPendingOperations()
        self.info("safeApplyOperations(ops=%s)" % (ops))
        # Check if we need to take care of dangerous operations
        if self.getForceDangerousOperations():
            dangerMsgs = []
        else:
            dangerMsgs = [op.getDangerMessage() for op in ops
                          if len(op.getDangerMessage()) > 0]
        # warn the user if need be
        if self.isDangerousAction():
            WarnTitle = "Potentially dangerous action"
            WarnMsg = "%s\nProceed?" % (dangerMsgs[0])
            Buttons = Qt.QMessageBox.Ok | Qt.QMessageBox.Cancel
            Default = Qt.QMessageBox.Cancel
            result = Qt.QMessageBox.warning(self, WarnTitle, WarnMsg,
                                            Buttons, Default)
            # Important default behaviour shall be the Cancel ---
            if result == Qt.QMessageBox.Cancel:
                self.info("safeApplyOperations(...) answer = Cancel")
                self._OperationCancelled()
            else:
                self.info("safeApplyOperations(...) answer = Ok")
                self.applyPendingOperations(ops)
        else:
            self.applyPendingOperations(ops)


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
        self._taurusSpinBox =  LinacValueSpinBox()
        self._taurusSpinBox.setModel(model)
        self._layout.addWidget(self._taurusSpinBox, 1, column)
        self._widgets.append(self._taurusSpinBox)
        self._saveRetrieve = SaveRetrieveSpinBox()
        self._layout.addWidget(self._saveRetrieve, 2, column)
        self._widgets.append(self._saveRetrieve)
        self._doubleSaveRetrieve = SaveRetrieveDoubleSpinBox()
        self._layout.addWidget(self._doubleSaveRetrieve, 3, column)
        self._widgets.append(self._doubleSaveRetrieve)
        self._checkbox.stateChanged.connect(lambda: self.enable(self._checkbox))

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
