# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 13:26:12 2024

@author: niran
"""


# Ask the user to enter two integers a and b
a = int(input("Enter an integer a: "))
b = int(input("Enter an integer b: "))

# Initialise an integer variable secret to store your secret number
secret = 5

# Use an if-elif-else statement to check the signs of a and b
if a > 0 and b > 0:
  # Print both numbers are positive
  print("Both numbers are positive")
elif a < 0 and b < 0:
  # Print both numbers are negative
  print("Both numbers are negative")
elif a == 0 or b == 0:
  # Print one number is 0
  print("One number is 0")
else:
  # Print numbers have opposite signs
  print("Numbers have opposite signs")

# Use an if-else statement to check if either a or b is equal to the secret number
if a == secret or b == secret:
  # Print you also guessed my secret number
  print("You also guessed my secret number!")
else:
  # Print no luck this time
  print("No luck this time")
