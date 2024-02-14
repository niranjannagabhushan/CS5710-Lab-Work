# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 13:07:53 2024

@author: niran
"""


# Ask the user to enter an integer n
n = int(input("Enter an integer n: "))

# Use an if-elif-else statement to check the sign of n
if n > 0:
  # Print n is positive
  print(f"{n} is positive")
elif n < 0:
  # Print n is negative
  print(f"{n} is negative")
else:
  # Print n is zero
  print(f"{n} is zero")
