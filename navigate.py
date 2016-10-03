import msvcrt
import time

import fileoperation

class NavigateMain:

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

    def key_capture(self):

        while True:
            key = ord(msvcrt.getch())
            if key == 27:  # ESC
                break

            elif key == 13:  # Enter
                self.on_enter()

            elif key == 13:  # Enter
                self.on_enter()

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
                    response = input("\n\n  Are you sure you want to delete this entry?\n"
                                     "  [Y]es or any other key for no:  ")
                    if response.lower() == 'y':
                        fileoperation.Delete(self.display.browse_row+1)
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
