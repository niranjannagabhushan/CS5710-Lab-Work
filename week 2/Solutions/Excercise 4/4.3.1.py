# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 11:24:25 2024

@author: niran
"""

def min_max(digits):
  """
  This function finds the smallest and largest digits in a string and returns them as a string.

  Args:
      digits: A string containing digits.

  Returns:
      A string containing the smallest and largest digits in the input string,
      separated by a space.
  """

  smallest = largest = None

  for x in digits:
    digit_int = int(x)
    if smallest is None or digit_int < smallest:
      smallest = digit_int
    if largest is None or digit_int > largest:
      largest = digit_int

 

  return f"{smallest}{largest}"

# Example usage
result = min_max("31805")
print(result)  