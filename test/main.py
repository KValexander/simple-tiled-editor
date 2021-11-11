import pygame, sys
from pygame.locals import *

from screen import Screen

class Main:
	def __init__(self):
		pygame.init()

		self.window = pygame.display.set_mode((800, 600), RESIZABLE)
		pygame.display.set_caption("Test")

		# Screens
		self.screens = []
		self.addScreenAndPanels()

		self.clock = pygame.time.Clock()
		self.running = True
		self.run()

	# Adding basic elements
	def addScreenAndPanels(self):
		screen = Screen(self.window, "Test screen")
		screen.addPanel("Test panel", (0,0), (100, 100))
		self.screens.append(screen)

	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False

			# Screen events
			for screen in self.screens:
				screen.events(event)

	def render(self):
		self.window.fill((255,255,255))

		# Rendering the screen
		for screen in self.screens:
			screen.render()

		pygame.display.update()
		self.clock.tick(30)

	def run(self):
		while self.running:
			self.events()
			self.render()

if __name__ == "__main__":
	main = Main()
	pygame.quit()
	sys.exit()