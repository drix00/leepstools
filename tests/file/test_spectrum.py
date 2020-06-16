#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.file.spectrum

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`leepstools.file.spectrum`.
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

# Third party modules.
from pkg_resources import resource_filename  # @UnresolvedImport
import pytest

# Local modules.

# Project modules.
from leepstools.file.spectrum import Spectrum
from tests import is_bad_file


# Globals and constants variables.


class TestSpectrum(unittest.TestCase):
    """
    TestCase class for the module `leepstools.file.spectrum`.
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

        file_path = resource_filename(__name__, "../../test_data/li2o/spectrum.dat")
        if is_bad_file(file_path):  # pragma: no cover
            pytest.skip("File not found: {}".format(file_path))

        spectrum_file = Spectrum()
        self.assertEqual(0, len(spectrum_file.energy_eV))
        self.assertEqual(0, len(spectrum_file.energy_loss_eV))
        self.assertEqual(0, len(spectrum_file.probability_1_eVe))
        self.assertEqual(0, len(spectrum_file.stu_1_eVe))

        spectrum_file.read(file_path)

        self.assertEqual(1000, len(spectrum_file.energy_eV))
        self.assertEqual(1000, len(spectrum_file.energy_loss_eV))
        self.assertEqual(1000, len(spectrum_file.probability_1_eVe))
        self.assertEqual(1000, len(spectrum_file.stu_1_eVe))

        # 2.900050E+04  9.995000E+02  1.650000E-08  8.616843E-09
        self.assertAlmostEqual(2.900050E+04, spectrum_file.energy_eV[0])
        self.assertAlmostEqual(9.995000E+02, spectrum_file.energy_loss_eV[0])
        self.assertAlmostEqual(1.650000E-08, spectrum_file.probability_1_eVe[0])
        self.assertAlmostEqual(8.616843E-09, spectrum_file.stu_1_eVe[0])

        # 2.999950E+04  4.999000E-01  3.053247E-01  3.089428E-05
        self.assertAlmostEqual(2.999950E+04, spectrum_file.energy_eV[-1])
        self.assertAlmostEqual(4.999000E-01, spectrum_file.energy_loss_eV[-1])
        self.assertAlmostEqual(3.053247E-01, spectrum_file.probability_1_eVe[-1])
        self.assertAlmostEqual(3.089428E-05, spectrum_file.stu_1_eVe[-1])

        # self.fail("Test if the testcase is working.")
        self.assertTrue(True)
