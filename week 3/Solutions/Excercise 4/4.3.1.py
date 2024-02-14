# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 20:12:58 2024

@author: niran
"""

def get_duplicates(words):
  """
  Finds and counts duplicate words in a list.

  Args:
      words: A list of words.

  Returns:
      A dictionary mapping each duplicate word to its frequency.
  """

  duplicates = {}
  for word in words:
    if word in duplicates:
      duplicates[word] += 1  # Increment count for existing duplicate
    else:
      duplicates[word] = 1  # Add new word with count 1

  return {word: count for word, count in duplicates.items() if count > 1}  # Filter only true duplicates

# Test cases
print(get_duplicates(["it", "is", "the", "right", "right", "is", "not", "it", "right"]))  # {'it': 2, 'is': 2, 'right': 3}
print(get_duplicates(["hello", "world", "unique"]))  # {} (no duplicates)
print(get_duplicates([]))  # {} (empty list)
