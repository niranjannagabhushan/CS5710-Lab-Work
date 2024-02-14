#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 15:12:32 2024

@author: stephen
"""
# Exercise 5
import numpy
x=int(input("Enter number x: "))
y=int(input("Enter number y: "))
print("x**y = ",x**y)
print("log(x) = ", numpy.log2(x))

# Exercise 6.1
n=int( input("Enter an integer: "))
total=0
for i in range(3,n+1):
    total+=i
print(total)

# Exercise 6.2
n=int( input("Enter an integer: "))
total=0
for i in range(3,n+1,2):
    total+=i
print(total)

# Exercise 6.3
n=int( input("Enter an integer: "))
total=0
for i in range(3,n+1,3):
    total+=i
print(total)

# Exercise 6.4
n=int( input("Enter an integer: "))
total=sum(range(3,n+1,1))
print(total)

# Exercise 6.5
n=int( input("Enter an integer: "))
for i in range(n,-1,-1):
    print(i) 
    
# Exercise 6.6
n=int( input("Enter an integer: "))
ans=1
for i in range(1,n+1):
    ans*=i
print(ans)

# Exercise 7.1
n=int( input("Enter an integer: "))
if n>0:
    print("n is positive")
elif n<0:
    print("n is negative")
else:
    print("n is zero")

    
# Exercise 7.2
n=input("Enter an integer: ")
if n[0]=="-" and n[1:].isdigit():
    print("n is negative")
elif not n.isdigit():
    print("string is not a number")
elif int(n)>0:
    print("n is positive")
else:
    print("n is zero")
    
    
    
# Exercise 7.3
secret=7
a=int(input("Enter an integer a: "))
b=int(input("Enter an integer b: "))
if a>0 and b>0:
    print('both numbers are positive')
elif a < 0 and b < 0:
    print('both numbers are positive')
elif a==0 or b==0:
    print("one number is 0")
else:
    print("numbers have opposite signs")
    
if a==secret or b==secret:
    print("you also guessed my secret number")
else:
    print("no luck this time")

#%Exercise 7.4
n=int( input("Enter an integer: "))
if n==0:
    print(1)
else:
    ans=1
    for i in range(1,n+1):
        ans*=i
    print(ans)

# Exercise 8.1
n=int( input("Enter an integer: "))
i=1
total=0
while i <=n:
    total+=i**2
    i+=1
print(total)

# Exercise 8.2a
secret=4
while True:
    n=int( input("Enter an integer between 0 and 10: "))
    if n== secret:
        print("Well done!")
        break
    
# Exercise 8.2b
secret=4
while n!=secret:
    n=int( input("Enter an integer between 0 and 10: "))
print("Well done!")






