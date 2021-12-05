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
	def __init__(self, screen, name, xy, wh, color):
		super().__init__(screen, name, xy, wh, color)

		# Camera config
		self.camera = {}
		self.setCamera()
		self.setCameraIndent()

		# Boolean variables
		self.put = False

		# Highlighting
		self.highlight = pygame.Surface((self.screen.tile["size"], self.screen.tile["size"]))
		self.highlight.fill(COLORS["WHITE"])
		self.highlight.set_alpha(128)

	# Set camera
	def setCamera(self):
		self.camera["wh"] = self.wh
		self.camera["direction"] = 0
		self.camera["coefficient"] = 4

	# Set camera indent
	def setCameraIndent(self):
		self.camera["indent"] = self.screen.tile["size"] * self.camera["coefficient"]

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

		self.camera["wh"] = move

	# Handling events
	def events(self, e):
		# MOUSEMOTION
		if e.type == pygame.MOUSEMOTION:
			# Check hover and not hover on action bar
			if self.hover and not self.actionBar["hover"]:
				# Highlight color
				if mouseCollision(self.screen.grid["startXY"], self.screen.grid["size"], self.mxy):
					self.put = True
				else: self.put = False

				# Adding tiles on hold
				if self.click and self.screen.asset != None and self.put and self.button == 1:
					self.screen.addTile(self.mxy)
				elif self.button == 3 and self.put:
					self.screen.deleteTile(self.screen.getTileUid(self.mxy))

		# MOUSEBUTTONDOWN
		if e.type == pygame.MOUSEBUTTONDOWN:

			# Adding assets to the grid
			if self.put:
				if e.button == 1 and self.screen.asset != None:
					self.screen.addTile(self.mxy)
				elif e.button == 3:
					self.screen.deleteTile(self.screen.getTileUid(self.mxy))

			# Check selected and not hover on action bar
			if self.selected and not self.actionBar["hover"]:
				scale = self.screen.tile["scale"]

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
				if self.keys["ctrl"] and not self.keys["alt"]:
					self.screen.setTileSize(scale)
				# Moving the camera
				else: self.cameraMove()

				# Common Methods
				self.setCameraIndent()
				self.screen.setGrid(self.camera["wh"])
				self.screen.setTilesXY(self.camera["direction"], self.camera["indent"])
				self.camera["direction"] = 0

	# Rendering data
	def render(self, panel):
		if self.put: self.highlight.fill((0, 128, 0))
		else: self.highlight.fill((128, 0, 0))

		# Render tiles
		if len(self.screen.tile["tiles"]) != 0:
			for tile in self.screen.tile["tiles"]:
				panel.blit(tile["image"], tile["xy"])

		# Render highlight surface
		if self.hover and not self.actionBar["hover"]:
			panel.blit(pygame.transform.scale(self.highlight, (self.screen.tile["size"], self.screen.tile["size"])), self.screen.toGridSize(self.mxy))

		# Draw grid
		self.drawGrid(panel)

	# Draw grid
	def drawGrid(self, panel):
		for x in range(self.screen.grid["startX"], self.screen.grid["condX"] + 1, self.screen.tile["size"]):
			pygame.draw.line(panel, COLORS["WHITE"], (x, self.screen.grid["startY"]), (x, self.screen.grid["condY"]), 1)
		for y in range(self.screen.grid["startY"], self.screen.grid["condY"] + 1, self.screen.tile["size"]):
			pygame.draw.line(panel, COLORS["WHITE"], (self.screen.grid["startX"], y), (self.screen.grid["condX"], y), 1)
