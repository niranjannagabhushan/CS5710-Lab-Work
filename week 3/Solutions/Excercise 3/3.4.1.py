# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 19:15:01 2024

@author: niran
"""

def filter_odd(data):
  """
  Returns a new tuple containing every other element of the input tuple starting from the first one.

  Args:
      data: A tuple containing any data types.

  Returns:
      A new tuple containing every other element of the input tuple.
  """

  return data[::2]  # Efficiently slice every other element using step size 2

# Example usage
sample_tuple = ("I", "love", "Python", "and", "Java")
filtered_tuple = filter_odd(sample_tuple)
print(filtered_tuple)  # Output: ('I', 'Python', 'Java')
