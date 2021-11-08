# Import libraries
import pygame

# Import files
from config import *
from common import *

# Import classes
from panel import Panel
from cell import Cell

# Class Map
class Map(Panel):
	# Constructor
	def __init__(self, screen, xy, wh, color):
		super().__init__(screen, xy, wh, color)

		# Camera wh
		self.cwh = self.wh

		# Tile config
		self.tile = {}
		self.setTile()

		# Grid config
		self.grid = {}
		self.setGrid()

	# Set tile
	def setTile(self):
		self.tile["original_size"] = 16
		self.tile["scale"] = 2
		self.tile["cellX"] = 10
		self.tile["cellY"] = 10
		self.tile["cells"] = (self.tile["cellX"], self.tile["cellY"])
		self.setTileSize()

	# Set tile size
	def setTileSize(self):
		self.tile["size"] = self.tile["original_size"] * self.tile["scale"]

	# Set grid
	def setGrid(self):
		self.grid["width"] = self.tile["size"] * self.tile["cellX"]
		self.grid["height"] = self.tile["size"] * self.tile["cellY"]
		self.grid["size"] = (self.grid["width"], self.grid["height"])
		self.setGridPos()

	# Set grid position
	def setGridPos(self):
		self.grid["startX"] = (int)(self.cwh[0] / 2 - self.grid["width"] / 2)
		self.grid["startY"] = (int)(self.cwh[1] / 2 - self.grid["height"] / 2)
		self.grid["condX"] = (int)(self.grid["width"] + self.grid["startX"] + 1)
		self.grid["condY"] = (int)(self.grid["height"] + self.grid["startY"] + 1)

	# Map moving
	def mapMoving(self, wh):
		self.cwh = wh
		self.setGridPos()

	# Map scale
	def mapScale(self, scale):
		self.tile["scale"] = scale
		self.setTileSize()
		self.setGrid()

	# Handling events
	def events(self, e):
		# MOUSEBUTTONDOWN
		if e.type == pygame.MOUSEBUTTONDOWN:
			if self.selected:
				move, scale = self.cwh, self.tile["scale"]
				# Scroll up
				if e.button == 4:
					if self.keys["alt"]: move = (self.cwh[0] - 50, self.cwh[1])
					elif self.keys["ctrl"]: scale += 1
					else: move = (self.cwh[0], self.cwh[1] - 50)
				# Scroll down
				if e.button == 5:
					if self.keys["alt"]: move = (self.cwh[0] + 50, self.cwh[1])
					elif self.keys["ctrl"]: scale -= 1
					else: move = (self.cwh[0], self.cwh[1] + 50)
				if scale <= 0: scale = 1
				if self.keys["ctrl"] and not self.keys["alt"]: self.mapScale(scale)
				else: self.mapMoving(move)

	# Rendering data
	def render(self):
		self.panel.fill(self.color)

		# Draw grid
		self.drawGrid()

	# Draw grid
	def drawGrid(self):
		for x in range(self.grid["startX"], self.grid["condX"], self.tile["size"]):
			pygame.draw.line(self.panel, COLORS["WHITE"], (x, self.grid["startY"]), (x, self.grid["condY"]), 1)
		for y in range(self.grid["startY"], self.grid["condY"], self.tile["size"]):
			pygame.draw.line(self.panel, COLORS["WHITE"], (self.grid["startX"], y), (self.grid["condX"], y), 1)
