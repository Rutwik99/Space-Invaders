from functions import *
from unicurses import *


class missile:
    def __init__(self, foreground=None, background=None, attribute=0):
        self.min_y = self.y - 7

        self.window_missile = newwin(1, 1, self.y, self.x)

        box(self.window_missile)
        waddstr(self.window_missile, self.body)
        self.panel = new_panel(self.window_missile)

        self.attribute = attribute
        self.show_changes()
        if foreground is not None and background is not None:
            self.set_colors(foreground, background)
            self.show_changes()

    def set_colors(self, foreground, background):
        self.color = make_color(foreground, background)
        self.foreground = foreground
        self.background = background
        waddstr(self.window_missile, self.body, color_pair(self.color))

        self.show_changes()

    def show_changes(self):
        update_panels()
        doupdate()


class first_missile(missile):
    def __init__(self, body, player_x, player_y,
                 foreground=None, background=None, attribute=0):
        self.body = body
        self.x = player_x
        self.y = player_y - 1

        missile.__init__(self, foreground, background, attribute)


class second_missile(missile):

    def __init__(self, body, player_x, player_y,
                 foreground=None, background=None, attribute=0):
        self.body = body
        self.x = player_x
        self.y = player_y - 1

        missile.__init__(self, foreground, background, attribute)
