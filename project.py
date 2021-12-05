# Import libraries
import pygame

# Import files
from config import *
from common import *

# Import classes
from screen import Screen
from map import Map
from assets import Assets
from operations import Operations

# Class Screen
class Project(Screen):
	# Constructor
	def __init__(self,name):
		super().__init__(name)

		self.asset = None

		# Tile config
		self.tile = {}
		self.setTile()

		# Grid config
		self.grid = {}

		# Panel Operations
		panel = Operations(self, "Operations", (self.screen.get_size()[0] / 4, 0), (self.screen.get_size()[0] * 0.75, self.screen.get_size()[1] / 4), COLORS["GRAY"])
		panel.addInscription("width", (50, 30), "Number of cells horizontally", 16, COLORS["WHITE"])
		panel.addInscription("height", (50, 60), "Number of cells vertically", 16, COLORS["WHITE"])

		panel.addInputBox("cellsX", (10, 30), (30, 24), 16)
		panel.addInputBox("cellsY", (10, 60), (30, 24), 16)

		panel.getElement("cellsX").text = str(self.tile["cellX"])
		panel.getElement("cellsY").text = str(self.tile["cellY"])

		panel.addButton("change", (10, 100), (100, 30), "Change", 16)

		self.panels.append(panel)

		# Panel Map
		panel = Map(self, "Map", (self.screen.get_size()[0] / 4, self.screen.get_size()[1] / 4), (self.screen.get_size()[0] * 0.75, self.screen.get_size()[1] * 0.75), COLORS["TAUPEGRAY"])
		self.panels.append(panel)

		# Set grid properties
		self.setGrid(panel.wh)

		# Panel Assets
		panel = Assets(self, "Assets",(0, 0), (self.screen.get_size()[0] / 4, self.screen.get_size()[1]), COLORS["GRAY"])
		panel.addInputBox("pathToAssets", (10, 30), (panel.wh[0] - 20, 30), 20)
		panel.getElement("pathToAssets").text = "assets/"
		panel.addButton("load", (10, 70), (100, 30), "Load", 16)
		panel.addButton("reset", (120, 70), (100, 30), "Reset", 16)
		panel.addButton("clear", (panel.wh[0] - 110, 70), (100, 30), "Clear", 16)
		self.panels.append(panel)

	# Set tile
	def setTile(self):
		self.tile["originalSize"] = 4
		self.tile["uid"] = 1
		self.tile["scale"] = 8
		self.tile["cellX"] = 10
		self.tile["cellY"] = 10
		self.tile["cells"] = (self.tile["cellX"], self.tile["cellY"])
		self.tile["tiles"] = []
		self.setTileSize(self.tile["scale"])

	# Set tile size
	def setTileSize(self, scale):
		self.tile["scale"] = scale
		self.tile["size"] = self.tile["originalSize"] * self.tile["scale"]
		self.setTilesImage()

	# Set tiles image
	def setTilesImage(self):
		for tile in self.tile["tiles"]:
			tile["xy"]
			tile["image"] = scLoadImage(tile["path"], (self.tile["size"], self.tile["size"]))

	# Set tiles coords
	def setTilesXY(self, direction, indent):
		for i, tile in enumerate(self.tile["tiles"], 0):
			# UP
			if direction == 1:
				move = (tile["xy"][0], tile["xy"][1] + indent / 2)
			# RIGHT
			elif direction == 2:
				move = (tile["xy"][0] + indent / 2, tile["xy"][1])
			# DOWN
			elif direction == 3:
				move = (tile["xy"][0], tile["xy"][1] - indent / 2)
			# LEFT
			elif direction == 4:
				move = (tile["xy"][0] - indent / 2, tile["xy"][1])
			# ELSE
			else:
				button = self.getPanel("Map").button
				if(button == 4):
					move = self.toGridSize(tile["xy"])
				elif(button == 5): move = self.toGridSize((tile["xy"][0] + 16, tile["xy"][1] + 16))
				else: move = tile["xy"]

			self.tile["tiles"][i]["xy"] = move

	# Add tile
	def addTile(self, mxy):
		# Checking a tile
		check = [x for x in self.tile["tiles"] if x["xy"] == self.toGridSize(mxy)]
		if len(check) != 0:
			if check[0]["path"] != self.asset.imagePath:
				self.deleteTile(check[0]["uid"])
				# print("Наложение")
			else: return

		# Adding a tile
		tile = {}
		tile["uid"] = self.tile["uid"]
		self.tile["uid"] += 1
		tile["n"] = self.asset.n
		tile["xy"] = self.toGridSize(mxy)
		tile["path"] = self.asset.imagePath
		tile["image"] = scLoadImage(tile["path"], (self.tile["size"], self.tile["size"]))
		self.tile["tiles"].append(tile)

	# Get tile uid
	def getTileUid(self, mxy):
		for tile in self.tile["tiles"]:
			if tile["xy"] == self.toGridSize(mxy):
				return tile["uid"]

	# Delete tile
	def deleteTile(self, uid):
		for i, tile in enumerate(self.tile["tiles"], 0):
			if tile["uid"] == uid:
				self.tile["tiles"].pop(i)

	# Set grid
	def setGrid(self, wh):
		self.grid["width"] = self.tile["size"] * self.tile["cellX"]
		self.grid["height"] = self.tile["size"] * self.tile["cellY"]
		self.grid["size"] = (self.grid["width"], self.grid["height"])

		self.grid["startX"] = int(wh[0] / 2 - self.grid["width"] / 2)
		self.grid["startY"] = int(wh[1] / 2 - self.grid["height"] / 2)
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