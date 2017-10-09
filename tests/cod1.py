#!/usr/bin/env python3

class Matrix(object):
    """
        Class Matrix
        dim -> define dimension of matrix.
        var matrix
        Functions
        get() -> self.matrix
    """
    def __init__(self, dim):
        self.dim = dim
        # Dim -> matrix MxN m= dim[0] and n = dim[1]. Create matrix
        self.matrix = [ [ 0 for j in range(self.dim[1]) ]
                          for i in range(self.dim[0]) ]                        
        print("\033[0;31mOk\033[0m")

    def get(self):
        return self.matrix


    def add(self):
        pass
    def sub(self):
        pass
    def prod(self):
        pass

class Image(Matrix):
    def __init__(self, dim, name_file=None, mode="color"):
        Matrix.__init__(self, dim)  
        self.name_file = name_file
        self.mode = mode

        #self.matrix =  [ [ 0 for j in range(dim[1]) ] for i in range(dim[0]) ]

        print("OK!")


# Tests
im = Image( (5,3) )
print(im, '\n', im.matrix)
