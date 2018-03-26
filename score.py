from unicurses import *


class score:
    def __init__(self, body, board_x, board_y,
                 foreground=None, background=None, attribute=0):
        self.x = board_x
        self.y = board_y - 1
        self.body = body
        self.val = 0
        self.window = newwin(1, 10, self.y, self.x)
        waddstr(self.window, self.body)
        self.panel = new_panel(self.window)
        self.foreground = foreground
        self.background = background
        self.color = 0
        self.attribute = attribute

        if foreground is not None and background is not None:
            self.set_colors(foreground, background)
        self.show_changes()

    def set_colors(self, foreground, background):
        self.color = make_color(foreground, background)
        self.foreground = foreground
        self.background = background
        waddstr(self.window, self.body,
                color_pair(self.color) + self.attribute)
        self.show_changes()

    def show_changes(self):
        update_panels()
        doupdate()
