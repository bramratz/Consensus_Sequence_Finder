#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 12:52:55 2020

@author: bram
"""

# Import modules 
import sys
import numpy as np

# List to hold lines from raw fasta file 
DNAStringMatrix = []

with open(sys.argv[1]) as f:
    for line in f.readlines():
        if ">" in line:
            continue # Skip ID lines 
        else:
            string= [] # Temp list to hold bases from single line
            for char in line:
                if char == "\n":
                    continue # Don't include newline characters 
                string.append(char) # Add bases to string list
            DNAStringMatrix.append(string) # Append sequence to main list as a list 

# Convert to numpy array 
DNAStringArray = np.array(DNAStringMatrix)
print(DNAStringArray)

