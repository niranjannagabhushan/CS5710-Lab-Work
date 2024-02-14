# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 14:41:43 2024

@author: niran
"""


# Ask the user to enter an integer n
n = int(input("Enter an integer n: "))


# Use the built-in sum function to compute the sum of all multiples of 3 from 3 to n
sum1 = sum(range(3,n+1))

# Print out the sum
print(f"The sum of all objects in the range (n,m) {sum1}")


# Ask the user to enter an integer n
n = int(input("Enter an integer n: "))

# Use the built-in sum function to compute the sum of odd numbers from 3 to n
sum2 = sum(range(3, n + 1, 2))

# Print out the sum
print(f"The sum of all odd number from 3 to n is {sum2}")



# Ask the user to enter an integer n
n = int(input("Enter an integer n: "))

# Use the built-in sum function to compute the sum of all multiples of 3 from 3 to n
sum3 = sum(range(3, n + 1, 3))

# Print out the sum
print(f"The sum of all multiples of 3 from 3 to n is {sum3}")