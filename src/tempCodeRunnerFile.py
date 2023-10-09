    def color_detection(self):
        # Hier wird die Farberkennung implementiert.
        hsv_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)

        # Farbschwellenwerte für die verschiedenen Farben
        color_thresholds = {
            "Red": ([0, 100, 100], [10, 255, 255]),
            "Green": ([40, 100, 100], [80, 255, 255]),
            "Blue": ([100, 100, 100], [140, 255, 255]),
            "Yellow": ([20, 100, 100], [30, 255, 255]),
            "Violet": ([120, 100, 100], [140, 255, 255]),
        }

        for contour in self.contours:
            area = cv2.contourArea(contour)
            if area > 100:  # Filtere kleine Konturen aus
                # Berechne den Durchschnitt der x- und y-Koordinaten der Konturpunkte
                M = cv2.moments(contour)
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])

                # Überprüfe für jede Farbe, ob sie im Mittelpunkt der Kontur vorhanden ist
                color_found = False
                for color, (lower, upper) in color_thresholds.items():
                    pixel_color = hsv_image[cy, cx]
                    if all(lower <= pixel_color <= upper):
                        self.shapes_and_colors.append((self.shape_detection(index=self.contours.index(contour)), color))
                        color_found = True
                        break

                # Falls keine passende Farbe gefunden wurde, füge None ein
                if not color_found:
                    self.shapes_and_colors.append((self.shape_detection(index=self.contours.index(contour)), None))