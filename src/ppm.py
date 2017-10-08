#-------------------------------------------------------------------------------
# Name:         PPM
# Purpose:      Save/Read image format PPM
#
# Author:      Wandeson Ricardo
#
# Created:     26/02/2013
# Copyright:   (c) 2013
# License:      GPL
# Blog:		www.wanartsci.blogspot.com
#		www.gaenos.blogspot.com
#-------------------------------------------------------------------------------
#!/usr/bin/env python3

# --- NOTAS -  Modificações e Correções de Projeto ---
# Necessário alterações e limpeza no codigo
# na passagem para funções usar o argumento <MatrixImage>.Matrix
# selecionando a matriz que representa a imagem para manipulação
# correções na classe PPM no metodo __init__ para permitir
# a criação da matriz duma imagem inicial com valores nulos
# para casos de sinteses de imagens; tratando esse caso
# de escolha de criação.

from matrixImage import*

# Manipulate image file ppm format (save file).  
class PPM:
    """ Write and read image file format ppm.  """

    def __init__(self, name_file=None, row=None, columm=None, mode='color'):
        self.name_file = name_file
        self.row, self.columm = row, columm
        self.dim = (self.row, self.columm)
        self.mode = mode
        self.Img_file = None
        self.Img = MatrixImage(self.dim,self.mode).matrix
        if self.name_file is not None:
            self.Img_file = open(self.name_file,'wr')
            #self.Img_file.write('P3\n'+' '+str(self.columm)+' '+str(self.row)+' 255\n')
            #self.putPixel = lambda Pixel: self.Img_file.write( (Pixel[i][j].r+' ' +
            #                                                   Pixel[i][j].g+' '+
            #                                                   Pixel[i][j].b))
        
    # Open read file PPM images.
    def read(self, imname=None):
        """
        Open read file PPM and return image (matrixImage).
        """
        i, j, k, c = 0, 0, 0, None
        if imname is not None:
            self.name_file= imname
            self.Img_file = open(self.name_file, 'r')
        else:
            print('\nError! Define file_name\n')

        im_temp = self.Img_file.read()
        img = im_temp.split('\n')
        self.mode = img[0]
        # Remove element in index -1. (end list, element empty).
        img.pop(-1) 
        # dimension of image. It is in type 'string'. 'm n' in the line of file.
        temp = img[2].split() 
        # Tuple with dimension of image (m,n); m rows and n columns.
        self.dim = ( int( temp[0] ), int( temp[1] ) )
        # Create object image fro MatrixImage class.
        self.Img = MatrixImage( self.dim, self.mode )

        print(type(img),img)
        # Convert of string to integer color pixel values from file.
        img = map( lambda p: int(p), img[4:] ) 
        
        l = self.dim[0]*self.dim[1] # Tamanho da imagem para um vetor.

        # Image mode color
        if self.mode == 'P3':
            
            # First implementation to map pixels in 
            # file and set Matrix of image.
            # Reading content in file image PPM in list
            # Read elements from list to matrix image
            for k in range(l):
                while j <= self.dim[0]:
                    self.Img[i][j].r  = img[k].r 
                    self.Img[i][j].b  = img[k].g 
                    self.Img[i][j].g  = img[k].b
                    j = j + 1 # Next collum.

                # Next line.
                i = i + 1
            
                   
        # Black and White color
        elif self.mode == 'P2':
		
            # If image mode is black/white
            # c = 0
            for c in img[3:]:
                if i >= self.dim[0]:
                    i += 1
                else:
                    self.Img.Matrix[i][j] = c
                    j += 1
        else:
            return 0
        return 1


    def writePixel(self,Pixel,i,j):
        self.Pixel = Pixel
        self.Img_file.write((str(Pixel[i][j].r)+' '
                             + str(Pixel[i][j].g)+' '+str(Pixel[i][j].b)))
        pass

    def write(self, Img):
        self.Img = Img
        self.Img_file.write('P3\n'+str(self.columm)+' '+str(self.row)+'\n255\n')
        for i in range(0,self.row):
            for j in range(0,self.columm):
                self.Img_file.write(str(self.Img[i][j].r)+'\n'
                                    +str(self.Img[i][j].g)+'\n'
                                    +str(self.Img[i][j].b)+'\n')

        self.save()
        pass

    def save(self):
        self.Img_file.close()
        print('Saved...')
