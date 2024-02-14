# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 19:28:50 2024

@author: niran
"""

def apply_to_all(t, f):
  """
  Applies a function f to all elements of a tuple and returns a new tuple with the results.

  Args:
      t: A tuple containing any data types.
      f: A function to apply to each element of the tuple.

  Returns:
      A new tuple containing the results of applying f to each element of t.

  Raises:
      TypeError: If f is not a callable function.
  """

  if not callable(f):
    raise TypeError("f must be a callable function")

  return tuple(f(item) for item in t)  # List comprehension for cleaner, efficient generation

# Example usage with built-in/library functions
import math
print(apply_to_all((1, -5, -6, 3), abs))  # Output: (1, 5, 6, 3)
print(apply_to_all((4.2, 3.14, -2.5), int))  # Output: (4, 3, -2)
print(apply_to_all((9, 16, 25), math.sqrt))  # Output: (3.0, 4.0, 5.0)

# Example usage with custom function
def double(x):
  return x * 2

print(apply_to_all((1, 2, 3), double))  # Output: (2, 4, 6)
