#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: leepstools.file.angle

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Read angle distribution result from LEEPS simulation.
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


class Angle():
    def __init__(self):
        self.theta_deg = []
        self.probability_1_sr = []
        self.stu_1_sr = []

    def read(self, file_path):
        lines = []

        with open(file_path) as input_file:
            lines = input_file.readlines()

        for line in lines:
            line = line .strip()

            if not line.startswith('#'):
                items = line.split()

                try:
                    theta_deg = float(items[0])
                    probability_1_sr = float(items[1])
                    stu_1_sr = float(items[2])

                    self.theta_deg.append(theta_deg)
                    self.probability_1_sr.append(probability_1_sr)
                    self.stu_1_sr.append(stu_1_sr)
                except IndexError:
                    pass
