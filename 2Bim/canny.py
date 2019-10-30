import cv2
import numpy as np

img = cv2.imread('messi.jpg', 0)
# img = cv2.blur(img,(5,5))
img = cv2.GaussianBlur(img,(5,5), cv2.BORDER_DEFAULT)
edges = cv2.Canny(img,100,250)

cv2.imshow('Messi', img)
cv2.imshow('Canny', edges)

cv2.waitKey(0)
