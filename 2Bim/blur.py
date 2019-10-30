import cv2
import numpy as np

img = cv2.imread('opencv_original.jpg')

blur = cv2.blur(img,(5,5))
gBlur = cv2.GaussianBlur(img,(5,5), cv2.BORDER_DEFAULT)

cv2.imshow('Original', img)
cv2.imshow('Blurred', blur)
cv2.imshow('GBlurred', gBlur)

cv2.waitKey(0)
