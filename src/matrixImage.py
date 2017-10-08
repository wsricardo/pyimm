#!/usr/bin/env python3


# Name:        matrixImage.py
# Purpose:     Create matrix for image
#
# Author:      Wandeson Ricardo
# Created:     2013
# Copyright:   (c) 2013
# Licence:     GPL
# Blog:		www.wanartsci.blogspot.com
#		www.gaenos.blogspot.com

# Module to create and manipulate Image.
# Function lambda to create matrix with 0's.
# Matrix = lambda m, n: map(lambda k: Vector(n), range(0, m))
# Function to create matrix for image with chanel RGB.
MatrixImRGB = lambda m, n: map(lambda k: map(lambda k: RGB(), range(0, n)), range(0, m))


class MatrixImage:
    """
        Class for build matrix structure for image.
        Format supported to color in this moment RGB.
    """

    def __init__(self, dim, mode="rgb", fileformat=None):
        # type: (object, object, object) -> object
        """
        Create Image object to manipulation images 
        file ppm, color mode rgb.
        
        :rtype: object
        :type dim: list, of length 2.
        :type mode: object string.
        :type fileformat string.

        """

        self.dim = dim
        self.mode = mode
        self.fileformat = fileformat
        #self.Matrix = MatrixImRGB(dim[0], dim[1])
        m, n = self.dim[0], self.dim[1]
        self.matrix = [ [ RGB() for j in range(n) ] for i in range(m) ]
        if mode == "rgb":
            print("RGB mode")
        elif not mode.lower() in ('rgb','gray'):
            print("Modes: rgb color or gray scale")


class RGB:
    def __init__(self, r=0, g=0, b=0):
        self.r = r
        self.b = b
        self.g = g

    def centralizergb(self):
        if self.r < 0:
            self.r = 0
        elif self.r > 255:
            self.r = 255

        if self.g < 0:
            self.g = 0
        elif self.g > 255:
            self.g = 255

        if self.b < 0:
            self.b = 0
        elif self.b > 255:
            self.b = 255

        pass
