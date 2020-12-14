from utils import SENDToQt

class ClsCustomized:
	def __init__(self):
		self.default_model_path = "CNN.pth"
		self.label = []
		self.training_log = {"training acc": [], "training loss": [], "validation acc": [], "validation loss": []}

	def train(epochs, img_path, model_path=self.default_model_path):
		if not check_format_cls(img_path):
			return -3

		load_model()
		train_val_split(0.2)
		load_data()
		self.label = load_label()

		self.training_log = {"training acc": [], "training loss": [], "validation acc": [], "validation loss": []}
		for epoch in epochs:
			for inputs, labels in data_loader:
				SENDTOQt("Training loss: XXX, Training acc: XXX")
				time.sleep()
				self.training_log["training acc"].append(acc)
				self.training_log["training loss"].append(acc)
				.........

		save(model_path)
		return 0


	def plot():
		plot_img = plot_graph(self.training_results)
		SENDTOQt(plot_img)

	def visualize(img_path, model_path=self.default_model_path):
		# try:
		img_mat = cv2.imread(img_path)
		# except:
		# 	return -2
		if not os.path.exist(model_path):
			return -1
		pred = model(img_mat)
		result_img = plot_vis_cls(pred, self.label)
		SENDTOQt(plot_img)
		return 0

	def visulize_webcam(model_path=self.default_model_path)
		if not os.path.exist(model_path):
			return -1
		# try:
		while True:
			img_mat = capture(0)
			pred = model(img_mat)
			result_img = plot_vis_cls(pred, self.label)
			SENDTOQt(plot_img)
			if stop:
				break
		# except:
		# 	return -2
		return 0

def main():
	#plot()
	#visualize()
	train(10, "data/wrong_format_path")
	train(10, "data/small_set_images")
	plot()
	visualize("data/catdog/cat.jpg")
	visualize("data/catdog/cat2.jpg")
	visualize("data/catdog/dog.jpg")
	visulize_webcam()
	train(30, "data/large_set_images")
	plot()
	visualize("data/catdog/cat.jpg")
	visualize("data/catdog/dog.jpg")
	......
	reset()

main()