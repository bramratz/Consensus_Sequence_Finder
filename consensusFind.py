#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 12:52:55 2020

@author: bram
"""

# Import modules 
import sys
import numpy as np
import collections

# List to hold lines from raw fasta file 
DNAStringMatrix = []

###########################3

# Open and parse input file
with open(sys.argv[1]) as f:
    lines = [item.strip() for item in f.readlines() if not item == '']
    tempList = [] # list for sequences associated with each ID. Solves sequences on multiple lines issue.
    for line in lines:
        # All Lines with sequence IDs start with '>'
        if line.startswith('>'):
            # If sequences in temp when new ID reached add sequences to main 
            # list and empty tempList 
            if not len(tempList) == 0:
                DNAStringMatrix.append([','.join(tempList[1:])])
                tempList = [line,] # Empty List, Add new ID to it 
            # Add seq ID to list if it's the first sequence ID
            else:
                tempList = [line,]
        # Add sequences to the tempList if no ID is encountered
        else:
            for char in line:
                if char == "\n":
                    pass
                else:
                    tempList.append(char)
    # Handles sequence for last ID
    else:
        DNAStringMatrix.append([','.join(tempList[1:])])
"""
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
"""

print(DNAStringMatrix)
DNAStringArray = np.array(DNAStringMatrix) # Convert to numpy array 
DNAStringArray = np.transpose(DNAStringMatrix) # Transpose array so we can iterate down columns to find row[i] for each sequence 
print(DNAStringArray)

#############################################################3

basePosCount = {'A': [], 'C': [], 'G': [], 'T': []} # Dict to hold number of instances of a base at each position
consensusSeq = '' # Empty string to hold consensus sequence 

# Count number of time each base appears in row[i] in each column
for column in DNAStringArray:
    count = collections.Counter({'A': 0, 'C': 0, 'G': 0, 'T': 0}) # Initalize empty counter object 
    for item in column:
        for char in item:
            count[char] += 1 # Increase count if the base is present
    
    for k, v in count.items():
        basePosCount[k].append(v) # Add the number of times each base occured in row[i] to the position dict
    
    consensus = count.most_common(1) # Find most common base in row[i]
    consensusSeq += str(consensus[0][0]) # Add that base to the consensus sequence 

# Return consensus sequence and base counts for bases at position row[i]
print(consensusSeq)
for k, v in basePosCount.items():
    print("%s:" % (k), *v)
