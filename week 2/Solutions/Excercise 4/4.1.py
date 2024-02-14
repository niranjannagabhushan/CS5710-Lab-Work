# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 10:50:10 2024

@author: niran
"""

def max3(a, b, c):
    """
    Returns the largest of three integers.

    Parameters:
    a (int): The first integer.
    b (int): The second integer.
    c (int): The third integer.

    Returns:
    int: The largest of the three integers.
    """
    return max(a, b, c)

# Example usage:
largest = max3(5, 10, 3)
print("The largest of the three integers is:", largest)
