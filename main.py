import pygame, sys, time, random
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
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
        grid[row].append(0)

grid[1][5] = 1
#FRUIT = fruit()

#def spawn(FRUIT):
    #grid = random.randint(1,234)
    #screen.blit(FRUIT.image)

done = False
screen.fill(BLACK)
print(grid)
while not done:
    for row in range(13):
        for column in range(18):
            color = WHITE
            pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN , WIDTH, HEIGHT])

            clock.tick(60)

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
