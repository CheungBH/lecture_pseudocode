from utils import SENDToQt
import time
import cv2


class DemoQtPython:
    def __init__(self):
        self.default_model_path = "model.pth"
        self.label = []

    def train(self, epochs, img_path):
        for epoch in range(epochs):
            localtime = time.asctime( time.localtime(time.time()) )
            time.sleep(1)
            message = "{}: {}".format(localtime, epoch)
            SENDToQt(message)

    def visualize(self, img_path):
        img_mat = cv2.imread(img_path)
        result_mat = cv2.flip(img_mat, 1)
        SENDToQt(result_mat)

    def visualize_video(self, video_path="0"):
        stop = False
        cap = cv2.VideoCapture(video_path)
        while True:
            ret, frame = cap.read()
            if ret:
                result_mat = cv2.flip(frame, 1)
                SENDToQt(result_mat, wk=100)
                if stop:
                    cap.release()
                    break
            else:
                cap.release()
                break


if __name__ == '__main__':
    demo = DemoQtPython()
    demo.train(20, "dalk")
    demo.visualize("demo/horse.jpg")
    demo.visualize_video("demo/ice.mp4")
