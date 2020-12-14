

def SENDToQt(msg):
	if isinstance(msg, str):
		print(msg)
	else:  # image
		cv2.imshow("result", msg)
		cv2.waitKey(1)
