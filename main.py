# Import libraries
import pygame
from pygame.locals import *

# Import files
from config import *
from common import *

# Import classes
from project import Project
from map import Map
from assets import Assets
from operations import Operations

# Main class
class Main:
	# Constructor
	def __init__(self):
		pygame.init();

		# Window
		self.window = pygame.display.set_mode(SIZE, RESIZABLE)
		pygame.display.set_caption("Simple tiled editor")

		# Window icon
		icon = loadImage("gui/icon.ico")
		pygame.display.set_icon(icon)

		# Loop variables
		self.running = True
		self.clock = pygame.time.Clock()

		# Screen list
		self.screens = []
		self.screens.append(Project("Project screen"))

		# Run game loop
		self.run()

	# Handling events
	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.end()

			# SCREEN EVENTS
			if len(self.screens) != 0:
				for screen in self.screens:
					if not screen.disabled:
						screen.screenEvents(event)

	# Updating data
	def update(self):

		# UPDATING SCREENS
		if len(self.screens) != 0:
			for screen in self.screens:
				if not screen.disabled:
					screen.updateScreen()

		# Handling events
		self.events()

	# Rendering data
	def render(self):
		# Background color
		self.window.fill((50, 50, 50))

		# RENDERING SCREENS
		if len(self.screens) != 0:
			for screen in self.screens:
				if not screen.disabled:
					screen.renderScreen(self.window)

		pygame.display.update()
		# Frame rendering speed
		self.clock.tick(FPS)

	# Game loop
	def run(self):
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
