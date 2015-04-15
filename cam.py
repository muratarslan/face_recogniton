import cv2
import sys

cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
cam = cv2.VideoCapture(0)
file = "screenshot.png"


# Crop Image
def crop(faces):
	img = cv2.imread(file)
	for (x, y, w, h) in faces:
		print x, y, w, h
		crop_img = img[y: y + h, x: x + w] # Crop from x, y, w, h 
         	cv2.imshow("cropped", crop_img)
        	cv2.imwrite('face.png', crop_img)




def run():
    stop = False

    if cam.isOpened(): # try to get the first frame
        rval, frame = cam.read()
    else:
        rval = False
        print "Camera is not found"

    while rval or not stop:
        ret, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30),
		flags=cv2.cv.CV_HAAR_SCALE_IMAGE
	    )

	# Draw a rectangle around the faces
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        key = cv2.waitKey(20)

        cv2.imshow('Face Detection', frame)

        if key & 0xFF in [ord('S'), ord('s')]: # Screenshot
            cv2.imwrite(file, gray)
	    crop(faces)
            print "Screenshot taken!"
        elif key & 0xFF in [ord('C'), ord('c')]: # Cropped
            crop(faces)
            print "Cropped"
        elif key & 0xFF in [ord('Q'), ord('q')]: # Exit
            print "Exiting"
            stop = True
            break


    cam.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    run()
