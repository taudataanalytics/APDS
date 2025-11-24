# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 09:34:33 2025
@author: Taufik Sutanto

Compile from the terminal using the following command:
    python setup.py build_ext --inplace
"""

from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("HelloWorld.pyx")
)