#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: leepstools.file.input

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Read and write LEEPS input file .in
"""

###############################################################################
# Copyright 2017 Hendrix Demers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
###############################################################################

# Standard library modules.

# Third party modules.

# Local modules.

# Project modules.

# Globals and constants variables.


class Parameter:
    keyword_length = 6
    separator = ' '
    value_length = 120

    def __init__(self, keyword, default_value, comment, conversion):
        self.keyword = keyword
        self.default_value = default_value
        self.comment = comment
        self.conversion = conversion

        self.value = self.default_value

    def line(self):
        if isinstance(self.value, tuple):
            value = " ".join([str(item) for item in self.value])
        else:
            value = self.value

        line = "{:6s} {:120s}\n".format(self.keyword, str(value))
        return line

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        try:
            self._value = self.conversion(new_value)
        except (TypeError, ValueError):
            try:
                items = new_value.split()
            except AttributeError:
                items = new_value

            self._value = tuple((self.conversion(item) for item in items))


class Input:
    def __init__(self):
        self.title = Parameter("TITLE", "title", "Title of the job, up to 120 characters", str)
        self.energy_eV = Parameter("ENERGY", 30.0e3, "Initial energy (monoenergetic sources only)", float)
        # .. todo:: Find unit of SPOSIT.
        self.source_position = Parameter("SPOSIT", (0.0, 0.0, -1.0), "Coordinates of the source centre", float)
        self.source_angle_deg = Parameter("SCONE", (0.0, 0.0, 0.1146), "Conical beam; angles in deg", float)
        # .. todo:: Find unit of THICK.
        self.thickness_cm = Parameter("THICK", 1.0e-5, "Slab thickness", float)
        self.absorption_energy_eV = Parameter("EABS", 50.0, "Absorption energy", float)
        self.spectrometer_angle_deg = Parameter("SPCANG", (0.0, 0.0, 0.5730), "Spectrometer directions; angles in deg", float)
        self.spectrometer_energy_eV = Parameter("SPCEN", (199500, 200e3, 2000), "Energy interval and no. of E-bins", float)
        self.elastic_file = Parameter("ELSCAT", "Al.ees", "Elastic scattering data", str)
        self.inelastic_file = Parameter("INSCAT", "Al.oos", "Inelastic scattering data", str)
        self.energy_distribution_eV = Parameter("NBE", (0.0, 200e3, 2000), "Energy interval and no. of E-bins", float)
        self.angle_distribution = Parameter("NBTH", 90, "No. of bins for the polar angle THETA", int)
        self.depth_distribution = Parameter("NBZ", 100, "No. of bins for the Z-coordinate", int)
        # .. todo:: Find unit of NBTL.
        self.track_length_distribution = Parameter("NBTL", (0, 10, 100), "Track-length interval and no. of TL-bins", int)
        self.resume_file = Parameter("RESUME", "dump1.dmp", "Resume from this dump file, 20 chars", str)
        self.dump_file = Parameter("DUMPTO", "dump1.dmp", "Generate this dump file, 20 chars", str)
        self.dump_period_s = Parameter("DUMPP", 60, "Dumping period, in sec", int)
        self.number_trajectories = Parameter("NSIMSH", 2e9, "Desired number of simulated showers", float)
        self.simulation_time_s = Parameter("TIME", 2e9, "Allotted simulation time, in sec", float)
        self.random_number_seed = Parameter("RSEED", (1, 1), "Seeds of the random-number generator", float)

    def read(self, file_path):
        with open(file_path) as input_file:
            lines = input_file.readlines()

            for line in lines:
                keyword = line[:Parameter.keyword_length].strip()
                value_string = line[Parameter.keyword_length:].strip()

                extract_value_from_line(self.title, keyword, value_string)
                extract_value_from_line(self.energy_eV, keyword, value_string)
                extract_value_from_line(self.source_position, keyword, value_string)
                extract_value_from_line(self.source_angle_deg, keyword, value_string)
                extract_value_from_line(self.thickness_cm, keyword, value_string)
                extract_value_from_line(self.absorption_energy_eV, keyword, value_string)
                extract_value_from_line(self.spectrometer_angle_deg, keyword, value_string)
                extract_value_from_line(self.spectrometer_energy_eV, keyword, value_string)
                extract_value_from_line(self.elastic_file, keyword, value_string)
                extract_value_from_line(self.inelastic_file, keyword, value_string)
                extract_value_from_line(self.energy_distribution_eV, keyword, value_string)
                extract_value_from_line(self.angle_distribution, keyword, value_string)
                extract_value_from_line(self.depth_distribution, keyword, value_string)
                extract_value_from_line(self.track_length_distribution, keyword, value_string)
                extract_value_from_line(self.resume_file, keyword, value_string)
                extract_value_from_line(self.dump_file, keyword, value_string)
                extract_value_from_line(self.dump_period_s, keyword, value_string)
                extract_value_from_line(self.number_trajectories, keyword, value_string)
                extract_value_from_line(self.simulation_time_s, keyword, value_string)
                extract_value_from_line(self.random_number_seed, keyword, value_string)

    def write(self, file_path):
        with open(file_path, 'w') as input_file:
            write_parameter(input_file, self.title)
            write_parameter(input_file, self.energy_eV)
            write_parameter(input_file, self.source_position)
            write_parameter(input_file, self.source_angle_deg)
            write_parameter(input_file, self.thickness_cm)
            write_parameter(input_file, self.absorption_energy_eV)
            write_parameter(input_file, self.spectrometer_angle_deg)
            write_parameter(input_file, self.spectrometer_energy_eV)
            write_parameter(input_file, self.elastic_file)
            write_parameter(input_file, self.inelastic_file)
            write_parameter(input_file, self.energy_distribution_eV)
            write_parameter(input_file, self.angle_distribution)
            write_parameter(input_file, self.depth_distribution)
            write_parameter(input_file, self.track_length_distribution)
            write_parameter(input_file, self.resume_file)
            write_parameter(input_file, self.dump_file)
            write_parameter(input_file, self.dump_period_s)
            write_parameter(input_file, self.number_trajectories)
            write_parameter(input_file, self.simulation_time_s)
            write_parameter(input_file, self.random_number_seed)


def extract_value_from_line(parameter, keyword, value_string):
    if keyword == parameter.keyword:
        value_end = value_string.find('[')
        if value_end != -1:
            value = value_string[:value_end]
        else:
            value = value_string

        parameter.value = value.strip()


def write_parameter(input_file, parameter):
    line = parameter.line()
    input_file.write(line)
