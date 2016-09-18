import datetime
import pytz
import csv
import os
import sys
import fileoperation

# Add a new entry or lookup previous entries


def clear():
    if sys.platform == 'win32':
        os.system("cls")
    else:
        os.system("clear")


def add_or_browse():
    clear()
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
        clear()
        print("Please press 'A' to add or 'B' to browse")

# If adding a new entry:
    # Record into CSV file with timestamp
    # Ask for a task name
    # Ask for number of minutes spent on task
    # Ask for notes about task

# If looking up previous entries:
    # Navigate through results of search
    # find by date
        # within a range of dates
        # See a list of entries and choose among them.
    # find by time spent
        # within a range of time spent
    # find by exact search
        # Present entries that contain exact string in task name or description
    # find by pattern
        # Regex input task name or notes

# Delete or Edit entries
# Quit the script from menu

if __name__ == '__main__':
    add_or_browse()
    a = fileoperation.FileOperation()