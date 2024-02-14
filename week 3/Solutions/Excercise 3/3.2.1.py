# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 18:55:22 2024

@author: niran
"""

def reverse(data):
  """
  Reverses the elements of a tuple.

  Args:
      data: A tuple containing any data types.

  Returns:
      A new tuple with the elements of the input tuple in reversed order.
  """

  reversed_data = []
  for item in reversed(data):
    # Recursively reverse nested tuples
    if isinstance(item, tuple):
      item = reverse(item)
    reversed_data.insert(0, item)
  return tuple(reversed_data)

# Example usage
data = (3, "hi", (5, 7), 8)
reversed_data = reverse(data)
print(reversed_data)  # Output: (8, (7, 5), 'hi', 3)
