#!/usr/bin/env python

from os.path import exists
from setuptools import setup

packages = ['streamz4', 'streamz4.dataframe']

tests = [p + '.tests' for p in packages]


setup(name='streamz4',
      version='0.0.1',
      description='Streams',
      url='https://github.com/keepexploring/streamz3',
      maintainer='Joel',
      license='BSD',
      keywords='streams',
      packages=packages + tests,
      install_requires=['tornado', 'toolz', 'zict', 'six'],
      zip_safe=False)