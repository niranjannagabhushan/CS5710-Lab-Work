# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 14:10:03 2024

@author: niran
"""

import random

# Initialize the secret number
secret = random.randint(0, 10)

# Repeatedly ask the user to guess the number
while True:
    guess = int(input("Enter a number between 0 and 10: "))
    
    # Check if the guess is correct
    if guess == secret:
        print("Well done!")
        break
    else:
        print("Try again!")
