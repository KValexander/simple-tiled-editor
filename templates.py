# Import libraries
import pygame
import os

# Import files
from config import *
from common import *

# Import classes
from element import Element

# Templates:
# 	Icon
# 	Link
# 	Button
# 	TextInput
# 	Inscription

# Class Icon
class Icon(Element):
	# Constructor
	def __init__(self, name, xy, src, wh=None):
		super().__init__(name, xy)

		# Custom variables
		self.src = src
		self.wh = wh

		# Default variables
		self.srcStock = STOCKIMAGE
		self.imagePath = ""

		# Checking for the existence of a file
		if os.path.exists(self.src):
			self.imagePath = self.src
		else: self.imagePath = self.srcStock

		# Loading an image
		if self.wh != None:
			self.image = scLoadImage(self.imagePath, self.wh)
		else: self.image = loadImage(self.imagePath)

		# Retrieving image dimensions
		self.irect = self.image.get_rect()
		self.wh = self.irect.size

		# Border
		self.border = pygame.Rect(self.xy, self.wh)

	# Handling hover
	def hoverEvent(self, pos):
		# MOUSEMOTION
		if mouseCollision(self.xy, self.wh, pos):
			self.hover = True
		else: self.hover = False

	# Rendering image
	def draw(self, screen):
		if not self.hide:
			screen.blit(self.image, self.xy)
			# In the case of hovering
			if self.hover:
				pygame.draw.rect(screen, COLORS["BORDER"], self.border, 3)

# Class Link
class Link(Element):
	# Constructor
	def __init__(self, name, xy, value, size, color, font):
		super().__init__(name, xy, size, color, font)

		# Custom variables
		self.value = value

		# Default variables
		self.fvalue = self.font.render(str(self.value), True, self.color)
		self.frect = self.fvalue.get_rect()
		self.lineStart = (self.xy[0], self.xy[1] + self.frect.height)
		self.lineEnd = (self.xy[0] + self.frect.width, self.lineStart[1])

	# Handling hover
	def hoverEvent(self, pos):
		# MOUSEMOTION
		if mouseCollision(self.xy, self.frect.size, pos):
			self.hover = True
		else: self.hover = False

	# Handling click
	def clickEvent(self, pos, etype):
		# MOUSEBUTTONDOWN
		if etype == "down":
			if mouseCollision(self.xy, self.frect.size, pos):
				self.click = True
		# MOUSEBUTTONUP
		if etype == "up":
			self.click = False

	# Rendering link
	def draw(self, screen): 
		if not self.hide:
			screen.blit(self.fvalue, self.xy)
			# In the case of hovering
			if self.hover:
				pygame.draw.line(screen, self.color, self.lineStart, self.lineEnd, 1)

# Class Button
class Button(Element):
	# Constructor
	def __init__(self, name, xy, wh, value, size, background, color, font):
		super().__init__(name, xy, size, color, font)
		# Custom variables
		self.wh = wh
		self.value = value
		self.background = background

		# Default variable
		self.fvalue = self.font.render(str(self.value), True, self.color)
		self.frect = self.fvalue.get_rect()
		self.rect = pygame.Rect(self.xy, self.wh)
		self.fxy = (self.rect.centerx - self.frect.width / 2, self.rect.centery - self.frect.height / 2)

	# Handling hover
	def hoverEvent(self, pos):
		# MOUSEMOTION
		if mouseCollision(self.xy, self.wh, pos):
			self.hover = True
		else: self.hover = False

	# Handling click
	def clickEvent(self, pos, etype):
		# MOUSEBUTTONDOWN
		if etype == "down":
			if mouseCollision(self.xy, self.wh, pos):
				self.click = True
		# MOUSEBUTTONUP
		if etype == "up":
			self.click = False

	# Rendering button
	def draw(self, screen):
		if not self.hide:
			pygame.draw.rect(screen, self.background, self.rect)
			screen.blit(self.fvalue, self.fxy)
			# In the case of hovering
			if self.hover:
				pygame.draw.rect(screen, COLORS["BORDER"], self.rect, 3)

# Class TextInput
class TextInput(Element):
	# Constructor
	def __init__(self, name, xy, size, color, font):
		super().__init__(name, xy, size, color, font)

# Class Inscription
class Inscription(Element):
	# Constructor
	def __init__(self, name, xy, value, size, color, font):
		super().__init__(name, xy, size, color, font)

		# Custom variables
		self.value = value

		# Default variables
		self.fvalue = self.font.render(str(self.value), True, self.color)

	# Rendering inscription
	def draw(self, screen):
		if not self.hide:
			screen.blit(self.fvalue, self.xy)
