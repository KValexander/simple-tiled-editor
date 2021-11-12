# Import libraries
import pygame

# Import files
from config import *
from common import *

# Import classes
from panel import Panel

# Class Map
class Map(Panel):
	# Constructor
	def __init__(self, name, xy, wh, color):
		super().__init__(name, xy, wh, color)

		# Camera config
		self.camera = {}
		self.setCamera()

		# Lock
		self.lock = True

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
		self.camera["acceleration"] = 10
		self.camera["rewind"] = self.camera["coefficient"]

	# Set camera indent
	def setCameraIndent(self):
		self.camera["indent"] = self.tile["size"] * self.camera["rewind"]

	# Set tile
	def setTile(self):
		self.tile["originalSize"] = 4
		self.tile["scale"] = 8
		self.tile["cellX"] = 10
		self.tile["cellY"] = 10
		self.tile["cells"] = (self.tile["cellX"], self.tile["cellY"])
		self.setTileSize(self.tile["scale"])

	# Set tile size
	def setTileSize(self, scale):
		self.tile["scale"] = scale
		self.tile["size"] = self.tile["originalSize"] * self.tile["scale"]

	# Set grid
	def setGrid(self):
		self.grid["width"] = self.tile["size"] * self.tile["cellX"]
		self.grid["height"] = self.tile["size"] * self.tile["cellY"]
		self.grid["size"] = (self.grid["width"], self.grid["height"])
		self.setGridPos()

	# Set grid position
	def setGridPos(self):
		self.grid["startX"] = int(self.camera["wh"][0] / 2 - self.grid["width"] / 2)
		self.grid["startY"] = int(self.camera["wh"][1] / 2 - self.grid["height"] / 2)
		self.grid["condX"] = int(self.grid["width"] + self.grid["startX"])
		self.grid["condY"] = int(self.grid["height"] + self.grid["startY"])
		self.grid["startXY"] = (self.grid["startX"], self.grid["startY"])
		self.grid["condXY"] = self.grid["condX"], self.grid["condY"]

	# Coercing a position to a grid
	def toGridSize(self, xy):
		xy = (xy[0] - self.grid["startX"], xy[1] - self.grid["startY"])
		x = (int(xy[0] / self.tile["size"]) * self.tile["size"]) + self.grid["startX"]
		y = (int(xy[1] / self.tile["size"]) * self.tile["size"]) + self.grid["startY"]
		if(xy[0] < 0): x -= self.tile["size"]
		if(xy[1] < 0): y -= self.tile["size"]
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

	# Handling events
	def events(self, e):
		# MOUSEMOTION
		if e.type == pygame.MOUSEMOTION:
			# Check hover and not hover on action bar
			if self.hover and not self.actionBar["hover"]:
				# Highlight color
				if mouseCollision(self.grid["startXY"], self.grid["size"], self.mxy):
					self.highlight.fill((0, 128, 0))
				else: self.highlight.fill((128, 0, 0))

		# MOUSEBUTTONDOWN
		if e.type == pygame.MOUSEBUTTONDOWN:
			# Check selected and not hover on action bar
			if self.selected and not self.actionBar["hover"]:
				scale = self.tile["scale"]

				# Rewind acceleration
				if self.keys["shift"]: self.camera["rewind"] = self.camera["coefficient"] * self.camera["acceleration"]
				else: self.camera["rewind"] = self.camera["coefficient"]

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

				# Resizing the grid
				if self.keys["ctrl"] and not self.keys["alt"]: self.setTileSize(scale)
				# Moving the camera
				else: self.cameraMove()

				# Common Methods
				self.setCameraIndent()
				self.setGrid()

	# Rendering data
	def render(self, panel):
		# Render highlight surface
		if self.hover and not self.actionBar["hover"]:
			panel.blit(pygame.transform.scale(self.highlight, (self.tile["size"], self.tile["size"])), self.toGridSize((self.mxy[0], self.mxy[1])))

		# Draw grid
		self.drawGrid(panel)

	# Draw grid
	def drawGrid(self, panel):
		for x in range(self.grid["startX"], self.grid["condX"] + 1, self.tile["size"]):
			pygame.draw.line(panel, COLORS["WHITE"], (x, self.grid["startY"]), (x, self.grid["condY"]), 1)
		for y in range(self.grid["startY"], self.grid["condY"] + 1, self.tile["size"]):
			pygame.draw.line(panel, COLORS["WHITE"], (self.grid["startX"], y), (self.grid["condX"], y), 1)
