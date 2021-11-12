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
	def __init__(self,name):
		super().__init__(name)

		# Panel Map
		panel = Map("Map", (self.screen.get_size()[0] / 4, 0), (self.screen.get_size()[0] * 0.75, self.screen.get_size()[1] * 0.75), COLORS["GRAY"])
		panel.addInscription("ins1", (10, 10), "Grid", 100, COLORS["WHITE"])
		# panel.deleteElement("ins1")
		self.panels.append(panel)

		# Panel Operations
		panel = Operations("Operations", (self.screen.get_size()[0] / 4, self.screen.get_size()[1] * 0.75), (self.screen.get_size()[0] * 0.75, self.screen.get_size()[1] / 4), COLORS["SPANISHGRAY"])
		panel.addButton("btn1", (10, 30), (100, 30), "GRID")
		self.panels.append(panel)

		# Panel Assets
		panel = Assets("Assets", (0, 0), (self.screen.get_size()[0] / 4, self.screen.get_size()[1]), COLORS["TAUPEGRAY"])
		self.panels.append(panel)
