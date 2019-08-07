#!/usr/bin/env python3

from cplane_np import ArrayComplexPlane
import matplotlib.pyplot as plt
import numpy as np
import math

class NewtonRaphson(ArrayComplexPlane):
    """The new class JuliaPlane subclasses the ArrayComplexPlane.
    """
    
    def __init__(self): 
        """Have the init call the init method of the parent class.
        
        The Attributes will assume default values. Have the init
        call also immediately apply the function julia to the plane
        using the input argument c.
        
        Attributes:
            xmax (float) : default value is -2
            xmin (float) : default value is 2
            xlen (int)   : default value is 1000
            ymax (float) : default value is -2
            ymin (float) : default value is 2
            ylen (int)   : default value is 1000
        """
        
        super(NewtonRaphson, self).__init__(-2,2,400,-2,2,400)
        self.e=math.sqrt((0.01)**2+((0.01)**2))
        self.roots=()

    def apply(self):
        
        f=np.poly1d([35, 0, -180, 0, 378, 0, -420, 0, 315, 0])
        q=np.polyder(f)
        def newton_raphson(z):
            zplus = z - (f(z)/q(z))
            magnitude = abs(zplus-z)
            n = 1
            while magnitude > e:
                n += 1
                z = zplus
                zplus = z - (f(z)/q(z))
                magnitude = abs(zplus-z)
            return zplus,n
        
        v = np.vectorize(self.newton_raphson)
        self.roots = v(self.plane)

    def show(self):
            '''This will plot an image of the complex plane after it has
            been transformed by the julia function.
            '''
            tmp = np.zeros((xlen,ylen))
            zs = np.outer(tmp, tmp)
            for i in range(xlen):
                for j in range(ylen):
                    zs[i,j]=self.roots(i,j)
            plt.imshow(zs.T, origin='lower', extent=(self.xmin, self.xmax, self.ymin, self.ymax))
