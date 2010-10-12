#!/usr/bin/env python
"""
    Collection of python utility scripts for OSX

    @author: Jean-Lou Dupont
"""
__author__  ="Jean-Lou Dupont"
__version__ ="0.2"

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
      install_requires=[ "appscript >= 0.21", "jld_scripts >= 0.6"
                        ],
      zip_safe=False
      )
