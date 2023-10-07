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

    def shape_detection(self,index):
        # Determine forms
        epsilon = 0.04 * cv2.arcLength(self.contours[index], True)
        approx = cv2.approxPolyDP(self.contours[index], epsilon, True)#determine corners

        # In terms of corners determine if its a triangle or rectangle.
        if len(approx) == 3:
            return "Triangle"
        elif len(approx) == 4:
            x, y, w, h = cv2.boundingRect(self.contours[index])
            aspect_ratio = float(w) / h
            if 0.95 <= aspect_ratio <= 1.05:#if ration in certain threshold it will be a square
                return "Square"
            else:
                return "Rectangle"
        elif len(approx) == 5:#adaptioin for pentagon or eben star
            return "Pentagon"
        else:#if there is no corner it must be a circle
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
            area = cv2.contourArea(contour)#amount of pixel in contour
            if area > 100:  # get sure, that we only have big enough areas
                # Determine mean of area and its locatoin
                M = cv2.moments(contour)
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])

                # Überprüfe für jede Farbe, ob sie im Mittelpunkt der Kontur vorhanden ist
                color_found = False
                for color, (lower, upper) in color_thresholds.items():#for example: color:red, lower:[0, 100, 100], upper:[10, 255, 255]
                    pixel_color = hsv_image[cy, cx]#get color in middle
                    if all(np.logical_and(lower <= pixel_color, pixel_color <= upper)):#determine if color is in threshold
                        self.shapes_and_colors.append((self.shape_detection(index=self.contours.index(contour)), color))
                        color_found = True #if color in threshold append array and break out of for loop
                        break

                # if color is not found add a none to shapes_and_colors
                if not color_found:
                    self.shapes_and_colors.append((self.shape_detection(index=self.contours.index(contour)), None))


# esample usage:
input_image = cv2.imread('C:/AA_Studium/Unterlagen/Semester_5/Software_Engineering/software-engineering-project-yan-tim/resources/sample_image.JPG', cv2.IMREAD_COLOR)  # Laden Sie hier Ihr Bild.
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

