# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 19:52:06 2024

@author: niran
"""

def make_histogram(text):
  """
  Creates a dictionary mapping each letter in a string to its frequency.

  Args:
      text: A string of letters.

  Returns:
      A dictionary mapping each letter in the string to its frequency.
  """

  histogram = {}
  for letter in text.lower():  # Convert to lowercase for case-insensitive counting
    if letter.isalpha():  # Check if it's a letter
      histogram[letter] = histogram.get(letter, 0) + 1  # Use get() for efficiency

  return histogram

# Test cases
for test_text in [
    "parrot",
    "Mississippi",
    "aA!b@1c#2d$",
    "",  # Handle empty string
]:
  print(f"{test_text}: {make_histogram(test_text)}")
