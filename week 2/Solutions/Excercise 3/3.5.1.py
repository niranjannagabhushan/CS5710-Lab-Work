# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 10:45:45 2024

@author: niran
"""

string = input("Enter a string: ")

tart_count = 0
i = 0
while i < len(string) - 3:
  if string[i:i+4] == "tart":
    # Count all occurrences starting from the current index
    while i < len(string) and string[i:i+4] == "tart":
      tart_count += 1
      i += 4
  else:
    i += 1  # Move to the next character if "tart" not found

print(f"The number of times 'tart' appears in the string is: {tart_count}")

'''
It uses a while loop with two parts:
The outer loop iterates through the string until it reaches the end (similar to the function's loop).
The inner loop starts when "tart" is found and continues incrementing tart_count and moving the index as long as "tart" repeats.
'''