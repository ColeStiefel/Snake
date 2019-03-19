import pygame, sys, time, random
from pygame.locals import *
class Snake:
    #making snake parts, we need a sprite class in main.py and add them to it I think
    def __init__(self,x,y,color,headbod):
        self.x = x
        self.y = y
        self.color = BLUE
        self.headbod = headbod
        self.rect = pygame.Rect(self.x,self.y,20,20)

    #making the snake part go up
    def  snake_up(self):
        self.rect.y -= 24

    #making the snake part go down
    def snake_down(self):
        self.rect.y += 24

    #making the snake part go left
    def snake_left(self):
        self.rect.x -= 24

    #making the snake part go right
    def snake_right(self):
        self.rect.x += 24

    #finds out which way each part of  the snake should be moving
    #I need a timer in the main file
    #UDLR is a variable for determining which way it is going (up,down,left,right)
    def snake_move(self,UDLR):
        if self.headbod == 'head':
            if UDLR == 'up':
                snake_up(self)
            if UDLR == 'down':
                snake_down(self):
            if UDLR == 'left':
                snake_left(self):
            if UDLR == 'right':
                snake_right(self)
        if self.headbod == 'bod':
            for n in snakes

    #displaying snake parts
    def update(self):
        display.draw.rect(screen, WHITE, (self.rect, 20, 20), 0)
