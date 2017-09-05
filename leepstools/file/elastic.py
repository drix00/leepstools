#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: leepstools.file.elastic

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Read and generate LEEPS elastic file .ees.
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
import os.path

# Third party modules.

# Local modules.

# Project modules.

# Globals and constants variables.


class Elastic():
    pass


def generate_elastic_file(program_file_path, elastic_file_path, composition):
    if not os.path.isfile(program_file_path):
        raise ValueError

