from utils import SENDToQt

class DetCustomized:
	def __init__(self):
		self.default_path = "model.pth"
		self.label = []
		self.training_results = {"ave classification loss": [], "ave objectness loss": [], "ave iou loss": []}

	def train(epochs, img_path, model_path="model.pth"):
		if not check_format_det(img_path):
			return -3
		img_num = img_count(img_path)

		load_model()
		load_data()
		self.label = load_label()
		self.training_results = {"ave classification loss": [], "ave objectness loss": [], "ave iou loss": []}

		for epoch in epochs:
			for inputs, labels in data_loader:
				SENDTOQt("ave classification loss: XXX, ave objectness loss: XXX, ave iou loss: XXX")
				self.training_results["ave classification loss"].append(cls_loss)
				self.training_results["ave objectness loss"].append(obj_loss)
				self.training_results["ave iou loss"].append(iou_loss)
				.........

		save(model_path)


	def plot():
		if not os.path.exist(self.default_path):
			return -1
		plot_img = plot_graph(self.training_results)
		SENDTOQt(plot_img)
		return 0

	def visualize(img_path, model_path=self.default_path):
		img_mat = cv2.imread(img_path)
		if not os.path.exist(model_path):
			return -1
		pred = model(img_mat)
		result_img = plot_vis_det(pred, self.label)
		SENDTOQt(plot_img)
		return 0

	def visulize_webcam(model_path=self.default_path)
		if not os.path.exist(model_path):
			return -1
		while True:
			img_mat = capture(0)
			pred = model(img_mat)
			result_img = plot_vis_det(pred, self.label)
			SENDTOQt(plot_img)
			if stop:
				break
		return 0
