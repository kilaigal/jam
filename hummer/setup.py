#!/usr/bin/env python
# ~*~ encoding: utf-8 ~*~
"""setup.py for flap.hummer."""

# import built-in
import os
import re
from codecs import open

from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))


PROJECT = 'flap.hummer'
VERSION = '0.1.0'
URL = ''
DESC = "flap hummer"


def read_file(file_name):
    file_path = os.path.join(here, file_name)
    return open(file_path, encoding='utf-8').read().strip()


def parse_requirements(file_name):
    """Taken from http://cburgmer.posterous.com/pip-requirementstxt-and-setuppy"""
    with open(os.path.join(here, file_name), encoding='utf-8') as in_file:
        filtered = filter(lambda x: not re.match(r'(^#)|(^$)', x), in_file)
        filtered = filter(lambda x: not x.startswith('-'), filtered)
        return list(filtered)


setup(
    name=PROJECT,
    version=VERSION,
    description=DESC,
    long_description=read_file('README.rst'),
    keywords="",
    url=URL,
    license=read_file('LICENSE'),
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests", "doc"]),
    namespace_packages=[u'flap'],
    include_package_data=True,
    install_requires=parse_requirements("requirements.txt"),
    zip_safe=False,
    classifiers=[
        # see http://pypi.python.org/pypi?:action=list_classifiers
        # -*- Classifiers -*-
        "Programming Language :: Python",
    ],
)
