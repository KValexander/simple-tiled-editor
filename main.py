# Import libraries
import pygame

# Import files
from config import *

# Import classes
from map import Map
from assets import Assets

# Main class
class Main:
	# Constructor
	def __init__(self):
		pygame.init();

		# Window
		self.screen = pygame.display.set_mode(SIZE)
		pygame.display.set_caption("Simple tiled editor")

		# Loop variables
		self.running = True
		self.clock = pygame.time.Clock()

		# Instantiating classes
		self.map = Map(self.screen)
		self.assets = Assets(self.screen)

		# Call game loop
		self.gameloop()

	# Handling events
	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.end()

			# Map events
			self.map.events(event)

	# Updating data
	def update(self):
		# Frame rendering speed
		self.clock.tick(FPS)
		# Handling events
		self.events()

	# Rendering data
	def render(self):
		self.screen.fill(COLORS["BLACK"])

		# Rendering cells
		self.map.drawCells(self.screen)

		pygame.display.update()

	# Game loop
	def gameloop(self):
		while self.running:
			self.update()
			self.render()

	# Stopping the game loop
	def end(self):
		self.running = False

main = Main()
pygame.quit()
