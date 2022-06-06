#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Wandeson Ricardo 
# Site: https://www.wsricardo.blogspot.com


#Modelling objects
#Sphere
class sphere:
    """
    Define equation to sphere.
    """
    def __init__(self, center=(0,0), radius=1.0):
        self.center = center
        self.radius = radius

        pass

class ray:
    """
    Define ray like line equation with director vector passing in 'point'
    ray = P0 + t*d
    
    """
    def __init__(self, point, vector_diretor):
        self.P0 = point
        self.dir = vector_director

        pass


class trace:
    """
    Generate the rays.
    """
    def __init__(self):

        pass

class shade():
    """
    Drawing and paint pixels. (include ilumination formulas).
    """
    def __init__(self):

        pass
    
def main():
    pass
if __name__=="__name__":
    main()
