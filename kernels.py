import numpy as np
import cv2

blurKernel = np.full((3, 3), 1/9)
sharpenKernel = np.array([[-1, -1, -1],
                   	[-1, 9, -1],
                   	[-1, -1, -1]])

cap = cv2.VideoCapture(0)

ret, frame = cap.read()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

while (True):
	cv2.imshow('og', gray)
	
	cv2.imshow('blur', cv2.filter2D(gray, -1, blurKernel))
	cv2.imshow('sharpen', cv2.filter2D(gray, -1, sharpenKernel))

	if cv2.waitKey(1) & 0xFF == ord('q'):
        	break

cap.release()
cv2.destroyAllWindows()
