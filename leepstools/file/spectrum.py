#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: leepstools.file.spectrum

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Read electron energy loss spectrum result from LEEPS simulation.
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


class Spectrum():
    def __init__(self):
        self.energy_eV = []
        self.energy_loss_eV = []
        self.probability_1_eVe = []
        self.stu_1_eVe = []

    def read(self, file_path):
        lines = []

        with open(file_path) as input_file:
            lines = input_file.readlines()

        for line in lines:
            line = line .strip()

            if not line.startswith('#'):
                items = line.split()

                try:
                    energy_eV = float(items[0])
                    energy_loss_eV = float(items[1])
                    probability_1_eVe = float(items[2])
                    stu_1_eVe = float(items[3])

                    self.energy_eV.append(energy_eV)
                    self.energy_loss_eV.append(energy_loss_eV)
                    self.probability_1_eVe.append(probability_1_eVe)
                    self.stu_1_eVe.append(stu_1_eVe)
                except IndexError:
                    pass
