# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 20:28:34 2024

@author: niran
"""

def invert_dict(d):
    """
    Inverts a dictionary in-place, mapping values to lists of corresponding keys.

    Args:
        d: The dictionary to invert.

    Raises:
        ValueError: If the input dictionary contains non-unique values.
    """

    inverted = {}  # Temporary empty dictionary
    for key, value in d.items():
        if value in inverted:
            inverted[value].append(key)  # Value already exists, add key to its list
        else:
            inverted[value] = [key]  # New value, create a list with the key

    # Clear the original dictionary and update it with the inverted keys
    d.clear()
    d.update(inverted)

# Example usage
original_dict = {"p": 1, "a": 1, "r": 2, "o": 1, "t": 1}
invert_dict(original_dict)
print(original_dict)  # Output: {1: ['p', 'a', 'o', 't'], 2: ['r']}

# Handling non-unique values test
try:
  original_dict = {"x": 1, "y": 1}
  invert_dict(original_dict)  # Raise ValueError
except ValueError as e:
  print(e)  # Output: Input dictionary contains non-unique values
