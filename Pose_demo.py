from utils import SENDToQt

class PoseDemo:
	def __init__(self):
		self.threshold = -1
		self.model_path = ""
		self.training_log = {"loss": [], "PCK": [], "PCKH": [], "mse": []}


	def train(epochs, img_path, model_path=None):
		self.training_log = {"loss": [], "PCK": [], "PCKH": [], "mse": []}
		if not check_format_pose(img_path):
			return -3

		img_num = img_count(img_path)
		self.threshold = determine_threshold(img_num * epochs)

		for epoch in epochs:
			SENDTOQt("Epoch: epoch [X/X], loss: XXX, PCK: XXX, PCKH: XXX, mse: XXX")
			self.training_log["loss"].append(loss)
			self.training_log["PCK"].append(PCK)
			self.training_log["mse"].append(mse)
			self.training_log["PCKH"].append(PCKH)
			.........

		if model_path:
			save(model_path)


	def plot():
		plot_img = plot_graph_pose(self.training_log)
		SENDTOQt(plot_img)

	def visualize(img_path):
		img_mat = cv2.imread(img_path)
		model = load_model(self.model_path)
		pred = model(img_mat)
		result_img = plot_vis_pose(pred, self.threshold)
		SENDTOQt(plot_img)

	def visulize_webcam():
		model = load_model(self.model_path)
		while True:
			img_mat = capture(0)
			pred = model(img_mat)
			result_img = plot_vis_pose(pred, self.threshold)
			SENDTOQt(plot_img)
			if stop:
				break
		return 0

	def annotate(img_folder):
		total_num = img_count(img_folder)
		for img in img_folder:
			SENDTOQt(img)
			record_annot_info()
			write_annot()
			SENDTOQt("Finish annotation [X/total_num]")

	def reset():
		self.level = -1


def main():
	#annotate("data/kps/small_set_images")
	#annotate("data/kps/large_set_images")
	#plot()
	#visualize()
	train(10, "data/small_set_images")
	plot()
	visualize("data/person/person1.jpg")
	visualize("data/person/person2.jpg")
	visualize("data/person/person3.jpg")
	visualize_webcam()
	train(30, "data/large_set_images")
	plot()
	visualize("data/person/person2.jpg")
	visualize("data/person/person3.jpg")
	......
	reset()

main()



