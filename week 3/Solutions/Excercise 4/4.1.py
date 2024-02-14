# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 19:43:49 2024

@author: niran
"""

def make_histogram(string):
    """
    Returns a dictionary mapping each letter to its frequency in the input string.

    Parameters:
    string (str): The input string of letters.

    Returns:
    dict: A dictionary mapping each letter to its frequency.
    """
    histogram = {}
    for char in string:
        if char.isalpha():
            char = char.lower()  # Convert the letter to lowercase to ensure case-insensitive counting
            histogram[char] = histogram.get(char, 0) + 1
    return histogram

# Example usage:
input_string = 'parrot'
result = make_histogram(input_string)
print(result)
