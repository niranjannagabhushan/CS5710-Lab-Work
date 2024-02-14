# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 13:38:45 2024

@author: niran
"""


# Get input from the user
n = int(input("Enter an integer (n): "))

# Check if n is 0
if n == 0:
    print("0! = 1")
# For positive n, calculate factorial
elif n > 0:
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(f"{n}! =", result)
# For negative n, factorial is undefined
else:
    print("Factorial is undefined for negative integers.")
