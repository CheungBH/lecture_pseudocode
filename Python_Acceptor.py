from app_class.Det_customized import DetCustomized
from app_class.Cls_customized import ClsCustomized
from app_class.Det_demo import DetDemo as FRUIT
from app_class.Pose_demo import PoseDemo as PERSON
from app_class.Cls_demo import ClsDemo as CATDOG


class PythonAcceptor:
    def __init__(self):
        # Train
        self.model_path = ""
        self.data_path = ""
        self.epoch = 15

        # Visualize
        self.image_path = ""
        # self.video_path = 0

        self.fruit = FRUIT()
        self.catdog = CATDOG()
        self.person = PERSON()
        self.det = DetCustomized()
        self.cls = ClsCustomized()
        self.signal = "00"

    def set_signal(self, sig):
        self.signal = sig

    def set_model_path(self, string):
        self.model_path = string

    def set_image_path(self, string):
        self.image_path = string

    def set_data_path(self, string):
        self.data_path = string

    def set_epoch(self, epo):
        self.epoch = epo

    def set_webcam_stop(self):
        self.fruit.stop = True
        self.catdog.stop = True

    def run(self):
        if self.signal[0] == "1":
            if self.signal[1] == "1":
                self.fruit.train(img_path=self.data_path, epochs=self.epoch, model_path=self.model_path)
            elif self.signal[1] == "2":
                self.fruit.visualize(self.image_path, self.model_path)
            elif self.signal[1] == "3":
                self.fruit.visualize_webcam(self.model_path)
            elif self.signal[1] == "4":
                self.fruit.plot()

        elif self.signal[0] == "2":
            if self.signal[1] == "1":
                self.catdog.train(epochs=self.epoch, img_path=self.data_path, model_path=self.model_path)
            elif self.signal[1] == "2":
                self.catdog.visualize(self.image_path, self.model_path)
            elif self.signal[1] == "3":
                self.catdog.visualize_webcam(self.model_path)
            elif self.signal[1] == "4":
                self.catdog.plot()

        elif self.signal[0] == "3":
            if self.signal[1] == "1":
                self.person.train(img_path=self.data_path, epochs=self.epoch, model_path=self.model_path)
            elif self.signal[1] == "2":
                self.person.visualize(self.image_path, self.model_path)
            elif self.signal[1] == "3":
                self.person.visualize_webcam(self.model_path)
            elif self.signal[1] == "4":
                self.person.plot()

        elif self.signal[0] == "4":
            if self.signal[1] == "1":
                self.det.train(epochs=self.epoch, img_path=self.data_path, model_path=self.model_path)
            elif self.signal[1] == "2":
                self.det.visualize(self.image_path, self.model_path)
            elif self.signal[1] == "3":
                self.det.visualize_webcam(self.model_path)
            elif self.signal[1] == "4":
                self.det.plot()

        elif self.signal[0] == "5":
            if self.signal[1] == "1":
                self.cls.train(epochs=self.epoch, img_path=self.data_path, model_path=self.model_path)
            elif self.signal[1] == "2":
                self.cls.visualize(self.image_path, self.model_path)
            elif self.signal[1] == "3":
                self.cls.visualize_webcam(self.model_path)
            elif self.signal[1] == "4":
                self.cls.plot()

        else:
            pass
        
        self.signal = "00"


PA = PythonAcceptor()
PA.run()


def tcp_init():
    pass


def parse():
    pass



