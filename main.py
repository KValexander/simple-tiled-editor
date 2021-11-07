# Import libraries
import pygame

# Import files
from config import *
from common import *

# Import classes
from map import Map
from assets import Assets
from operations import Operations

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

		# Dict of panels
		self.panels = {}
		self.panels["map"] = Map(self.screen, (SIZE[0] / 4, 0), (SIZE[0] * 0.75, SIZE[1] * 0.75), COLORS["GRAY"])
		self.panels["assets"] = Assets(self.screen, (0, 0), (SIZE[0] / 4, SIZE[1]), COLORS["TAUPEGRAY"])
		self.panels["operations"] = Assets(self.screen, (SIZE[0] / 4, SIZE[1] * 0.75), (SIZE[0] * 0.75, SIZE[1] / 4), COLORS["SPANISHGRAY"])

		# Call game loop
		self.gameloop()

	# Handling events
	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.end()

			# Panel events
			for key in self.panels:
				self.panels[key].panelEvents(event)
				# Panel selected
				if self.panels[key].hover:
					if event.type == pygame.MOUSEBUTTONUP:
						if mouseCollision(self.panels[key].xy, self.panels[key].wh, event.pos):
							self.panels[key].selected = True
				else: self.panels[key].selected = False

	# Updating data
	def update(self):
		# Frame rendering speed
		self.clock.tick(FPS)
		# Handling events
		self.events()

	# Rendering data
	def render(self):
		# Background color
		self.screen.fill(COLORS["WHITE"])

		# Rendering panels
		for key in self.panels:
			if self.panels[key].visible:
				self.panels[key].drawPanel()

		# Rendering grid on map
		self.panels["map"].drawGrid()

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
