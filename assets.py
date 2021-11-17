# Import libraries
import pygame
import os
import re

# Import classes
from panel import Panel

# Class Assets
class Assets(Panel):
	# Constructor
	def __init__(self, name, xy, wh, color):
		super().__init__(name, xy, wh, color)

	# Handling events
	def events(self, e):
		# Button click handling
		if e.type == pygame.MOUSEBUTTONDOWN:
			for element in self.elements:
				if element.type == "button" and element.click:
					# Load assets
					if element.name == "load":
						self.loadAssets()
					# Clear
					elif element.name == "clear":
						self.clearAssets()

	# Clear assets
	def clearAssets(self):
		self.getElement("pathToAssets").text = ""
		for element in self.elements:
			if element.type == "icon":
				self.removeElement(element.name)
		print(self.elements)


	# Load assets
	def loadAssets(self):
		# Getting the path to assets
		pathToAssets = self.getElement("pathToAssets").text

		# Checking for the existence of a path
		if not os.path.exists(pathToAssets) or not os.path.isdir(pathToAssets): return

		# Removing previous loadings
		for element in self.elements:
			if element.type == "icon":
				print(self.removeElement(element.name))

		# Getting images of assets
		images = os.listdir(pathToAssets)

		xy = [10, 110]
		size = 64
		maxCol = self.wh[0] / size
		maxRow = self.wh[1] / size
		currentCol = 1
		currentRow = 1

		# Image processing
		for image in images:
			if re.search(r"\.png|jpg|jpeg", image):
				name = re.sub(r"\.png|jpg|jpeg", "", image)
				self.addIcon(name, xy, pathToAssets+image, (size, size))
				xy[0] += size

				if xy[0] > self.wh[0]:
					xy[0] = 10
					xy[1] += size
				if xy[1] > self.wh[1]: return
