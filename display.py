import os
import sys
import datetime
import csv

import fileoperation


class Display:

    @staticmethod
    def clear():
        if sys.platform == 'win32':
            os.system("cls")
        else:
            os.system("clear")

    @staticmethod
    def timestamp_now():
        now = datetime.datetime.now()
        string_format = "%Y-%m-%d %H:%M:%S"
        return now.strftime(format=string_format)

    def add_or_browse(self):
        self.clear()
        response = input("Welcome to Work Log!\n\n"
                         "[  MAIN MENU  ]\n\n"
                         "[A]dd entry\n"
                         "[B]rowse entries\n"
                         "[Q]uit program\n\n"
                         ": ")
        if response.lower() == 'a':
            add = fileoperation.Add()
            self.clear()
            print(self.timestamp_now()+"\n")
            temp_dict = {}
            for field in add.fieldnames:
                if field == 'Entry Time':
                    temp_dict[field] = self.timestamp_now()
                else:
                    value = input("{}: ".format(field))
                    temp_dict[field] = value
            add.entry(**temp_dict)

        elif response.lower() == 'b':
            pass
        else:
            self.clear()
            print("Please press 'A' to add or 'B' to browse")

    def browse_display(self):

        add = fileoperation.Add()
        print(' '+"_"*96)
        heading = (' '*5+'|'+' '*5).join(add.fieldnames)
        print('|'+'\033[0;41m'+' '*5+heading+' '*5+'\033[0m'+'|')
        print(' '+"=" * 96)
        path = os.path.dirname(__file__)
        with open(path + '/worklog.csv', mode='r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                n = 0
                for value in add.fieldnames:
                    print(' '*2 + row[value]+' '*10, end='')

                    if n % 4 == 0 and n != 0:
                        print('\n', end='')
                    n += 1


