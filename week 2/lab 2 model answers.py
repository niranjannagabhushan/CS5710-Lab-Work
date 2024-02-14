#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 17:40:41 2018

@author: uxac007
"""

# Exercise 3.1
s=input("Enter a string: ")
if len(s)==0:
    print()
elif len(s)==1:
    print(s)
else:
    print(s[0]+s[-1])
    
# Exercise 3.2
s=input("Enter a string: ")
vowels="aeiou"
flag=True
for letter in vowels:
    if letter not in s:
        flag=False
        break
if flag==True:
    print("All vowels are there")
    if s[0]=="a" and s[-1]=="z":
        print("And it could be alphabetical!")

# Exercise 3.2
s=input("Enter a string: ")
if "a" in s and "e" in s and "i" in s and "o" in s and "u" in s:
    print("All vowels are there")
    if s[0]=="a" and s[-1]=="z":
        print("And it could be alphabetical!")

# Exercise 3.3
s=input("Enter a string: ")
total=0
for i in range(1,len(s),2):
    print(s[i])
    if s[i] in "aeiou":
        total+=1
print(total)

# Exercise 3.3
s=input("Enter a string: ")
total=0
for i in s[1::2]:
    if i in "aeiou":
        total+=1
print(total)


# Exercise 3.4
s=input("Enter a string: ")
l=len(s)
part=l//3
s1=s[0:part]
s2=s[part:2*part]
s3=s[2*part:]
if s1==s2 and s2==s3:
    print("String is a triple concat of ",s1)
else: print ("String is not a triple concat")


# Exercise 3.5
s=input("Enter a string: ")
total=0
for i in range(len(s)):
    if s[i:i+4]=="tart":
        total+=1
print(total)



# Exercise 4.1

def max3(a, b, c):
    """
    Input: a, b, c, integers
    Returns the maximum among the three inputs
    """
    m = a
    if b > m:
        m = b
    if c > m:
        m = c
    return m

# Exercise 4.2
def sort3(a, b, c):
    """
    Input: a, b, c, integers
    Returns a sorted tuple using worst-case 12 comparisons
    """
    #abc
    if a <= b and b <= c:
        return (a, b, c)
    #acb
    if a <= c and c <= b:
        return (a, c, b)
    #bac
    if b <= a and a <= c:
        return (b, a, c)
    #bca
    if b <= c and c <= a:
        return (b, c, a)
    #cab
    if c <= a and a <= b:
        return (c, a, b)
    #cba
    if c <= b and b <= a:
        return (c, b, a)

def __sort3(a, b, c):
    """
    Input: a, b, c, integers
    Returns a sorted tuple using exactly 3 comparisons
    by simulating bublesort
    """
    if a > b:
        (a, b) = (b, a)
    if b > c:
        (b, c) = (c, b)
    if a > b:
        (a, b) = (b, a)
    return (a, b, c)

def ___sort3(a, b, c):
    """
    Input: a, b, c, integers
    Returns a sorted tuple using only 3 comparisons at the worst case
    by recursing to sorting a pair of numbers. Note the use
    of a nested function.
    """
    def sort2(x, y):
        if x < y:
            return (x, y)
        else:
            return (y, x)
    t = sort2(a, b)
    if c <= t[0]:
        return (c,) + t
    elif c >= t[1]:
        return t + (c,)
    else:
        return (t[0], c, t[1])

def ____sort3(a, b, c):
    """
    Input: a, b, c, integers
    Returns a sorted tuple by using the 
    built-in sorted function. Need to convert 
    both the input parameters, and the 
    return value of sorted to a tuple.
    """
    return tuple(sorted((a, b, c)))

# Exercise 4.3
def min_max(t):
    """
    Input: t, non-empty tuple of integers
    Returns (min(t), max(t))
    """
    min = t[0]
    max = t[0]
    for n in t:
        if n < min:
            min = n
        if n > max:
            max = n
    return min, max


# Exercise 4.4
def reverse(t):
    """
    Input: t, string or tuple
    Returns a reversal of t in its original type
    """
    return t[::-1]

def _reverse(t):
    """
    Input: t, string or tuple
    Returns a tuple which is the reversal of t
    """
    _t = ()
    for i in range(len(t)-1, -1, -1):
        _t += (t[i],)
    return _t

def __reverse(t):
    """
    Input: t, string or tuple
    Returns a tuple which is the reversal of t using list mutation
    """
    t = list(t)
    for i in range(0, len(t)//2):
        (t[i], t[-1-i]) = (t[-1-i], t[i])
    return tuple(t)

def ___reverse(t):
    """
    Input: t, string or tuple
    Returns a tuple which is the reversal of t using recursion
    """
    if len(t) == 0:
        return t
    if len(t) == 1:
        return (t[0],)
    return (t[-1],) + ___reverse(t[1:-1]) + (t[0],) 


# Exercise 4.5

def partialPalindrome(s,n):
    for i in range(len(s)-n):
        if s[i:i+n]==reverse(s[i:i+n]):
            return True
    return False

# Exercise 4.6

def extract_strings(a,b,c):
    output=""
    for i in [a,b,c]:
        if type(i)==str:
            output=output+i
    return output


# Exercise 5.1

"""
Generic area
"""
def area(shape, n):
#    write a line to return the area
#    of a generic shape with a parameter of n
    return shape(n)

def circle(radius):
    """
    Input: radius, a positive float
    Returns the area of a circle with the given radius
    """
    return 3.14*radius**2

def square(length):
    """
    Input: length, a positive float
    Returns the area of a square with sides of the given length
    """
    return length*length



print(area(circle,10))  # example function call
print(area(square,5)) # example function call
print(area(circle,4/2))
"""
End of generic area
"""

# Exercise 5.2

def person(age):
     print("I am a person")
     def student(degree):
         print("I like learning")
         def holiday(place):
             print("But I need to take holidays")
             print(age,"|",degree,"|",place)
         # write a line to return the appropriate function
         return holiday
     # write a line to return the appropriate function
     return student
    
person(12)("Math")("beach")
person(29)("Data Science")("Japan")
person(23)("Law")("Barbados")   