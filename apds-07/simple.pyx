# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 05:14:34 2025
Cython Example 02
@author: Taufik Sutanto
"""

def py_square(numbers):
    result = []
    for n in numbers:
        result.append(n*n)
    return result