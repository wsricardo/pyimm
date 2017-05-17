# -- coding: latin-1 --
from PPM import*
from matrixImage import*
from math import*

dim = (600, 800)
I = matrixImage(dim)
#mapear i gerando (i=0,1,2,...dim[0]) e para cada i calcular f(i)=y,onde x=j e y = i. 
#antes deslocar todos os x,y em k_x e k_y unidades afim de centralizar o gráfico.
k_j, k_i  = 300, 400
f = lambda x: sin(x)
def drawGraph(f,intervalo_x):
    """
    f is function
    intervalo_x lista (k1,k2) intervalos das coordenadas x.
    """

file_name="test.ppm"
I2PPM = PPM(file_name,dim[0],dim[1])
for i in range(0,600):
    I.Matrix[i][800/2].g = 255
for j in range(0,800):
    I.Matrix[600/2][j].r = 255

#teste requer correçoes
for j in range(0,800):
    I.Matrix[int(-j/2)][j].b = 255 
I.Matrix[1][2].b=23
I2PPM.write(I.Matrix)
