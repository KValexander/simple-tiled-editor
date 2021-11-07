# Import libraries
import pygame

# Import files
from config import *
from common import *

# Import classes
from cell import Cell

# Class Map
class Map:
	# Constructor
	def __init__(self, screen):
		# Screen
		self.screen = screen

		# Tile config
		self.tile = {
			"original_size": 16,
			"scale": 2,
			"cellX": 10,
			"cellY": 10
		}
		self.tile["size"] = self.tile["original_size"] * self.tile["scale"]
		self.tile["cells"] = (self.tile["cellX"], self.tile["cellY"])

		# Grid config
		self.grid = {
			"width": self.tile["size"] * self.tile["cellX"],
			"height": self.tile["size"] * self.tile["cellY"],
			"startpos": (self.tile["size"], self.tile["size"])
		}
		self.grid["size"] = (self.grid["width"], self.grid["height"])

		# Cells
		self.cells = []
		self.createCells()

	# Handling events
	def events(self, e):
		# Cell Events
		for cell in self.cells:
			# Mouse events
			# MOUSEMOTION
			if e.type == pygame.MOUSEMOTION:
				# Checking mouse hover over a cell
				if(mouseCollision(cell.xy, cell.wh, e.pos)):
					cell.hover = True
				else: cell.hover = False
			# MOUSEBUTTONDOWN
			if e.type == pygame.MOUSEBUTTONDOWN:
				# Left mouse button
				if e.button == 1:
					# Checking mouse click over a cell
					if(mouseCollision(cell.xy, cell.wh, e.pos)):
						cell.click = True
					else: cell.click = False

	# Create cells
	def createCells(self):
		for x in range(self.grid["startpos"][0], self.grid["width"], self.tile["size"]):
			for y in range(self.grid["startpos"][1], self.grid["height"], self.tile["size"]):
				cell = Cell((x,y), self.tile["size"], COLORS["WHITE"])
				self.cells.append(cell)

	# Draw cells
	def drawCells(self, screen):
		for cell in self.cells:
			cell.draw(self.screen)
