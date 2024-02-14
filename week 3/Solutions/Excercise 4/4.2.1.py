# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 20:01:15 2024

@author: niran
"""

def has_duplicates(words):
 """
 Determines if a list of words contains any duplicates.

 Args:
     words: A list of words.

 Returns:
     True if there are duplicates, False otherwise.
 """

 seen_words = {}
 for word in words:
   if word in seen_words:
     return True  # Duplicate found
   seen_words[word] = None  # Store word as key (value doesn't matter)

 return False  # No duplicates found

# Test cases
print(has_duplicates(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]))  # True
print(has_duplicates(["magic", "tree", "house"]))  # False
print(has_duplicates([]))  # False (handles empty list)
