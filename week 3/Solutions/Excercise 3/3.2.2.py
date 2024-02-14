# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 18:56:31 2024

@author: niran

modified the code to reverse the elements of the tuple inside
"""

def reverse(tup):
    """
    Returns the reversal of the input tuple with reversed elements inside tuples.

    Parameters:
    tup (tuple): The input tuple.

    Returns:
    tuple: The reversal of the input tuple with reversed elements inside tuples.
    """
    # Use slicing with a step of -1 to reverse the tuple
    reversed_tuple = tup[::-1]

    # Check each element in the reversed tuple
    for i, element in enumerate(reversed_tuple):
        # If the element is a tuple, reverse it
        if isinstance(element, tuple):
            reversed_tuple[i] = element[::-1]  # Reverse the tuple

    return reversed_tuple

# Example usage:
input_tuple = (3, 'hi', (5, 7), 8)
reversed_tuple = reverse(input_tuple)
print("The reversed tuple with reversed elements inside is:", reversed_tuple)
