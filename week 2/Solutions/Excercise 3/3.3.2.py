# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 09:53:19 2024

@author: niran
"""

def count_odd_vowels(string):
  """
  Counts the number of vowels appearing at odd indices in a string.

  Args:
      string: The input string.

  Returns:
      The number of vowels at odd indices.
  """
  vowels = "aeiouAEIOU"
  odd_vowel_count = 0
  for i, char in enumerate(string):
    if char in vowels and i % 2 == 1:
      odd_vowel_count += 1
  return odd_vowel_count

string = input("Enter a string: ")
vowel_count = count_odd_vowels(string)
print(f"The number of vowels at odd indices is: {vowel_count}")
