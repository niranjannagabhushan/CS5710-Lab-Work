# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 19:53:05 2024

@author: niran
"""

def has_duplicates(words):
    """
    Returns True if there are any duplicate elements in the input list of words.

    Parameters:
    words (list): The input list of words.

    Returns:
    bool: True if there are any duplicate elements, False otherwise.
    """
    word_count = {}
    for word in words:
        if word in word_count:
            return True
        else:
            word_count[word] = None
    return False

# Test cases
words1 = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
print(has_duplicates(words1))  # Output: True

words2 = ['magic', 'tree', 'house']
print(has_duplicates(words2))  # Output: False
