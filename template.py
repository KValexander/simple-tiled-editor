# Import libraries
import pygame

# Import files
from config import *

# Import classes
from templates import *

# Class Template
class Template:
	# Constructor
	def __init__(self):
		# List elements
		self.elements = []
		
		# Disabled
		self.disabled = False

		# Mouse position for the current surface
		self.mxy = pygame.mouse.get_pos()

	# Delete element
	def deleteElement(self, name):
		if len(self.elements) != 0:
			for i, element in enumerate(self.elements, 0):
				if element.name == name:
					self.elements.pop(i)

	# Add icon
	def addIcon(self, name, xy, src, wh=None):
		icon = Icon(name, xy, src, wh)
		self.elements.append(icon)

	# Add link
	def addLink(self, name, xy, value, size=12, color=COLORS["WHITE"], font=FONT):
		link = Link(name, xy, value, size, color, font)
		self.elements.append(link)

	# Add button
	def addButton(self, name, xy, wh, value, size=12, background=COLORS["BUTTON"], color=COLORS["WHITE"], font=FONT):
		button = Button(name, xy, wh, value, size, background, color, font)
		self.elements.append(button)

	# Add text input
	def addTextInput(self):
		pass

	# Add inscription
	def addInscription(self, name, xy, value, size=12, color=COLORS["WHITE"], font=FONT):
		inscription = Inscription(name, xy, value, size, color, font)
		self.elements.append(inscription)

	# Child class method
	def events(self, e):
		pass

	# Child class method
	def update(self):
		pass

	# Child class method
	def render(self, screen):
		pass
