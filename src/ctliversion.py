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


#Look at https://en.wikipedia.org/wiki/Software_versioning

__MAJOR_VERSION = 2
__MINOR_VERSION = 64
__BUILD_VERSION = 0
__REVISION_VERSION = 0
__RELEASE_CANDIDATE = None


def version():
    if __RELEASE_CANDIDATE:
        return "%d.%d-rc%d"%(__MAJOR_VERSION,__MINOR_VERSION,
                             __RELEASE_CANDIDATE)
    else:
        return "%d.%d.%d-%d"%(__MAJOR_VERSION,__MINOR_VERSION,
                              __BUILD_VERSION,__REVISION_VERSION)