import pygame, sys, time, random
from pygame.locals import *
from fruit import fruit
#from snake import Snake

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREENLIGHT = (135,234,85)
GREENDARK = (0,100,0)
RED = (255, 0, 0)


WIDTH = 20
HEIGHT = 20
MARGIN = 2

UDLR = 'right'
snake_ob = Snake(4,6,BLUE,head)
snakes = pygame.sprite.Group()
snakes.add(snake_ob)

clock = pygame.time.Clock()

WINDOW_SIZE = [420,310] #400 px by 300 px size of the window
screen = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption("Snake Game")  #Set the title at the top of the game

grid = []
for row in range(14):
    grid.append([])
    for column in range(19):
        grid[row].append((row, column))

good_stuff = pygame.sprite.Group()
FRUIT = fruit()
def add_fruit():
    FRUIT = fruit()
    good_stuff.add(FRUIT)


def spawn():
    where = random.randint(1,234)
    screen.blit(FRUIT.image, FRUIT.rect)
    print(where)
    if pygame.sprite.spritecollideany(FRUIT, SNAKE) == True:
        FRUIT.update(True)
    elif pygame.sprite.spritecollideany(FRUIT, SNAKE) == True:
        FRUIT.update(False)

color_one = 1
done = False
screen.fill(BLACK)
#print(grid)
#The game loop undernearth will define the colors of the grid, the cords are displayed with the variable "grid". Margin, Width, and Height are defined above
while not done:
    for row in range(14):
        for column in range(19):
                if color_one == 1:
                    pygame.draw.rect(screen, GREENLIGHT, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN , WIDTH, HEIGHT])
                    color_one = 0
                elif color_one == 0:
                    pygame.draw.rect(screen, GREENDARK, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
                    color_one = 1


        clock.tick(60) #60 fps

        spawn()
        #print(where)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == K_UP:
                UDLR = 'up'
            if event.type == K_DOWN:
                UDLR = 'down'
            if event.type == K_RIGHT:
                UDLR = 'right'
            if event.type == K_LEFT:
                UDLR = 'left'
