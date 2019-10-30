import cv2
import numpy as np

img = cv2.imread('sudoku.jpg', 0)
blur = cv2.medianBlur(img, 5)

ret, thr = cv2.threshold(blur,127,255,cv2.THRESH_BINARY)
cv2.imshow('Input', img)
cv2.imshow('Threshold', thr)
cv2.waitKey(0)

th2 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

cv2.imshow('Mediana', th2)
cv2.waitKey(0)
cv2.imshow('Adaptativo', th3)
cv2.waitKey(0)

kernel = np.ones((3,3), np.uint8)
img_dilation = cv2.dilate(th3, kernel, iterations=1)
img_erosion = cv2.erode(img_dilation, kernel, iterations=2)

cv2.imshow('Dilate/Erode',img_erosion)
cv2.waitKey(0)

