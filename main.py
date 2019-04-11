import pygame, sys, time, random
from pygame.locals import *
from fruit import fruit
from snake import Snake
#Defines all the colors used in the snake game (Such as the board, the snake, the margins, and the fruit)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREENLIGHT = (124,252,0)
GREENDARK = (50,205,50)
RED = (255, 0, 0)

#These are the dimensions of each cell on the board)
WIDTH = 20
HEIGHT = 20
MARGIN = 2

cords = []
cords.append((0,0))
head_x = 0
head_y = 0
snake_ob = Snake(0,0,cords)
#snakes = pygame.sprite.Group()
#snakes.add(snake_ob)
UDLR = 'placeholder'
last_UDLR = UDLR
movecheck = 0
#Surf = BASICFONT.render("Gameover", 1, (0,0,0))

clock = pygame.time.Clock()

WINDOW_SIZE = [420,310] #420 px by 310 px size of the window
screen = pygame.display.set_mode(WINDOW_SIZE) #Defines screen as the board size

pygame.display.set_caption("Snake Game")  #Set the title at the top of the game

#defines the grid for snake game later on, in order to make it easier for the snake to move
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
        if UDLR != 'down':
            movecheck = 1
            UDLR = 'up'
            snake_ob.snake_up()
    elif event.key == K_DOWN:
        if UDLR != 'up':
            movecheck = 1
            UDLR = 'down'
            snake_ob.snake_down()
    elif event.key == K_LEFT:
        if UDLR != 'right':
            movecheck = 1
            UDLR = 'left'
            snake_ob.snake_left()
    elif event.key == K_RIGHT:
        if UDLR != 'left':
            movecheck = 1
            UDLR = 'right'
            snake_ob.snake_right()
    last_UDLR = UDLR

def noudlrmove():
    if last_UDLR == 'up':
        snake_ob.snake_up()
    if last_UDLR == 'down':
        snake_ob.snake_down()
    if last_UDLR == 'left':
        snake_ob.snake_left()
    if last_UDLR == 'right':
        snake_ob.snake_right()

def draw_apple():
    global FRUIT
    FRUIT.image = pygame.transform.scale(FRUIT.image,(15,20))
    screen.blit(FRUIT.image, FRUIT.rect)
#if (row, column) == apple:
    #pygame.draw.rect(screen, (255, 0, 0), [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN , WIDTH, HEIGHT])
#apple = (0, 0)

def add_fruit():
    good_stuff.add(FRUIT)

FRUIT = fruit(9,10)

def is_apple():
    if pygame.sprite.spritecollideany(FRUIT, cords):
        return True
    else:
        return False
    #return pygame.sprite.spritecollideany(FRUIT, snakes)
    #return (FRUIT.grid_x, FRUIT.grid_y) in snake_ob.cords

grid_y_values = [288, 266, 244, 222, 200, 178, 156, 134, 112, 90, 68, 46, 24, 2]
grid_x_values = [398, 376, 354, 332, 310, 288, 266, 244, 222, 200, 178, 156, 134, 112, 90, 68, 46, 24, 2]

def spawn_apple():
    global FRUIT
    FRUIT.grid_x = grid_x_values[random.randint(0,12)]
    FRUIT.grid_y = grid_y_values[random.randint(0,17)]
    FRUIT.rect.x = (MARGIN + WIDTH) * FRUIT.grid_x + MARGIN
    FRUIT.rect.y = (MARGIN + HEIGHT) * FRUIT.grid_y + MARGIN


#This is a function which defines the "wall" which in the end is going to make it as the snake hits the wall, the game ends
color_one = 1
done = False
screen.fill(BLACK)
game = True
def iswall(): #still have to add the snake variable to the code
    if snake_ob.cords[0][0] not in range (0,14) or snake_ob.cords[0][1] not in range (0,19):
        game = False




#print(grid)
#The game loop undernearth will define the colors of the grid, the cords are displayed with the variable "grid". Margin, Width, and Height are defined above
while not done:
    movecheck = 0
    draw_board(color_one)

    clock.tick(3) #60 fps

    if is_apple() == True:
        spawn_apple()

    draw_apple()

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                if UDLR != 'down':
                    movecheck = 1
                    UDLR = 'up'
                    snake_ob.snake_up()
            elif event.key == K_DOWN:
                if UDLR != 'up':
                    movecheck = 1
                    UDLR = 'down'
                    snake_ob.snake_down()
            elif event.key == K_LEFT:
                if UDLR != 'right':
                    movecheck = 1
                    UDLR = 'left'
                    snake_ob.snake_left()
            elif event.key == K_RIGHT:
                if UDLR != 'left':
                    movecheck = 1
                    UDLR = 'right'
                    snake_ob.snake_right()
            last_UDLR = UDLR

    if movecheck == 0:
        noudlrmove()
    check = 0
    for coords in snake_ob.cords:
        #pygame.draw.rect(screen,WHITE,(grid[0][0],20,20))
        pygame.draw.rect(screen, WHITE, [(MARGIN + WIDTH) * coords[0] + MARGIN, (MARGIN + HEIGHT) * coords[1] + MARGIN , WIDTH, HEIGHT])
        check += 1
    pygame.display.update()
