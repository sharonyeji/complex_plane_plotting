#!/usr/bin/env python3

from cplane_np import ArrayComplexPlane
import matplotlib.pyplot as plt
import numba as nb



def julia(c, max=100):
    """Create a function that takes a complex parameter
    c and an optional positive integer max, and returns
    a function.
    
    Args:
        c (complex): A complex parameter
        max (integer): A positive integer that always
        equals 100
        
    Returns:
        f (function): A function is stored in the return
        value
    """
    @nb.vectorize([nb.int32(nb.complex128)])
    def f(z):
        """Takes one complex parameter z as an input, and
        returns one positive integer as an output.
        If z has a magnitude abs(z) > 2, the function should
        output the integer 1. Otherwise, a counter is set to
        n=1. Increment n by 1, then transform the input z
        according to the formula z = z**2 + c. Check the
        resulting magnitude abs(z): If the magnitude now
        exceeds 2, then return the value of n; If the magnitude
        does not yet exceed 2, repeat this step. If the positive
        integer max=100 is reached before the magnitude of z
        exceeds 2, the preceding loop should abort and return
        the output integer 0
       
        
        Args:
            z (complex): A complex parameter
        
        Returns:
            f(z) (integer): A positive integer
        
        """
        
        if abs(z) > 2: 
            return 1
        else: 
            n = 1
        absolute = abs(z)
        while absolute <= 2:
            n += 1
            z = z**2 + c
            if abs(z) > 2:
                return n
            else:
                absolute = abs(z)
            if n > max:
                return 0
    return f

#test=julia(2+2*1j)
#print(test(3))

class JuliaPlane(ArrayComplexPlane):
    """The new class JuliaPlane subclasses the ArrayComplexPlane.
    """
    
    def __init__(self, c): 
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
        
        super(JuliaPlane, self).__init__(-10,10,20000,-10,10,20000)
        self.c=c
        f=julia(c)
        self.plane=f(self.plane)
        
    def refresh(self,c):
        '''Refresh is changed to accept only c (complex number).

        This function regenerates a fresh plane and empty the fs
        list as before, but next applies the function julia to the
        plane with the updated argument c analogously to the 
        initialization.
        '''

        self.c=c
        f=julia(c)
        self.fs = []
        super(JuliaPlane, self).__init__(self.xmin, self.xmax, self.xlen, self.ymin, self.ymax, self.ylen)
        self.plane = f(self.plane)
        
    def show(self):
        '''This will plot an image of the complex plane after it has
        been transformed by the julia function.
        '''

        plt.imshow(self.plane, cmap = 'hot', interpolation='bicubic', extent=(self.xmin, self.xmax, self.ymin, self.ymax))
        plt.title("c = " + str(self.c))
        plt.show()
            
    def toCSV(self, filename):
        """Exports the transformed plane of integers to a .csv file.
        
        The file stores all the needed parameters for the plane,
        including the value of c and the current zoom settings
        
        Args:
            filename: The name of the file.
        """
        
        default_attribute_id = ['xmin', 'xmax', 'xlen', 'ymin', 'ymax', 'ylen', 'c']
        default_attribute = [self.xmin, self.xmax, self.xlen, self.ymin, self.ymax, self.ylen, self.c]
        parameters = pd.Series( default_attribute, index = default_attribute_id)
        pd.Dataframe(parameters).T.to_csv(filename, sep='\t')
        
        #https://docs.python.org/3/library/csv.html#id2
        with open(filename, 'a') as csvfile:
            self.plane.to_csv(csvfile, sep='\t', index = TRUE)
        
    def fromCSV(self, filename):
        """Imports a .csv file previously exported by the class.
        
        This method resets the plane parameters to match the settings
        in the file, and refreshes the plane array to the values stored
        in the .csv file directly
        
        Args:
            filename: The name of the file.
        """
        #https://stackoverflow.com/questions/328059/create-a-list-that-contain-each-line-of-a-file
        with open(filename, 'b') as csvfile2:
            attribute = [csvfile2.readline().split(',')[1] for _ in range(7)]
            self.plane = pd.Dataframe.from_csv(csvfile2)
        self.xmin, self.xmax, self.ymin, self.ymax = [float(c) for c in attribute[:4]]
        self.xlen, self.ylen = [int(i) for i in attribute[4:6]]
        self.c = complex(attribute[-1])
            
