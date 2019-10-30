from __future__ import print_function
from __future__ import division

import cv2

slider_max = 255
title = 'Threshold value'

def on_trackbar(val):
    ret, thr = cv2.threshold(img, val, 255, cv2.THRESH_BINARY)
    cv2.imshow(title, thr)

img = cv2.imread('sudoku.jpg',0)

cv2.namedWindow(title)
trackbar_name = 'Threshold x %d' % slider_max
cv2.createTrackbar(trackbar_name, title , 0, slider_max, on_trackbar)

# Show some stuff
on_trackbar(0)

# Wait until user press some key
cv2.waitKey()
