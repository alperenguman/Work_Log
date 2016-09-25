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
            print(add.csvfile_name)
            temp_dict = {}
            for field in add.fieldnames:
                if field == 'Entry Time':
                    temp_dict[field] = self.timestamp_now()
                else:
                    value = input("{}: ".format(field))
                    temp_dict[field] = value
            print(temp_dict)
            print(add.writer)
            add.entry(**temp_dict)

        elif response.lower() == 'b':
            pass
        else:
            self.clear()
            print("Please press 'A' to add or 'B' to browse")

    def browse_display(self):

        browse = fileoperation.Browse()
        print('  '+"_"*96)
        heading = (' '*5+'|'+' '*5).join(browse.fieldnames)
        print(" ", end='')
        print('|'+'\033[1;37;41m'+' '*5+heading+' '*5+'\033[0m'+'|')
        print(' ' * 2 + "\033[1;37;40m" + '=' * 96 + "\033[0m")
        heading_width = []
        for name in browse.fieldnames:
            heading_width.append(len(name)+11)
        for row in browse.reader:
            n = 0
            for value in browse.fieldnames:
                if value == browse.fieldnames[0]:
                    print(' '+"\033[1;37;40m"+'|'+"\033[0m", end='')
                print("\033[0;32;40m"+row[value]+"\033[0m"+' '*((10+len(value))-(len(row[value]))) +
                      "\033[1;37;40m"+'|'+"\033[0m", end='')

                if n % (len(browse.fieldnames)-1) == 0 and n != 0:
                    print('\n', end='')
                n += 1


