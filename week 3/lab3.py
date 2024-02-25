#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 17:43:11 2018

@author: uxac007
"""

import random
import copy
import math


class Coordinate(object):
    """ A coordinate made up of an x and y value """
    def __init__(self, x, y):
        """ Sets the x and y values """
        self.x = x
        self.y = y

    def distance(self, other):
        """ Returns the euclidean distance between two points """
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
    
    # getter and setter for x
    def getX(self):
        return self.x
    
    def setX(self, x):
        self.x = x
        
    # getter and setter for y
 
 
    def __str__(self):
        """ Returns a string representation of self """
        return "<" + str(self.x) + "," + str(self.y) + ">"
    

class Circle(object):
    """
    
    input centre - Coordinate
          radius - number (float or int)
    """
    

        
    
# Write your testing code here
if __name__ == '__main__':
    r = Coordinate(1, 1)
    print(r)  
    