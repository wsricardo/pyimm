#!/usr/bin/env python3
# Author: Wandeson Ricardo
# Instagram: @wsricardo.arts
# https://github.com/wsricardo
# Github: https://github.com/wsricardo
# Blog: www.wsricardo.blogspot.com
#
# License: GPL https://www.gnu.org/licenses/gpl.txt
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses



# File images PPM (ascii)
class PPM(object):
	
	def __init__(self, dim=None, color = None, filename=None):
		'''
		Create object image file.
		dim -> size image
		color -> P3 = color, P2 = gray scale.
		'''

		self.filename = filename
		if dim != None: self.dim = dim[0], dim[1]
		self.color = color
		self.image = None
	
	# Proccess file PPM and create temp object for 
	# image matrix, and define dimension 
	# of image when file.
	def __parser_PPM(self, im_data):
		'''
		Parser PPM image file (ASCII format).
		--------------------------------------

		Extrair e checar cabeçalho e valores de pixels da imagem.
		* P3/P2 (cor ou escala de cinza);
		* tamanho da imagem;
		* numero máximo de cores (255);
		* valores inteiros entre 0 e 255 para pixeis 
		da imagem (de acordo com tamanho).
		'''
		# 
		print('\nParser file PPM.')
		
		im_data.remove('')
		if self.dim == None: # Size image
			dim = im_data[2].split()
			self.dim = tuple( ( int(dim[0]), int(dim[1]) ) )
		if str.upper(im_data[0]) != 'P3' and str.upper(im_data[0]) != 'P2': return 'Fail in spec color(Must be P3 or P2).'
		self.color = '3' if im_data[0]=='P3' else '2'
		im = MatrixImage( [int(self.dim[0]), int(self.dim[1] )], self.color )
		
		# --- Pixels data from image file.  ----
		__temp = im_data[4:] # Pixels from image.
		_k_index = 0
		_color_vec = [] 
		print('__temp', __temp, len(__temp))
		# Color image
		if self.color=='3':
			
			for i in range( int(self.dim[1]) ):
				for j in range( int(self.dim[0]) ):
						for k in range(3):
							_color_vec.append( int(__temp[_k_index]) )
							_k_index +=  1   # Next line of image file PPM. 
							print('_k_index = %d'%(_k_index))
						print('#', _color_vec)	
						im[i][j].r, im[i][j].g, im[i][j].b  = list( [ _color_vec[0], _color_vec[1], _color_vec[2] ] ) 
						print("##", im[i][j].r, im[i][j].g, im[i][j].b)
						_color_vec = [] # reset
						

		
		# Gray scale
		elif self.color=='2':
			for i in range( self.dim[0] ):
				for j in range( self.dim[1] ):
					im[i][j] = int( __temp[_k_index] )
					_k_index += 1
		
		# --- Pixels data from image file. ---
		else:
			return'Fail specify format type image colors.'
		print('*',im[0][0].r)
		return im
				
	# Open file (ASCII).
	def open(self, filename):
		'''
		Open Image file.
		'''
		image_data = []
		self.filename = filename
		with open(self.filename, 'r') as fn:
			image_data=(fn.read().split('\n'))
		print(image_data)
		self.image= self.__parser_PPM(image_data)

		return self.image

	# Save file image.
	def save(self, Img, filename):
		'''
		Save image.
		save(self, Img, filename)
		Img -> Object ImageMatrix
		filename -> Name of file
		'''
		self.filename = filename
		self.dim = Img.dim
		self.color = Img.color
		
		with open(self.filename,'w') as fn: # Open file. First write header of PPM file format.
			_vector_color = []
			if self.color=='3': # Color image, color model RGB.
				fn.write('P3\n')
				fn.write( str( self.dim[0] )+' '+str( self.dim[1] )+'\n' )
				fn.write('255\n')
				
				for i in range( self.dim[0] ):
					for j in range( self.dim[1] ): # list error index out range
												
						fn.write( str( Img[i][j].r )+'\n' )
						fn.write( str( Img[i][j].g )+'\n' )
						fn.write( str( Img[i][j].b )+'\n' )

			else: # Gray scale images.
				fn.write('P2\n')
				fn.write( str(self.dim[0]+self.dim[1])+'' )
				for i in range(self.dim[0]):
					for j in range(self.dim[1]):
						fn.write( str( Img[i][j] ) )
				
			
		print('\nSave.\n')


# Color model RGB
class RGB(object):
	'''
	Color mode RGB
	'''
	def __init__(self):
		self.r = 0
		self.g = 0
		self.b = 0
		
	def __repr__(self):
		return "(red, green, blue) =\n\t\t\t(%d, %d, %d)"%(self.r, self.g, self.b)
	
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


# Image
class MatrixImage(object):
	"""
	Image matrix, operations/methods over matrix and vectors.. 
	* dim - dimension of image
	* color - 3 for RGB (red, green, blue) and 2 for black and white images
	"""
	
	"""
    Matrix A m por n,
	A = [	[lin_1],
			[lin_2],
				.
				.
				.
			[lin_m] ]
	onde A tem m linhas e n colunas. Com lin_i sendo com n colunas, para i=0,1,..., (m-1)
	"""
	def __init__(self, dim, color='3', colormodel=None):

		self.dim = dim[1], dim[0] # (lin, col) = (y, x)
		self.color = color
		self.colormodel = colormodel # RGB, CMYK, etc. Color models.
		self.__lin = dim[1]
		self.__col = dim[0]
		# self.Matrix = [ [ RGB() for j in range(dim[1])] for i in range(dim[0]) ]
		# 
		# Color images
		if color=='3':
			self.__matrix = [ [ RGB() for j in range(self.__col) ] for i in range(self.__lin) ] #self.__col*[ self.__lin*[ RGB() ] ]
		# Black and white image
		elif color=='2':
			self.__matrix = [ [ 0 for j in range(self.__col) ] for i in range(self.__lin) ] #self.__col*[ self.__lin*[ 0 ] ]
	
	# Checar compatibilidade de tipo na atribuição (caso int ou tupla).
	@property
	def matrix(self):
		return self.__matrix
	
	def __get__(self):
		return self.matrix
		
	def __getitem__(self, key):
		return self.__get__()[key]
	

# Function tests processsing
def tests():
	import random
	out = MatrixImage((300, 300), '3')
	#in_img = MatrixImage(( im.dim[1], im.dim[0]), '3')
	m,n = out.dim[1],out.dim[0]
	imfile = PPM((300,300), '3')
	for i in range(m):
		for j in range(n):
			out[i][j].r = random.randint(0,255) 
			out[i][j].g = random.randint(0,255)
			out[i][j].b = random.randint(0,255)
	imfile.save(out, 'image-test.ppm')
	print('end..')
def tests2():
	# Open and processing image.
	pass
	
# tests and examples of use modules.
if __name__=="__main__":
	l = PPM((2,3), '3')
	img = l.open('test.ppm')
	im = MatrixImage((2,3),'3')
	
	l.save(im, "test2.ppm")
	print('>>im',im.matrix)
	im[0][1] = (120, 0, 0)
	print('>',im[0][1])
	print(im[0][0].r,im[0][0].g,im[0][0].b)
	print(im[0][0])
	print(4*'*')
	print('>', img.matrix)
	print('>>', img[0][0].r)
	print('\nTESTS\n...')
	tests()
	
