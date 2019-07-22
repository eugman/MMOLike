import curses
import time

screen = curses.initscr()
height, width = screen.getmaxyx()
win = curses.newwin(height, width, 0, 0)

win.keypad(1)
curses.curs_set(0)

player = [10,10]
mob = [20,20]

win.addch(player[0], player[1], curses.ACS_DIAMOND)
key = curses.KEY_RIGHT

while True:
        win.border(0)
        win.timeout(100)

        next_key = win.getch()

        if next_key == -1:
            key = key
        else:
            key = next_key

        if key == curses.KEY_LEFT:
            player[0] -= 1
        win.addch(player[0], player[1], curses.ACS_DIAMOND)
