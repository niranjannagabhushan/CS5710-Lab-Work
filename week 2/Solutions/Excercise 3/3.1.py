# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 14:11:00 2024

@author: niran
"""


# Get input from the user
string = input("Enter a string: ")

# Check if the string is empty
if string == '':
    print()
# Check if the string has length one
elif len(string) == 1:
    print("First and last character:", string)
else:
    print("First character:", string[0])
    print("Last character:", string[-1])
