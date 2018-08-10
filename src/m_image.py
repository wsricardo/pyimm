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
		print('\nParser file PPM.')
		if self.dim==None: self.dim = im_data[1].split()
		im = MatrixImage(self.dim[0], self.dim[1])
		return im
				
	# Open file (ASCII).
	def open(self, filename=None):
		im_data = []
		if filename != None:
			with open(self.filename, 'r') as fn:
				im_data.append(fn.read().split('\n'))
		else:
			pass
		return self.__parser_PPM()
	
	# Save file image.
	def save(self, Img, filename='image.ppm'):
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