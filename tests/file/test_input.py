#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.file.test_input

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`leepstools.file.input`.
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
import unittest
import os.path

# Third party modules.
from pkg_resources import resource_filename  # @UnresolvedImport
import pytest

# Local modules.

# Project modules.
from leepstools.file.input import Input
from tests import is_bad_file


# Globals and constants variables.


class TestInput(unittest.TestCase):
    """
    TestCase class for the module `leepstools.file.input`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

    def tearDown(self):
        """
        Teardown method.
        """

        unittest.TestCase.tearDown(self)

    def testSkeleton(self):
        """
        First test to check if the testcase is working with the testing framework.
        """

        # self.fail("Test if the testcase is working.")
        self.assertTrue(True)

    def test_read(self):
        """
        Test the read method.
        """

        file_path = resource_filename(__name__, "../../test_data/al/mcslab.in")
        if is_bad_file(file_path):  # pragma: no cover
            raise pytest.skip("File not found: {}".format(file_path))

        input_file = Input()

        input_file.read(file_path)

        self.assertEqual("Al xphoto", input_file.title.value)
        self.assertEqual(200e3, input_file.energy_eV.value)
        self.assertEqual((0.0, 0.0, -1.0), input_file.source_position.value)
        self.assertEqual((0.0, 0.0, 0.1146), input_file.source_angle_deg.value)
        self.assertEqual(1e-5, input_file.thickness_cm.value)
        self.assertEqual(50.0, input_file.absorption_energy_eV.value)
        self.assertEqual((0.0, 0.0, 0.5730), input_file.spectrometer_angle_deg.value)
        self.assertEqual((199500, 200e3, 2000), input_file.spectrometer_energy_eV.value)
        self.assertEqual("Al.ees", input_file.elastic_file.value)
        self.assertEqual("Al.oos", input_file.inelastic_file.value)
        self.assertEqual((0, 200e3, 2000), input_file.energy_distribution_eV.value)
        self.assertEqual(90, input_file.angle_distribution.value)
        self.assertEqual(100, input_file.depth_distribution.value)
        self.assertEqual((0, 10, 100), input_file.track_length_distribution.value)
        self.assertEqual("dump1.dmp", input_file.resume_file.value)
        self.assertEqual("dump2.dmp", input_file.dump_file.value)
        self.assertEqual(60, input_file.dump_period_s.value)
        self.assertEqual(2e9, input_file.number_trajectories.value)
        self.assertEqual(2e9, input_file.simulation_time_s.value)
        self.assertEqual((1, 1), input_file.random_number_seed.value)

        # self.fail("Test if the testcase is working.")
        self.assertTrue(True)

    def test_write(self):
        """
        Test the write method.
        """

        file_path = resource_filename(__name__, "../../test_data/al/mcslab.in")
        if is_bad_file(file_path):  # pragma: no cover
            raise pytest.skip("File not found: {}".format(file_path))

        input_file_ref = Input()
        input_file_ref.read(file_path)

        file_path = resource_filename(__name__, "../../test_data/al/mcslab_test_write.in")

        input_file = Input()

        input_file.title.value = "Al xphoto"
        input_file.energy_eV.value = 200.0e3
        input_file.dump_file.value = "dump2.dmp"

        input_file.write(file_path)

        self.assertEqual(True, os.path.isfile(file_path))

        input_file = Input()
        input_file.read(file_path)

        self.assertEqual(input_file_ref.title.value, input_file.title.value)
        self.assertEqual(input_file_ref.energy_eV.value, input_file.energy_eV.value)
        self.assertEqual(input_file_ref.source_position.value, input_file.source_position.value)
        self.assertEqual(input_file_ref.source_angle_deg.value, input_file.source_angle_deg.value)
        self.assertEqual(input_file_ref.thickness_cm.value, input_file.thickness_cm.value)
        self.assertEqual(input_file_ref.absorption_energy_eV.value, input_file.absorption_energy_eV.value)
        self.assertEqual(input_file_ref.spectrometer_angle_deg.value, input_file.spectrometer_angle_deg.value)
        self.assertEqual(input_file_ref.spectrometer_energy_eV.value, input_file.spectrometer_energy_eV.value)
        self.assertEqual(input_file_ref.elastic_file.value, input_file.elastic_file.value)
        self.assertEqual(input_file_ref.inelastic_file.value, input_file.inelastic_file.value)
        self.assertEqual(input_file_ref.energy_distribution_eV.value, input_file.energy_distribution_eV.value)
        self.assertEqual(input_file_ref.angle_distribution.value, input_file.angle_distribution.value)
        self.assertEqual(input_file_ref.depth_distribution.value, input_file.depth_distribution.value)
        self.assertEqual(input_file_ref.track_length_distribution.value, input_file.track_length_distribution.value)
        self.assertEqual(input_file_ref.resume_file.value, input_file.resume_file.value)
        self.assertEqual(input_file_ref.dump_file.value, input_file.dump_file.value)
        self.assertEqual(input_file_ref.dump_period_s.value, input_file.dump_period_s.value)
        self.assertEqual(input_file_ref.number_trajectories.value, input_file.number_trajectories.value)
        self.assertEqual(input_file_ref.simulation_time_s.value, input_file.simulation_time_s.value)
        self.assertEqual(input_file_ref.random_number_seed.value, input_file.random_number_seed.value)

        os.remove(file_path)

        # self.fail("Test if the testcase is working.")
        self.assertTrue(True)
