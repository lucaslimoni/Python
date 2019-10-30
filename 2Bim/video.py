import cv2
import numpy as np
import sys

video_capture = cv2.VideoCapture(0)

while True:

    ret, image = video_capture.read()
    blur = cv2.GaussianBlur(image,(5,5), cv2.BORDER_DEFAULT)
    edges = cv2.Canny(blur,25,25)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # load the cat detector Haar cascade, then detect cat faces
    # in the input image
    
    detector = cv2.CascadeClassifier("./detector/detector/haarcascade_frontalface_default.xml")
    rects = detector.detectMultiScale(gray, scaleFactor=1.1,minNeighbors=5)

    # loop over the face and draw a rectangle surrounding each
    for (i, (x, y, w, h)) in enumerate(rects):
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(image, "Rosto #{}".format(i + 1), (x, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
        cv2.putText(image, "Dist: #{}".format(i + 1), (x, y - 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)

    # show the detected cat faces

    # cv2.imshow("Video1", image)
    # cv2.imshow("Video2", edges)
    # cv2.imshow("Video3", blur)

    cv2.imshow("Rostos encontrados", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
