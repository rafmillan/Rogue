import curses
import time
import random
import sys
from Player import player
from Board import board, room, roomSizes

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
		b = board(1)

		if len(sys.argv) > 1:
			seed = int(sys.argv[1])
		else: seed = ''

		random.seed()
		roomSizeIdx = random.randrange(0, len(roomSizes))

		random.seed()
		numRooms = random.randrange(1, 6)
		for i in range(0,  numRooms):
			random.seed()
			roomSizeIdx = random.randrange(0, len(roomSizes))

			originX = random.randrange(0, w - 20)
			originY = random.randrange(0, h - 15)
			origin = (originX, originY)
			b.addRoom(room(roomSizes[roomSizeIdx], stdscr, origin))

		running = True
		while running:

			stdscr.addstr(h-1, int(w/2), '           ') 
			stdscr.addstr(h-1, int(w/2), '(%i, %i)' % (p1.getX(), p1.getY())) 
			stdscr.addstr(h-1, 1, '        ') 
			stdscr.addstr(h-1, 1, 'Health: %i' % (p1.getHealth()))
			stdscr.addstr(h-1, w-10, '        ') 
			stdscr.addstr(h-1, w-10, 'Rooms: %i' % (b.getNumRooms()))
			
			b.printBoard()

			stdscr.move(p1.y, p1.x)
			key = stdscr.getch()

			if key == curses.KEY_UP:
				if p1.y == 0:
					p1.y = 0
				else:
					p1.y -= 1

			elif key == curses.KEY_DOWN:
				if p1.y == h-2:
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


			b.updateRooms(p1)
			stdscr.refresh()

	curses.wrapper(main)


