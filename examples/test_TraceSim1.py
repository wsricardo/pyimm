# Author: Wandeson Ricardo
# Web: www.wsricardo.blogspot.com
from TraceSim1 import*
P0 = [400.0,400.0,-2.0]
win = [800,800]
Cen = [400.0,400.0,10.0]
radius =  2
d = [0.0,0.0,12.0]
t = Intersection_sphere(P0,Cen,d,2)
print("\n",t)
