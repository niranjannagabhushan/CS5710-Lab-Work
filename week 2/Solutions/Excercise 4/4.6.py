# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 12:01:16 2024

@author: niran
"""

def extract_strings(*args):
    """
    Concatenates all the string arguments together.

    Parameters:
    *args: Arbitrary number of input arguments.

    Returns:
    str: Concatenated string of all string arguments.
    """
    # Initialize an empty string to store the concatenated strings
    result = ""

    # Iterate over the input arguments
    for arg in args:
        # Check if the argument is a string
        if type(arg) is str:
            # Concatenate the string to the result
            result += arg

    # Return the concatenated string
    return result

# Example usage:
print(extract_strings('foo', 5, 'aaa'))  # Output: 'fooaaa'
