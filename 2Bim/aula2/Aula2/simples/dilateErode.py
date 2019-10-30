import cv2
import numpy as np

img = cv2.imread('j.png', 0)

#img = (255-img)
#img = cv2.bitwise_not(img)

kernel = np.ones((5,5), np.uint8)

# erode e dilate aumentam e diminuem a area branca da imagem
img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img, kernel, iterations=1)

cv2.imshow('Input', img)
cv2.imshow('Erosion', img_erosion)
cv2.imshow('Dilation', img_dilation)

cv2.waitKey(0)
