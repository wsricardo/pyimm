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
#!/usr/bin/env python

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
        self.Img = None # self.Img = MatrixImage(self.dim,self.mode)
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
        img.pop(-1) # Remove element in index -1. (end list, element empty).
        temp = img[2].split() # dimension of image. It is in type 'string'. 'm n' in the line of file.
        self.dim = ( int( temp[0] ), int( temp[1] ) ) # Tuple with dimension of image (m,n); m rows and n columns.
        self.Img = MatrixImage( self.dim, self.mode ) # Create object image fro MatrixImage class.
        print(type(img),img)
        img = map( lambda p: int(p), img[4:] ) # Convert of string to integer color pixel values from file.
        # Image mode color
        if self.mode == 'P3':
            """
            # First implementation to map pixels in file and set Matrix of image.
            # Reading content in file image PPM in list
            for c in img[3:]:
                print(i,j)
                # Pixels i,j
                if k == 0:
                    self.Img.Matrix[i][j].r = c
                    j += 1 # next element colum from line i
                elif k == 1:
                    self.Img.Matrix[i][j].g = c                    
                    j += 1 
                elif k == 2:
                    self.Img.Matrix[i][j].b = c
                    k = 0
                    j = 0
                    i += 1
                # Next channel rgb element value.
                k += 1
            """
            #
            # Reading content file in PPM and set Matrix image. Second Implementation.
            # Start c in element 3 in the list img (list with rgb values of file PPM)
            #
            c = 4
            # Map pixels from file with Img.
            # Error here
            while i < self.dim[0]:
                while j < self.dim[1]:
                    self.Img.Matrix[i][j] = c

                   
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
