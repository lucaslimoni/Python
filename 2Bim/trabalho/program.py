import cv2
import numpy as np

img = cv2.imread('bubles4.jpg')
height, width, channels = img.shape
print(height, width, channels)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray,5)

circles = cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,50,param1=50,param2=30,minRadius=10,maxRadius=80)
circles = np.uint16(np.around(circles))
print(circles)
start = (np.uint16(np.around((width / 2))),0)
end = (np.uint16(np.around((width / 2))), height)
color = (255,255,0)
espessura = 3

totalCircle = 0
esquerda = 0
direita = 0
img = cv2.line(img, start, end, color, espessura)
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
    totalCircle += 1

for y in circles[0:]:
    for i in y[0:]:
        if i[0] < np.uint16(np.around((width / 2))):
            esquerda += 1
        if i[0] > np.uint16(np.around((width / 2))):
            direita += 1

print(esquerda)
print(direita)

font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (50,30)
bottomRightCornerOfText = (width - 50,30)
fontScale              = 1
fontColor              = (0,0,255)
lineType               = 2
img = cv2.putText(img,str(esquerda), bottomLeftCornerOfText, font, fontScale, fontColor, lineType)
img = cv2.putText(img,str(direita), bottomRightCornerOfText, font, fontScale, fontColor, lineType)
cv2.imshow('detected circles',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
