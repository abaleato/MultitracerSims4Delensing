#!/usr/bin/env python

from distutils.core import setup

setup(name='multsims',
      version='0.1dev',
      description="""Generate Gaussian simulations of large-scale tracers which are 
                     appropriately correlated with a reference simulation and with 
                     themselves""",
      author='Anton Baleato Lizancos',
      author_email='ab2368@cam.ac.uk',
      packages=['multsims'],
     )