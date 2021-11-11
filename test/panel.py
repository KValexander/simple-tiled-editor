import pygame
from pygame.locals import *

class Panel:
	def __init__(self, screen, name, xy, wh):
		self.screen = screen
		self.name = name
		self.xy = xy
		self.wh = wh

		self.panel = pygame.Surface(self.wh)

	def events(self, e):
		if e.type == VIDEORESIZE:
			print(self.wh, self.screen.get_size(), self.screen.get_rect().size, pygame.display.get_window_size())

	def render(self):
		self.screen.blit(self.panel, self.xy)
		self.panel.fill((100, 100, 100))

