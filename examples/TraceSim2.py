#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# Author: Wandeson Ricardo
# Web: www.wsricardo.blogspot.com
# Python Hack CG and Tests/Study CG Theory
# Python version 3
# TraceSim2 Create shade funtion(definy light model)
from math import*
from random import*

# Vector functions (sum, product scalar, ...)
V_Sum = lambda u,v: [u[0]+v[0], u[1]+v[1], u[2]+v[2]]
V_Sub = lambda u,v: [u[0]-v[0], u[1]-v[1], u[2]-v[2]]
V_ScalarProd = lambda a,v: [a*v[0],a*v[1],a*v[2]]
V_VecProd = lambda u,v: u[0]*v[0] + u[1]*v[1] + u[2]*v[2]
# u = (a1,b1,c1), v=(a2,b2,c3). <u,v>=(b1c2 - b2c1, a2c1 - a1c2, a1b2 - a2b1)
V_InnerProd = lambda u,v: [ u[1]*v[2] - v[2]*u[1], u[0]*v[2] - v[2]*u[0], u[0]*v[1] - v[0]*u[1] ]
#---- Functions will be build in other file implementation.---

# Location to camera point to view scene
# Observador da cena posição.
P_Viewer = {'x':.0,'y':.0,'z':.0}


# Dimension of plane view in pixels.
# Dimensão do plano mxn pixeis.
Window_View_Dim = [1600,1600]
color_rgb= [0,0,0]
# Inicialização da posição do ponto de view.
P_Viewer['x'],P_Viewer['y'],P_Viewer['z'] = int(Window_View_Dim[0]/2.0),int(Window_View_Dim[0]/2.0),-int(Window_View_Dim[0]/2.0 )

# Vector diretor d and unit normal to sphere
d = {'x':1.0,'y':3.0,'z':5.0}
n = {'x':.0,'y':.0,'z':.0}


# Lights sources and models
Light_source = {'x':.0,'y':.0,'z':.0}

# Ray equation
# Equação para o raio
# P = P0 + t*d (P point (x,y,z), point of rect 'ray' P0, t parameter, d director vector)
# Python ordena os elementos do dicionario, visto em stackoverflow. (conferir doc)
Ray = lambda P,d,t: tuple([ P['x'] + t*d['x'],
                      P['y'] + t*d['y'],
                      P['z'] + t*d['z']
                     ])
# Modelo para Intensidade da luz.
y = lambda i: i # 'y' função que determina a intensidade propagada numa distancia
I = lambda k,y: k*y(1)  #Intensidade da luz
#---------------------------------------------

# Sphere equation (x - xc)^2 + (y - yc)^2 + (z - zc)^2 = radius^2
# Function lambda to compute intersection ray with sphere.
# Ray equation R = P0 + t*d. R,P0,d (x,y,z)
# Sphere_Inter = lambda ray, C, radius:
#
def Intersection_sphere(Point_viewer, Center, director_ray,radius):
    #Dx,Dy,Dz =  x -x0, y -y0, z - z0
    t1 = 0.0
    t2 = 0.0
    # observador ao centro da circunferência.
    # Point view to circle center
    v = V_Sub(Point_viewer,Center)
    # delta = <formula>
    delta = 4*( (V_VecProd(v,director_ray))**2 - (V_VecProd(director_ray,director_ray)*(V_VecProd(v,v) - radius**2)))
    # P_inter_sphere = 0.0
    if delta > 0:
        #-2*v*d +- sqrt(delta)
        # Two point intersections. Dois pontos de interseção com esfera.
        t1 = -V_VecProd(V_ScalarProd(2,v), director_ray) + sqrt(delta) 
        t2 = -V_VecProd(V_ScalarProd(2,v), director_ray) - sqrt(delta)
        
        
    elif delta == 0:
        t1 = -V_VecProd(V_ScalarProd(2,v), director_ray)
        
        
    else:
        return False
    # Compute ray intersection with sphere. Calculando interseção com
    # a esfera.
    if t1 < t2:
        P_inter_sphere = V_Sum(v,V_ScalarProd(t1,director_ray)) # <formula>(t)
    else:
        P_inter_sphere = V_Sum(v,V_ScalarProd(t2,director_ray))
    
    return P_inter_sphere
    

P= {'x':1.0,'y':2.0,'z':.0}
# Testing Ray equation, rect r
# Modelling equation line P = P0 + t*d
ray = Ray(P, d, 2.0 )
#print(ray)

# Compute light interference in visual point color of the scene.
def shade(P, I, Ir, obj_color):
    color = obj_color
    return color
    
# Define sphere and intersection formula

# Define pixel coordenate in plane xy Pixel_coord = {'x':1.0,'y':1.0,'z':.0}
# like plane view xy 'z' componnent equals to zero.

def main(func=None,**args):
    # Header of the ppm format image
    print('P3\n', Window_View_Dim[0], Window_View_Dim[1],' 255\n')
    # Escalando o plano de visualização para
    #centar ponto do observador (Viewer)
    v_dir = [0,0,0]
    P_i = [0,0,0] # ponto de interseção na cena.
    normal_surf = [0,0,0]
    P0 = [P_Viewer['x'], P_Viewer['y'], P_Viewer['z']]
    # Loop rays create and draw image
    for i in range(Window_View_Dim[0]):
        for j in range(Window_View_Dim[1]):
            # Compute new ray for each pixel in plane view (x,y,0)
            v_dir = V_Sub([i,j,0],[P_Viewer['x'], P_Viewer['y'], P_Viewer['z']])
            # Compute intersections with scen
            P_i = Intersection_sphere(P0,[P0[0],P0[1],P0[2]+10.0 ], v_dir, 2.0)
            # Normal to sphere
            #normal_surf = V_Sub([0,0,0],P_i)
            # ray = P0 + t*d

            # Verificar se raio refletido pela superficie atinge uma fonte de luz,
            # ou se o ponto da superficie é atingido por um "raio de luz".
            
            # Compute color in point (xi,yj)
            #color_rgb = shade([P_i[0],P_i[1]], nornal_surf,  [255,0,0])
            if P_i==False:
                color_rgb = [0,0,215] #background
                print(color_rgb[0],color_rgb[1],color_rgb[2])
            else:
                color_rgb = [255,0,0] #cor da esfera
                
                print(color_rgb[0],color_rgb[1],color_rgb[2])
                
    return 0
        

if __name__ == "__main__":

    main()
