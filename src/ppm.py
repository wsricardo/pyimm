#-------------------------------------------------------------------------------
# Name:         PPM
# Purpose:      Save image format PPM
#
# Author:      Wandeson Ricardo
#
# Created:     26/02/2013
# Copyright:   (c) 2013
# License:      GPL
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from matrixImage import*
#Manipulate image file ppm format (save file).  

class PPM:
    """ Write image file format ppm.  """
    def __init__(self, name_file=None, row=None, columm=None, mode='color'):
        self.name_file = name_file
        self.row, self.columm = row, columm
        self.mode = mode
        if file_name != None:
            self.Img_file = open(name_file,'wr')
            #self.Img_file.write('P3\n'+' '+str(self.columm)+' '+str(self.row)+' 255\n')
            #self.putPixel = lambda Pixel: self.Img_file.write( (Pixel[i][j].r+' ' +
            #                                                   Pixel[i][j].g+' '+
            #                                                   Pixel[i][j].b))
        
    #No implemented in the momment
    def read(self,imname=None):
        self.Img_file.read()
        if imname != None:
            self.name_file= imname
            self.Img_file = open(self.name_file, 'wr')
        else:
            print('\nError! Define file_name\n')
        self.Img_file.read(self.name_file)

        #Reading content in file image PPM
        

    def writePixel(self,Pixel,i,j):
        self.Pixel = Pixel
        self.Img_file.write((str(Pixel[i][j].r)+' '
                             + str(Pixel[i][j].g)+' '+str(Pixel[i][j].b)))
        pass

    def write(self, Img):
        self.Img = Img
        self.Img_file.write('P3\n'+' '+str(self.columm)+' '+str(self.row)+' 255\n')
        for i in range(0,self.row):
            for j in range(0,self.columm):
                self.Img_file.write(str(self.Img[i][j].r)+' '
                                    +str(self.Img[i][j].g)+' '
                                    +str(self.Img[i][j].b)+'\n')

        self.save()
        pass

    def save(self):
        self.Img_file.close()
        print 'Saved...'
