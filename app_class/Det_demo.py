from Qt_transmittor import SendToQt
import cv2
import os


class DetDemo:
	def __init__(self):
		self.level = -1
		self.model_path = {0: "", 1: "", 2: "", ...  9: ""}
		self.label = 1# fruit label
		self.stop = False
		self.training_log = {"ave classification loss": [], "ave objectness loss": [], "ave iou loss": []}

	def train(self, epochs, img_path, model_path=None):
		self.training_log = {"ave classification loss": [], "ave objectness loss": [], "ave iou loss": []}
		if not check_format_det(img_path):
			return -3

		img_num = img_count(img_path)
		self.level = determine_level(img_num * epochs)

		for epoch in epochs:
			SendToQt("ave classification loss: XXX, ave objectness loss: XXX, ave iou loss: XXX")
			self.training_log["ave classification loss"].append(cls_loss)
			self.training_log["ave objectness loss"].append(obj_loss)
			self.training_log["ave iou loss"].append(iou_loss)
			.........

		if model_path:
			move_model(model_path, self.level)


	def plot(self):
		plot_img = plot_graph_det(self.training_log)
		SendToQt(plot_img)

	def visualize(self, img_path, model_path=None):
		if self.level < 0:
			return -1
		img_mat = cv2.imread(img_path)
		if model_path:
			model = load_model(model_path)
		else:
			model = load_model(self.model_path[self.level])
		pred = model(img_mat)
		result_img = plot_vis_det(pred, self.label)
		SendToQt(plot_img)

	def visualize_webcam(self, model_path=None):
		self.stop = False
		if self.level < 0:
			return -1
		if model_path:
			model = load_model(model_path)
		else:
			model = load_model(self.model_path[self.level])
		while True:
			img_mat = capture(0)
			pred = model(img_mat)
			result_img = plot_vis_det(pred, self.label)
			SendToQt(plot_img)
			if self.stop:
				break
		return 0

	def reset(self):
		self.level = -1


def main():
	#plot()
	#visualize()
	train(10, "data/small_set_images")
	plot()
	visualize("data/det/image1.jpg")
	visualize("data/det/image2.jpg")
	visualize("data/det/image3.jpg")
	visulize_webcam()
	train(30, "data/large_set_images")
	plot()	
	'''
	The results should be more accurate
	'''
	visualize("data/det/image2.jpg")
	visualize("data/det/image3.jpg")
	......
	reset()

main()