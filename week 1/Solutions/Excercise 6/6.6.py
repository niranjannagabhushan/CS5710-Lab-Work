# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 14:58:45 2024

@author: niran
"""


# Ask the user to enter an integer n
n = int(input("Enter an integer n: "))

# Initialize the factorial variable
factorial = 1

# Use a for loop to iterate from 1 to n
for i in range(1, n + 1):
  # Multiply i to the factorial
  factorial *= i

# Print out the factorial
print(f"The factorial of n is {factorial}")
