import pygame, sys, time, random
from pygame.locals import *

#creates a variable for the fruit
FRUIT = pygame.image.load('fruit.png')

#extends functionality from the sprite class, or something like that
class fruit(pygame.sprite.Sprite):

    def __init__(self, box_x, box_y):
        super().__init__()

        #takes the x and y values from the grid box that the fruit will be located in
        self.grid_x = box_x
        self.grid_y = box_y

        #does fruit stuff. image and rect/hitbox
        self.image = FRUIT
        self.rect = pygame.Rect(self.grid_x, self.grid_y, 10,10)
