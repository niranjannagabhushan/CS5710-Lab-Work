# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 18:46:57 2024

@author: niran
"""

def reverse(tup):
    """
    Returns the reversal of the input tuple.

    Parameters:
    tup (tuple): The input tuple.

    Returns:
    tuple: The reversal of the input tuple.
    """
    # Use slicing with a step of -1 to reverse the tuple
    return tup[::-1]

# Example usage:
input_tuple = (3, 'hi', (5, 7), 8)
reversed_tuple = reverse(input_tuple)
print("The reversed tuple is:", reversed_tuple)
