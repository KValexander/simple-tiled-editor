import pygame
from pygame.locals import *

from panel import Panel

class Screen:
	def __init__(self, window, name):
		self.window = window
		self.name = name

		self.screen = pygame.Surface(pygame.display.get_window_size())
		self.rect = pygame.Rect(self.screen.get_offset(), pygame.display.get_window_size())

		# Panels
		self.panels = []

	# Add panel
	def addPanel(self, name, xy, wh):
		panel = Panel(self.screen, name, xy, wh)
		self.panels.append(panel)

	def events(self, e):
		if e.type == VIDEORESIZE:
			self.resizeScreen()

		# Panel events
		for panel in self.panels:
			panel.events(e)

	# Resize screen
	def resizeScreen(self):
		self.screen = pygame.Surface(pygame.display.get_window_size())
		for panel in self.panels:
			panel.screen = self.screen

	def render(self):
		self.window.blit(self.screen, (0, 0))
		self.screen.fill((50, 50, 50))

		# Rendering the panel
		for panel in self.panels:
			panel.render()

