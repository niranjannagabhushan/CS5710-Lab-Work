# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 11:41:54 2024

@author: niran
"""

def partialPalindrome(s, n):
    """
    Checks if there is a sub-string in s that is a palindrome of length n.

    Parameters:
    s (str): The input string.
    n (int): The length of the palindrome substring to check.

    Returns:
    bool: True if there is a palindrome sub-string of length n, False otherwise.
    """
    # Iterate over all possible starting indices of the substring
    for i in range(len(s) - n + 1):
        # Get the substring of length n starting at index i
        substring = s[i:i+n]
        
        # Check if the substring is equal to its reversal (i.e., a palindrome)
        if substring == reverse(substring):
            return True  # Return True if a palindrome is found
    
    return False  # Return False if no palindrome of length n is found

# Function to reverse a string
def reverse(s):
    """
    Returns the reversal of the input string.

    Parameters:
    s (str): The input string.

    Returns:
    str: The reversal of the input string.
    """
    return s[::-1]

# Example usage:
print(partialPalindrome("AGTTGCC", 4))  # Output: True
print(partialPalindrome("AGTTGCC", 3))  # Output: False
