# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 20:04:24 2024

@author: niran
"""

#Hereis the Python function `get_duplicates()` that takes a list of words as input and returns a dictionary mapping all duplicate words to their frequencies:

def get_duplicates(words):
    """
    Returns a dictionary mapping all duplicate words to their frequencies.

    Parameters:
    words (list): The input list of words.

    Returns:
    dict: A dictionary mapping duplicate words to their frequencies.
    """
    word_count = {}
    duplicates = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
            duplicates[word] = word_count[word]
        else:
            word_count[word] = 1
    return duplicates

# Test case
input_words = ['it', 'is', 'the', 'right', 'right', 'is', 'not', 'it', 'right']
result = get_duplicates(input_words)
print(result)  # Output: {'it': 2, 'is': 2, 'right': 3}

'''
Explanation:
- The `get_duplicates()` function takes a list `words` as input.
- It initializes an empty dictionary `word_count` to store the frequencies of words encountered.
- It also initializes an empty dictionary `duplicates` to store the duplicate words and their frequencies.
- It iterates over each word in the input list.
- For each word, it checks if the word is already in the `word_count` dictionary.
  - If it is, it increments the frequency of the word in `word_count` and adds it to `duplicates` along with its frequency.
  - If it is not, it adds the word to `word_count` with a frequency of 1.
- Finally, it returns the `duplicates` dictionary containing duplicate words and their frequencies.
'''