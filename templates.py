# Import libraries
import pygame

# Import files
from config import *
from common import *

# Import classes
from element import Element

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

		# Border
		self.border = pygame.Rect(self.xy, self.wh)

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
		pygame.draw.rect(screen, self.background, self.rect)
		screen.blit(self.fvalue, self.fxy)
		# In the case of hovering
		if self.hover: pygame.draw.rect(screen, COLORS["BORDER"], self.border, 3)

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
		self.textSize = self.font.size(self.value)
		self.fvalue = self.font.render(str(self.value), True, self.color)
		self.rect = self.fvalue.get_rect()

	# Rendering inscription
	def draw(self, screen):
		screen.blit(self.fvalue, self.xy)
