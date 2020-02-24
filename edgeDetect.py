from absl import flags
from absl import app
import cv2
import numpy as np

FLAGS = flags.FLAGS

flags.DEFINE_boolean('f', False, 'Runs Fast Edge Detection')
flags.DEFINE_boolean('s', False, 'Runs Shi Tomasi Edge Detection')
flags.DEFINE_boolean('h', False, 'Runs Harris Edge Detection')
flags.DEFINE_integer('q', 1000, 'Amount of Points Drawn')

def shiTomasi(frame, sharp):
	corners = cv2.goodFeaturesToTrack(sharp, FLAGS.q, 0.01, 10)
	corners = np.int0(corners)

	for i in corners:
		x,y = i.ravel()
		cv2.circle(frame, (x,y),3,255,-1)

	cv2.imshow('shi tomasi', frame)

def harris(frame, sharp):
	gray = np.float32(sharp)

	dst = cv2.cornerHarris(gray,2,3,0.04)

	dst = cv2.dilate(dst,None)

	frame[dst>0.05*dst.max()]=[0,0,255]

	cv2.imshow('harris',frame)

def fast(frame, sharp, fst):
	kp = fst.detect(sharp, None)

	frame = cv2.drawKeypoints(frame, kp, outImage = None, color=(255, 0, 0))
	
	cv2.imshow('fast', frame)

def main(argv):
	cap = cv2.VideoCapture(0)

	sharp = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

	fst = cv2.FastFeatureDetector_create(400)

	while (True):

		ret, frame = cap.read()

		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		sharpen = cv2.filter2D(gray, -1, sharp)
	
		if FLAGS.h:
			harris(frame, sharpen)

		if FLAGS.s:
			shiTomasi(frame, sharpen)
	
		if FLAGS.f:
			fast(frame, sharpen, fst)

		if cv2.waitKey(1) & 0xFF == ord('q'):
                	break

if __name__ == '__main__':
  app.run(main)
