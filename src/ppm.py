#!/usr/bin/env python3
#-*- coding: utf-8 -*-
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
    
    def __init__(self, name_file=None, dim = None, mode='color',mode_file='r'):
        self.name_file = name_file
        self.dim = dim # dimension of image (pixels).
        self.mode = mode # Color (P3) or gray scale (P2)
        self.Img_file = None
        # Matrix for image (channels included if rgb)
        #self.Img = MatrixImage(self.dim,self.mode).matrix
        # Decisão de Projeto : em qual modo abrir o arquivo?
        # Obs.: modo escrita apaga coteudo sobrescrevendo 
        # se já existe ou cria se não existir.
        #self.Img_file = open(self.name_file,'w')
    
    # Open read file PPM images.
    def iread(self):
        """
        Open read file PPM and return image (matrixImage).
        """
        i, j, k, c = 0, 0, 0, 0
        
        if self.name_file is not None: 
            self.Img_file = open(self.name_file, 'r')
        else:
            return False
        im_temp = self.Img_file.read()
        img = im_temp.split('\n')
        self.mode = img[0]
        # Remove element in index -1. (end list, element empty).
        img.pop(-1) 
        # dimension of image. It is in type 'string'. 'm n' in the line of file.
        temp = img[1].split() 
        # Tuple with dimension of image (m,n); m rows and n columns.
        print('temp',temp)
        self.dim = ( int( temp[0] ), int( temp[1] ) )
        # Create object image fro MatrixImage class.
        self.Img = MatrixImage( self.dim, self.mode ).matrix

        print(type(img),img)
        # Convert of string to integer color pixel values from file. 
        # version 2, maybe alterations for version Python3 in this line.
        #img = map( lambda p: int(p), img[4:] ) 
        img = [ int(i) for i in img[3:] ]
        print('>',len(img),img)
        l = self.dim[0]*self.dim[1]*3 # Dimension of image for define size vector
        # Image mode color
        if self.mode == 'P3':
            
            # First implementation to map pixels in 
            # file and set Matrix of image.
            # Reading content in file image PPM in list
            # Read elements from list to matrix image.
            #for k in range(l):
            
                 
            if c==0: 
                self.Img[i][j].r  = img[k]
                c += 1
            elif c==1: 
                self.Img[i][j].b  = img[k] 
                c += 1
            elif c==2:                
                self.Img[i][j].g  = img[k]
                c = 0
                j = j + 1 # Next collum.

            # Next line.
            i = i + 1
            k += 1
                   
        # Black and White color
        elif self.mode == 'P2':
		
            # If image mode is black/white
            # c = 0
            for c in img[3:]:
                if i >= self.dim[0]:
                    i += 1
                else:
                    self.Img[i][j] = c
                    j += 1
        else:
			
            return 0
        
        return 1 # return self.Img


    def write(self):
        self.Img = Img
        self.Img_file.write('P3\n'+str(self.columm)+' '+str(self.row)+'\n255\n')
        for i in range(0,self.row):
            for j in range(0,self.columm):
                self.Img_file.write(str(self.Img[i][j].r)+'\n'
                                    +str(self.Img[i][j].g)+'\n'
                                    +str(self.Img[i][j].b)+'\n')

        self.save()

    def save(self):
        self.Img_file.close()
        print('Saved...')
        return True
