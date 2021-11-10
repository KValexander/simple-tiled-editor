# Import libraries
import pygame
from pygame.locals import *

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
		self.window = pygame.display.set_mode(SIZE, RESIZABLE)
		pygame.display.set_caption("Simple tiled editor")

		# Window icon
		icon = loadImage("gui/icon.ico")
		pygame.display.set_icon(icon)

		# Loop variables
		self.running = True
		self.clock = pygame.time.Clock()

		# Panel List
		self.panels = []
		# Panel Map
		self.panels.append(Map(self.window, "Map", (SIZE[0] / 4, 0), (SIZE[0] * 0.75, SIZE[1] * 0.75), COLORS["GRAY"]))
		# Panel Operations
		self.panels.append(Operations(self.window, "Operations", (SIZE[0] / 4, SIZE[1] * 0.75), (SIZE[0] * 0.75, SIZE[1] / 4), COLORS["SPANISHGRAY"]))
		# Panel Assets
		self.panels.append(Assets(self.window, "Assets", (0, 0), (SIZE[0] / 4, SIZE[1]), COLORS["TAUPEGRAY"]))

		# Buffer list
		self.bufferList = []

		# Selected panel number
		self.panelSelected = 0

		# Run game loop
		self.run()

	# Handling events
	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.end()

			# Panel events
			for i, panel in enumerate(self.panels, 1):
				# If the panel is not disabled
				if not panel.disabled:
					panel.panelEvents(event)
					# MOUSEBUTTONDOWN
					if event.type == pygame.MOUSEBUTTONDOWN:
						# If panel not selected
						if self.panelSelected != i:
							if mouseCollision(panel.xy, panel.wh, event.pos):
								for pnl in self.panels:
									pnl.selected = False
								panel.selected = True
								self.panelSelected = i

	# Updating data
	def update(self):
		# Frame rendering speed
		self.clock.tick(FPS)

		# Sorting the list of panels
		for i, panel in enumerate(self.panels, 1):
			if not panel.disabled:
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
			panel.updatePanel()

		# Handling events
		self.events()

	# Rendering data
	def render(self):
		# Background color
		self.window.fill(COLORS["BACKGROUND"])

		# Rendering panels
		for panel in self.panels:
			panel.renderPanel()

		pygame.display.update()

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
