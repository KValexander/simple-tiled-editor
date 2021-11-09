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
		self.hide = False;
		self.move = False;
		self.hover = False;
		self.click = False;
		self.selected = False;
		self.disabled = False;

		# Keys
		self.keys = {
			"alt": False,
			"ctrl": False,
			"shift": False
		}

		# Default variables
		self.panel = pygame.Surface(self.wh)
		self.panel.fill(self.color)
		# Border
		self.rect = pygame.Rect(self.xy, self.wh)

		# Action bar
		self.actionBar = {
			"xy": self.xy,
			"wh": (self.wh[0], 20),
			"hover": False,
			"clickPos": (0, 0)
		}
		self.actionBar["surface"] = pygame.Surface(self.actionBar["wh"])
		self.actionBar["surface"].fill(COLORS["BORDER"])

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
			
			# Hovering on the panel
			if mouseCollision(self.xy, self.wh, e.pos):
				self.hover = True
			else: self.hover = False

			# Hovering on action bar
			if mouseCollision(self.actionBar["xy"], self.actionBar["wh"], e.pos):
				self.actionBar["hover"] = True
			else: self.actionBar["hover"] = False

			# Check not selected or and click
			if not self.selected or not self.click: self.move = False

			# Moving the panel
			if self.move:
				self.movePanel()

		# If the mouse is on the panel
		if self.hover:
			# MOUSEBUTTONDOWN
			if e.type == pygame.MOUSEBUTTONDOWN:
				# Click on the panel
				if mouseCollision(self.xy, self.wh, e.pos):
					self.click = True
					# Check move state
					if self.actionBar["hover"]:
						if(self.actionBar["clickPos"][0] == 0 and self.actionBar["clickPos"][1] == 0): self.actionBar["clickPos"] = self.mxy
						if(self.actionBar["clickPos"][0] != 0 and self.actionBar["clickPos"][1] != 0): self.move = True

			# MOUSEBUTTONUP
			if e.type == pygame.MOUSEBUTTONUP:
				self.click = False
				self.actionBar["clickPos"] = (0, 0)

		# Child class method
		self.events(e)

	# Moving the panel
	def movePanel(self):
		# Finding the coordinate difference
		differenceX = self.actionBar["clickPos"][0] - self.mxy[0]
		differenceY = self.actionBar["clickPos"][1] - self.mxy[1]
		# Subtracting the difference from the current coordinates
		self.xy = (self.xy[0] - differenceX, self.xy[1] - differenceY)
		self.actionBar["xy"] = self.xy
		self.rect.x = self.xy[0]
		self.rect.y = self.xy[1]

	# Resizing the panel
	def resizePanel(self):
		pass

	# Updating the panel
	def updatePanel(self):
		# Child class method
		self.update()

	# Rendering the panel
	def renderPanel(self):
		# Rendering the panel
		if not self.hide: self.screen.blit(self.panel, self.xy)

		# Rendering action bar on the panel
		self.screen.blit(self.actionBar["surface"], self.actionBar["xy"])

		# Rendering rect
		if not self.hide: pygame.draw.rect(self.screen, COLORS["BORDER"], self.rect, 3)

		# Child class method
		self.render()

	# Handling events
	def events(self, e):
		pass

	# Updating data on the panel
	def update(self):
		pass

	# Rendering data on the panel
	def render(self):
		pass
