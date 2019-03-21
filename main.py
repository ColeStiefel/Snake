import pygame, sys, time, random
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREENLIGHT = (135,234,85)
GREENDARK = (59,227,7)
RED = (255, 0, 0)

WIDTH = 20
HEIGHT = 20
MARGIN = 2

clock = pygame.time.Clock()

WINDOW_SIZE = [400,290] #400 px by 300 px size of the window
screen = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption("Snake Game")  #Set the title at the top of the game

grid = []
for row in range(13):
    grid.append([])
    for column in range(18):
        grid[row].append((row, column))



color_one = 1
done = False
screen.fill(BLACK)

while not done:
    for row in range(13):
        for column in range(18):
                if color_one == 1:
                    pygame.draw.rect(screen, GREENLIGHT, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN , WIDTH, HEIGHT])
                    color_one = 0
                elif color_one == 0:
                    pygame.draw.rect(screen, GREENDARK, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
                    color_one = 1


        clock.tick(60)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()