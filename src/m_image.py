#!/usr/bin/env python3

# File images PPM(ascii)
class PPM(object):
	
	def __init__(self, filename=None, dim=None, colormodel=None):
		self.filename = filename
		self.dim = dim
		self.colormodel = colormodel
	
	# Proccess file PPM and create temp object for 
	# image matrix, and define dimension 
	# of image when file.
	def __parser_PPM(self, im_data):
		'''
		Extrair e checar cabeçalho e valores de pixels da imagem.
		* P3/P2 (cor ou PB);
		* tamanho da imagem;
		* numero máximo de cores (255);
		* valores inteiros entre 0 e 255 para pixeis 
		da imagem (de acordo com tamanho).

		Parser PPM image file (ASCII format).
		'''
		print('\nParser file PPM.')
		if self.dim==None: self.dim = im_data[1].split()
		im = MatrixImage(self.dim[0], self.dim[1])
		if str.upper(im_data[0]) != 'P3' and str.upper(im_data[0]) != 'P2': return 'Fail in spec color(Must be P3 or P2).'
		self.colormodel = im_data[0]
		
		# --- Pixels data from image file black/white mode. ----
		__temp = im_data[3:] # Pixels from image.
		_k_index = 3

		if self.colormodel=='P3':
			# Color image
			for i in range(self.dim[0]):
				for j in range(self.dim[1]):
					if color_channel > 3:
						color_channel = 1
					else:
						if color_channel == 1 :  im[i][j].r = __temp[_k_index] # red channel
						elif color_channel == 2: im[i][j].g = __temp[_k_index] # green channel
						elif color_channel == 3: im[i][j].b = __temp[_k_index] # blue channel
						# im[i][j].r, im[i][j].g, im[i][j].b =  0, 0, 0
						_k_index += 1 # Próximo linha do arquivo PPM.
						color_channel += 1
		
		# Black White
		elif self.colormodel=='P2':
			for i in range(self.dim[0]):
				for j in range(self.dim[1]):
					im[i][j] = __temp[_k_index]
		
		# --- Pixels data from image file black/white mode. ---
		
		return im
				
	# Open file (ASCII).
	def open(self, filename=None):
		'''
		Open Image file.
		'''
		image_data = []
		if filename != None:
			with open(self.filename, 'r') as fn:
				image_data.append(fn.read().split('\n'))
		else:
			pass
		return self.__parser_PPM(image_data)
	
	# Save file image.
	def save(self, Img, filename='image.ppm'):
		'''
		Save image.
		open(self, Img, filename)
		Img -> Object ImageMatrix
		filename -> Name of file
		'''
		self.filename = filename
		with open(self.filename,'w') as fn: # Open file. First write header of PPM file format.
			if self.colormodel=='color':
				fn.write('P3\n')
				fn.write(str(self.dim[0]+self.dim[1])+'')

			else: # Black and white images.
				fn.write('P2\n')
			
		print('\nSave')


# Color model RGB
class RGB(object):
	'''
	Color mode RGB
	'''
	def __init__(self):
		self.r = 0
		self.g = 0
		self.b = 0
		pass
	#def __str__(self):
	#	pass 
	
	def __repr__(self):
		return "(red,green,blue) =\n\t\t\t(%d, %d, %d)"%(self.r, self.g, self.b)
		
	def normalize(self):
		pass

# Image
class MatrixImage(object):
	'''
	Image matrix, operations/methods over matrix and vectors.. 
	'''
	def __init__(self, dim):
		self.dim = dim
		self.__lin = dim[0]
		self.__col = dim[1]
		#self.Matrix = [ [ RGB() for j in range(dim[1])] for i in range(dim[0]) ]
		self.__matrix = self.__col*[ self.__lin*[ RGB() ] ]
	
	# Checar compatibilidade de tipo na atribuição (caso int ou tupla).
	@property
	def matrix(self):
		return self.__matrix
		
	#@matrix.setter 
	#def matrix(self):
	#	return self.__col*[ self.__lin*[ RGB() ] ]
	
	def __get__(self):
		return self.matrix
		
	def __getitem__(self, key):
		return self.__get__()[key]
	
	#def __str__(self):
	#	pass
	
	#def __repr__(self, i=None, j=None):
	#	if i != None: 
	#		return "pixel (%d, %d) "%(i, j)
	#	else:
	#		return "%s" % 0
		

# tests and examples of use modules.
if __name__=="__main__":
	im = MatrixImage((2,3))
	print(im)
	im[0][1] = (120,0,0)
	print(im[0][1])
	print(im[0][0].r,im[0][0].g,im[0][0].b)
	print(im[0][0])

	# Show nheader and data for ppm file. Create use: $ python3 m_image.py > im.ppm
	#print('P3')
	#print('2 3')
	#print('255')
	#for j in range(2):
	#	for i in range(3):
	#		print(str(im[i][j].r)+'\n'+str(im[i][j].g)+'\n'+str(im[i][j].b))