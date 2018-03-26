from unicurses import *
from random import *
from functions import *


class alien:
    def __init__(self, body, fix, fiy, th_id,
                 foreground=None, background=None, attribute=0):
        self.x = randrange(fix+1, fix+9)
        self.y = randrange(fiy+1, fiy+3)
        self.th_id = th_id
        self.window_alien = newwin(1, 1, self.y, self.x)
        self.body = body
        waddstr(self.window_alien, self.body)
        self.panel = new_panel(self.window_alien)

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
        waddstr(self.window_alien, self.body,
                color_pair(self.color) + self.attribute)
        self.show_changes()

    def show_changes(self):
        update_panels()
        doupdate()
