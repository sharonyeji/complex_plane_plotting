#!/usr/bin/env python3

import abscplane

"""CS510 - CW05 Abstract Base Classes.

This module provides abstract base classes for CW05.
Note that such a class does nothing by itself: all functionality
is just a pass statement as written. Instead, a coder is
intended to inherit from this class in order to adopt its
interface. The set of attributes and methods of a class
that subclasses the abstract base class should provide
implementations as appropriate.

The point of such a structure is to guide other programmers
into good design, so that they can use an interface that
you expect to exist. This is part of the communal nature of
coding. Your code does not exist in a vacuum. It exists in
a community of other coders that are all sharing code with
each other. Without proper communication on what people 
expect from each other, it devolves into chaos.
"""

class ListComplexPlane(abscplane.AbsComplexPlane):
    """Abstract base class for complex plane.
    
    A complex plane is a 2D grid of complex numbers, having
    the form (x + y*1j), where 1j is the unit imaginary number in
    Python, and one can think of x and y as the coordinates for
    the horizontal axis and the vertical axis of the plane, 
    respectively. Recall that (1j)*(1j) == -1. Also recall that 
    the FOIL rule for multiplication still works:
        (x + y*1j)*(v + w*1j) = (x*v - y*w + (x*w + y*v)*1j)
    You can check these results in an interpreter.
    
    We will explore several implementations for a complex plane in
    this course, so we wish to have an abstract interface that
    is independent of any particular implementation.
    
    In addition to generating the 2D grid of numbers (x + y*1j),
    we wish to easily support transformations of the plane with
    arbitrary complex functions f. The class attribute self.plane
    should store a 2D grid of numbers (x + y*1j) such that the
    parameter x ranges from self.xmin to self.xmax with self.xlen
    total points, while the parameter y ranges from self.ymin to
    self.ymax with self.ylen total points. The class attribute
    self.fs should store a list of functions that are being applied
    in order to each point of the complex plane, initially empty. 
    The method self.apply(self,f) should take a function f that transforms 
    a complex number into another complex number and map that function 
    over the complex plane to produce the grid of numbers f(x + y*1j),
    adding the function f to the list self.fs in the process. If the
    method apply is called multiple times with different functions, then
    self.fs should record the ordered sequence of functions, and self.plane
    should contain the final output after applying the entire sequence
    of functions. The method self.refresh should regenerate the complex
    plane and clear all functions that transform the plane. The method
    self.zoom should reset the parameters for the 2D grid of points and
    regenerate the grid, reapplying all collected functions to each point.
    
    Note that it may be advantageous to define other methods for your
    implementation that are not specified here. By convention, "private"
    methods should be named with a double underscore (e.g., __mymethod)
    to hide it from the user interface. Helper methods that you define
    should be made private in this manner to keep the interface clean.
    
    Attributes:
        xmax (float) : maximum horizontal axis value
        xmin (float) : minimum horizontal axis value
        xlen (int)   : number of horizontal points
        ymax (float) : maximum vertical axis value
        ymin (float) : minimum vertical axis value
        ylen (int)   : number of vertical points
        plane        : stored complex plane implementation
        fs (list[function]) : function sequence to transform plane
    """ 
    
    # Class attributes, to be set during an __init__
    # The six resolution parameters should be floats
    def __init__(self,xmin,xmax,xlen,ymin,ymax,ylen):
        self.xmin  = float(xmin)
        self.xmax  = float(xmax)
        self.xlen  = int(xlen)
        self.ymin  = float(ymin)
        self.ymax  = float(ymax)
        self.ylen  = int(ylen)
        # The implementation type of plane is up to the user
        self.plane = self.__creategrid__()
        # fs should be a list of functions, initialized to be empty
        self.fs    = []
        
   
    def __creategrid__(self):
        
        dx = (self.xmax - self.xmin)/(self.xlen - 1)
        dy = (self.ymax-self.ymin)/(self.ylen - 1)
        
        return [[(self.xmin + i*dx)+(self.ymin + j*dy)*1j for i in range(self.xlen)] for j in range(self.ylen)]
        #list comprehension to compress for loop that is creating a new list of values
        
    def refresh(self):
        self.fs = []
        self.plane = self.__creategrid__()
    
    '''The method self.apply(self,f) should take a function f that transforms 
    a complex number into another complex number and map that function 
    over the complex plane to produce the grid of numbers f(x + y*1j),
    adding the function f to the list self.fs in the process. If the
    method apply is called multiple times with different functions, then
    self.fs should record the ordered sequence of functions, and self.plane
    should contain the final output after applying the entire sequence
    of functions.'''
    def apply(self, f):
        
        self.plane = [[f(i) for i in j] for j in self.plane ]
        self.fs = self.fs.append(f)
    
    def zoom(self,xmin,xmax,xlen,ymin,ymax,ylen):
        """Reset self.xmin, self.xmax, and self.xlen.
        Also reset self.ymin, self.ymax, and self.ylen.
        Regenerate the plane with the new range of the x- and y-axes,
        then apply all transformations in fs in the correct order to
        the new points so that the resulting value of self.plane is the
        final output of the sequence of transformations collected in
        the list self.fs.
        """
        self.xmin  = float(xmin)
        self.xmax  = float(xmax)
        self.xlen  = int(xlen)
        self.ymin  = float(ymin)
        self.ymax  = float(ymax)
        self.ylen  = int(ylen)
        self.plane = self.__creategrid__()
        
        fs=self.fs
        self.fs= []
        
        for f in fs:
            self.apply(f)

#lcp = ListComplexPlane(-10,10,20,-10,10,20)
#for y in lcp.plane:
    #for x in y:
        #print(x)
