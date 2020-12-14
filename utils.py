import cv2


def SENDToQt(msg, wk=0):
	if isinstance(msg, str):
		print(msg)
	else:  # image
		cv2.imshow("result", msg)
		cv2.waitKey(wk)
