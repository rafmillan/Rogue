import curses
import time
import random
import sys
from Player import player
from Board import room, roomSizes

if __name__ == "__main__":
	def setCurses(stdscr):
		curses.curs_set(1)
		curses.noecho()
		curses.cbreak()
		stdscr.keypad(True)

	def main(stdscr):
		setCurses(stdscr)
		h, w = stdscr.getmaxyx()
		p1 = player('raf', 10)

		if len(sys.argv) > 1:
			seed = int(sys.argv[1])


		random.seed(seed)
		roomSizeIdx = random.randrange(0, len(roomSizes))

		r1 = room(roomSizes[roomSizeIdx], stdscr)
		running = True
		while running:

			stdscr.addstr(h-1, int(w/2), '           ') 
			stdscr.addstr(h-1, int(w/2), '(%i, %i)' % (p1.getX(), p1.getY())) 
			r1.makeRoom()


			stdscr.move(p1.y, p1.x)
			key = stdscr.getch()

			if key == curses.KEY_UP:
				if p1.y == 0:
					p1.y = 0
				else:
					p1.y -= 1

			elif key == curses.KEY_DOWN:
				if p1.y == h-1:
					p1.y = p1.y
				else:
					p1.y += 1

			elif key == curses.KEY_LEFT:
				if p1.x == 0:
					p1.x = 0
				else:
					p1.x -= 1

			elif key == curses.KEY_RIGHT:
				if p1.x == w-1:
					p1.x = p1.x
				else:
					p1.x += 1

			elif key == ord('q') or key == ord('Q'):
				exit()


			r1.update(p1)
			stdscr.refresh()


	curses.wrapper(main)


