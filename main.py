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

head_x = 2
head_y = 2
snake_ob = Snake(2,2,WHITE,'head')
snakes = []
snakes.append(snake_ob)
UDLR = 'placeholder'
last_UDLR = 'placeholder'

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
FRUIT = fruit(6, 10)
def draw_board(color_one):
    for row in range(14):
        for column in range(19):
                if color_one == 1:
                    pygame.draw.rect(screen, GREENLIGHT, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN , WIDTH, HEIGHT])
                    color_one = 0
                elif color_one == 0:
                    pygame.draw.rect(screen, GREENDARK, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
                    color_one = 1

#finds out which way the snake is going and uses it for the snake.py movement fnc
def udlr(UDLR, last_UDLR):
    if event.key == K_UP:
        if UDLR != 'up':
            last_UDLR = UDLR
            UDLR = 'up'
    elif event.key == K_DOWN:
        if UDLR != 'down':
            last_UDLR = UDLR
            UDLR = 'down'
    elif event.key == K_LEFT:
        if UDLR != 'left':
            last_UDLR = UDLR
            UDLR = 'left'
    elif event.key == K_RIGHT:
        if UDLR != 'right':
            last_UDLR = UDLR
            UDLR = 'right'

def draw_apple():
    global FRUIT
    FRUIT.image = pygame.transform.scale(FRUIT.image,(20,50))
    grid = random.randint(1,234)
    screen.blit(FRUIT.image, FRUIT.rect)
#if (row, column) == apple:
    #pygame.draw.rect(screen, (255, 0, 0), [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN , WIDTH, HEIGHT])
#apple = (0, 0)

def add_fruit():
    good_stuff.add(FRUIT)


def spawn_apple():
    x_value = random.randint(0,12)
    y_value = random.randint(0,17)
    grid_x = x_value
    grid_y = y_value
    FRUIT = fruit(grid_x, grid_y)
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

    snake_ob.bod_cords(snakes)

    clock.tick(3) #60 fps

    spawn_apple()

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            udlr(UDLR, last_UDLR)

    snake_ob.snake_move(UDLR, last_UDLR, snakes)
    snake_ob.update(snakes, screen)
    pygame.display.update()
