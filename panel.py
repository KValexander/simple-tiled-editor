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
		self.xy = xy
		self.wh = wh
		self.color = color

		# Boolean variables
		self.disabled = False;
		self.hover = False;
		self.click = False;
		self.selected = False;

		# Keys
		self.keys = {
			"alt": False,
			"ctrl": False,
			"shift": False
		}

		# Default variables
		self.panel = pygame.Surface(self.wh)
		self.panel.fill(self.color)
		# Mouse position on the panel
		self.mxy = pygame.mouse.get_pos()

	# Panel events
	def panelEvents(self, e):
		# If the panel is selected
		if self.selected:
			# KEYPRESSED
			pressed = pygame.key.get_pressed()
			# ALT
			if pressed[pygame.K_LALT] or pressed[pygame.K_RALT]:
				self.keys["alt"] = True
			else: self.keys["alt"] = False
			# CTRL
			if pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]:
				self.keys["ctrl"] = True
			else: self.keys["ctrl"] = False
			# SHIFT
			if pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]:
				self.keys["shift"] = True
			else: self.keys["shift"] = False

		# MOUSEMOTION
		if e.type == pygame.MOUSEMOTION:
			# Mouse position on the panel
			self.mxy = (int(e.pos[0] - self.xy[0]), int(e.pos[1] - self.xy[1]))
			# Panel targeting check
			if mouseCollision(self.xy, self.wh, e.pos):
				self.hover = True
			else: self.hover = False

		# If the mouse is on the panel
		if self.hover:
			# MOUSEBUTTONDOWN
			if e.type == pygame.MOUSEBUTTONDOWN:
				if mouseCollision(self.xy, self.wh, e.pos):
					self.click = True
				else: self.click = False
			# MOUSEBUTTONUP
			if e.type == pygame.MOUSEBUTTONUP:
				self.click = False

		# Child class events
		self.events(e)

	# Updating panel
	def updatePanel(self):
		# Child class updating
		self.update()

	# Rendering panel
	def renderPanel(self):
		self.screen.blit(self.panel, self.xy)

		# Child class rendering
		self.render()

	# Handling events
	def events(self, e):
		pass

	# Updating data on panel
	def update(self):
		pass

	# Rendering data on panel
	def render(self):
		pass
