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
		self.panels = []
		# Panel Map
		self.panels.append(Map(self.screen, (SIZE[0] / 4, 0), (SIZE[0] * 0.75, SIZE[1] * 0.75), COLORS["GRAY"]))
		# Panel Assets
		self.panels.append(Assets(self.screen, (0, 0), (SIZE[0] / 4, SIZE[1]), COLORS["TAUPEGRAY"]))
		# Panel Operations
		self.panels.append(Operations(self.screen, (SIZE[0] / 4, SIZE[1] * 0.75), (SIZE[0] * 0.75, SIZE[1] / 4), COLORS["SPANISHGRAY"]))

		# Call game loop
		self.gameloop()

	# Handling events
	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.end()

			# Panel events
			for panel in self.panels:
				if not panel.disabled:
					panel.panelEvents(event)
					# Panel selected
					if panel.hover:
						if event.type == pygame.MOUSEBUTTONDOWN:
							if mouseCollision(panel.xy, panel.wh, event.pos):
								panel.selected = True
					else: panel.selected = False

	# Updating data
	def update(self):
		# Frame rendering speed
		self.clock.tick(FPS)

		# Updating panels
		for panel in self.panels:
			if not panel.disabled:
				panel.updatePanel()

		# Handling events
		self.events()

	# Rendering data
	def render(self):
		# Background color
		self.screen.fill(COLORS["WHITE"])

		# Rendering panels
		for panel in self.panels:
			if not panel.disabled:
				panel.renderPanel()

		pygame.display.update()

	# Game loop
	def gameloop(self):
		while self.running:
			self.update()
			self.render()

	# Stopping the game loop
	def end(self):
		self.running = False

# Start app
if __name__ == "__main__":
	main = Main()
	pygame.quit()
