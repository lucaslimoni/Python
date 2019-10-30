import argparse
import os.path
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the input image")
args = vars(ap.parse_args())

if not os.path.exists(args['image']):
  print('File does not exist!')
  exit()

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Imagem", image)
cv2.waitKey(0)
