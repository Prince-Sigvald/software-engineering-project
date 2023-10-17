import cv2

class Camera:
    def __init__(self, camera_index=0):
        self.cap = cv2.VideoCapture(camera_index)

    def camera_open(self):
        if not self.cap.isOpened():
            self.cap.open()

        if self.cap.isOpened():
            print("Camera open.")
        else:
            print("Failure: Camera isn't working.")

    def camera_close(self):
        if self.cap.isOpened():
            self.cap.release()
            print("Camera closed.")
        else:
            print("Camera isn't running.")

    def get_frame(self):
        ret, frame = self.cap.read()
        if ret:
            return frame
        else:
            print("Failure: Reading image from camera.")
            return None