import random
import curses
from Player import player

roomSizes = [ (10,5), (10,7), (10,10), (15, 5), (15,7), (15,10), (20,7), (20,10), (20,15) ]

class room:
	def __init__(self, roomSize, stdscr):
		self.width = roomSize[0]
		self.height = roomSize[1]
		self.wallV = '|'
		self.wallH = '-'
		self.wallC = '+'
		self.lit = ':'
		self.stdscr = stdscr
		self.origin = 0, 0
		self.isLit = False

	def makeRoom(self):
		h, w = self.stdscr.getmaxyx()
		curX = 1
		curY = 1

		self.stdscr.addstr(self.origin[1], self.origin[0], self.wallC)
		self.stdscr.addstr(self.origin[1] + self.height + 1, self.origin[0], self.wallC)
		self.stdscr.addstr(self.origin[1], self.origin[0] + self.width + 1, self.wallC)
		self.stdscr.addstr(self.origin[1] + self.height + 1, self.origin[0] + self.width + 1, self.wallC)

		for i in range(0, self.width):
			self.stdscr.addstr(self.origin[1], self.origin[0]+curX, self.wallH)
			self.stdscr.addstr(self.origin[1] + self.height + 1, self.origin[0]+curX, self.wallH)
			curX+=1

		for j in range(0, self.height):
			self.stdscr.addstr(self.origin[1] + curY, self.origin[0], self.wallV)
			self.stdscr.addstr(self.origin[1] + curY, self.origin[0] + self.width + 1, self.wallV)
			curY+=1

		if self.isLit:
			for i in range(0, self.height):
				for j in range(0, self.width):
					self.stdscr.addstr(self.origin[1] + 1 + i, self.origin[0] + 1 + j, self.lit)
					j+=1
				i += 1
				
		self.stdscr.addstr(self.origin[1] + self.height + 2, 0, '%i x %i' % (self.width, self.height))

		return 0
	def update(self, p):
		if self.hasPlayer(p):
			self.isLit = True
		else:
			self.isLit = False

	def hasPlayer(self, p):
		if p.getX() > self.origin[0] and p.getX() < self.origin[0]+self.width + 1 and p.getY() > self.origin[1] and p.getY() < self.origin[1] + self.height + 1:
			return True
		else:
			return False


