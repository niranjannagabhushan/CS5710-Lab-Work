# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 11:41:20 2024

@author: niran
"""

def reverse(s):
    """
    Returns the reversal of the input string.

    Parameters:
    s (str): The input string.

    Returns:
    str: The reversal of the input string.
    """
    # Initialize an empty string to store the reversed string
    reversed_string = ""

    # Iterate over the characters of the string in reverse order
    for char in s[::-1]:
        # Append each character to the reversed string
        reversed_string += char

    # Return the reversed string
    return reversed_string

# Example usage:
result = reverse("left to right")
print("The reversed string is:", result)
