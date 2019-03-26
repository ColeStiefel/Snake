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

    #making the snake head go up
    #headx and heady save the head's location so it can be used for the following piece
    def  snake_up(self,head_x,head__y):
        head_x = self.rect.x
        head_y = self.rect.y
        self.rect.y -= 24

    #making the snake head go down
    def snake_down(self,head_x,head_y):
        head_x = self.rect.x
        head_y = self.rect.y
        self.rect.y += 24

    #making the snake head go left
    def snake_left(self,head_x,head_y):
        head_x = self.rect.x
        head_y = self.rect.y
        self.rect.x -= 24

    #making the snake head go right
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

    #bodxcheck and bodycheck store the snake piece's location, then moves to bod_x and bod_y, and then bod_x and bod_y become bodxcheck and bodycheck
    def move2bod(self,bod_x,bod_y,bodxcheck,bodycheck):
        bodxcheck = self.rect.x
        bodycheck = self.rect.y
        self.rect.x = bod_x
        self.rect.y = bod_y
        bod_x = bodxcheck
        bod_y = bodycheck

    #finds out which way each part of  the snake should be moving
    #I need a timer in the main file
    #UDLR is a variable for determining which way it is going (up,down,left,right)
    def snake_move(self,UDLR, snakes):
        if self.headbod == 'head':
            if UDLR == 'up':
                self.snake_up(head_x,head_y)
            elif UDLR == 'down':
                self.snake_down(head_x,head_y):
            elif UDLR == 'left':
                self.snake_left(head_x,head_y):
            elif UDLR == 'right':
                self.snake_right(head_x,head_y)
        if self.headbod == 'bod':
            #check determines how far down the body the piece is
            check = 1
            for x in snakes:
                if check == 1:
                    self.move2head(bod_x,bod_y)
                else:
                    self.move2bod(bod_x,bod_y,bodxcheck,bodycheck)
                check += 1

    #displaying snake parts
    def update(self):
        display.draw.rect(screen, WHITE, (self.rect, 20, 20), 0)
