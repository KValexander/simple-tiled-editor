# Import libraries
import pygame
import os
import re

# Import files
from config import *
from common import *

# Import classes
from panel import Panel

# Class Assets
class Assets(Panel):
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
					if element.name == "load":
						self.screen.asset = None
						self.loadAssets()
					# Reset
					elif element.name == "reset":
						self.getElement("pathToAssets").text = ""
					# Clear
					elif element.name == "clear":
						self.removeElement("type", "icon")
						self.screen.asset = None
				# Clicking on the icon
				elif element.type == "icon" and element.hover:
					self.screen.asset = element
					self.screen.asset.rect = pygame.Rect(self.screen.asset.xy, self.screen.asset.wh)

	# Load assets
	def loadAssets(self):
		# Getting the path to assets
		pathToAssets = self.getElement("pathToAssets").text

		# Checking for the existence of a path
		if not os.path.exists(pathToAssets) or not os.path.isdir(pathToAssets): return

		# Removing previous loadings
		self.removeElement("type", "icon")

		# Getting images of assets
		images = os.listdir(pathToAssets)

		# for y in range(110, self.wh[1], 64):
		# 	for x in range(10, self.wh[0], 64):
		# 		print(x, y)

		xy = [10, 110]
		size = 64
		maxCol = self.wh[0] / size
		maxRow = self.wh[1] / size
		currentCol = 1
		currentRow = 1

		# Image processing
		for i, image in enumerate(images, 0):
			if re.search(r"\.png|jpg|jpeg", image):
				name = re.sub(r"\.png|jpg|jpeg", "", image)
				self.addIcon(name, xy.copy(), pathToAssets+image, (size, size), i+1)
				xy[0] += size
				if xy[0] + size > self.wh[0]:
					xy[0] = 10
					xy[1] += size
				if xy[1] + size > self.wh[1]: return

	# Rendering data
	def render(self, panel):
		# Rendering the selected asset
		if self.screen.asset != None:
			pygame.draw.rect(panel, (0, 255, 0), self.screen.asset.rect, 3)
