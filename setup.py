#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: setup

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Setup and configuration file for project leepstools.
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
from setuptools import setup, find_packages

# Local modules.

# Project modules.
from leepstools import __version__

# Globals and constants variables.


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    "nose",
    "coverage"
]

description = "Python script to use LEEPS Monte Carlo code"
# long_description = readme + '\n\n' + history
long_description = """
Python script to use LEEPS Monte Carlo code
"""

packages = find_packages()

setup(
    name='leepstools',
    version=__version__,
    description=description,
    long_description=long_description,
    author="Hendrix Demers",
    author_email='hendrix.demers@mail.mcgill.ca',
    url='https://github.com/drix00/leepstools',
    packages=packages,
    package_dir={'leepstools':
                 'leepstools'},
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='leepstools',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Physics',
        ],
    test_suite='nose.collector',
    tests_require=test_requirements
)
