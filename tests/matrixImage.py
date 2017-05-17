#-------------------------------------------------------------------------------
# Name:        matrixImage.py
# Purpose:     Create matrix for image
#
# Author:      Wandeson Ricardo
#
# Created:     2013
# Copyright:   (c) 2012
# Licence:     GPL
#-------------------------------------------------------------------------------
#!/usr/bin/env python


#Module to create and manipulate Image.

#Function lambda to create matrix with 0's.
Matrix = lambda m,n: map(lambda k:  Vector(n), range(0,m))
#Function to create matrix for image with chanel RGB.
MatrixImRGB = lambda m,n: map( lambda k: map(lambda k: RGB(), range(0,n) ), range(0,m) )


class matrixImage:
    """
        Class for build matrix structure for image.
        Format supported to color in this momment RGB.
    """
    def __init__(self, dim, mode="rgb", fileFormat=None):
        self.dim = dim
        self.mode = mode
        self.fileFormat = fileFormat
        self.Matrix = MatrixImRGB(dim[0],dim[1])
        if mode=="rgb":
            print "RGB mode"



class RGB:
    def __init__(self, r=0,g=0,b=0):
        self.r = r
        self.b = b
        self.g = g

    def centralizeRGB(self):
        if self.r < 0:
            self.r=0
        elif self.r > 255:
            self.r=255

        if self.g < 0:
            self.g = 0
        elif self.g > 255:
            self.g=255

        if self.b < 0:
            self.b= 0
        elif self.b > 255:
            self.b = 255

        pass
