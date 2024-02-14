# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 11:14:40 2024

@author: niran
"""

def min_max(digits):
    """
    Returns a string consisting of the smallest and largest integers in the input string.

    Parameters:
    digits (str): A string of digits.

    Returns:
    str: A string consisting of the smallest and largest integers.
    """
    # Initialize variables to keep track of the smallest and largest digits
    smallest = float('inf')  # Initialize to positive infinity
    largest = float('-inf')  # Initialize to negative infinity

    # Iterate over the characters of the string
    for x in digits:
        # Convert the character to an integer
        num = int(x)

        # Update smallest and largest if necessary
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    # Convert the smallest and largest integers to strings and concatenate them
    return str(smallest) + str(largest)

# Example usage:
result = min_max("31805")
print("The smallest and largest integers are:", result)
