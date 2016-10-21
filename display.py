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
        self.search_input = []

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
            print("\n")
            print(" "*2+self.timestamp_now()+"\n\n")
            temp_dict = {}
            for field in add.fieldnames:
                if field == 'Entry Time':
                    temp_dict[field] = self.timestamp_now()
                elif field == 'Date':
                    print("  " + "Please enter the" + "\033[1;32;40m" + " date " + "\033[0m" +
                          "in MM-DD-YYYY format.\n\n"

                          "  Please enter the" + "\033[1;32;40m" + " duration " + "\033[0m"
                          "in 5 mins/hours/days etc. format\n"
                          "  Alternatively, you can specify the time range i.e. 5:06pm - 6:07am")
                    value = input("\n" + " "*2 + "{}: ".format(field))
                    temp_dict[field] = value
                else:
                    value = input(" " * 2 + "{}: ".format(field))
                    temp_dict[field] = value
            print(temp_dict)
            print(add.writer)
            add.entry(**temp_dict)

        elif response.lower() == 'b':
            pass
        else:
            self.clear()
            print("Please press 'A' to add or 'B' to browse")

    def browse_display(self, *args):
        self.clear()

        try:
            dicts_list = args[0]

        except IndexError:
            pass

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

        try:
            for row in dicts_list:
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

        except UnboundLocalError:
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

        print("\n" + " "*15 + "Use arrow keys to navigate, ENTER to select, DEL to delete entry,\n"
              + " "*24 + "S to bring up search and ESC to quit browsing.")

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
                string = ''.join(self.search_input)
                print("\n\n" + " " * 52 + "^")
                print(" " * 40 + "Search by " + "\033[0;32;41m" + self.search_types[self.search_select] +
                      "\033[0m" + ":  " + "|" + "\033[4;37;40m" + string +
                      "_"*(44-len(self.search_types[self.search_select])-len(string)) + "\033[0m" + "|")
                print(" " * 52 + "v")
            elif args[0] == 1:
                try:
                    if args[1] == "backspace":
                        self.search_input.pop()
                    else:
                        self.search_input.append(args[1])
                    string = ''.join(self.search_input)
                    print("\n\n\n" + " " * 40 + "Search by " + "\033[0;32;40m" +
                          self.search_types[self.search_select] + "\033[0m" + ":  " +
                          "|" + "\033[4;37;41m" + string +
                          "_"*(44-len(self.search_types[self.search_select])-len(string))
                          + "\033[0m" + "|")
                except IndexError:
                    string = ''.join(self.search_input)
                    print("\n\n\n" + " " * 40 + "Search by " + "\033[0;32;40m" +
                          self.search_types[self.search_select] + "\033[0m" + ":  " +
                          "|" + "\033[4;37;41m" + string + "_" * (
                          44 - len(self.search_types[self.search_select]) - len(string))
                          + "\033[0m" + "|")

        except IndexError:
            pass
