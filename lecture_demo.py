from api import SendToQt, AcceptFromQt
import time
import cv2
import numpy as np


class DemoQtPython:
    def __init__(self):
        self.default_model_path = "model.pth"
        self.label = []

    def train(self, epochs, img_path, model_path="model.pth"):
        stop = False
        for epoch in range(epochs):
            time.sleep(1)
            stop = AcceptFromQt(stop)
            message = "{}: {}".format(time.asctime(time.localtime(time.time())), epoch)
            SendToQt(message)
            if stop:
                break

    def plot(self):
        import matplotlib.pyplot as plt

        x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
        y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
        y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]

        ln1, = plt.plot(x_data, y_data, color='red', linewidth=2.0, linestyle='--')
        ln2, = plt.plot(x_data, y_data2, color='blue', linewidth=3.0, linestyle='-.')

        plt.title("test")  # 设置标题及字体

        plt.legend(handles=[ln1, ln2], labels=['1', '2'])
        ax = plt.gca()
        ax.spines['right'].set_color('none')  # right边框属性设置为none 不显示
        ax.spines['top'].set_color('none')  # top边框属性设置为none 不显示
        plt.savefig('image.jpg')
        # plt.show()

    def visualize(self, img_path, model_path="model.pth"):
        img_mat = cv2.imread(img_path)
        result_mat = cv2.flip(img_mat, 1)
        SendToQt(result_mat)

    def visualize_video(self, video_path=0, model_path="model.pth"):
        stop = False
        cap = cv2.VideoCapture(video_path)
        height, width = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)), int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        while True:
            ret, frame = cap.read()
            if ret:
                result_mat = cv2.flip(frame, 1)
                SendToQt(result_mat, wk=100)
                stop = AcceptFromQt(stop)
                if stop:
                    cap.release()
                    SendToQt(np.full((height, width, 3), 0).astype(np.uint8), wk=0)
                    break
            else:
                cap.release()
                SendToQt(np.full((height, width, 3), 0).astype(np.uint8), wk=0)
                break


if __name__ == '__main__':
    demo = DemoQtPython()
    demo.plot()
    # demo.train(1, "dalk")
    # demo.visualize("demo/horse.jpg")
    # demo.visualize_video("demo/ice.mp4")
