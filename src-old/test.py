import ppm
import matrixImage

#im = matrixImage.MatrixImage((2,2)).matrix
#print(im)
#img_filename = "test.ppm"
#img_file = ppm.PPM(img_filename,2,2)
#img_file.write(im)

# Test read image PPM
im = ppm.PPM('test.ppm').iread()


