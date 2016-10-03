import os
import sys
import datetime
import csv
import msvcrt
import time
import subprocess

import fileoperation
import threading


class Display:

    def __init__(self):
        self.browse_row = 0
        self.entry_row = 0
        self.search_select = 0
        self.search_types = ["date", "exact string", "time spent", "pattern"]

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
        self.clear()
        browse = fileoperation.Browse()
        print('  '+"_"*96)
        heading = (' '*5+'|'+' '*5).join(browse.fieldnames)
        print(" ", end='')
        print('|'+'\033[1;37;41m'+' '*5+heading+' '*5+'\033[0m'+'|')
        print(' ' * 2 + "\033[1;37;40m" + '=' * 96 + "\033[0m")
        heading_width = []

        for name in browse.fieldnames:
            heading_width.append(len(name)+11)
            m = 0
            for row in browse.reader:
                n = 0

                if self.browse_row == m:
                    for value in browse.fieldnames:
                        if value == browse.fieldnames[0]:
                            print(' ' + "\033[1;37;40m" + '|' + "\033[0m", end='')
                        print("\033[0;32;41m" + row[value] + ' ' * ((10 + len(value)) - (len(row[value]))) + "\033[0m" +
                              "\033[1;37;40m" + '|' + "\033[0m", end='')
                        if n % (len(browse.fieldnames) - 1) == 0 and n != 0:
                            print('\n', end='')
                        n += 1
                    m += 1
                    continue

                for value in browse.fieldnames:

                    if value == browse.fieldnames[0]:
                        print(' ' + "\033[1;37;40m" + '|' + "\033[0m", end='')
                    print("\033[0;32;40m" + row[value] + "\033[0m" + ' ' * ((10 + len(value)) - (len(row[value]))) +
                          "\033[1;37;40m" + '|' + "\033[0m", end='')

                    if n % (len(browse.fieldnames)-1) == 0 and n != 0:
                        print('\n', end='')
                    n += 1
                m += 1
        print("\n" + " "*4 + "Use arrow keys to navigate, ENTER to select,"
                             " S to bring up search and ESC to quit browsing.")

    def full_display(self, *args):

        try:
            hl_color = str(args[0])
        except IndexError:
            hl_color = str(41)

        browse = fileoperation.Browse()
        entries_list = []
        display_list = []
        for row in browse.reader:
            entries_list.append(row)
        m = 0
        for title in browse.fieldnames:
            if m == self.entry_row:
                display_list.append(' '*2 + title + ': ' + "\033[0;32;"+hl_color+"m" +
                                    entries_list[self.browse_row][title] + "\033[0m" + '\n')
            else:
                display_list.append(' ' * 2 + title + ': ' + "\033[0;32;40m" +
                                    entries_list[self.browse_row][title] + "\033[0m" + '\n')
            m += 1
        a = ''.join(display_list)
        print('\n\n' + a)

    def search_display(self, *args):
        try:
            if args[0] == 0:
                print("\n\n" + " " * 62 + "^")
                print(" " * 50 + "Search by " + "\033[0;37;41m" + self.search_types[self.search_select] +
                      "\033[0m" + ":  " + "|______________________________|")
                print(" " * 62 + "v")
            elif args[0] == 1:
                print("\n\n\n" + " " * 50 + "Search by " + self.search_types[self.search_select] + ":  " +
                      "|" + "\033[0;37;41m" + "______________________________" + "\033[0m" + "|")
                try:
                    temp_list = []
                    temp_list.append(args[1])
                    string = ''.join(temp_list)
                    print("\n\n\n" + " " * 50 + "Search by " + self.search_types[self.search_select] + ":  " +
                          "|" + "\033[4;37;41m" + string + "_"*(30-len(string)) + + "\033[0m" + "|")
                except IndexError:
                    pass
        except IndexError:
            pass
