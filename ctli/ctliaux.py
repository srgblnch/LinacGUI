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

__author__ = "Sergi Blanch-Torne"
__copyright__ = "Copyright 2015, CELLS / ALBA Synchrotron"
__license__ = "GPLv3+"


import os
from socket import gethostname
from getpass import getuser
from taurus import setLogLevel, Trace, Info
from taurus.core.tango.util import tangoFormatter
from taurus.external.qt import Qt
from .ctliversion import version

VERSION = "%s" % (version())

# storage sandbox ---
sandbox = '/data'
linacbox = "%s/LINAC" % (sandbox)
defaultConfigurations = "%s/Configurations" % (linacbox)
commentsfile = "%s/.ctli_comments" % (linacbox)
defaultPreconfTrends = "%s/Taurustrend_preconfig" % (linacbox)


######
# Auxiliar methods to configure widgets ---
def _setupLed4UnknownAttr(widget):
    widget.setLedPatternName("leds_images256:led_{color}_{status}.png")
    widget.setOnColor('green')
    widget.setOffColor('white')
    widget.hide()


def _setupLed4Attr(widget, attrName, inverted=False, onColor='green',
                   offColor='red', pattern='on', blinkOnChange=None):
    widget.setModel(attrName)
    if pattern == 'on':
        widget.setLedPatternName("leds_images256:led_{color}_on.png")
    widget.setOnColor(onColor)
    widget.setOffColor(offColor)
    if inverted:
        widget.setLedInverted(True)
    # FIXME: not operative by now
#     if blinkOnChange:
#         #list ['on','off'] or only one of them.
#         widget.setBlinkOnChange(blinkOnChange)
#         widget.setBlinkTime(10)
#         widget.setBlinkPeriod(1)


def _setupCheckbox4UnknownAttr(widget):
    widget.setEnabled(False)


def _setupCheckbox4Attr(widget, attrName, isRst=False, DangerMsg='',
                        riseEdge=False, fallingEdge=False):
    widget.setModel(attrName)
    if isRst:
        widget.setResetCheckBox(True)
    if len(DangerMsg) > 0:
        widget.setDangerMessage(DangerMsg)
    if riseEdge:
        widget.setDangerRiseEdge(True)
    if fallingEdge:
        widget.setDangerFallingEdge(True)
    widget.setAutoApply(True)
    if not riseEdge and not fallingEdge:
        widget.setForcedApply(True)


def _setupSpinBox4Attr(widget, attrName, step=None, DangerMsg='',
                       dangerAbove=None, dangerBelow=None):
    magnitudeSuffix = "#wvalue.magnitude"  # avoid units on the spinboxes
    if not attrName.endswith(magnitudeSuffix):
        attrName = "%s%s" % (attrName, magnitudeSuffix)
    widget.setModel(attrName)
    widget.FORMAT = tangoFormatter
    widget.setAutoApply(True)
    widget.setForcedApply(False)
    if step is not None:
        widget.setSingleStep(step)
    if len(DangerMsg) > 0:
        widget.setDangerMessage(DangerMsg)
    if dangerAbove is not None:
        widget.setDangerAbove(dangerAbove)
    if dangerBelow is not None:
        widget.setDangerBelow(dangerBelow)


def _setupTaurusLabel4Attr(widget, attrName, unit=None):
    widget.setModel(attrName)
    widget.FORMAT = tangoFormatter
    try:
        attrModelObj = widget.getModelObj()
        # First check if the TaurusAttribute has interpreted the unit from
        # the TangoAttribute configuration.
        if hasattr(attrModelObj, 'rvalue') and \
                hasattr(attrModelObj.rvalue, 'u'):
            attrUnit = attrModelObj.rvalue.u
            if len(str(attrUnit)) == 0:
                attrUnit = None
        else:  # Initialise the variable, no unit within the device attribute
            attrUnit = None
        if attrUnit is not None:
            if str(attrUnit) != unit:
                widget.warning("Indicated unit (%s)doesn't match with the "
                               "specified in the device attribute (%s). "
                               "Ignoring the indicated."
                               % (unit, attrUnit))
            # else, they match, no suffix needed
        elif unit:  # not specified but indicated
            widget.warning("Device attribute miss the unit configuration, "
                           "but fixed in the gui.")
            widget.setSuffixText(' %s' % (unit))
        # else, no units anywhere
    except Exception as e:
        widget.error("With %s, exception: %s" % (attrName, e))


def _setupCombobox4Attr(widget, attrName, valueNames=None):
    widget.setModel(attrName)
    widget.setAutoApply(True)
    widget.setForcedApply(True)
    if valueNames is not None and type(valueNames) == list and \
            len(valueNames) > 0:
        widget.addValueNames(valueNames)


def _setupActionWidget(widget, attrName, text='on/off', isRst=False,
                       isValve=False, isLight=False, DangerMsg='',
                       riseEdge=False, fallingEdge=False):
    widget._ui.Label.setText(text)
    if isRst:
        _setupLed4Attr(widget._ui.Led, attrName, offColor='black',
                       onColor='yellow')
    elif isValve:
        _setupLed4Attr(widget._ui.Led, attrName, offColor='green',
                       onColor='red', pattern='')
    elif isLight:
        _setupLed4Attr(widget._ui.Led, attrName, offColor='black',
                       onColor='white')
    else:
        _setupLed4Attr(widget._ui.Led, attrName, pattern='')
    _setupCheckbox4Attr(widget._ui.Check, attrName, isRst, DangerMsg,
                        riseEdge, fallingEdge)
# Done auxiliar methods to configure widgets ---
######


######
# log the output ---
def prepareToLog(app, appName):
    LOGDIR = "/control/logs"
    ALTERNATIVE_LOGDIR = "/tmp"
    if os.path.isdir(LOGDIR):
        logdirectory = LOGDIR
    else:
        logdirectory = ALTERNATIVE_LOGDIR
    hostname = gethostname()
    username = getuser()
    logfilename = "%s/%s_%s_%s.log" % (logdirectory, appName, hostname,
                                       username)
    app.basicConfig(log_file_name=logfilename)
    setLogLevel(Info)
# Done logging the output ---
######
