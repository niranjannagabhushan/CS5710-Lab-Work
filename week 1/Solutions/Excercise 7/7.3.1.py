# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 13:37:20 2024

@author: niran
"""


# Get input from the user for a and b
a = int(input("Enter the first integer (a): "))
b = int(input("Enter the second integer (b): "))

# Initialize the secret number
secret = 5  # Change this to your secret number

# Check the conditions and print the appropriate message
if a > 0 and b > 0:
    print("both numbers are positive")
elif a < 0 and b < 0:
    print("both numbers are negative")
elif a == 0 or b == 0:
    print("one number is 0")
else:
    print("numbers have opposite signs")

# Check if either a or b is equal to the secret number
if a == secret or b == secret:
    print("you also guessed my secret number!")
else:
    print("no luck this time")
