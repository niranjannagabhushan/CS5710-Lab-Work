# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 19:06:39 2024

@author: niran
"""

def sum_mult(numbers):
  """
  Calculates the sum and product of numbers in a tuple.

  Args:
      numbers: A tuple of numbers (integers or floats).

  Returns:
      A tuple containing the sum and product of the numbers, or None if the tuple is empty.
  """

  if not numbers:
    return None  # Handle empty tuple efficiently

  sum_value = 0
  product_value = 1

  for number in numbers:
    if not isinstance(number, (int, float)):
      # Raise a ValueError for non-numeric values
      raise ValueError("Input tuple must contain only numbers (integers or floats)")
    sum_value += number
    product_value *= number

  return sum_value, product_value

# Example usage
print(sum_mult((1, 2, 3, 6)))  # Output: (12, 36)
print(sum_mult((10,)))  # Output: (10, 10)
print(sum_mult(()))  # Output: None
print(sum_mult((1, "hello", 3)))  # Output: ValueError
