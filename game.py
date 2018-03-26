from unicurses import *
from player import *
from aliens import *
import threading
from functions import *
from missile import *
from score import *


def make_updates():
    update_panels()
    doupdate()


def update_score(scoreboard):
    wmove(scoreboard.window, 0, 0)
    waddstr(scoreboard.window, 'Score: ' + str(scoreboard.val),
            color_pair(scoreboard.color) + scoreboard.attribute)


def delete_alien(alien_list):
    if len(alien_list) == 0:
        return
    del alien_list[0]
    make_updates()


def move_missile(missile_type, num, ind, alien_ls, scoreboard):
    if missile_type[ind].y - num < missile_type[ind].min_y+1:
        del missile_type[ind].panel
        make_updates()
        return

    missile_type[ind].y -= num
    move_panel(missile_type[ind].panel, missile_type[ind].y,
               missile_type[ind].x)

    # if num == 1:
    #     for i in range(len(alien_ls)):
    #         if (missile_type[ind].x == alien_ls[i].x and
    #             missile_type[ind].y == alien_ls[i].y):
    #             del alien_ls[i]
    #             scoreboard.val += 1
    #             update_score(scoreboard)
    #         if i+1 < len(alien_ls)
    #    tem = len(alien_ls)
    #   for i in range()
    if num == 1:
        for i in alien_ls[:]:
            if missile_type[ind].x == i.x and missile_type[ind].y == i.y:
                alien_ls.remove(i)
                make_updates()
                scoreboard.val += 1
                update_score(scoreboard)

    if num == 2:
        for i in range(len(alien_ls)):
            if (missile_type[ind].x == alien_ls[i].x and
                missile_type[ind].y == alien_ls[i].y) or (
                    missile_type[ind].x == alien_ls[i].x and
                    missile_type[ind].y + 1 == alien_ls[i].y):
                alien_ls[i].th_id.cancel()
                alien_ls[i].th_id = threading.Timer(5, delete_alien,
                	                                [alien_ls])
                alien_ls[i].th_id.daemon = True
                alien_ls[i].th_id.start()
                waddstr(alien_ls[i].window_alien, 'a',
                        color_pair(alien_ls[i].color))

    make_updates()
    temp = threading.Timer(1, move_missile,
                           [missile_type, num, ind, alien_ls, scoreboard])
    temp.daemon = True
    temp.start()


def insert_alien(s, board_x, board_y):
    th_id = threading.Timer(8, delete_alien, [s])
    th_id.daemon = True
    s.insert(0, alien('@', board_x, board_y, th_id, COLOR_RED, COLOR_BLACK))
    make_updates()

    s[0].th_id.start()

    ct = threading.Timer(10, insert_alien, [s, board_x, board_y])
    ct.daemon = True
    ct.start()


def main():
    stdscr = initscr()
    use_default_colors()
    start_color()
    noecho()
    curs_set(False)
    keypad(stdscr, True)
    fiy, fix = getmaxyx(stdscr)
    board_x = int(fix / 2) - 5
    board_y = int(fiy / 2) - 5

    board = newwin(10, 10, board_y, board_x)

    box(board)
    panel_game = new_panel(board)

    scoreboard = score('Score: 0', board_x, board_y)

    oplayer = Player(stdscr, '🛦', board_x, board_y, COLOR_YELLOW, COLOR_BLACK)
    top_panel(oplayer.panel)

    ialien = []
    insert_alien(ialien, board_x, board_y)

    fis_mis_list = []
    sec_mis_list = []
    fis_mis_timer = []

    while True:
        key = getch()
        if key == 113:
            break

        if key == 32:
            fis_mis_list.append(first_missile('i', oplayer.x, oplayer.y,
                                COLOR_BLUE, COLOR_BLACK))
            temp = threading.Timer(1, move_missile,
                                   [fis_mis_list, 1, len(fis_mis_list) - 1,
                                    ialien, scoreboard])
            temp.daemon = True
            temp.start()

        elif key == 115:
            sec_mis_list.append(second_missile('l', oplayer.x, oplayer.y,
                                               COLOR_CYAN, COLOR_BLACK))
            temp = threading.Timer(1, move_missile,
                                   [sec_mis_list, 2, len(sec_mis_list)-1,
                                    ialien, scoreboard])
            temp.daemon = True
            temp.start()

        else:
            oplayer.move(key)
        update_panels()
        doupdate()

    endwin()
    return 0


main()
