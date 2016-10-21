import csv
import os
import sys
import datetime
import pdb
import msvcrt

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
            if key == 'Date':
                self.datecheck(value)
            elif key == 'Duration':
                self.durationcheck()
            temp_dict[key] = value
        self.writer.writerow(temp_dict)

    def datecheck(self, value):
        pass

    def durationcheck(self):
        pass


class Edit(FileOperation):

    def __init__(self, entry_no, field, value):
        FileOperation.__init__(self)
        self.entry(entry_no, field, value)

    def entry(self, entry_no, field, value):
        self.csvfile_mode = 'r'
        self.csvfile = open(self.csvfile_name, mode=self.csvfile_mode, newline='')
        self.reader = csv.DictReader(self.csvfile, fieldnames=self.fieldnames)
        temp_list = []
        for row in self.reader:  # This appends header as well, hence +1 to row number
            temp_list.append(row)
        temp_list[entry_no+1][field] = value
        self.csvfile_mode = 'w'
        self.csvfile = open(self.csvfile_name, mode=self.csvfile_mode, newline='')
        self.writer = csv.DictWriter(self.csvfile, fieldnames=self.fieldnames)
        for row in temp_list:
            self.writer.writerow(row)


class Delete(FileOperation):
    def __init__(self, entry_no):
        FileOperation.__init__(self)
        self.delete_row(entry_no)

    def delete_row(self, entry_no):
        self.csvfile_mode = 'r'
        self.csvfile = open(self.csvfile_name, mode=self.csvfile_mode, newline='')
        self.reader = csv.DictReader(self.csvfile, fieldnames=self.fieldnames)
        temp_list = []
        for row in self.reader:  # This appends header as well, hence +1 to row number
            temp_list.append(row)
        del temp_list[entry_no+1]
        self.csvfile_mode = 'w'
        self.csvfile = open(self.csvfile_name, mode=self.csvfile_mode, newline='')
        self.writer = csv.DictWriter(self.csvfile, fieldnames=self.fieldnames)
        for row in temp_list:
            self.writer.writerow(row)


class Browse(FileOperation):
    def __init__(self):
        FileOperation.__init__(self)
        self.csvfile_mode = 'r'
        self.csvfile = open(self.csvfile_name, mode=self.csvfile_mode, newline='')
        self.reader = csv.DictReader(self.csvfile)
        self.total_entries = 0

    def get_total_entries(self):
        csvitems = []
        for row in self.reader:
            csvitems.append(row)
        self.total_entries = len(csvitems)
        return self.total_entries

    def get_data(self):
        temp_list = []
        for row in self.reader:
            temp_list.append(row)
        return temp_list

