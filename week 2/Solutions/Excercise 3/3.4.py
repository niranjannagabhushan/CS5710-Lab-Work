# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 09:54:14 2024

@author: niran
"""

# Get input from the user
string = input("Enter a string: ")

# Length of the string
length = len(string)

# Length of each possible substring
subl = length // 3

# Check if the string is a concatenation of three identical substrings
if string[:subl] == string[subl:2*subl] == string[2*subl:]:
    print("string is a triple concat of", string[:subl])
else:
    print("string is not a triple concat")
