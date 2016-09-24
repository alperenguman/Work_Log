import csv
import os
import sys
import datetime
import pdb

import display


class FileOperation:

    def __init__(self):
        if sys.platform == 'win32':
            self.csvfile_name = os.path.dirname(__file__)+'/worklog.csv'
        else:
            self.csvfile_name = 'worklog.csv'

        self.csvfile_mode = 'a+'
        self.csvfile = open(self.csvfile_name, mode=self.csvfile_mode, newline='')

        self.fieldnames = ['Entry Time', 'Date', 'Task Name', 'Duration', 'Description']
        self.reader = csv.DictReader(self.csvfile)
        self.writer = csv.DictWriter(self.csvfile, fieldnames=self.fieldnames)


class Add(FileOperation):

    def __init__(self):
        display.Display.clear()
        FileOperation.__init__(self)

        l = []
        with open('worklog.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                l.append(row)
        try:
            if l[0] == self.fieldnames[0]:
                self.writer.writeheader()
        except IndexError:
            self.writer.writeheader()

    def entry(self, **kwargs):
        temp_dict = {}
        for key, value in kwargs.items():
            temp_dict[key] = value
        self.writer.writerow(temp_dict)


class Edit(FileOperation):
    pass


class Delete(FileOperation):
    pass


class Browse(FileOperation):
    def __init__(self):
        display.Display.clear()
        FileOperation.__init__(self)
        self.csvfile_mode = 'r'
        self.csvfile = open(self.csvfile_name, mode=self.csvfile_mode, newline='')
        self.reader = csv.DictReader(self.csvfile)