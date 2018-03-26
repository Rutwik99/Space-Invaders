from unicurses import *
from functions import *


class Player:
    def __init__(self, stdscr, body, fix, fiy,
                 foreground=None, background=None, attribute=0):
        self.min_x = fix + 1
        self.min_y = fiy + 1
        self.max_x = fix + 8
        self.max_y = fiy + 8

        self.x = self.min_x + 3
        self.y = self.max_y
        self.body = body
        del stdscr
        self.window_player = newwin(1, 1, self.y, self.x)
        waddstr = (self.window_player, self.body)
        self.panel = new_panel(self.window_player)
        self.foreground = foreground
        self.background = background
        self.color = 0
        self.attribute = attribute

        if foreground is not None and background is not None:
            self.set_colors(foreground, background)

        self.show_changes()

    def move(self, k):
        moved = False
        if k == 97 or k == KEY_LEFT:
            if not self.x - 1 < self.min_x:
                moved = True
                self.x -= 1

        if k == 100 or k == KEY_RIGHT:
            if not self.x + 1 > self.max_x:
                moved = True
                self.x += 1

        if moved:
            move_panel(self.panel, self.y, self.x)
            self.show_changes()

    def set_colors(self, foreground, background):
        self.color = make_color(foreground, background)
        self.foreground = foreground
        self.background = background
        waddstr(self.window_player, self.body,
                color_pair(self.color) + self.attribute)
        self.show_changes()

    def show_changes(self):
        update_panels()
        doupdate()
