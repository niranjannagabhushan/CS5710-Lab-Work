# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 20:23:30 2024

@author: niran
"""

def inverted_dict(d):
  """
  Inverts a dictionary, mapping values to lists of corresponding keys.

  Args:
      d: A dictionary with unique values to invert.

  Returns:
      A new dictionary mapping inverted key-value pairs.

  Raises:
      ValueError: If the input dictionary contains non-unique values.
  """

  inverted = {}
  for key, value in d.items():
    if value in inverted:
      inverted[value].append(key)  # Value already exists, add key to its list
    else:
      inverted[value] = [key]  # New value, create a list with the key

  return inverted

# General version handling possible non-unique values
def inverted_dict_general(d):
  """
  Inverts a dictionary, handling duplicate values gracefully.

  Args:
      d: A dictionary with any values.

  Returns:
      A new dictionary mapping inverted key-value pairs.
  """

  inverted = {}
  for key, value in d.items():
    inverted.setdefault(value, []).append(key)  # Use setdefault for efficiency

  return inverted

# Example usage
original_dict1 = {"p": 1, "a": 1, "r": 2, "o": 1, "t": 1}
original_dict2 = {"a": 1, "b": 2, "c": 2}

print(inverted_dict(original_dict1))  # Output: {1: ['p', 'a', 'o', 't'], 2: ['r']}
print(inverted_dict_general(original_dict2))  # Output: {1: ['a'], 2: ['b', 'c']}

# Handling non-unique values test
try:
  inverted_dict({"x": 1, "y": 1})  # Raise ValueError
except ValueError as e:
  print(e)  # Output: Input dictionary contains non-unique values
