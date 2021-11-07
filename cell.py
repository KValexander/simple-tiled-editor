# Import libraries
import pygame

# Class Сell
class Cell:
	# Constructor
	def __init__(self, xy, size, color, border=1):
		# Custom variables
		self.xy = xy
		self.x = xy[0]
		self.y = xy[1]
		self.size = size
		self.color = color
		self.border = border

		# Boolean variables
		self.hover = False
		self.click = False

		# Default variables
		self.wh = (self.size, self.size)
		self.alpha = 128

		# Instances of classes
		self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
		self.surface = pygame.Surface(self.wh)
		self.surface.fill(self.color)
		self.surface.set_alpha(self.alpha)

	# Rendering cell
	def draw(self, screen):
		pygame.draw.rect(screen, self.color, self.rect, self.border)
		# When you hover the mouse over a cell
		if self.hover or self.click:
			screen.blit(self.surface, self.xy)
