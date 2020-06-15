#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 12:52:55 2020

@author: bram
"""

# Import modules 
import sys

DNAStringMatrix = []

with open(sys.argv[1]) as f:
    DNAStringMatrix.append([line for line in f if not ">" in line])
    
print(DNAStringMatrix)
        