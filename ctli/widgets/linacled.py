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
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

__author__ = "Sergi Blanch-Torne"
__copyright__ = "Copyright 2015, CELLS / ALBA Synchrotron"
__license__ = "GPLv3+"

"""This module provides an specialization of the TaurusLed to include
   any new feature request for this linac control"""

__all__ = ["LinacLed"]

from taurus.qt.qtgui.display import TaurusLed
from taurus.qt.qtgui.display.taurusled import _TaurusLedController
from time import time, sleep
from threading import Thread

BLINK_OFF2ON = 0b01
BLINK_ON2OFF = 0b10
BLINK_BOTH = BLINK_OFF2ON | BLINK_ON2OFF


class LinacLed(TaurusLed):
    def __init__(self, parent=None, designMode=False):
        super(LinacLed, self).__init__(parent, designMode)
        self._blinking = None
        self._blinkTime = None  # seconds
        self._blinkPeriod = None  # seconds
        self._blinkThread = None
        self._blinkStart = None
        self._evtvalue_value = None

    def _calculate_controller_class(self):
        try:
            return TaurusLed._calculate_controller_class(self)
        except Exception as e:
            self.warning("For %s model exception in "
                         "_calculate_controller_class(): %s"
                         % (self.getModel(), e))
            return _TaurusLedController

    def handleEvent(self, evt_src, evt_type, evt_value):
        if self._blinking and hasattr(evt_value, 'value'):
            self.info("Received event %s (%s) = %s"
                      % (evt_src, evt_type, evt_value.value))
            self._evtvalue_value = evt_value.value
            if self.hasToBlink() and not self._blinkThread:
                self._blinkThread = Thread(target=self.doBlink,
                                           args=([evt_value.value]))
                self.info("Created a blinking thread")
                self._blinkThread.start()
                self.info("Started the blinking thread")
        TaurusLed.handleEvent(self, evt_src, evt_type, evt_value)

    def hasToBlink(self):
        if bool(self._blinking & BLINK_OFF2ON) and self._evtvalue_value:
            return True
        if bool(self._blinking & BLINK_ON2OFF) and not self._evtvalue_value:
            return True
        return False

    def doBlink(self, value):
        self._blinkStart = time()
        color = self.getColor(value)
        print color
        setter = self.getColorSetter(value)
        while time() - self._blinkStart < self._blinkTime:
            if value and self.controller().widget().ledColor == "black":
                self.info("tic %s" % self.controller().valueObj().value)
                setter(color)
            else:
                self.info("tac %s" % self.controller().valueObj().value)
                setter("black")
            sleep(self._blinkPeriod)
            if not (value == self._evtvalue_value):
                # check if the other transition should blink
                # if it's the case restart blinking's count down
                # otherwise finish the blink
                if self.hasToBlink():
                    self.info("Restart blinking")
                    self._blinkStart = time()
                    value = self._evtvalue_value
                    color = self.getColor(value)
                else:
                    self.info("Abort blinking")
                    break
        setter(color)
        self.info("End blinking")
        self._blinkThread = None

    def getColor(self, value):
        if value:
            return self.onColor
        else:
            return self.offColor

    def getColorSetter(self, value):
        if value:
            return self.setOnColor
        else:
            return self.setOffColor

    def getBlinkOnChange(self):
        if self._blinking == BLINK_BOTH:
            return ['on', 'off']
        elif self._blinking == BLINK_ON2OFF:
            return ['off']
        elif self._blinking == BLINK_OFF2ON:
            return ['on']
        else:
            return []

    def setBlinkOnChange(self, when):
        whenBlink = 0
        if type(when) == str:
            when = [when]
        if type(when) == list:
            if 'on' in when:
                whenBlink |= BLINK_OFF2ON
            if 'off' in when:
                whenBlink |= BLINK_ON2OFF
        else:
            raise TypeError("Invalid Blinking configuration")
        self._blinking = whenBlink

    def getBlinkTime(self):
        return self._blinkTime

    def setBlinkTime(self, value):
        self._blinkTime = float(value)

    def getBlinkPeriod(self):
        return self._blinkPeriod

    def setBlinkPeriod(self, value):
        self._blinkPeriod = float(value)
