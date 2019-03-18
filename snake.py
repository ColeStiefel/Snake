import pygame, sys, time, random
from pygame.locals import *
class Snake:
    #making snake parts, we need a sprite class in main.py and add them to it I think
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = WHITE
        self.rect = pygame.Rect(self.x,self.y,20,20)

    #making the snake part go up
    def  snake_up(self):
        self.rect.y -= 20

    #making the snake part go down
    def snake_down(self):
        self.rect.y += 20

    #finds out which way each part of  the snake should be moving
    #I need a timer in the main file
    #UDLR is a variable for determining which way it is going (up,down,left,right)
    def snake_move(self,UDLR):

    #displaying snake parts
    def update(self):
        display.draw.rect(screen, WHITE, (self.rect, 20, 20), 0)
