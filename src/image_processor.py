import cv2
import numpy as np

class ImageProcessor:
    def __init__(self, image):
        self.image = image
        self.shapes_and_colors = []  #List for forms and colours

    def convert_to_grayscale(self):
        # convert pic into grey image
        self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def picture_binary(self):
        # convert grey image to binary image
        _, self.binary_image = cv2.threshold(self.gray_image, 200, 255, cv2.THRESH_BINARY)

    def find_edges(self):
        # determine edges of binary image
        self.edges = cv2.Canny(self.binary_image, 100, 200)

    def find_contours(self):
        # find contours of edge picture
        self.contours, _ = cv2.findContours(self.edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    def shape_detection(self, contour):
        epsilon = 0.04 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)  # Determine corners

        if len(approx) == 3:
            return "Triangle"
        elif len(approx) == 4:
            x, y, w, h = cv2.boundingRect(contour)
            aspect_ratio = float(w) / h
            if 0.95 <= aspect_ratio <= 1.05:
                return "Square"
            else:
                return "Rectangle"
        elif len(approx) == 5:
            return "Pentagon"
        elif len(approx) >= 8:
            return "Circle"

    def color_detection(self):
        # change image do hsv image.
        hsv_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)

        # Thresholds for colourss
        color_thresholds = {
            "Red": ([0, 100, 100], [10, 255, 255]),
            "Green": ([40, 100, 100], [80, 255, 255]),
            "Blue": ([100, 50, 50], [130, 255, 255]),
            "Yellow": ([20, 100, 100], [30, 255, 255]),
            "Violet": ([120, 50, 50], [140, 255, 255]),
        }

        for contour in self.contours:
            area = cv2.contourArea(contour)  # amount of pixel in contour
            if area > 100:  # ensure that we only have big enough areas
                # Determine mean of area and its location
                M = cv2.moments(contour)
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])

                # Check for each color if it is present at the center of the contour
                color_found = False
                for color, (lower, upper) in color_thresholds.items():
                    pixel_color = hsv_image[cy, cx]  # get color in the middle
                    if all(np.logical_and(lower <= pixel_color, pixel_color <= upper)):
                        # Determine the shape for the current contour
                        shape = self.shape_detection(contour)
                        self.shapes_and_colors.append((shape, color))
                        color_found = True
                        break

                # if color is not found, add None to shapes_and_colors
                if not color_found:
                    shape = self.shape_detection(contour)
                    self.shapes_and_colors.append((shape, None))
