from datetime import datetime
import csv

class data_logger:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

    def timestamp(self):
        now = datetime.now()
        self.date = now.strftime("%Y-%m-%d %H:%M:%S")

    def csv_save(self, file_path):
        # Check if the file is existing, if not build it and make the titles.
        try:
            with open(file_path, mode='x', newline='') as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=',')
                csv_writer.writerow(['Datum/Uhrzeit', 'Form', 'Farbe'])
        except FileExistsError:
            pass

        # Add the current data, with each attribute in its own column
        with open(file_path, mode='a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerow([self.date, self.shape, self.color])