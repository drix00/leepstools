#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.test_composition

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`leepstools.composition`.
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

# Local modules.

# Project modules.
from leepstools.composition import Composition, Element


# Globals and constants variables.


class TestComposition(unittest.TestCase):
    """
    TestCase class for the module `leepstools.composition`.
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
        self.assert_(True)

    def test_add_element(self):
        """
        Test add element in composition.
        """

        composition = Composition()

        self.assertEqual(0, len(composition.elements))

        composition.elements.append(Element(3, 2.0))
        composition.elements.append(Element(8, 1.0))

        self.assertEqual(2, len(composition.elements))

        self.assertEqual(3, composition.elements[0].atomic_number)
        self.assertEqual(8, composition.elements[1].atomic_number)

        self.assertAlmostEqual(2.0, composition.elements[0].stoichiometric_fraction)
        self.assertAlmostEqual(1.0, composition.elements[1].stoichiometric_fraction)

        # self.fail("Test if the testcase is working.")
        self.assert_(True)


if __name__ == '__main__':  # pragma: no cover
    import nose

    nose.runmodule()
