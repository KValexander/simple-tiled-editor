# Import libraries
import pygame

# Import files
from config import *
from common import *

# Class Panel
class Panel:
	# Constructor
	def __init__(self, screen, name, xy, wh, color):
		# Custom variables
		self.screen = screen
		self.name = name
		self.xy = xy
		self.wh = (int(wh[0]), int(wh[1]))
		self.color = color

		# Boolean variables
		self.hide = False
		self.move = False
		self.hover = False
		self.click = False
		self.resize = False
		self.selected = False
		self.disabled = False

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
		self.border = {
			"size": 5,
			"hover": False,
			"rect": pygame.Rect(self.xy, self.wh),
			"direction": 0,
			"cursor": pygame.SYSTEM_CURSOR_ARROW
		}

		# Action bar
		self.actionBar = {
			"height": 20,
			"xy": self.xy,
			"hover": False,
			"clickPos": (0, 0),
			"font": pygame.font.Font("gui/Montserrat-Light.ttf", 12),
		}
		self.actionBar["wh"] = (self.wh[0], self.actionBar["height"])
		self.actionBar["surface"] = pygame.Surface(self.actionBar["wh"])
		self.actionBar["surface"].fill(COLORS["BORDER"])
		self.actionBar["name"] = self.actionBar["font"].render(str(self.name), True, COLORS["WHITE"])

		# Mouse position on the panel
		self.mxy = pygame.mouse.get_pos()
		# Mouse coordinates while clicking
		self.clickPos = (0, 0)

	# Panel events
	def panelEvents(self, e):
		# If the panel is selected
		if self.selected and not self.hide:
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

			# Check mousemotion collision
			self.checkMousemotionCollision(e.pos)

			# Check not selected or and click
			if not self.selected or not self.click:
				self.border["direction"] = 0
				self.resize = False
				self.move = False

			# Resizible the panel
			if self.resize:
				self.resizePanel()

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
					# Mouse coordinates while clicking
					if (self.clickPos[0] == 0 and self.clickPos[1] == 0):
						self.clickPos = self.mxy
					# Chech resize state
					# Check move state
					if self.border["hover"]:
						self.resize = True
					elif self.actionBar["hover"]:
						if(self.actionBar["clickPos"][0] == 0 and self.actionBar["clickPos"][1] == 0):
							self.actionBar["clickPos"] = self.mxy
						if(self.actionBar["clickPos"][0] != 0 and self.actionBar["clickPos"][1] != 0):
							self.move = True

		# MOUSEBUTTONUP
		if e.type == pygame.MOUSEBUTTONUP:
			self.click = False
			self.resize = False
			self.clickPos = (0,0)
			self.border["direction"] = 0
			self.actionBar["clickPos"] = (0, 0)

		# Child class method
		self.events(e)

	# Check mousemotion collision
	def checkMousemotionCollision(self, pos):
		# Hovering on the panel
		if mouseCollision(self.xy, self.wh, pos):
			self.hover = True
		else: self.hover = False

		# Hovering on action bar
		if mouseCollision(self.actionBar["xy"], self.actionBar["wh"], pos):
			self.actionBar["hover"] = True
		else: self.actionBar["hover"] = False

		# Hover to the edge of the panel
		if borderCollision(self.xy, self.wh, pos, self.border["size"]):
			self.border["hover"] = True

			# Determining the direction of the edge
			if self.border["direction"] == 0:
				# UP
				if(self.mxy[1] >= 1 and self.mxy[1] <= self.border["size"]):
					self.border["direction"] = 1
					self.border["cursor"] = pygame.SYSTEM_CURSOR_SIZENS
				# RIGHT
				elif(self.mxy[0] >= self.wh[0] - self.border["size"] and self.mxy[0] <= self.wh[0] - 1):
					self.border["direction"] = 2
					self.border["cursor"] = pygame.SYSTEM_CURSOR_SIZEWE
				# DOWN
				elif(self.mxy[1] >= self.wh[1] - self.border["size"] and self.mxy[1] <= self.wh[1] - 1):
					self.border["direction"] = 3
					self.border["cursor"] = pygame.SYSTEM_CURSOR_SIZENS
				# LEFT
				elif(self.mxy[0] >= 1 and self.mxy[0] <= self.border["size"]):
					self.border["direction"] = 4
					self.border["cursor"] = pygame.SYSTEM_CURSOR_SIZEWE
				# ELSE
				else:
					self.border["direction"] = 0
					self.border["cursor"] = pygame.SYSTEM_CURSOR_ARROW

			pygame.mouse.set_system_cursor(self.border["cursor"])
		else:
			self.border["hover"] = False
			pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)


	# Moving the panel
	def movePanel(self):
		# Finding the coordinate difference
		differenceX = self.actionBar["clickPos"][0] - self.mxy[0]
		differenceY = self.actionBar["clickPos"][1] - self.mxy[1]
		# Subtracting the difference from the current coordinates
		self.xy = (self.xy[0] - differenceX, self.xy[1] - differenceY)
		self.actionBar["xy"] = self.xy
		self.border["rect"].x = self.xy[0]
		self.border["rect"].y = self.xy[1]

	# Resizing the panel
	def resizePanel(self):
		# Finding the coordinate difference
		differenceX = self.mxy[0] - self.clickPos[0]
		differenceY = self.mxy[1] - self.clickPos[1]
		xy, wh = self.xy, self.wh
		print(self.border["direction"])

		# !!!??? What is the problem here? I do not understand ???!!!

		# UP Correct
		if self.border["direction"] == 1:
			xy = [xy[0], xy[1] + differenceY]
			wh = [wh[0], wh[1] - differenceY]
		# RIGHT NOT CORRECT
		elif self.border["direction"] == 2:
			xy = [xy[0], xy[1]]
			wh = [wh[0] + differenceX, wh[1]]
		# DOWN NOT CORRECT
		elif self.border["direction"] == 3:
			xy = [xy[0], xy[1]]
			wh = [wh[0], wh[1] + differenceY]
		# LEFT Correct
		elif self.border["direction"] == 4:
			xy = [xy[0] + differenceX, xy[1]]
			wh = [wh[0] - differenceX, wh[1]]

		# Check wh for scale
		if(wh[0] <= 100): return
		if(wh[1] <= self.actionBar["height"] + 10): return

		# Resizible
		self.xy = xy
		self.wh = wh
		self.actionBar["xy"] = self.xy
		self.actionBar["wh"] = (self.wh[0], self.actionBar["height"])
		self.border["rect"].x = self.xy[0]
		self.border["rect"].y = self.xy[1]
		self.border["rect"].size = self.wh

	# Updating the panel
	def updatePanel(self):
		# Child class method
		self.update()

	# Rendering the panel
	def renderPanel(self):
		# Rendering the panel
		if not self.hide: self.screen.blit(pygame.transform.scale(self.panel, self.wh), self.xy)

		# Rendering action bar on the panel
		self.screen.blit(pygame.transform.scale(self.actionBar["surface"], self.actionBar["wh"]), self.actionBar["xy"])
		self.actionBar["surface"].blit(self.actionBar["name"], (8, 4))

		# Rendering rect
		if not self.hide: pygame.draw.rect(self.screen, COLORS["BORDER"], self.border["rect"], 3)

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