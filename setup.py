#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    "nose"
]

setup(
    name='leepstools',
    version='0.1.0',
    description="Python script to use LEEPS Monte Carlo code",
    long_description=readme + '\n\n' + history,
    author="Hendrix Demers",
    author_email='hendrix.demers@mail.mcgill.ca',
    url='https://github.com/drix00/leepstools',
    packages=[
        'leepstools',
    ],
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
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
