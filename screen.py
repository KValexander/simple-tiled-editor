# Import libraries
import pygame
from pygame.locals import *

# Import files
from config import *
from common import *

# Import classes
from template import Template

# Class Screen
class Screen(Template):
	# Constructor
	def __init__(self, name):
		super().__init__()

		# Custom variables
		self.name = name

		# Default variables
		self.screen = pygame.Surface(pygame.display.get_window_size())

		# Panel List
		self.panels = []

		# Buffer list
		self.bufferList = []

		# Selected panel number
		self.panelSelected = 0

	# Get panel
	def getPanel(self, name):
		if len(self.panels) != 0:
			for panel in self.panels:
				if panel.name == name:
					return panel

	# Handling events
	def screenEvents(self, e):
		# Resize window
		if e.type == VIDEORESIZE:
			self.resizeScreen()

		# MOUSEMOTION
		if e.type == MOUSEMOTION:
			self.mxy = e.pos

		# Child class method
		self.events(e)

		# ELEMENT EVENTS
		if len(self.elements) != 0:
			for element in self.elements:
				if not element.disabled:
					element.events(e, self.mxy)

		# PANEL EVENTS
		if len(self.panels) != 0:
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

	# Updating data
	def updateScreen(self):
		# Child class method
		self.update()

		# UPDATING PANELS
		if len(self.panels) != 0:
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

			# UPDATING PANELS
			for panel in self.panels:
				if not panel.disabled:
					panel.updatePanel()

	# Rendering data
	def renderScreen(self, window):
		window.blit(self.screen, (0, 0))
		self.screen.fill(COLORS["BACKGROUND"])

		# Child class method
		self.render(self.screen)

		# RENDERING ELEMENTS
		if len(self.elements) != 0:
			for element in self.elements:
				if not element.disabled:
					element.draw(self.screen)

		# RENDERING PANELS
		if len(self.panels) != 0:
			for panel in self.panels:
				if not panel.disabled:
					panel.renderPanel(self.screen)
