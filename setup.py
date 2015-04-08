#! /usr/bin/env python

from setuptools import setup

setup(name = 'doit-plugin-sample',
      description = 'a simple doit command plugin',
      version = '0.1.0',
      license = 'MIT',
      author = 'Eduardo Naufel Schettino',
      url = 'http://github.com/pydoit/doit-plugin-sample',
      py_modules=['doit_sample_cmd'],
      entry_points = {
          'doit.COMMAND': [
              'plug_sample = doit_sample_cmd:SampleCmd'
          ]
      },
      )
