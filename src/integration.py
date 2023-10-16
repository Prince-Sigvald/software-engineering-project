from image_processor import ImageProcessor
from image_visualizer import ImageVisualizer
from camera import Camera
from data_logger import data_logger
import cv2

class Integration:
    def run():
        # Call Camera
        my_camera = Camera(camera_index=0)
        my_camera.camera_open()

        frame = my_camera.get_frame()
        if frame is not None:
            cv2.imshow("frame", frame)
            cv2.waitKey(0)
        
        my_camera.camera_close()
        
        # Call Image Processor
        input_image = cv2.imread('C:/Users/Tim/Desktop/Weihnachten/sample_image.JPG', cv2.IMREAD_COLOR)  # Laden Sie hier Ihr Bild.
        image_processor = ImageProcessor(input_image)

        image_processor.convert_to_grayscale()
        image_processor.picture_binary()
        image_processor.find_edges()
        image_processor.find_contours()
        image_processor.color_detection()

        # print the forms and colors
        if 1:
            for shape, color in image_processor.shapes_and_colors:
                print(f"Shape: {shape}, Color: {color}")

        print(len(image_processor.contours))
        cv2.imshow("original",image_processor.image)
        cv2.imshow("binary",image_processor.binary_image)
        cv2.imshow("edges",image_processor.edges)

        cv2.waitKey(0)

        # Call Visualizer
        image_visualizer = ImageVisualizer(image_processor)

        image_visualizer.draw_frame()
        image_visualizer.draw_label()
        image_visualizer.show_frame()

        if 1:
            for shape, color in image_processor.shapes_and_colors:
                data=data_logger(shape, color)
                data.timestamp()
                data.csv_save("C:/AA_Studium/Unterlagen/Semester_5/Software_Engineering/software-engineering-project-yan-tim/output/data_log.csv")
        print("Finished")