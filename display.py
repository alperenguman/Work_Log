import os
import sys


class Display:

    def __init__(self):
        self.os = self.which_os()

    @staticmethod
    def which_os():
        if sys.platform == 'win32':
            return 'Windows'
        else:
            return 'Unix'

    def clear(self):
        if self.os == 'windows':
            os.system("cls")
        else:
            os.system("clear")

    def add_or_browse(self):
        self.clear()
        response = input("Welcome to Work Log!\n\n"
                         "[  MAIN MENU  ]\n\n"
                         "[A]dd entry\n"
                         "[B]rowse entries\n"
                         "[Q]uit program\n\n"
                         ": ")
        if response.lower() == 'a':
            pass
        elif response.lower() == 'b':
            pass
        else:
            display.Display.clear()
            print("Please press 'A' to add or 'B' to browse")