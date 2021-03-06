import pygame, sys, time, random
from pygame.locals import *
from fruit import fruit
from snake import Snake

pygame.init()
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

#list of coordinates and adding the first coordinate to it
cords = []
cords.append((0,0))
head_x = 0
head_y = 0
#making snake object
snake_ob = Snake(0,0,cords)
#UDLR determines if the snake is going Up, Down, Left, or Right
UDLR = 'placeholder'
#last_UDLR keeps track of the last direction the snake was going, so it can continue to go in that direction
last_UDLR = 'placeholder'
#movecheck determines if the snake's direction was changed in a given iteration, so it continues to move without a key being pressed
movecheck = 0
#sees if it ate a fruit on a given iteration, indicating whether or not to remove the last coordinate from the list, which is what causes the snake to grow
removecheck = 0
BASICFONT = pygame.font.Font('freesansbold.ttf', 50)
Surf = BASICFONT.render("Gameover", 1, (0,0,0))

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

#makes the snake continue moving in the same direction when there has not been any change in direction given
def noudlrmove():
    global removecheck
    if last_UDLR == 'up':
        snake_ob.snake_up(removecheck)
    if last_UDLR == 'down':
        snake_ob.snake_down(removecheck)
    if last_UDLR == 'left':
        snake_ob.snake_left(removecheck)
    if last_UDLR == 'right':
        snake_ob.snake_right(removecheck)

#draws the apple where the rect says it is and makes the appple scale to the right size
def draw_apple():
    global FRUIT
    FRUIT.image = pygame.transform.scale(FRUIT.image,(15,20))
    screen.blit(FRUIT.image, FRUIT.rect)

def add_fruit():
    good_stuff.add(FRUIT)

#makes the fruit object
FRUIT = fruit(9,10)

#checks for collisions
def is_apple():
    return (FRUIT.grid_x, FRUIT.grid_y) in snake_ob.cords

def spawn_apple():
    global FRUIT
    FRUIT.grid_x = random.randint(0,18)
    FRUIT.grid_y = random.randint(0,13)
    FRUIT.rect.x = (MARGIN + WIDTH) * FRUIT.grid_x + MARGIN
    FRUIT.rect.y = (MARGIN + HEIGHT) * FRUIT.grid_y + MARGIN


#This is a function which defines the "wall" which in the end is going to make it as the snake hits the wall, the game ends
color_one = 1
done = False
screen.fill(BLACK)
game = True
def iswall(): #still have to add the snake variable to the code
    global game
    if snake_ob.cords[0][0] not in range (0,19) or snake_ob.cords[0][1] not in range (0,14):
        game = False

def insnake():
    global game
    for x in range (1,len(cords)):
        if snake_ob.cords[x] == snake_ob.cords[0]:
            game = False

spawn_apple()

#The game loop undernearth will define the colors of the grid, the cords are displayed with the variable "grid". Margin, Width, and Height are defined above
while True:
    if game == True:
        #defining these variables for each iteration
        movecheck = 0
        removecheck = 0
        draw_board(color_one)

        clock.tick(5) #5 fps

        #has an apple been eater? If so spawn a new apple and change the variable so the snake will grow
        if is_apple() == True:
            spawn_apple()
            removecheck = 1

        #draws the new apple
        draw_apple()

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                #if the up key is pressed
                if event.key == K_UP:
                    #making sure it is not going down (it cannot being going one way and then immediately go the other direction)
                    if UDLR != 'down':
                        #showing that a change in direction did happen, so it should not execute noudlrmove()
                        movecheck = 1
                        #showing that it is now going up
                        UDLR = 'up'
                elif event.key == K_DOWN:
                    if UDLR != 'up':
                        movecheck = 1
                        UDLR = 'down'
                elif event.key == K_LEFT:
                    if UDLR != 'right':
                        movecheck = 1
                        UDLR = 'left'
                elif event.key == K_RIGHT:
                    if UDLR != 'left':
                        movecheck = 1
                        UDLR = 'right'
                last_UDLR = UDLR
        iswall()
        insnake()
        #if it did not move, make it continue in that direction
        noudlrmove()
        #drawing all the coordinates in cords
        for coords in snake_ob.cords:
            pygame.draw.rect(screen, WHITE, [(MARGIN + WIDTH) * coords[0] + MARGIN, (MARGIN + HEIGHT) * coords[1] + MARGIN , WIDTH, HEIGHT])
    else:
        screen.blit(Surf,(88 ,110))  #displays the gameover screen
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    pygame.display.update()
