#!/usr/bin/env python

#############################################################################
##
## This file is part of Taurus, a Tango User Interface Library
## 
## http://www.tango-controls.org/static/taurus/latest/doc/html/index.html
##
## Copyright 2013 CELLS / ALBA Synchrotron, Bellaterra, Spain
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
###########################################################################

VERSION = '2.4.2'

import os
from socket import gethostname
from getpass import getuser
from taurus import setLogLevel,Trace

#---- storage sandbox
sandbox = '/data'
linacbox = "%s/LINAC"%(sandbox)
defaultConfigurations = "%s/Configurations"%(linacbox)
commentsfile = "%s/.ctli_comments"%(linacbox)
defaultPreconfTrends = "%s/Taurustrend_preconfig"%(linacbox)

######
#---- Auxiliar methods to configure widgets
def _setupLed4UnknownAttr(widget):
    widget.setLedPatternName(":leds/images256/led_{color}_{status}.png")
    widget.setOnColor('green')
    widget.setOffColor('white')
    widget.hide()

def _setupLed4Attr(widget,attrName,inverted=False,
                   onColor='green',offColor='red',pattern='on'):
    widget.setModel(attrName)
    if pattern == 'on':
        widget.setLedPatternName(":leds/images256/led_{color}_on.png")
    widget.setOnColor(onColor)
    widget.setOffColor(offColor)
    if inverted:
        widget.setLedInverted(True)

def _setupCheckbox4UnknownAttr(widget):
    widget.setEnabled(False)

def _setupCheckbox4Attr(widget,attrName,
                        isRst=False,DangerMsg='',
                        riseEdge=False,fallingEdge=False):
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

def _setupSpinBox4Attr(widget,attrName,step=None):
    widget.setModel(attrName)
    widget.setAutoApply(True)
    widget.setForcedApply(False)
    #if not step == widget.getSingleStep():
    if not step == None:
        widget.setSingleStep(step)

def _setupTaurusLabel4Attr(widget,attrName,unit=None):
    widget.setModel(attrName)
    if unit:
        widget.setSuffixText(' %s'%unit)

def _setupCombobox4Attr(widget,attrName,valueNames=None):
    widget.setModel(attrName)
    widget.setAutoApply(True)
    widget.setForcedApply(True)
    if valueNames != None and type(valueNames) == list and len(valueNames) > 0:
        widget.addValueNames(valueNames)
        
def _setupActionWidget(widget,attrName,text='on/off',
                       isRst=False,isValve=False,isLight=False,
                       DangerMsg='',riseEdge=False,fallingEdge=False):
    widget._ui.Label.setText(text)
    if isRst:
        _setupLed4Attr(widget._ui.Led,attrName,
                       offColor='black',onColor='yellow')
    elif isValve:
        _setupLed4Attr(widget._ui.Led,attrName,
                       offColor='green',onColor='red',pattern='')
    elif isLight:
        _setupLed4Attr(widget._ui.Led,attrName,
                       offColor='black',onColor='white')
    else:
        _setupLed4Attr(widget._ui.Led,attrName,pattern='')
    _setupCheckbox4Attr(widget._ui.Check,attrName,
                        isRst,DangerMsg,riseEdge,fallingEdge)
#---- Done auxiliar methods to configure widgets
######

######
#---- log the output
def prepareToLog(app,appName):
    LOGDIR = "/control/logs"
    ALTERNATIVE_LOGDIR = "/tmp"
    if os.path.isdir(LOGDIR):
        logdirectory = LOGDIR
    else:
        logdirectory = ALTERNATIVE_LOGDIR
    hostname = gethostname()
    username = getuser()
    logfilename = "%s/%s_%s_%s.log"%(logdirectory,appName,hostname,username)
    app.basicConfig(log_file_name=logfilename)
    setLogLevel(Trace)
#---- Done logging the output
######
