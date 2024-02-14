# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 14:34:54 2024

@author: niran
"""


# Ask the user to enter an integer n
n = int(input("Enter an integer n: "))

# Initialize the sum variable
sum = 0

# Use a for loop to iterate from 3 to n with a step of 3
for i in range(3, n + 1, 3):
  # Add i to the sum
  sum += i

# Print out the sum
print(f"The sum of all multiples of 3 from 3 to n is {sum}")


# using if function

#    if i%3==0 (multiple of 3 condition)