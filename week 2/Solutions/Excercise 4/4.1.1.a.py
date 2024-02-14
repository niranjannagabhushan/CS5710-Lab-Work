# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 10:55:36 2024

@author: niran
"""

def max3(a: int, b: int, c: int) -> int:
  """
  This function takes three integers as input and returns the largest of them.

  Args:
      a: The first integer.
      b: The second integer.
      c: The third integer.

  Returns:
      The largest of the three input integers.
  """

  # Compare a and b, and store the larger value in temp
  temp = a if a > b else b

  # Compare max_so_far and c, and return the larger value
  return temp if temp > c else c

# Example usage
result = max3(10, 20, 5)
print(result)  # Output: 20
