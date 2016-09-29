import msvcrt
import time

import fileoperation

class NavigateBrowse:

    def __init__(self, display):
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

            elif key == 224:  # Special keys (arrows, f keys, ins, del, etc.)
                key = ord(msvcrt.getch())
                if key == 80:  # Down arrow
                    self.display.browse_row += 1
                    self.display.browse_display()
                elif key == 72:  # Up arrow
                    self.display.browse_row -= 1
                    self.display.browse_display()
            time.sleep(.2)


class NavigateEntry:

    def __init__(self, display):
        self.display = display
        self.key_capture()

    def on_enter(self):

        add1 = fileoperation.Add()

        self.display.browse_display()
        self.display.edit_display()
        fileoperation.Edit(self.display.browse_row, add1.fieldnames[self.display.entry_row], "bok")


    def key_capture(self):
        while True:
            key = ord(msvcrt.getch())
            if key == 27:  # ESC
                break

            elif key == 13:  # Enter
                self.on_enter()

            elif key == 224:  # Special keys (arrows, f keys, ins, del, etc.)
                key = ord(msvcrt.getch())
                if key == 80:  # Down arrow
                    self.display.entry_row += 1
                    self.display.browse_display()
                    self.display.full_display()
                elif key == 72:  # Up arrow
                    self.display.entry_row -= 1
                    self.display.browse_display()
                    self.display.full_display()
            time.sleep(.2)
