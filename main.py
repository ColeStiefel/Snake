import pygame, sys, time, random
from pygame.locals import *
from fruit import fruit
from snake import Snake

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREENLIGHT = (124,252,0)
GREENDARK = (50,205,50)
RED = (255, 0, 0)


WIDTH = 20
HEIGHT = 20
MARGIN = 2

snake_ob = Snake(4,6,WHITE,'head')
snakes = []
UDLR = 'right'

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
def draw_board(color_one):
    for row in range(14):
        for column in range(19):
                if color_one == 1:
                    pygame.draw.rect(screen, GREENLIGHT, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN , WIDTH, HEIGHT])
                    color_one = 0
                elif color_one == 0:
                    pygame.draw.rect(screen, GREENDARK, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
                    color_one = 1

def udlr(udlr):
    if event.type == K_UP:
        UDLR = 'up'
    if event.type == K_DOWN:
        UDLR = 'down'
    if event.type == K_LEFT:
        UDLR = 'left'
    if event.type == K_RIGHT:
        UDLR = 'right'


def spawn(FRUIT):
    grid = random.randint(1,234)
    screen.blit(FRUIT.image)
#if (row, column) == apple:
    #pygame.draw.rect(screen, (255, 0, 0), [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN , WIDTH, HEIGHT])
#apple = (0, 0)

def add_fruit():
    FRUIT = fruit()
    good_stuff.add(FRUIT)


def spawn():
    grid_x = random.randint(0,12)
    grid_y = random.randint(0,17)
    screen.blit(FRUIT.image, FRUIT.rect)
    if pygame.sprite.spritecollideany(FRUIT, snakes) == True:
        FRUIT.update(True)
    elif pygame.sprite.spritecollideany(FRUIT, snakes) == False:
        FRUIT.update(False)


color_one = 1
done = False
screen.fill(BLACK)
#print(grid)
#The game loop undernearth will define the colors of the grid, the cords are displayed with the variable "grid". Margin, Width, and Height are defined above
while not done:
    draw_board(color_one)

    clock.tick(60) #60 fps

    spawn()

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        udlr(udlr)

        snake_ob.snake_move(UDLR, snakes)
        snake_ob.update(snakes)
