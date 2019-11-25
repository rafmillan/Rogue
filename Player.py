class player:
	def  __init__(self, name, health):
		self.health = health
		self.name = name
		self.x = 15
		self.y = 15
		self.inv = []

	def getX(self):
		return self.x

	def getY(self):
		return self.y
		
	def getHealth(self):
		return self.health

	def addItem(self, item):
		self.inv.append(item)

	def removeItem(self, item):
		for i in self.inv:
			if i == item:
				self.inv.remove(item)

	#returns index of item
	def findItem(self, item):
		for i in self.inv:
			if i == item:
				return i



