import pygame

from Assets.constants import *

pygame.init()

#Maintains the floor and all relevant info
class FloorInterface:
    def __init__(self, environment, height):
        self.screen = environment.getScreen()

        #Relevant classes
        self.environment = environment

        #Define dimensions and location of floor
        self.width = self.screen.get_width()
        self.height = height

        self.x = (.5)*(self.screen.get_width() - self.width)
        self.y = (self.screen.get_height() - self.height)

    #Displays the floor on the screen
    def draw(self):
        pygame.draw.rect(self.screen, D_GREY, pygame.Rect(self.x, self.y, self.width, self.height))

    #GETTERS

    def getRect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def getHeight(self):
        return self.height