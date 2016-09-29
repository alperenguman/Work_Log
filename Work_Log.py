import datetime
import pytz
import csv
import os
import sys
import msvcrt
import threading
import time

import fileoperation
import display
import navigate

# Add a new entry or lookup previous entries


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
    display1 = display.Display()
    display1.add_or_browse()
    display1.browse_display()
    nav1 = navigate.NavigateBrowse(display1)
