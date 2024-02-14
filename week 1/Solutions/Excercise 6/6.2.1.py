# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 14:27:12 2024

@author: niran
"""


# Ask the user to enter an integer n
n = int(input("Enter an integer n: "))

# Initialize the sum variable
sum = 0

# Use a for loop to iterate from 2 to n with a step of 2
for i in range(2, n + 1, 2):
  # Add i to the sum
  sum += i

# Print out the sum
print(f"The sum of all even integers from 2 to n is {sum}")
