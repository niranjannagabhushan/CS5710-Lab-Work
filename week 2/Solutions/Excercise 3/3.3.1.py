# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 09:52:46 2024

@author: niran
"""

string = input("Enter a string: ")

vowels = "aeiouAEIOU"
odd_vowel_count = 0

for i, char in enumerate(string):
  if char in vowels and i % 2 == 1:
    odd_vowel_count += 1

print(f"The number of vowels at odd indices is: {odd_vowel_count}")
