# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 09:41:26 2024

@author: niran
"""

# Get input from the user
string = input("Enter a string: ")

# Define vowels
vowels = {'a', 'e', 'i', 'o', 'u'}

# Initialize a counter for vowels at odd indices
count = 0

# Iterate over characters at odd indices in the string
for i in range(1, len(string), 2):
    if string[i].lower() in vowels:
        count += 1

# Print the result
print("Number of vowels at odd indices:", count)
