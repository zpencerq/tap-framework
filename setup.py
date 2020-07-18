#!/usr/bin/env python

from setuptools import setup, find_packages
import os.path

setup(name='tap-framework',
      version='0.1.1',
      description='Framework for building Singer.io taps',
      author='Fishtown Analytics',
      url='http://fishtownanalytics.com',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_framework'],
      install_requires=[
          'singer-python>=5.8.0,<6.0.0',
          'requests==2.24.0',
      ],
      packages=['tap_framework'])
