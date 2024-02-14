# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 18:58:31 2024

@author: niran
"""

def sum_mult(numbers):
    """
    Returns a tuple consisting of the sum and product of numbers in the input tuple.

    Parameters:
    numbers (tuple): A tuple of numbers (integers or floats).

    Returns:
    tuple: A tuple consisting of the sum and product of numbers if the tuple is non-empty, otherwise None.
    """
    # Check if the tuple is empty
    if not numbers:
        return None

    # Initialize variables to store sum and product
    sum_result = 0
    product_result = 1

    # Calculate sum and product of numbers in the tuple
    for num in numbers:
        sum_result += num
        product_result *= num

    # Return tuple consisting of sum and product
    return sum_result, product_result

# Example usage:
print(sum_mult((1, 2, 3, 6)))  # Output: (12, 36)
print(sum_mult((10,)))         # Output: (10, 10)
print(sum_mult(()))            # Output: None
