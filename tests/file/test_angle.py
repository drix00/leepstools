#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.file.angle

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`leepstools.file.angle`.
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
from leepstools.file.angle import Angle
from tests import is_bad_file

# Globals and constants variables.


class TestAngle(unittest.TestCase):
    """
    TestCase class for the module `leepstools.file.angle`.
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

        file_path = resource_filename(__name__, "../../test_data/li2o/angle.dat")
        if is_bad_file(file_path):  # pragma: no cover
            pytest.skip("File not found: {}".format(file_path))

        angle_file = Angle()
        self.assertEqual(0, len(angle_file.theta_deg))
        self.assertEqual(0, len(angle_file.probability_1_sr))
        self.assertEqual(0, len(angle_file.stu_1_sr))

        angle_file.read(file_path)

        self.assertEqual(180, len(angle_file.theta_deg))
        self.assertEqual(180, len(angle_file.probability_1_sr))
        self.assertEqual(180, len(angle_file.stu_1_sr))

        # 5.000001E-01  4.789122E+02  3.492745E-02
        self.assertAlmostEqual(5.000001E-01, angle_file.theta_deg[0])
        self.assertAlmostEqual(4.789122E+02, angle_file.probability_1_sr[0])
        self.assertAlmostEqual(3.492745E-02, angle_file.stu_1_sr[0])

        # 1.795000E+02  1.807874E-04  2.915756E-05
        self.assertAlmostEqual(1.795000E+02, angle_file.theta_deg[-1])
        self.assertAlmostEqual(1.807874E-04, angle_file.probability_1_sr[-1])
        self.assertAlmostEqual(2.915756E-05, angle_file.stu_1_sr[-1])

        # self.fail("Test if the testcase is working.")
        self.assertTrue(True)
