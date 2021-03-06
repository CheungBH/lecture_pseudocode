from Qt_transmittor import SendToQt
import cv2
import os

class ClsDemo:
	def __init__(self):
		self.level = -1
		self.model_path = {0: "", 1: "", 2: "", ...  9: ""}
		self.label = ["cat", "dog"]
		self.training_log = {"training acc": [], "training loss": [], "validation acc": [], "validation loss": []}
		self.image_path = ""
		self.stop = False


	def train(self, epochs, img_path, model_path=None):
		self.training_log = {"training acc": [], "training loss": [], "validation acc": [], "validation loss": []}
		if not check_format_cls(img_path):
			return -3

		img_num = img_count(img_path)
		self.level = determine_level(img_num * epochs)

		for epoch in epochs:
			SendToQt("Training loss: XXX, Training acc: XXX")
			self.training_log["training acc"].append(acc)
			self.training_log["training loss"].append(acc)
			.........

		if model_path:
			move_model(model_path, self.level)


	def plot(self):
		plot_img = plot_graph_cls(self.training_log)
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
		result_img = plot_vis_cls(pred, self.label)
		SendToQt(plot_img)
		return 0

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
			result_img = plot_vis_cls(pred, self.label)
			SendToQt(plot_img)
			if self.stop:
				break
		return 0

	def reset():
		self.level = -1


def main():
	#plot()
	#visualize()
	train(10, "data/small_set_images")
	plot()
	visualize("data/catdog/cat.jpg")
	visualize("data/catdog/cat2.jpg")
	visualize("data/catdog/dog.jpg")
	visulize_webcam()
	train(30, "data/large_set_images")
	plot()
	'''
	The results should be more accurate
	'''
	visualize("data/catdog/cat.jpg")
	visualize("data/catdog/dog.jpg")
	......
	reset()

main()
