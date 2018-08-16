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
from taurus.external.qt import Qt  # QDoubleSpinBox

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
    def __init__(self, qt_parent=None, designMode=False):
        TaurusValueSpinBox.__init__(self, qt_parent, designMode)
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
