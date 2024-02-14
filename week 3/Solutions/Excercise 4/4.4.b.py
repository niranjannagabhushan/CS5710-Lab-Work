# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 20:22:51 2024

@author: niran
"""

def inverted_dict(input_dict):
    """
    Returns an inverted copy of the input dictionary.

    Parameters:
    input_dict (dict): The input dictionary.

    Returns:
    dict: An inverted copy of the input dictionary.
    """
    inverted = {}
    for key, value in input_dict.items():
        if value not in inverted:
            inverted[value] = [key]
        else:
            inverted[value].append(key)
    return inverted

# Test case
input_dict = {'p': 1, 'a': 1, 'r': 2, 'o': 1, 't': 1}
result = inverted_dict(input_dict)
print(result)  # Output: {1: ['p', 'a', 'o', 't'], 2: ['r']}
