# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 05:15:12 2025
Setup file for Cython 2nd Example
@author: Taufik Sutanto
"""

from setuptools import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize("simple.pyx"))