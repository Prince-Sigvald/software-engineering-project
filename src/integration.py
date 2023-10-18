from image_processor import ImageProcessor
from image_visualizer import ImageVisualizer
from camera import Camera
from data_logger import data_logger
import cv2
import numpy as np
import os

class Integration:
    def run():
        # Call Camera
        my_camera = Camera(camera_index=0)
        my_camera.camera_open()
        last_frame = cv2.cvtColor(my_camera.get_frame(), cv2.COLOR_BGR2GRAY)

        # Output
        current_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        output_folder = os.path.join(current_directory, 'output')

        while True:
            frame = my_camera.get_frame()

            # Call Image Processor
            image_processor = ImageProcessor(frame)
            image_processor.convert_to_grayscale()
            image_processor.picture_binary()
            image_processor.find_edges()
            image_processor.find_contours()
            image_processor.color_detection()

            # Call Visualizer
            image_visualizer = ImageVisualizer(image_processor)

            image_visualizer.draw_frame()
            image_visualizer.draw_label()
            image_visualizer.show_frame()

            # Camera quit with 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            # Data Logger
            if np.sum(np.abs(image_processor.gray_image-last_frame)) <= 1000:
                for shape, color in image_processor.shapes_and_colors:
                    if (shape != None and color != None):
                        data=data_logger(shape, color)
                        data.timestamp()
                        output_path = os.path.join(output_folder, "data_log.csv")
                        data.csv_save(output_path)
            
            last_frame = image_processor.gray_image
