# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 20:24:46 2024

@author: niran
"""

def inverted_dict(d):
    """
    Inverts a dictionary, mapping values to lists of corresponding keys.

    Args:
        d: The dictionary to invert.

    Returns:
        A new dictionary with inverted key-value pairs.
    """

    inverted = {}
    for key, value in d.items():
        try:
            inverted[value].append(key)  # Handle non-unique values gracefully
        except KeyError:
            inverted[value] = [key]  # Create a new list for the first occurrence of a value

    return inverted

# Example usage
original_dict = {"p": 1, "a": 1, "r": 2, "o": 1, "t": 1}
inverted_dict = inverted_dict(original_dict)
print(inverted_dict)  # Output: {1: ['p', 'a', 'o', 't'], 2: ['r']}
