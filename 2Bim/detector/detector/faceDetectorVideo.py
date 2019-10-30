# import the necessary packages
import cv2
import sys

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, image = video_capture.read()
    # load the input image and convert it to grayscale
    #image = cv2.imread(args["image"])
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # load the cat detector Haar cascade, then detect cat faces
    # in the input image
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    rects = detector.detectMultiScale(gray, scaleFactor=1.1,
	minNeighbors=5)

    # loop over the face and draw a rectangle surrounding each
    for (i, (x, y, w, h)) in enumerate(rects):
	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
	cv2.putText(image, "Rosto #{}".format(i + 1), (x, y - 10),
		cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)

    # show the detected cat faces
    cv2.imshow("Rostos encontrados", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
