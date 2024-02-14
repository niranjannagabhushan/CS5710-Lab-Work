# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 19:19:21 2024

@author: niran
"""

def person_with_details(age, degree, place):
    """
    Print information about a person, their desired degree, and preferred vacation spot.

    Args:
        age (int): The person's age.
        degree (str): The person's desired degree.
        place (str): The person's preferred vacation spot.
    """

    print(f"I am a person currently pursuing a degree in {degree}.")
    print(f"But I also need to relax and take holidays in places like {place}.")
    print(f"{age} | {degree} | {place}")

# Example function calls
# (a) Age of 29, degree of "Data Science", vacation place of "Japan"
person_with_details(29, "Data Science", "Japan")

# (b) Last line of printout: 23 | "Law" | "Barbados"
person_with_details(23, "Law", "Barbados")
