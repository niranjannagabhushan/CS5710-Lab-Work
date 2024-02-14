#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 17:43:11 2018

@author: uxac007
"""


# Exercise 3.1
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

# Exercise 3.2
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

# Exercise 3.3
def sum_mult(t):
    """
    Input: t, a tuple of numbers (ints and/or floats)
    Returns a tuple of sum and product of integers in t
    """
    if t == ():
        return None
    s = 0
    m = 1
    for n in t:
        s += n
        m *= n
    return s, m

#Exercise 3.4

def filter_odd(t):
    """
    Input: t, a tuple
    Returns a tuple consisting of every other element of t
    starting from the first one.
    """
    ans = ()
    select = True
    for e in t:
        if select:
            ans += (e,)
        select = not select
    return ans

#Exercise 3.5

def apply_to_all(t, f):
    """
    Input: t, a tuple
    f, a function
    Returns a tuple resulting from applying f to every element of t
    """
    ans = ()
    for e in t:
        ans += (f(e),)
    return ans


# Exercise 4.1

def make_histogram(word):
    """
    Just a straightforward application
    of the frequency dictionary pattern
    from the lecture slides.
    """
    dict = {}
    for l in word:
        if l in dict:
            dict[l] += 1
        else:
            dict[l] = 1
    return dict

def make_histogram_1(word):
    """
    More concise implementation with 
    setdefault(). 
    """
    dict = {}
    for l in word:
        dict[l] = dict.setdefault(l, 0) + 1
    return dict

#Exercise 4.2

def has_duplicates(lst):
    """
    Note that this implementation is
    using None as a value since we only need
    to compile a set of unique words. 
    """
    dict = {}
    for w in lst:
        if w in dict:
            return True
        dict[w] = None
    return False

#Exercise 4.3
def get_duplicates_1(lst):
    """
    This implementation mutates the 
    input dictionary to remove all
    non-duplicates
    """
    dict = {}
    for w in lst:
        dict[w] = dict.setdefault(w, 0) + 1
    for w in list(dict):
        if dict[w] == 1:
            del dict[w]
    return dict

def get_duplicates_2(lst):
    """
    This implementation creates
    a new dictionary to store the duplicates.
    Note that this implementation is doing
    everything in a single pass over the 
    input list. A simpler, but slightly less
    efficient implementation will first create
    a frequency dictionary, and the then, do 
    another pass over it to pick up all duplicates.
    """
    dict = {}
    dup_dict = {}
    for w in lst:
        if w in dup_dict:
            dup_dict[w] += 1
        elif w in dict:
            dup_dict[w] = 2
        else:
            dict[w] = None
    return dup_dict

# Exercise 4.4
def inverted_dict(d):
    inverted = {}
    for k in d:
        if d[k] in inverted:
            inverted[d[k]].append(k)
        else:
            inverted[d[k]] = [k]
    return inverted

# Exercise 4.5
def inverted_dict_1(d):
    """
    More concise version using setdefault (Ex 4.5)
    """
    inverted = {}
    for k in d:
        inverted.setdefault(d[k], []).append(k)
    return inverted

def invert_dict(d):
    """
    Simple implementation that calls
    inverted_dict() to create an inverted copy, 
    clears the content of d, and updates it
    with the content of inverted.
    """
    inverted = inverted_dict(d)
    d.clear()
    d.update(inverted)
    del inverted
    

def invert_dict_1(d):
    """
    Invert d in place. Slightly
    more efficient version.
    """
    for v in list(set(d.values())):
        key_list = []
        for k in list(d.keys()):
            if d[k] == v:
                key_list.append(k)
                del d[k]
            d[v] = key_list
  

# Section 5
        
class Coordinate(object):
    """ A coordinate made up of an x and y value """
    def __init__(self, x, y):
        """ Sets the x and y values """
        self.x = x
        self.y = y

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def setX(self, x):
        self.x = x
        
    def setY(self, y):
        self.y = y

    def distance(self, other):
        """ Returns the euclidean distance between two points """
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5

    def __str__(self):
        """ Returns a string representation of self """
        return "<" + str(self.x) + "," + str(self.y) + ">"

import math  
import copy

class Circle(object):
    def __init__(self, centre, radius):
        self.centre = copy.copy(centre)
        self.radius = radius
        
    def getCentre(self):
        return copy.copy(self.centre)
        
    def setCentre(self, centre):
        self.centre = copy.copy(centre)
        
    def getRadius(self):
        return self.radius
    
    def setRadius(self, radius):
        self.radius = radius
        
    def get_area(self):
        return math.pi * self.radius**2
        
    def is_point_in(self, point):
        """
        This impelementation also demonstrates the
        use of isinstance to verify that the argument
        is of a correct type (Coordinate). The same
        pattern can also be used for 
        implementing methods that expect their arguments
        to be of a certain type (e.g., the setter methods).
        """
        if not isinstance(point, Coordinate):
            raise TypeError()
        return point.distance(self.centre) <= self.radius
   
    def __str__(self):
        return 'Cirle('+str(self.centre)+','+str(self.radius)+')'

if __name__ == '__main__':
    print(make_histogram('parrot'))
    print(make_histogram_1('parrot'))
    lst_dups = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
    lst_nodups = ['magic', 'tree', 'house']
    print(has_duplicates(lst_dups))
    print(has_duplicates(lst_nodups))
    lst_dups = ['it', 'is', 'the', 'right', 'right', 'is', 'not', 'it', 'right']    
    print(get_duplicates_1(lst_dups))
    print(get_duplicates_2(lst_dups))
    d = make_histogram('tyrannosaurus')
    print('d=', d)
    print('inverse of d=', inverted_dict(d))
    print('inverse of d=', inverted_dict_1(d))
    d = make_histogram('tyrannosaurus')
    invert_dict(d)
    print('inverse of d (in place)=', d)
#    need another copy of d as the original one got mutated
    d = make_histogram('tyrannosaurus')
    invert_dict_1(d)
    print('inverse of d (in place)=', d)
    
    c = Coordinate(3, 4)
    c_copy = copy.copy(c) # create a copy of c using the Python's copy library
    c.setX(10) # modifies the object aliased by c, but not by c_copy
    print(c) # prints <10,4>
    print(c_copy) # prints <3,4>
    
    c = Coordinate(0, 0)
#    create a copy of c before it's mutated
    origin = copy.copy(c)
    
    print('c =', c)
    c.setX(3)
    c.setY(-4)
    print('c =', c)
    print('origin = ', origin)
    print('c.x =', c.getX(), 'c.y =', c.getY())
    dist = origin.distance(c)
    print('distance from', origin, 'to', c, 'is', dist)
    
    circle = Circle(origin, 5)
    print('circle =', circle)
    
    print('circle with centre at', circle.getCentre(), 'and radius', 
          circle.getRadius())
    
    circle.setRadius(10)
    print('circle with centre at', circle.getCentre(), 'and radius', 
          circle.getRadius())
    
    circle.setCentre(Coordinate(3, 4))
    print('circle with centre at', circle.getCentre(), 'and radius', 
          circle.getRadius())
  
    print('circle with centre at', circle.getCentre(), 'and radius', 
          circle.getRadius(), 'and area', circle.get_area())
    
    circle = Circle(origin, 6)
    point1 = Coordinate(3, 4)
    point2 = Coordinate(30, 40)
#   the code below uses Python's conditional expressions: 
#   <expr1> if <condition> else <expr2>
    print('Point', point1, 'is', '' if circle.is_point_in(point1) else 'not', 
          'inside', circle)
    print('Point', point2, 'is', '' if circle.is_point_in(point2) else 'not', 
          'inside', circle)  