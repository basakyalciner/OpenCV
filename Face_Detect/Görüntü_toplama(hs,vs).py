# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 15:48:54 2021

@author: bskyl
"""

import numpy
import cv2
import pandas as pd
import seaborn as sns
from scipy import ndimage

img=cv2.imread('b.jpg')

img3=ndimage.rotate(img, 90)

img4=ndimage.rotate(img, -90)

img2=ndimage.rotate(img, 180)

a = numpy.hstack((img,img3))
b = numpy.hstack((img4,img2))
horizontalAppendedImg = numpy.vstack((a,b))
c=ndimage.rotate(horizontalAppendedImg, 45)

cv2.imshow('c', c)
cv2.waitKey(0)
cv2.destroyAllWindows()