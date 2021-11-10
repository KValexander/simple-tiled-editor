# Import libraries
import pygame

# Import files
from config import *
from common import *

# Import classes
from screen import Screen
from map import Map
from assets import Assets
from operations import Operations

# Class Screen
class Project(Screen):
	# Constructor
	def __init__(self, window, name):
		super().__init__(window, name)

		# Panel Map
		self.panels.append(Map(self.screen, "Map", (self.screen.get_size()[0] / 4, 0), (self.screen.get_size()[0] * 0.75, self.screen.get_size()[1] * 0.75), COLORS["GRAY"]))
		# Panel Operations
		self.panels.append(Operations(self.screen, "Operations", (self.screen.get_size()[0] / 4, self.screen.get_size()[1] * 0.75), (self.screen.get_size()[0] * 0.75, self.screen.get_size()[1] / 4), COLORS["SPANISHGRAY"]))
		# Panel Assets
		self.panels.append(Assets(self.screen, "Assets", (0, 0), (self.screen.get_size()[0] / 4, self.screen.get_size()[1]), COLORS["TAUPEGRAY"]))
