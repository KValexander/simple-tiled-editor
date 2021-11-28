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

	# Get element
	def getElement(self, name):
		if len(self.elements) != 0:
			for i, element in enumerate(self.elements, 0):
				if element.name == name:
					return element

	# Remove element
	def removeElement(self, prop, val=None):
		self.elements = [x for x in self.elements if getattr(x, prop) != val]

	# Add icon
	def addIcon(self, name, xy, src, wh=None, n=None):
		icon = Icon(name, xy, src, wh, n)
		self.elements.append(icon)

	# Add link
	def addLink(self, name, xy, value, size=12, color=COLORS["WHITE"], font=FONT):
		link = Link(name, xy, value, size, color, font)
		self.elements.append(link)

	# Add button
	def addButton(self, name, xy, wh, value, size=12, background=COLORS["BUTTON"], color=COLORS["WHITE"], font=FONT):
		button = Button(name, xy, wh, value, size, background, color, font)
		self.elements.append(button)

	# Add input box
	def addInputBox(self, name, xy, wh, size=12, color=COLORS["WHITE"], font=FONT):
		textInput = InputBox(name, xy, wh, size, color, font)
		self.elements.append(textInput)

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
