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

		# Camera config
		self.camera = {}
		self.setCamera()

		# Tile config
		self.tile = {}
		self.setTile()
		self.setCameraIndent()

		# Grid config
		self.grid = {}
		self.setGrid()

		# Highlighting
		self.highlight = pygame.Surface((self.tile["size"], self.tile["size"]))
		self.highlight.fill(COLORS["WHITE"])
		self.highlight.set_alpha(128)

	# Set camera
	def setCamera(self):
		self.camera["wh"] = self.wh
		self.camera["direction"] = 0
		self.camera["coefficient"] = 2.5

	# Set camera indent
	def setCameraIndent(self):
		if(self.tile["scale"] >= 10): self.camera["coefficient"] = 2.5
		elif(self.tile["scale"] < 10 and self.tile["scale"] >= 5): self.camera["coefficient"] = 3.5
		elif(self.tile["scale"] < 5): self.camera["coefficient"] = 5.5
		self.camera["indent"] = self.tile["size"] * self.camera["coefficient"]

	# Set tile
	def setTile(self):
		self.tile["original_size"] = 4
		self.tile["scale"] = 8
		self.tile["cellX"] = 10
		self.tile["cellY"] = 10
		self.tile["cells"] = (self.tile["cellX"], self.tile["cellY"])
		self.setTileSize(self.tile["scale"])

	# Set tile size
	def setTileSize(self, scale):
		self.tile["scale"] = scale
		self.tile["size"] = self.tile["original_size"] * self.tile["scale"]

	# Set grid
	def setGrid(self):
		self.grid["width"] = self.tile["size"] * self.tile["cellX"]
		self.grid["height"] = self.tile["size"] * self.tile["cellY"]
		self.grid["size"] = (self.grid["width"], self.grid["height"])
		self.setGridPos()

	# Set grid position
	def setGridPos(self):
		self.grid["startX"] = (int)(self.camera["wh"][0] / 2 - self.grid["width"] / 2)
		self.grid["startY"] = (int)(self.camera["wh"][1] / 2 - self.grid["height"] / 2)
		self.grid["condX"] = (int)(self.grid["width"] + self.grid["startX"])
		self.grid["condY"] = (int)(self.grid["height"] + self.grid["startY"])

	# Coercing a position to a grid
	def toGridSize(self, xy):
		x = int(xy[0] / self.tile["size"]) * self.tile["size"]
		y = int(xy[1] / self.tile["size"]) * self.tile["size"]
		return (x, y)

	# Camera moving
	def cameraMove(self):
		# UP
		if self.camera["direction"] == 1:
			move = (self.camera["wh"][0], self.camera["wh"][1] + self.camera["indent"])
		# RIGHT
		elif self.camera["direction"] == 2:
			move = (self.camera["wh"][0] + self.camera["indent"], self.camera["wh"][1])
		# DOWN
		elif self.camera["direction"] == 3:
			move = (self.camera["wh"][0], self.camera["wh"][1] - self.camera["indent"])
		# LEFT
		elif self.camera["direction"] == 4:
			move = (self.camera["wh"][0] - self.camera["indent"], self.camera["wh"][1])
		# ELSE
		else: move = self.camera["wh"]

		self.camera["direction"] = 0
		self.camera["wh"] = move
		self.setGridPos()

	# Map scale
	def mapScale(self, scale):
		self.setTileSize(scale)
		self.setGrid()
		self.setCameraIndent()

	# Handling events
	def events(self, e):
		# MOUSEBUTTONDOWN
		if e.type == pygame.MOUSEBUTTONDOWN:
			if self.selected:
				scale = self.tile["scale"]

				# Scroll up
				if e.button == 4:
					if self.keys["ctrl"]: scale += 1
					elif self.keys["alt"]:
						self.camera["direction"] = 4
					else: self.camera["direction"] = 1

				# Scroll down
				if e.button == 5:
					if self.keys["ctrl"]: scale -= 1
					elif self.keys["alt"]:
						self.camera["direction"] = 2
					else: self.camera["direction"] = 3
				
				# Scale check
				if scale <= 0: scale = 1

				if self.keys["ctrl"] and not self.keys["alt"]: self.mapScale(scale)
				else: self.cameraMove()

	# Rendering data
	def render(self):
		# Background color
		self.panel.fill(self.color)

		# Render highlight surface
		if self.hover:
			self.panel.blit(pygame.transform.scale(self.highlight, (self.tile["size"], self.tile["size"])), self.toGridSize((self.mxy[0], self.mxy[1])))

		# Draw grid
		self.drawGrid()

	# Draw grid
	def drawGrid(self):
		for x in range(self.grid["startX"], self.grid["condX"] + 1, self.tile["size"]):
			pygame.draw.line(self.panel, COLORS["WHITE"], (x, self.grid["startY"]), (x, self.grid["condY"]), 1)
		for y in range(self.grid["startY"], self.grid["condY"] + 1, self.tile["size"]):
			pygame.draw.line(self.panel, COLORS["WHITE"], (self.grid["startX"], y), (self.grid["condX"], y), 1)
