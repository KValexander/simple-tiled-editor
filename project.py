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

		self.asset = None

		# Panel Map
		panel = Map(self, "Map", (self.screen.get_size()[0] / 4, 0), (self.screen.get_size()[0] * 0.75, self.screen.get_size()[1] * 0.75), COLORS["GRAY"])
		panel.addInscription("grid", (10, 10), "Grid", 100, COLORS["WHITE"])
		self.panels.append(panel)

		# Panel Operations
		panel = Operations(self, "Operations", (self.screen.get_size()[0] / 4, self.screen.get_size()[1] * 0.75), (self.screen.get_size()[0] * 0.75, self.screen.get_size()[1] / 4), COLORS["SPANISHGRAY"])
		self.panels.append(panel)

		# Panel Assets
		panel = Assets(self, "Assets",(0, 0), (self.screen.get_size()[0] / 4, self.screen.get_size()[1]), COLORS["TAUPEGRAY"])
		panel.addInputBox("pathToAssets", (10, 30), (panel.wh[0] - 20, 30), 20)
		panel.getElement("pathToAssets").text = "assets/"
		panel.addButton("load", (10, 70), (100, 30), "Load", 16)
		panel.addButton("reset", (120, 70), (100, 30), "Reset", 16)
		panel.addButton("clear", (panel.wh[0] - 110, 70), (100, 30), "Clear", 16)
		self.panels.append(panel)
