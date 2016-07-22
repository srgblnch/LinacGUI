#!/usr/bin/env python
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


from taurus import Device
import traceback


enums = {'1': ['ATT2_u', 'GUN_Cathode_u', 'GUN_CDB_u', 'GUN_HVps_u', 'TU_u',
               'A0_u', 'LLRF_u'],
         '2': ['IP%d_u' % i for i in range(1, 10)] +
              ['HVG%d_u' % i for i in range(1, 6)] +
              ['IPC%d_u' % i for i in range(1, 6)],
         '3': ['BC%dF_u' % i for i in range(1, 3)] + ['GL_u'] +
              ['SL%dF_u' % i for i in range(1, 5)] +
              ['QT1F_u', 'QT2F_u', 'QT1H_u', 'QT2V_u'],
         'k': ['ka_tube_u', 'ka_thyratron_u', 'ka_3GHz_RFampli_u',
               'ka_DCps_thyratron_u', 'ka_HVps_u', 'ka_IP_controller',
               'ka_fcoil1_u', 'ka_fcoil2_u', 'ka_fcoil3_u']
         }


class AttrEnum(object):
    def __init__(self, devName, attrPrefix, *args, **kwargs):
        super(AttrEnum, self).__init__(*args, **kwargs)
        self._devName = devName
        self._attrPrefix = attrPrefix
        self._device = Device(self._devName)
        try:
            self._device.ping()
        except Exception as e:
            print("Can not work with %s" % devName)

    @property
    def options(self):
        try:
            return eval(self._device[self._attrPrefix+'_options'].value)
        except:
            return '[]'

    @options.setter
    def options(self, value):
        try:
            self._device[self._attrPrefix+'_options'] = value
        except Exception as e:
            raise TypeError("Those options can not be set (%s)" % e)

    @property
    def active(self):
        try:
            return self._device[self._attrPrefix+'_active'].value
        except:
            return None

    @active.setter
    def active(self, value):
        options = self.options
        if value in options:
            self._device[self._attrPrefix+'_active'] = value
        else:
            raise ValueError("%s is not in the list of options %s"
                             % (value, options))

    @property
    def numeric(self):
        try:
            return self._device[self._attrPrefix+'_numeric'].value
        except:
            return None

    @property
    def meaning(self):
        try:
            return self._device[self._attrPrefix+'_meaning'].value
        except:
            return None


def getHeader():
    return "#Device Name\tElement\tOptions\tActive\tNumeric\tMeaning\n"


def doRead(devName, attrName):
    reader = AttrEnum(devName, attrName)
    return [devName, attrName, reader.options, reader.active,
            reader.numeric, reader.meaning]


def collect():
    rows = []
    for i in enums.keys():
        for attrName in enums[i]:
            if i == 'k':
                rows.append(doRead('li/ct/plc4', attrName))
                rows.append(doRead('li/ct/plc5', attrName))
            else:
                rows.append(doRead('li/ct/plc%s' % (i), attrName))
    return rows


def checkFile(fileName):
    if not fileName.endswith('.csv'):
        fileName += '.csv'
    return fileName


def fileExist(fileName):
    import os.path
    return os.path.isfile(fileName)


def store(fileName, rows):
    fileName = checkFile(fileName)
    if not fileExist(fileName):
        with open(fileName, 'w') as f:
            f.write(getHeader())
            for r in rows:
                line = "".join("%s\t" % c for c in r)
                f.write(line[:-1]+'\n')


def parse(fileName):
    dct = {}
    fileName = checkFile(fileName)
    if fileExist(fileName):
        with open(fileName, 'r') as f:
            line = f.readline().strip()
            while len(line) > 0:
                if not line.startswith('#'):  # ignore comment lines
                    lst = line.split('\t')
                    devName = lst[0]
                    attrName = lst[1]
                    options = eval(lst[2])
                    active = lst[3]
                    if active == 'None':
                        active = None
                    keyName = devName+'/'+attrName
                    if devName not in dct:
                        dct[devName] = {}
                    if attrName not in dct[devName]:
                        dct[devName][attrName] = [options, active]
                line = f.readline().strip()  # next()
        return dct
    else:
        print("File %s does not exist" % fileName)
        return None


def apply(values):
    for devName in values:
        for attrName in values[devName]:
            writter = AttrEnum(devName, attrName)
            options = values[devName][attrName][0]
            active = values[devName][attrName][1]
            # print("%s/%s: %s, %s" % (devName, attrName, options, active))
            try:
                options = str(options)
                if options != writter.options:
                    print("\tSet options for %s/%s: %s"
                          % (devName, attrName, options))
                    writter.options = options
                if writter.options is not None:
                    if active not in writter.options:
                        print("\t%s is not in the list of options")
                    elif writter.active is None or active != writter.active:
                        print("\tSet active element for %s/%s: %s"
                              % (devName, attrName, active))
                        writter.active = active
            except Exception as e:
                print("\t*** Do it manually ***")
                traceback.print_exc()


def main():
    from optparse import OptionParser
    parser = OptionParser()
#     parser.add_option('', "--debug", action="store_true", default=False,
#                       help="Set the debug flag")
    parser.add_option('', "--save-csv",
                      help="Generate a CSV file with the enumeration "
                           "information.")
    parser.add_option('', "--load-csv",
                      help="Given a csv file apply it to the devices")
    (options, args) = parser.parse_args()
    if options.save_csv is not None:
        values = collect()
        store(options.save_csv, values)
    elif options.load_csv is not None:
        values = parse(options.load_csv)
        if values is not None:
            apply(values)
    else:
        print("\nNo options selected. Please check help\n")

if __name__ == '__main__':
    main()
