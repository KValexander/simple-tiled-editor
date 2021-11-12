# Import libraries
import pygame

# Class Template
class Element:
	# Constructor
	def __init__(self, name, xy, size, color, font):
		# Custom variables
		self.name = name
		self.xy = xy
		self.size = size
		self.color = color
		self.srcFont = font

		# Boolean variables
		self.hide = False
		self.click = False
		self.hover = False
		self.selected = False
		self.disabled = False

		# Default variables
		self.font = pygame.font.Font(self.srcFont, self.size)

	# Handling hover
	def hoverEvent(self, pos):
		pass

	# Handling click
	def clickEvent(self, pos, etype):
		pass

	# Draw
	def draw(self, screen):
		pass