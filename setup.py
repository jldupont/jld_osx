#!/usr/bin/env python
"""
    Collection of python utility scripts

    @author: Jean-Lou Dupont
"""
__author__  ="Jean-Lou Dupont"
__version__ ="0.1"

from distutils.core import setup
from setuptools import find_packages

setup(name=         'jld_osx',
      version=      __version__,
      description=  'Collection of python utility scripts for OSX',
      author=       __author__,
      author_email= 'jl@jldupont.com',
      url=          'http://www.systemical.com/doc/opensource/jld_osx',
      package_dir=  {'': "src",},
      packages=     find_packages("src"),
      scripts=      [ 'src/scripts/itunes_update_playcount'
                     ],
      zip_safe=False
      )
