# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 14:14:03 2024

@author: niran
"""

n = int(input("Enter an integer n: "))

# Initialize the sum variable
sum = 0

# Use a for loop to iterate from 3 to n
for i in range(3, n + 1):
  # Add i to the sum
  sum += i

# Print out the sum
print(f"The sum of all integers from 3 to n is {sum}")
