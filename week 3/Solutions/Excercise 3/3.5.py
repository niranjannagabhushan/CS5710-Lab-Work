# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 19:32:57 2024

@author: niran
"""
import math
def apply_to_all(t, f):
    """
    Returns a tuple, which is the result of applying the function f to all elements of t.

    Parameters:
    t (tuple): The input tuple.
    f (function): The function to apply to each element of the tuple.

    Returns:
    tuple: A tuple containing the result of applying the function f to all elements of t.
    """
    # Apply the function f to each element of the tuple using a list comprehension
    result = tuple(f(x) for x in t)
    
    return result

# Example usage:

# Test with built-in/library functions
input_tuple = (1, -5, -6, 3)
result_abs = apply_to_all(input_tuple, abs)
print("Result with abs():", result_abs)

import math
result_sqrt = apply_to_all(input_tuple, math.sqrt)
print("Result with math.sqrt():", result_sqrt)

# Define a custom function
def square(x):
    return x ** 2

# Test with custom function
result_square = apply_to_all(input_tuple, square)
print("Result with custom square function:", result_square)
