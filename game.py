import curses
import time
import entity

screen = curses.initscr()
curses.noecho() #turn off echoing input
curses.cbreak() #don't wait for enter key

height, width = screen.getmaxyx()
win = curses.newwin(height, width, 0, 0)

win.keypad(1)
curses.curs_set(0) #Hide the blinking cursor

player = Entity(10, 10, ord('@')
mob = [20,20]

win.addch(player[0], player[1], curses.ACS_DIAMOND)
key = curses.KEY_RIGHT

while True:
    win.border(0)
    win.timeout(100)

    key = win.getch()
    win.

    if key == ord('q'):
        curses.nocbreak()
        screen.keypad(False)
        curses.echo()
        curses.endwin()
        break;

    if key == curses.KEY_LEFT:
        player.move(0, -1)

    if key == curses.KEY_RIGHT:
        player.move(0, 1)

    if key == curses.KEY_UP:
        player.move(-1, 0)

    if key == curses.KEY_DOWN:
        player.move(1, 0)

    key = -1
   
    player.draw(win)
