# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 14:20:19 2024

@author: niran
"""


n = int(input("Enter an integer n: "))

# Initialize the sum variable
sum = 0

# Use a for loop to iterate from 3 to n with a step of 2
for i in range(3, n + 1, 2):
  # Add i to the sum
  sum += i

# Print out the sum
print(f"The sum of all odd integers from 3 to n is {sum}")


# using if function

#    for i in range (3,n+1,1)
#       if i%2 != 0 (odd condition)