import msvcrt
import time
import threading

import fileoperation

class NavigateBrowse:

    def __init__(self, display):
        self.file = fileoperation.Browse()
        self.total_entries = self.file.get_total_entries()
        self.display = display
        self.key_capture()

    def on_enter(self):
        self.display.browse_display()
        self.display.full_display()
        nav2 = NavigateEntry(self.display)

    def search(self):
        type_or_input = 0
        key = ord(msvcrt.getch())
        if key == 27:  # ESC
            return "stop"

        elif key == 224:
            key = ord(msvcrt.getch())

            if type_or_input == 0 and self.display.search_select != 0 and key == 72:  # Up arrow
                self.display.browse_display()
                self.display.search_select -= 1
                self.display.search_display(type_or_input)

            elif type_or_input == 0 and self.display.search_select < len(self.display.search_types)-1 and \
                    key == 80:  # Down arrow

                self.display.search_select += 1
                self.display.browse_display()
                self.display.search_display(type_or_input)

            elif key == 75:
                type_or_input = 0
                self.display.browse_display()
                self.display.search_display(type_or_input)

            elif key == 77:
                type_or_input = 1
                self.display.browse_display()
                self.display.search_display(type_or_input)

    def key_capture(self):

        while True:
            key = ord(msvcrt.getch())
            if key == 27:  # ESC
                break

            elif key == 13:  # Enter
                self.on_enter()

            elif key == 115:  # S
                self.display.browse_display()
                self.display.search_display(0)
                while True:
                    if self.search() == "stop":
                        self.display.browse_display()
                        break

            elif key == 224:  # Special keys (arrows, f keys, ins, del, etc.)
                key = ord(msvcrt.getch())
                if key == 80 and self.display.browse_row != self.total_entries-1:  # Down arrow
                    self.display.browse_row += 1
                    self.display.browse_display()
                    print(self.display.browse_row)
                elif key == 72 and self.display.browse_row != 0:  # Up arrow
                    self.display.browse_row -= 1
                    self.display.browse_display()
                    print(self.display.browse_row)

                elif key == 83:  # Del
                    self.display.browse_display()
                    print("\n\n  Are you sure you want to delete this entry?\n"
                          "  [Y]es or any other key for no:  ", end='')
                    key = ord(msvcrt.getch())
                    if key == 121:
                        fileoperation.Delete(self.display.browse_row + 1)
                    self.display.browse_display()
            time.sleep(.2)


class NavigateEntry:

    def __init__(self, display):
        self.display = display
        self.display.entry_row = 1
        self.display.browse_display()
        self.display.full_display()
        self.key_capture()

    def on_enter(self):

        add1 = fileoperation.Add()

        self.display.browse_display()
        self.display.full_display(44)
        value = input("  Please enter new value: ")
        fileoperation.Edit(self.display.browse_row, add1.fieldnames[self.display.entry_row], value)
        self.display.browse_display()
        self.display.full_display()

    def key_capture(self):
        file = fileoperation.FileOperation()
        while True:
            key = ord(msvcrt.getch())
            if key == 27:  # ESC
                self.display.browse_display()
                break

            elif key == 13:  # Enter
                self.on_enter()

            elif key == 224:  # Special keys (arrows, f keys, ins, del, etc.)
                key = ord(msvcrt.getch())
                if key == 80 and self.display.entry_row != len(file.fieldnames)-1:  # Down arrow
                    self.display.entry_row += 1
                    self.display.browse_display()
                    self.display.full_display()
                elif key == 72 and self.display.entry_row != 1:  # Up arrow
                    self.display.entry_row -= 1
                    self.display.browse_display()
                    self.display.full_display()
            time.sleep(.2)
