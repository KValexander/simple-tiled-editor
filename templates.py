# Import libraries
import pygame

# Import classes
from element import Element

# Class Button
class Button(Element):
	# Constructor
	def __init__(self, name, xy, wh, value, background, size, color, font):
		super().__init__(name, xy, size, color, font)
		# Custom variables
		self.wh = wh
		self.value = value
		self.background = background

		# Default variable
		self.iname = self.font.render(str(self.value), True, self.color)
		self.rect = self.iname.get_rect()

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
		self.iname = self.font.render(str(self.value), True, self.color)
		self.rect = self.iname.get_rect()

	# Draw
	def draw(self, screen):
		screen.blit(self.iname, self.xy)
