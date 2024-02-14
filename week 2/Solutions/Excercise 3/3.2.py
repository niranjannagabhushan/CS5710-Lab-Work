# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 09:06:35 2024

@author: niran
"""

string = input("Enter a string: ")

vowels = "aeiou"
all_vowels_there = all(x in string for x in vowels)

if all_vowels_there:
    print("All vowels are there!")

if string[0].lower() == "a" and string[-1].lower() == "z":
    print("And it could be alphabetical!")

