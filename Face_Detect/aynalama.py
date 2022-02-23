# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 12:05:29 2021

@author: bskyl
"""
#Library:
import cv2
import numpy as np
from scipy import ndimage

#Loading:
img=cv2.imread("b.jpg")
cv2.imshow("resim",img)
aynalama= cv2.copyMakeBorder(img,290,20,290,20,cv2.BORDER_REFLECT)

#Rotation angle in degree:
rotated = ndimage.rotate(aynalama, 45)

#Showing:
cv2.imshow("aynalama",rotated)
cv2.waitKey(0)
cv2.destroyAllWindow()