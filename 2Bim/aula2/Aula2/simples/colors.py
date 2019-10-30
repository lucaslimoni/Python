import numpy as np
import cv2

img = cv2.imread('messi.jpg')
cv2.imshow('Messi', img)

print('pixel BGR posicao x = 100 y =100')
px = img[100,100]
print(px)

cv2.waitKey(0)

print('pixel azul na mesma posicao')
blue = img[100,100,0]
print(blue)

cv2.waitKey(0)

print('acessando dados da imagem')
print('H x W x D')
print(img.shape)

cv2.waitKey(0)

print('size')
print(img.size)

cv2.waitKey(0)

print('separando a bola')
ball = img[280:340, 330:390]

cv2.imshow('Bola', ball)
cv2.waitKey(0)

print(ball.shape)
img[273:333, 100:160] = ball

cv2.imshow('Messi2', img)
cv2.waitKey(0)

