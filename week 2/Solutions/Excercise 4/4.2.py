# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 11:00:31 2024

@author: niran
"""

def sort3(a, b, c):
    """
    Returns a tuple consisting of three integers sorted in increasing order.

    Parameters:
    a (int): The first integer.
    b (int): The second integer.
    c (int): The third integer.

    Returns:
    tuple: A tuple consisting of three integers sorted in increasing order.
    """
    # Sort the three integers
    sorted_numbers = sorted([a, b, c])

    # Return the sorted tuple
    return tuple(sorted_numbers)

# Example usage:
sorted_tuple = sort3(5, 2, 8)
print("The sorted tuple is:", sorted_tuple)
