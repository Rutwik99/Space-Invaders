from unicurses import *


gcn = 1


def make_color(foreground, background):
    global gcn
    cn = gcn
    init_pair(cn, foreground, background)
    gcn += 1
    return cn
