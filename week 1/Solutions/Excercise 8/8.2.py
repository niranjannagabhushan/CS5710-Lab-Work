# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 14:04:35 2024

@author: niran
"""


# Initialize the secret number
secret = 4

# Repeatedly ask the user to guess the number
while True:
    guess = int(input("Enter a number between 0 and 10: "))
    
    # Check if the guess is correct
    if guess == secret:
        print("Well done!")
        break
    else:
        print("Try again!")
