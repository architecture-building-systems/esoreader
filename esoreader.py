# This file is licensed under the terms of the MIT license. See the file
# "LICENSE" in the project root for more information.
#
# This module was developed by Daren Thomas at the assistant chair for
# Sustainable Architecture and Building Technologies (Suat) at the Institute of
# Technology in Architecture, ETH Zuerich. See http://suat.arch.ethz.ch for
# more information.

'''
esoreader.py

reads through EnergyPlus .eso files and returns
a dictionary containing the results.
'''


class DataDictionary(object):
    def __init__(self, version=None, timestamp=None):
        '''
        variables = dict of ids, int => [reporting_frequency,
                                         key, variable, unit]

        index = dict {(key, variable, reporting_frequency) => id)}
        '''
        self.version = version
        self.timestamp = timestamp
        self.variables = {}
        self.index = {}

    def build_index(self):
        """builds a reverse index for finding ids.
        """
        for id, value in self.variables.items():
            reporting_frequency, key, variable, unit = value
            self.index[reporting_frequency, key, variable] = id

    def find_variable(self, search):
        """returns the coordinates (timestep, key, variable_name) in the
        data dictionary that can be used to find an index. The search is case
        insensitive."""
        return [(timestep, key, variable_name)
                for timestep, key, variable_name in self.index.keys()
                if search.lower() in variable_name.lower()]


def read_reporting_frequency(line):
    reporting_frequency = None
    if '! ' in line:
        line = line.split('! ')[0]
    if ' !' in line:
        line, reporting_frequency = line.split(' !')
        # RunPeriod contains more stuff (" [Value,Min,Month,Day,Hour,Minute,
        # Max,Month,Day,Hour,Minute]")split it off
        reporting_frequency = reporting_frequency.split()[0]
    return line, reporting_frequency


def read_variable_unit(variable):
    unit = None
    if '[' in variable:
        variable, unit = variable.split('[')
        unit = unit[:-1]  # remove ']' at the end
        variable = variable.strip()
    return variable, unit


def read(eso_file_path):
    """Read in an .eso file and return the data dictionary and a dictionary
    representing the data.
    This is probably the function you are looking for...
    """
    eso_file = open(eso_file_path, 'r')
    dd = read_data_dictionary(eso_file)
    dd.build_index()
    data = read_data(dd, eso_file)
    return dd, data


def read_data_dictionary(eso_file):
    """parses the head of the eso_file, returning the data dictionary.
    the file object eso_file is advanced to the position needed by
    read_data.
    """
    version, timestamp = [s.strip() for s in eso_file.next().split(',')[1:]]
    dd = DataDictionary(version, timestamp)
    line = eso_file.next().strip()
    while line != 'End of Data Dictionary':
        line, reporting_frequency = read_reporting_frequency(line)
        if reporting_frequency:
            fields = [f.strip() for f in line.split(',')]
            if len(fields) >= 4:
                id, nfields, key, variable = fields[:4]
            else:
                id, nfields, variable = fields[:3]
                key = None
            variable, unit = read_variable_unit(variable)
            dd.variables[int(id)] = [reporting_frequency, key, variable, unit]
        else:
            # ignore the lines that aren't report variables
            pass
        line = eso_file.next().strip()
    dd.ids = set(dd.variables.keys())
    return dd


def read_data(dd, eso_file):
    '''parse the data from the .eso file returning,
    NOTE: eso_file should be the same file object that was passed to
    read_data_dictionary(eso_file) to obtain dd.'''
    data = {}  # id => [value]
    for id in dd.variables.keys():
        data[id] = []
    for line in eso_file:
        if line.startswith('End of Data'):
            break
        fields = [f.strip() for f in line.split(',')]
        id = int(fields[0])
        if not id in dd.ids:
            # skip entries that are not output:variables
            continue
        data[id].append(float(fields[1]))
    return data
