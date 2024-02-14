# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 14:01:02 2024

@author: niran
"""


# Get input from the user
n = int(input("Enter a positive integer n: "))

# Initialize variables
sum_of_squares = 0
i = 1

# Calculate the sum of squares using a while loop
while i <= n:
    sum_of_squares += i ** 2
    i += 1

# Print the result
print("The sum of squares from 1^2 to", n, "^2 is:", sum_of_squares)