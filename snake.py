import pygame, sys, time, random
from pygame.locals import *

WHITE = (255,255,255)

class Snake():
    #making snake parts, we need a sprite class in main.py and add them to it I think
    #headbod is whether it is a head piece or a body piece
    def __init__(self,head_x,head_y,cords):
        self.head_x = head_x
        self.head_y = head_y
        self.cords = cords
        #add head to coords lists

        #Example of accessing coordinates from list
        #head_cords = self.coords[0]
        #head_coord[0]
        #head_coords[1]

    def bod_cords(self, snakes):
        return cords

    #making the snake head go up
    #adding the cordinate above the snake and removing the last piece
    def  snake_up(self,cords):
        self.cords.append((head_x,head_y-1))
        #remove

    #making the snake head go down
    def snake_down(self,cords):
        self.cords.append((head_x,head_y+1))
        #remove

    #making the snake head go left
    def snake_left(self,cords):
        self.cords.append((head_x-1,head_y))
        #remove

    #making the snake head go right
    def snake_right(self,cords):
        self.cords.append((head_x+1,head_y))
        #remove

    #gets head's previous location so first non-head piece can follow it
    #also saves its location for the piece that will come after it
    #def move2head(self,bod_x,bod_y):
    #    bod_x = self.rect.x
    #    bod_y = self.rect.y
    #    self.rect.x = head_x
    #    self.rect.y = head_y

    #bodxcheck and bodycheck store the snake piece's location, then moves to bod_x and bod_y, and then bod_x and bod_y become bodxcheck and bodycheck
    #def move2bod(self,bod_x,bod_y,bodxcheck,bodycheck):
    #    bodxcheck = self.rect.x
    #    bodycheck = self.rect.y
    #    self.rect.x = bod_x
    #    self.rect.y = bod_y
    #    bod_x = bodxcheck
    #    bod_y = bodycheck

    #finds out which way each part of  the snake should be moving
    #I need a timer in the main file
    #UDLR is a variable for determining which way it is going (up,down,left,right)
    #def snake_move(self, last_UDLR, UDLR):
    #    if self.headbod == 'head':
    #            if UDLR == 'up':
    #                if last_UDLR != 'down':
    #                    self.snake_up(head_x,head_y)
    #            elif UDLR == 'down':
    #                if last_UDLR != 'up':
    #                    self.snake_down(head_x,head_y)
    #            elif UDLR == 'left':
    #                if last_UDLR != 'right':
    #                    self.snake_left(head_x,head_y)
    #            elif UDLR == 'right':
    #                if last_UDLR != 'left':
    #                    self.snake_right(head_x,head_y)
    #        if self.headbod == 'bod':
    #                if check == 2:
    #                    self.move2head(bod_x,bod_y)
    #                else:
    #                    self.move2bod(bod_x,bod_y,bodxcheck,bodycheck)
    #                check += 1

    #displaying snake parts
    def update(self, snakes, screen):
        for snake in snakes:
            pygame.draw.rect(screen, WHITE, (self.rect.x,self.rect.y, 20, 20), 0)
