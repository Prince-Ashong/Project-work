import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)

while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()
	faces = face_cascade.detectMultiScale(frame, scaleFactor = 1.5, minNeighbors = 5)
	for (x, y, w, h) in faces:
		print(x,y,w,h)
		roi_color = frame[y:y+h, x:x+w]
		roi_color = frame[y:y+h, x:x+w]

# recognize? deep learned model predict keras tensorflow pytorch scikit learn

		img_item = "my-image.png"
		cv2.imwrite(img_item, roi_color)

		color = (225, 200, 100)
		stroke = 2
		end_cord_x = x + w
		end_cord_y = y + h
		cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
	
	#Display the resultin frame
	cv2.imshow('frame',frame)
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break 

		#When everything done, release the capture
		cap.release()
		cv2.destroyAllWindows()
 