# Import libraries
import pygame
import time
import os

# Import classes
from panel import Panel

# Class Operations
class Operations(Panel):
	# Constructor
	def __init__(self, screen, name, xy, wh, color):
		super().__init__(screen, name, xy, wh, color)

	# Handling events
	def events(self, e):
		# Click handling
		if e.type == pygame.MOUSEBUTTONDOWN:
			# Handling element clicks
			for element in self.elements:
				if element.type == "button" and element.click:
					# Load assets
					if element.name == "change":
						self.changeCells()
					# Save map
					elif element.name == "save":
						if len(self.screen.tile["tiles"]) != 0:
							self.saveMap()

	# Change cell count
	def changeCells(self):
		cellsX = self.getElement("cellsX").text
		cellsY = self.getElement("cellsY").text

		self.screen.tile["tiles"].clear()
		self.screen.tile["uid"] = 0

		self.screen.tile["cellX"] = int(cellsX)
		self.screen.tile["cellY"] = int(cellsY)

		self.screen.setGrid(self.screen.getPanel("Map").wh)

	# Save map
	# Below is a rather unoptimized piece of code
	def saveMap(self):
		result = []
		# List creation
		for i in range(self.screen.tile["cellY"]):
			result.append([])
			for j in range(self.screen.tile["cellX"]):
				result[i].append(0)
		# Writing tile numbers
		for tile in self.screen.tile["tiles"]:
			for i, y in enumerate(range(self.screen.grid["startY"], self.screen.grid["condY"], self.screen.tile["size"]), 0):
				for j, x in enumerate(range(self.screen.grid["startX"], self.screen.grid["condX"], self.screen.tile["size"]), 0):
					t = self.screen.getTile(self.screen.getTileUid((x,y)))
					if t != None: result[i][j] = (t["n"])

		# Composing a file name
		if not os.path.exists("maps"):
			os.mkdir("maps")
		filename = "maps/map_" + str(len(os.listdir("maps"))) + "_" + str(int(round(time.time() * 1000))) + ".txt"

		# Saving a file
		file = open(filename, "w+")
		for i in range(len(result)):
			if i != 0: file.write("\n")
			for j in range(len(result[i])):
				file.write(str(result[i][j]) + " ")
		file.close()
