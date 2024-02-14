# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 19:19:54 2024

@author: niran
"""

def min_max(numbers):
    """
    Returns a tuple consisting of the smallest and largest numbers in the input tuple.

    Parameters:
    numbers (tuple): A tuple of numbers.

    Returns:
    tuple: A tuple consisting of the smallest and largest numbers.
    """
    # Initialize variables to keep track of the smallest and largest numbers
    smallest = float('inf')  # Initialize to positive infinity
    largest = float('-inf')  # Initialize to negative infinity

    # Iterate over the numbers in the tuple
    for num in numbers:
        # Update smallest and largest if necessary
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    # Return the tuple of smallest and largest numbers
    return (smallest, largest)

# Example usage:
numbers_tuple = (5, 2, 8, 3, 9)
result = min_max(numbers_tuple)
print("The smallest and largest numbers are:", result)
