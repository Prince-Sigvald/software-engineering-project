import cv2
import numpy as np

class ImageVisualizer:
    def __init__(self, image_processor):
        self.image_processor = image_processor

    def draw_frame(self):
        for contour in self.image_processor.contours:
            # Ignore small areas
            if cv2.contourArea(contour) > 100:
                cv2.drawContours(self.image_processor.image, [contour], -1, (0, 255, 0), 2)  # Draw the contour in green

    # Modify the draw_label method in the ImageVisualizer class
    def draw_label(self):
        for contour in self.image_processor.contours:
            if cv2.contourArea(contour) > 100:
                shape = self.image_processor.shape_detection(contour)
                x, y, _, _ = cv2.boundingRect(contour)
                color = None
                for shape_color_pair in self.image_processor.shapes_and_colors:
                    if shape_color_pair[0] == shape:
                        color = shape_color_pair[1]
                        break
                cv2.putText(self.image_processor.image, f"{color} {shape}", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

    def show_frame(self):
        cv2.imshow('Live Shape and Color Detection', self.image_processor.image)
        cv2.waitKey(0)