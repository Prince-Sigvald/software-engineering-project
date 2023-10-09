import cv2

class Camera:
    def __init__(self, camera_index=0):
        self.cap = cv2.VideoCapture(camera_index)

    def camera_open(self):
        if not self.cap.isOpened():
            self.cap.open()

        if self.cap.isOpened():
            print("Kamera wurde geöffnet.")
        else:
            print("Fehler beim Öffnen der Kamera.")

    def camera_close(self):
        if self.cap.isOpened():
            self.cap.release()
            print("Kamera wurde geschlossen.")
        else:
            print("Die Kamera ist nicht geöffnet.")

    def get_frame(self):
        ret, frame = self.cap.read()
        if ret:
            return frame
        else:
            print("Fehler beim Lesen des Bildes von der Kamera.")
            return None

# Exampe usage:
my_camera = Camera(camera_index=1)
my_camera.camera_open()

frame = my_camera.get_frame()
cv2.imshow("frame", frame)
cv2.waitKey(0)


my_camera.camera_close()