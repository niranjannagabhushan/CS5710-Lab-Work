# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 20:26:54 2024

@author: niran
"""

def invert_dict(input_dict):
    """
    Inverts the input dictionary in place.

    Parameters:
    input_dict (dict): The input dictionary to be inverted.
    """
    inverted = {}
    for key, value in input_dict.items():
        if value not in inverted:
            inverted[value] = [key]
        else:
            inverted[value].append(key)
    
    # Clear input_dict and update it with the inverted dictionary
    input_dict.clear()
    input_dict.update(inverted)

# Test case
input_dict = {'p': 1, 'a': 1, 'r': 2, 'o': 1, 't': 1}
invert_dict(input_dict)
print(input_dict)  # Output: {1: ['p', 'a', 'o', 't'], 2: ['r']}
