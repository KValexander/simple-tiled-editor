# Import libraries
import pygame

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

	# Change cell count
	def changeCells(self):
		cellsX = self.getElement("cellsX").text
		cellsY = self.getElement("cellsY").text

		self.screen.tile["tiles"].clear()
		self.screen.tile["uid"] = 0

		self.screen.tile["cellX"] = int(cellsX)
		self.screen.tile["cellY"] = int(cellsY)

		self.screen.setGrid(self.screen.getPanel("Map").wh)
