from PIL import Image
from numpy import *
from pylab import *

import imtools

#im = array(Image.open('images/girl_six.jpg'))
im = array(Image.open('images/beach_trash_3.jpg').convert('L'))
#hist(im.flatten(),128)
imshow(im)
show()
im2, cdf = imtools.histeq(im)
imshow(im2)
#hist(im2.flatten(),128)
show()
