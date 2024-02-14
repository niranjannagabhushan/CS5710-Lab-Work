# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 19:03:57 2024

@author: niran
"""

def area(shape, n):
    """
    Input: shape, a function representing a geometric shape
           n, a parameter for the shape function
    Returns: the area of the shape with parameter n
    """
    return shape(n)

def circle(radius):
    """
    Input: radius, a positive float
    Returns the area of a circle with the given radius
    """
    return 3.14 * radius ** 2

def square(length):
    """
    Input: length, a positive float
    Returns the area of a square with sides of the given length
    """
    return length * length

# Example function calls
print(area(circle, 10))  # (a) the area of a circle with a radius of 10
print(area(square, 5))   # (b) the area of a square with sides of length 5
print(area(circle, 2))   # (c) the area of a circle with diameter of length 4 (radius = 2)
