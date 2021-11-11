# Import libraries
import pygame
from pygame.locals import *

# Import files
from config import *
from common import *

# Class Screen
class Screen:
	# Constructor
	def __init__(self, window, name):
		# Custom variables
		self.window = window
		self.name = name

		# Default variables
		self.screen = pygame.Surface(pygame.display.get_window_size())

		# Panel List
		self.panels = []

		# Buffer list
		self.bufferList = []

		# Selected panel number
		self.panelSelected = 0

	# Handling events
	def screenEvents(self, e):
		# Resize window
		if e.type == VIDEORESIZE:
			self.resizeScreen()

		# Child class method
		self.events(e)

		# Panel events
		for i, panel in enumerate(self.panels, 1):
			# If the panel is not disabled
			if not panel.disabled:
				panel.panelEvents(e)
				# MOUSEBUTTONDOWN
				if e.type == pygame.MOUSEBUTTONDOWN:
					# If panel not selected
					if self.panelSelected != i:
						wh = panel.wh
						if panel.hide: wh = [wh[0], panel.actionBar["height"]]
						if mouseCollision(panel.xy, wh, e.pos):
							for pnl in self.panels:
								pnl.selected = False
							panel.selected = True
							self.panelSelected = i

	# Resize screen
	def resizeScreen(self):
		# Since the dimensions of the surface cannot be changed,
		# I create a new surface and overwrite the old surface of the panels with the new one.
		self.screen = pygame.Surface(pygame.display.get_window_size())
		for panel in self.panels:
			panel.screen = self.screen

	# Updating data
	def updateScreen(self):
		# Child class method
		self.update()

		# Sorting the list of panels
		for i, panel in enumerate(self.panels, 1):
			if self.panelSelected != i:
				self.bufferList.append(panel)
		if self.panelSelected != 0: self.bufferList.append(self.panels[self.panelSelected-1])

		# Passing sorted data
		self.panels = self.bufferList.copy()
		self.panelSelected = len(self.bufferList)
		self.panels[self.panelSelected-1].selected = True

		# Clear buffer list
		self.bufferList.clear()

		# Updating panels
		for panel in self.panels:
			if not panel.disabled:
				panel.updatePanel()

	# Rendering data
	def renderScreen(self):
		self.window.blit(self.screen, (0, 0))
		self.screen.fill(COLORS["BACKGROUND"])

		# Child class method
		self.render()

		# Rendering panels
		for panel in self.panels:
			if not panel.disabled:
				panel.renderPanel()


	# Child class method
	def events(self, e):
		pass

	# Child class method
	def update(self):
		pass

	# Child class method
	def render(self):
		pass
