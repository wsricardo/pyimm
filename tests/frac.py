from fractal import*
from PPM import*
from matrixImage import*

dim = (600, 800)
inter = 50
I = matrixImage(dim)
I2PPM = PPM('fractal.ppm',dim[0],dim[1])
f = fractal(I.Matrix, inter, dim[0], dim[1], [lambda i: i*sin(i)  + cos(i), lambda i: i*cos(i) + i, lambda i: cos(i) + 1 + i**5])
I2PPM.write(f)
