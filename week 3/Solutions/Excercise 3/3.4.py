# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 19:08:28 2024

@author: niran
"""

def filter_odd(tup):
    """
    Returns a new tuple consisting of every other element of the input tuple starting from the first one.

    Parameters:
    tup (tuple): The input tuple.

    Returns:
    tuple: A new tuple consisting of every other element of the input tuple starting from the first one.
    """
    # Use slicing with step 2 to get every other element starting from index 0
    filtered_tuple = tup[::2]
    
    return filtered_tuple

# Example usage:
input_tuple = ('I', 'love', 'Python', 'and', 'Java')
result = filter_odd(input_tuple)
print("Filtered tuple:", result)
