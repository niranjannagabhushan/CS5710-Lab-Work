# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 10:16:24 2024

@author: niran
"""


# Get input from the user
s = input("Enter a string: ")

# Initialize count
count = 0

# Iterate through the string
for i in range(len(s) - len('tart') + 1):
    # Check if the substring starting at index i is 'tart'
    if s[i:i+len('tart')] == 'tart':
        count += 1

# Print the result
print("Number of times 'tart' appears in the string:", count)