#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# Perlin Noise
import random
import math

from PPM import*
from matrixImage import*
#r = random.random()

def SimpleNoise(M, row, cols, c=0, V=None):
    r = 0.0
    V = [.01,2.5];
    #Defini polinomio de interpolação P para f de x,y
    for i in range(0,row):
        for j in range(0,cols):
            r = int(random.random()*(V[0])  + 0.2*i + random.random()*(V[1]) + 0.15*j) #Gradiente. Scale i,j
            M.Matrix[i][j].r = r
            M.Matrix[i][j].g = r
            M.Matrix[i][j].b = r
    return M

dim = (600, 800)
I = matrixImage(dim)

file_name="noise.ppm"
I2PPM = PPM(file_name,dim[0],dim[1])
I = SimpleNoise(I,dim[0],dim[1])
I2PPM.write(I.Matrix)