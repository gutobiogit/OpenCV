import cv2
import numpy as numpy

img=cv2.imread('lena.jpg',cv2.IMREAD_COLOR)
#img=cv2.VideoCapture(0)
print (img.shape)
img[10:400,20,:]=0
cv2.rectangle(img, (180,180),(410,400),(0,255,0),4, 8, 0)
cv2.imshow('hello',img) 

cv2.waitKey()
cv2.destroyWindow("hello")
