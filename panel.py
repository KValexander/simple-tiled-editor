# Import libraries
import pygame

# Import files
from config import *
from common import *

# Import classes
from template import Template

# Class Panel
class Panel(Template):
	# Constructor
	def __init__(self, name, xy, wh, color):
		super().__init__()

		# Custom variables
		self.name = name
		self.xy = [int(xy[0]), int(xy[1])]
		self.wh = [int(wh[0]), int(wh[1])]
		self.color = color

		# Boolean variables
		self.lock = False
		self.hide = False
		self.move = False
		self.hover = False
		self.click = False
		self.resize = False
		self.selected = False

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
			"size": 4,
			"direction": 0,
			"color": COLORS["BORDER"],
			"rect": pygame.Rect(self.xy, self.wh),
			"cursor": pygame.SYSTEM_CURSOR_ARROW,
		}

		# Action bar
		self.actionBar = {
			"height": 20,
			"hover": False,
			"clickPos": (0, 0),
			"iconSize": (12, 12),
			"iconHover": False,
			"font": pygame.font.Font(FONT, 12),
			"borderSize": 2,
		}
		self.actionBar["rect"] = pygame.Rect((0,0), (self.actionBar["iconSize"][0] + self.actionBar["borderSize"] * 2, self.actionBar["iconSize"][1] + self.actionBar["borderSize"] * 2))
		self.actionBar["surface"] = pygame.Surface((self.wh[0], self.actionBar["height"]))
		self.actionBar["name"] = self.actionBar["font"].render(str(self.name), True, COLORS["WHITE"])
		self.actionBar["unlock"] = scLoadImage("gui/unlock.png", self.actionBar["iconSize"])
		self.actionBar["lock"] = scLoadImage("gui/lock.png", self.actionBar["iconSize"])
		self.actionBar["hide"] = scLoadImage("gui/hide.png", self.actionBar["iconSize"])
		self.actionBar["close"] = scLoadImage("gui/close.png", self.actionBar["iconSize"])

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

				# Check click on the panel
				if self.click:
					# Check border direction 
					if self.border["direction"] != 0:
						if not self.lock:
							self.resize = True
					# Check hover on action bar
					elif self.actionBar["hover"]:
						if(self.actionBar["clickPos"][0] == 0 and self.actionBar["clickPos"][1] == 0):
							self.actionBar["clickPos"] = self.mxy
						if(self.actionBar["clickPos"][0] != 0 and self.actionBar["clickPos"][1] != 0):
							if not self.lock:
								self.move = True

					# CLOSE
					if mouseCollision((self.xy[0] + self.wh[0] - 20, self.xy[1] + 4), self.actionBar["iconSize"], e.pos):
						if not self.lock:
							self.disabled = True
					# HIDE
					elif mouseCollision((self.xy[0] + self.wh[0] - 40, self.xy[1] + 4), self.actionBar["iconSize"], e.pos):
						if not self.lock:
							if self.hide: self.hide = False
							else: self.hide = True
					# LOCK
					elif mouseCollision((self.xy[0] + self.wh[0] - 60, self.xy[1] + 4), self.actionBar["iconSize"], e.pos):
						if self.lock: self.lock = False
						else: self.lock = True

		# MOUSEBUTTONUP
		if e.type == pygame.MOUSEBUTTONUP:
			self.click = False
			self.resize = False
			self.clickPos = (0,0)
			self.actionBar["clickPos"] = (0, 0)

		if not self.hide:
			# ELEMENT EVENTS
			if len(self.elements) != 0:
				for element in self.elements:
					if not element.disabled:
						if e.type == pygame.MOUSEMOTION:
							element.hoverEvent(self.mxy)
						if e.type == pygame.MOUSEBUTTONDOWN:
							element.clickEvent(self.mxy, "down")
						if e.type == pygame.MOUSEBUTTONUP:
							element.clickEvent(self.mxy, "up")

			# Child class method
			self.events(e)

	# Check mousemotion collision
	def checkMousemotionCollision(self, pos):
		# Hovering on the panel
		if mouseCollision(self.xy, self.wh, pos):
			self.hover = True
		else: self.hover = False

		# Hovering on action bar
		if mouseCollision(self.xy, (self.wh[0], self.actionBar["height"]), pos):
			self.actionBar["hover"] = True

			# Hover over the close icon
			if mouseCollision((self.xy[0] + self.wh[0] - 20, self.xy[1] + 4), self.actionBar["iconSize"], pos):
				self.actionBar["iconHover"], self.move = True, False
				self.actionBar["rect"].x = self.xy[0] + self.wh[0] - 20 - self.actionBar["borderSize"]
				self.actionBar["rect"].y = self.xy[1] + 4 - self.actionBar["borderSize"]
			# Hover over the hide icon
			elif mouseCollision((self.xy[0] + self.wh[0] - 40, self.xy[1] + 4), self.actionBar["iconSize"], pos):
				self.actionBar["iconHover"], self.move = True, False
				self.actionBar["rect"].x = self.xy[0] + self.wh[0] - 40 - self.actionBar["borderSize"]
				self.actionBar["rect"].y = self.xy[1] + 4 - self.actionBar["borderSize"]
			# Hover over the lock icon
			elif mouseCollision((self.xy[0] + self.wh[0] - 60, self.xy[1] + 4), self.actionBar["iconSize"], pos):
				self.actionBar["iconHover"], self.move = True, False
				self.actionBar["rect"].x = self.xy[0] + self.wh[0] - 60 - self.actionBar["borderSize"]
				self.actionBar["rect"].y = self.xy[1] + 4 - self.actionBar["borderSize"]
			else: self.actionBar["iconHover"] = False

		else:
			self.actionBar["iconHover"] = False
			self.actionBar["hover"] = False

		if not self.hide:
			# Hover to the edge of the panel
			if borderCollision(self.xy, self.wh, pos, self.border["size"]):
				# Determining the direction of the edge
				if self.border["direction"] == 0:
					# LEFT UP
					if (self.mxy[0] >= 0 and self.mxy[0] <= self.border["size"] and
						self.mxy[1] >= 0 and self.mxy[1] <= self.border["size"]):
							self.border["direction"] = 5
							self.border["cursor"] = pygame.SYSTEM_CURSOR_SIZENWSE
					# RIGHT DOWN
					elif(self.mxy[0] >= self.wh[0] - self.border["size"] and self.mxy[0] <= self.wh[0] and
						self.mxy[1] >= self.wh[1] - self.border["size"] and self.mxy[1] <= self.wh[1]):
							self.border["direction"] = 6
							self.border["cursor"] = pygame.SYSTEM_CURSOR_SIZEALL
					# UP
					elif(self.mxy[1] >= 0 and self.mxy[1] <= self.border["size"]):
						self.border["direction"] = 1
						self.border["cursor"] = pygame.SYSTEM_CURSOR_SIZENS
					# RIGHT
					elif(self.mxy[0] >= self.wh[0] - self.border["size"] and self.mxy[0] <= self.wh[0]):
						self.border["direction"] = 2
						self.border["cursor"] = pygame.SYSTEM_CURSOR_SIZEWE
					# DOWN
					elif(self.mxy[1] >= self.wh[1] - self.border["size"] and self.mxy[1] <= self.wh[1]):
						self.border["direction"] = 3
						self.border["cursor"] = pygame.SYSTEM_CURSOR_SIZENS
					# LEFT
					elif(self.mxy[0] >= 0 and self.mxy[0] <= self.border["size"]):
						self.border["direction"] = 4
						self.border["cursor"] = pygame.SYSTEM_CURSOR_SIZEWE
					# ELSE
					else:
						self.border["direction"] = 0
						self.border["cursor"] = pygame.SYSTEM_CURSOR_ARROW

				pygame.mouse.set_system_cursor(self.border["cursor"])
			else:
				if not self.resize: self.border["direction"] = 0
				pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)


	# Moving the panel
	def movePanel(self):
		# Finding the coordinate difference
		differenceX = self.actionBar["clickPos"][0] - self.mxy[0]
		differenceY = self.actionBar["clickPos"][1] - self.mxy[1]
		# Subtracting the difference from the current coordinates
		self.xy[0] -= differenceX
		self.xy[1] -= differenceY
		self.border["rect"].x = self.xy[0]
		self.border["rect"].y = self.xy[1]

	# Resizing the panel
	def resizePanel(self):
		# Finding the coordinate difference
		differenceX = self.mxy[0] - self.clickPos[0]
		differenceY = self.mxy[1] - self.clickPos[1]
		xy, wh = self.xy.copy(), self.wh.copy()

		# LEFT UP
		if self.border["direction"] == 5:
			xy[0] += differenceY
			xy[1] += differenceY
			wh[0] -= differenceY
			wh[1] -= differenceY
		# RIGHT DOWN
		elif self.border["direction"] == 6:
			wh[0] = self.mxy[0]
			wh[1] = self.mxy[1]
		# UP
		elif self.border["direction"] == 1:
			xy[1] += differenceY
			wh[1] -= differenceY
		# RIGHT
		elif self.border["direction"] == 2:
			wh[0] = self.mxy[0]
		# DOWN
		elif self.border["direction"] == 3:
			wh[1] = self.mxy[1]
		# LEFT
		elif self.border["direction"] == 4:
			xy[0] += differenceX
			wh[0] -= differenceX

		# Check wh for scale
		if(	wh[0] <= 100 or
			wh[1] <= self.actionBar["height"] + 10
			): return 

		# Resizible
		self.xy = xy
		self.wh = wh
		self.panel = pygame.Surface(self.wh)
		self.actionBar["surface"] = pygame.Surface((self.wh[0], self.actionBar["height"]))
		self.border["rect"].x = self.xy[0]
		self.border["rect"].y = self.xy[1]
		self.border["rect"].size = self.wh

	# Updating the panel
	def updatePanel(self):
		if not self.hide:
			# Child class method
			self.update()

	# Rendering the panel
	def renderPanel(self, screen):
		# Border color
		if self.selected: self.border["color"] = COLORS["BORDERSELECTED"]
		else: self.border["color"] = COLORS["BORDER"]

		# Rendering the panel
		if not self.hide:
			screen.blit(self.panel, self.xy)
			self.panel.fill(self.color)

		# Rendering action bar on the panel
		self.renderActionBar(screen)

		if not self.hide:
			# Rendering rect
			pygame.draw.rect(screen, self.border["color"], self.border["rect"], 3)

			# RENDERING ELEMENTS
			if len(self.elements) != 0:
				for element in self.elements:
					if not element.disabled:
						element.draw(self.panel)

			# Child class method
			self.render(self.panel)

	# Rendering action bar on ther panel
	def renderActionBar(self, screen):
		screen.blit(self.actionBar["surface"], self.xy)
		self.actionBar["surface"].fill(self.border["color"])

		# Rendering parts of the action bar
		screen.blit(self.actionBar["name"], (self.xy[0] + 8, self.xy[1] + 4))
		drawImage(screen, self.actionBar["close"], (self.xy[0] + self.wh[0] - 20, self.xy[1] + 4))
		drawImage(screen, self.actionBar["hide"], (self.xy[0] + self.wh[0] - 40, self.xy[1] + 4))
		if self.lock: drawImage(screen, self.actionBar["lock"], (self.xy[0] + self.wh[0] - 60, self.xy[1] + 4))
		else: drawImage(screen, self.actionBar["unlock"], (self.xy[0] + self.wh[0] - 60, self.xy[1] + 4))
		
		# Highlighting for icons
		if self.actionBar["iconHover"]:
			pygame.draw.rect(screen, COLORS["WHITE"], self.actionBar["rect"], self.actionBar["borderSize"])