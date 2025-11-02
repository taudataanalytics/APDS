# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 11:06:44 2025

@author: taufi
"""

class Cat:
    def __init__(self, species, age=1):
        self.kind = species
        self.age = age
    def eat(self, name = ''):
        print("yum yum ")