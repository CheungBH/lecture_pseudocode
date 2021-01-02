from Qt_transmittor import SendToQt
import cv2
import os

class DetCustomized:
	def __init__(self):
		self.default_path = "det.pth"
		self.label = []
		self.training_results = {"ave classification loss": [], "ave objectness loss": [], "ave iou loss": []}
		self.stop = False

	def train(self, epochs, img_path, model_path="model.pth"):
		if not check_format_det(img_path):
			return -3
		img_num = img_count(img_path)

		load_model()
		load_data()
		self.label = load_label()
		self.training_results = {"ave classification loss": [], "ave objectness loss": [], "ave iou loss": []}

		for epoch in epochs:
			for inputs, labels in data_loader:
				SendToQt("ave classification loss: XXX, ave objectness loss: XXX, ave iou loss: XXX")
				self.training_results["ave classification loss"].append(cls_loss)
				self.training_results["ave objectness loss"].append(obj_loss)
				self.training_results["ave iou loss"].append(iou_loss)
				.........

		save(model_path)


	def plot(self):
		if not os.path.exists(self.default_path):
			return -1
		plot_img = plot_graph(self.training_results)
		SendToQt(plot_img)
		return 0

	def visualize(self, img_path, model_path=None):
		img_mat = cv2.imread(img_path)
		if not os.path.exists(model_path):
			return -1
		pred = model(img_mat)
		result_img = plot_vis_det(pred, self.label)
		SendToQt(plot_img)
		return 0

	def visualize_webcam(self, model_path=None):
		self.stop = False
		if not os.path.exists(model_path):
			return -1
		while True:
			img_mat = cv2.VideoCapture(0)
			pred = model(img_mat)
			result_img = plot_vis_det(pred, self.label)
			SendToQt(plot_img)
			if self.stop:
				break
		return 0
