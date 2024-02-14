# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 10:13:17 2024

@author: niran
"""

string = input("Enter a string: ")

# Check if the string length is divisible by 3
if len(string) % 3 != 0:
   print("string is not a triple concat")
else:
   # Extract the potential substring
   substring = string[:len(string) // 3]

   # Check if the entire string is composed of repetitions of the substring
   if string == substring * 3:
       print(f"string is a triple concat of {substring}")
   else:
       print("string is not a triple concat")
