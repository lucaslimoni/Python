# import the necessary packages
import argparse
import cv2
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the input image")
ap.add_argument("-c", "--cascade",
	default="haarcascade_frontalcatface.xml",
	help="path to cat detector haar cascade")
args = vars(ap.parse_args())

# load the input image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
# load the cat detector Haar cascade, then detect cat faces
# in the input image
catDetector = cv2.CascadeClassifier("haarcascade_frontalcatface.xml")
catRects = catDetector.detectMultiScale(gray, scaleFactor=1.4,
	minNeighbors=10, minSize=(75, 75))

faceDetector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
faceRects = faceDetector.detectMultiScale(gray, scaleFactor=1.1,
        minNeighbors=10, minSize=(75, 75))


# loop over the cat faces and draw a rectangle surrounding each
for (i, (x, y, w, h)) in enumerate(catRects):
	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
	cv2.putText(image, "Gato #{}".format(i + 1), (x, y - 10),
		cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)

# loop over the faces and draw a rectangle surrounding each
for (i, (x, y, w, h)) in enumerate(faceRects):
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, "Rosto #{}".format(i + 1), (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 2)

# show the detected cat faces
cv2.imshow("Total Faces", image)
cv2.waitKey(0)

# load the cat detector Haar cascade, then detect cat faces
# in the input image
#detector = cv2.CascadeClassifier(args["cascade"])
#rects = detector.detectMultiScale(gray, scaleFactor=1.3,
#	minNeighbors=5)


