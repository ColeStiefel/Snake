import pygame, sys, time, random
from pygame.locals import *

#creates a variable for the fruit
FRUIT = pygame.image.load('fruit.png')

#extends functionality from the sprite class, or something like that
class fruit(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        #takes the x and y values from the grid box that the fruit will be located in
        coordinate_x = box.x
        coordinate_y = box.y

        #does fruit stuff. image and rect/hitbox
        self.image = FRUIT
        self.rect = pygame.Rect(coordinate_x, coordinate_y, 10,10)

    def update(self, collected):
        if collected == True:
            self.kill()
            return snake_length + 1
