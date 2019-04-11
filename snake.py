import pygame, sys, time, random
from pygame.locals import *

WHITE = (255,255,255)

#variable that will track the head's x and y
head_x = 0
head_y = 0

class Snake():
    #making snake parts with the head_x and head_y being the head's x and y, and cords being a list of the snake's coordinates
    def __init__(self,head_x,head_y,cords):
        self.head_x = head_x
        self.head_y = head_y
        self.cords = cords

    #returns the coordinates list
    def bod_cords(self):
        return self.cords

    #making the snake head go up
    #adding the cordinate above the snake and removing the last piece
    def  snake_up(self,removecheck):
        if removecheck == 0:
            self.cords.remove(self.cords[len(self.cords)-1])
        self.cords.append((self.head_x,self.head_y-1))
        self.head_y -= 1

    #making the snake head go down
    def snake_down(self,removecheck):
        if removecheck == 0:
            self.cords.remove(self.cords[len(self.cords)-1])
        self.cords.append((self.head_x,self.head_y+1))
        self.head_y += 1

    #making the snake head go left
    def snake_left(self,removecheck):
        if removecheck == 0:
            self.cords.remove(self.cords[len(self.cords)-1])
        self.cords.append((self.head_x-1,self.head_y))
        self.head_x -= 1

    #making the snake head go right
    def snake_right(self,removecheck):
        if removecheck == 0:
            self.cords.remove(self.cords[len(self.cords)-1])
        self.cords.append((self.head_x+1,self.head_y))
        self.head_x += 1
