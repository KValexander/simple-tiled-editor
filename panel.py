# Import libraries
import pygame

# Class panel
# Import libraries
import pygame

# Import files
from config import *
from common import *

# Class Panel
class Panel:
	# Constructor
	def __init__(self, screen, xy, wh, color):
		# Custom variables
		self.screen = screen
		self.x = xy[0]
		self.y = xy[1]
		self.xy = (self.x, self.y)
		self.width = wh[0]
		self.height = wh[1]
		self.wh = (self.width, self.height)
		self.color = color

		# Boolean variables
		self.visible = True;
		self.hover = False;
		self.click = False;
		self.selected = False;

		# Default variables
		self.panel = pygame.Surface(self.wh)
		self.panel.fill(self.color)

	# Mouse events
	def panelEvents(self, e):
		# MOUSEMOTION
		if e.type == pygame.MOUSEMOTION:
			if mouseCollision(self.xy, self.wh, e.pos):
				self.hover = True
			else: self.hover = False

		# If mouse in area
		if self.hover:
			# MOUSEBUTTONDOWN
			if e.type == pygame.MOUSEBUTTONDOWN:
				if mouseCollision(self.xy, self.wh, e.pos):
					self.click = True
				else: self.click = False
			# MOUSEBUTTONUP
			if e.type == pygame.MOUSEBUTTONUP:
				self.click = False

	# Rendering area
	def drawPanel(self):
		self.screen.blit(self.panel, self.xy)