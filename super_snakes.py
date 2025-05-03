# next steps:
# do the continous effect (head of snake continues moving in previous direction clicked instead of just moving 1 x 1)
# do the trailing effect (create sqaures behind the head of the snake as it moves in each direction)
# storing array for each head position, we will draw a rect with something like:
  # for each previous position of head with length of snake, draw a rect at these positions
    # this will continue updating continously as you play and increase length 
# create food + increasing length


#import pygame & Numpy & file code snake_icon
import pygame
import numpy as np
import snake_icon
from snake_icon import body_list, counter

#define function to create board and empty array board_squares to store position of each rectangle grid and to reference movement
board_squares = []

def board():
  #initialize all pygame modules
  pygame.init()
  #creates display window with parameters
  stage = pygame.display.set_mode((500,500))
  #define 2-D array 
  rows = 20
  cols = 20
  movement_cols = 9 #x-movement 
  movement_rows = 9 #y-movement
  body_y = 8
  body_x = 9
  direction = ""  
  running = False
  image_display = True 
  while image_display:
    display_image = pygame.image.load("initial_board_screenshot.png")
    display_image = pygame.transform.scale(display_image, (500,500))
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT and direction != 'L' and direction != 'U' and direction != 'D':
            direction = 'R'
            running = True
            image_display = False
    stage.blit(display_image, (0,0))
    pygame.display.flip()

#main game loop 
  while running:
    #loops through possible user interactions
    for event in pygame.event.get():
      #if user presses close button exits loop and display closes
      if event.type == pygame.QUIT:
        running = False
      #handling key pressing and assigning direction
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT and direction != 'L':
          direction = 'R'
          body_x = (square[1] / 25)
        elif event.key == pygame.K_LEFT and direction != 'R':
          direction = 'L'
          body_x = (square[1] / 25)
        elif event.key == pygame.K_UP and direction != 'D':
          direction = 'U'
          body_y = (square[0] / 25)
        elif event.key == pygame.K_DOWN and direction != 'U':
          direction = 'D'
          body_y = (square[0] / 25)
    #using the current assignment of direction to update position of the head and body    
    if direction == 'R':
      movement_cols += 1
      body_y += 1
    elif direction == 'L':
      movement_cols -= 1
      body_y -= 1
    elif direction == 'U':
      movement_rows -= 1
      body_x -= 1
    elif direction == 'D':
      movement_rows += 1
      body_x += 1
    
    #clearing screen
    stage.fill((255, 255, 255))

    #creating rectangle and defining position
    
    
    generating_board(stage, rows, cols)
    square = board_squares[movement_rows][movement_cols]
    snake_icon.create_snake(stage,body_y,body_x, square.center)

 
    pygame.display.update()
    pygame.time.Clock().tick(7)  
    pygame.display.flip()
    
  pygame.display.flip()

  pygame.quit()

def generating_board(stage, rows, cols):
  for j in range(rows):
      squares_row = []
      for i in range(cols):
          #creating the boder
          if i == 0 or i == 19 or j == 0 or j == 19:
            square = pygame.draw.rect(stage, (83,0,0), pygame.Rect(i*25,j*25,25,25))
            squares_row.append(square)
          elif (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
            #creating grid
            square = pygame.draw.rect(stage, (100,100,100), pygame.Rect(i*25,j*25,25,25))
            squares_row.append(square)
          elif (i % 2 != 0 and j % 2 == 0) or (i % 2 == 0 and j % 2 != 0):
            #creating grid
            square = pygame.draw.rect(stage, (0,100,100), pygame.Rect(i*25,j*25,25,25))
            squares_row.append(square)
      board_squares.append(squares_row)

#calling function
board()