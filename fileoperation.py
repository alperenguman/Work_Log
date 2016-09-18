import csv
import display
import datetime
import pdb


class FileOperation:

    def __init__(self):
        self.csvfile_name = 'worklog.csv'
        self.csvfile_mode = 'a'
        self.csvfile = open(self.csvfile_name, mode=self.csvfile_mode)


class Add(FileOperation):

    def __init__(self):

        display.Display.clear()

        self.fieldnames = ['Date', 'Task Name', 'Duration', 'Description']
        self.add = csv.DictWriter(self.csvfile, fieldnames=self.fieldnames)
        self.add.writeheader()
        self.add.writerow({'Date': 'Baked', 'Task Name': 'Beans'})
        self.csvfile.close()


class Edit(FileOperation):
    pass


class Delete(FileOperation):
    pass