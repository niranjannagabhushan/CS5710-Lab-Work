# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 13:26:59 2024

@author: niran
"""

# Get input from the user
user_input = input("Enter an integer: ")

# Check if the input is a digit
if user_input.isdigit():
    n = float(user_input)
    
    # Check if n is positive, negative, or zero
    if n > 0:
        print(f"{n} is positive")
    elif n < 0:
        print(f"{n} is negative")
    else:
        print(f"{n} is zero")
else:
    print("String is not a number")
