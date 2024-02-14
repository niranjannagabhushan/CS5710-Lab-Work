# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 11:29:51 2024

@author: niran
"""

def reverse(text):
  """
  Reverses the given text.

  Args:
      text: The text to reverse.

  Returns:
      The reversed text.
  """

  reversed_text = ""
  for char in text:
    # Append each character to the beginning of the reversed_text string
    reversed_text = char + reversed_text
  return reversed_text

# Example usage
text = "left to right"
reversed_text = reverse(text)
print(reversed_text)  # Output: "thgir ot tfel"
