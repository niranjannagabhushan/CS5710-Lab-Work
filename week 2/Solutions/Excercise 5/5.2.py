# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 19:15:11 2024

@author: niran
"""

def person(age):
    print("I am a person")
    def student(degree):
        print("I like learning")
        def holiday(place):
            print("But I need to take holidays")
            print(age, "|", degree, "|", place)
        return holiday
    return student

# (a) Function call with age of 29, degree of "Data Science", and vacation place of "Japan"
person(29)("Data Science")("Japan")

# (b) Function call to match the specified printout
person(23)('"Law"')('"Barbados"')
