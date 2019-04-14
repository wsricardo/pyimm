# Test PYIMM, create fractal mandelbrot
import pyimm
from math import*
from time import*

def fractal(Img, max_iterations, m=400, n=400, F_color=None ):
	percent_pixel = 0.0
	nPixel =float(m*n)
	color = pyimm.RGB()
	if F_color==None: F_color = [lambda k: k**2, 0, 0]
	alfa = float(n)/float(m)
	#a,b = alfa*(-2.5), alfa*1.0 #interval x
	#c,d = alfa*(-1.5),alfa*1.5 #iterval y
	a, b = alfa*(-3.5), alfa*1.5 #interval x
	c, d = alfa*(-2.0), alfa*2.0 #interval y
	#Pixel size resolution.
	delta_x, delta_y = (abs(a-b))/float(n), (abs(c-d))/float(m)

	F = lambda i,j: [i*delta_x,j*delta_y] #scale i,j

	print( 'Draw...')
	x_c, y_c = 0,0
	k,l=0.0,0.0
	print( '[delta_x,delta_y]', [delta_x, delta_y] )
	sleep(5)
	for i in range(m):
		k = k + 1.0
		y_c = i*delta_y + c
		for j in range(n):
			l = l + 1.0
			percent_pixel =  100.0*((k+l)/nPixel)
			print('Percent calculated...',  percent_pixel,' %')

			x_c = j*delta_x + a



			x,y=0,0
			iteration = 0

			while(x*x + y*y < 4 and iteration < max_iterations):
				xtemp = x*x - y*y + x_c
				y = 2*x*y + y_c

				x = xtemp
				iteration = iteration + 1
			#iteration = int(log(sqrt(x*x+y*y))/2**iteration)

			color.r = int(F_color[0](iteration))
			color.g = int(F_color[1])
			color.b = int(F_color[2])

			color.centralizergb()

			Img[i][j].r = color.r
			Img[i][j].g = color.g
			Img[i][j].b = color.b

	return Img
	

im = pyimm.MatrixImage(width=400, height=400, color='3')
p = pyimm.PPM(color='3')

out_img = fractal(im, 200, 400,400)
p.save(Img=out_img, filename="fractal.ppm")
