import pygame, sys, time, random
from pygame.locals import *
class Snake:
    #making snake parts, we need a sprite class in main.py and add them to it I think
    #headbod is whether it is a head piece or a body piece
    def __init__(self,x,y,color,headbod):
        self.x = x
        self.y = y
        self.color = BLUE
        self.headbod = headbod
        self.rect = pygame.Rect(self.x,self.y,20,20)

    #making the snake part go up
    #headx and heady save the head's location so it can be used for the following piece
    def  snake_up(self,head_x,head__y):
        head_x = self.rect.x
        head_y = self.rect.y
        self.rect.y -= 24

    #making the snake part go down
    def snake_down(self,head_x,head_y):
        head_x = self.rect.x
        head_y = self.rect.y
        self.rect.y += 24

    #making the snake part go left
    def snake_left(self,head_x,head_y):
        head_x = self.rect.x
        head_y = self.rect.y
        self.rect.x -= 24

    #making the snake part go right
    def snake_right(self,head_x,head_y):
        head_x = self.rect.x
        head_y = self.rect.y
        self.rect.x += 24

    #gets head's previous location so first non-head piece can follow it
    #also saves its location for the piece that will come after it
    def move2head(self,bod_x,bod_y):
        bod_x = self.rect.x
        bod_y = self.rect.y
        self.rect.x = head_x
        self.rect.y = head_y

    #finds out which way each part of  the snake should be moving
    #I need a timer in the main file
    #UDLR is a variable for determining which way it is going (up,down,left,right)
    def snake_move(self,UDLR, snakes):
        if self.headbod == 'head':
            if UDLR == 'up':
                snake_up(self,head_x,head_y)
            if UDLR == 'down':
                snake_down(self,head_x,head_y):
            if UDLR == 'left':
                snake_left(self,head_x,head_y):
            if UDLR == 'right':
                snake_right(self,head_x,head_y)
        if self.headbod == 'bod':
            #check works as an index for the snake list
            check = 1
            for x in snakes:
                if check == 1:
                    get_head(self,bod_x,bod_y)
                else:
                    snakes[check].rect = rectsaver
                check += 1



    #displaying snake parts
    def update(self):
        display.draw.rect(screen, WHITE, (self.rect, 20, 20), 0)
