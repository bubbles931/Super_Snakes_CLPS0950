#import pygame & Numpy
import pygame as pgame
import numpy as np
import snake_icon
#define function to create board

board_squares = []

def board():
  #initialize all pygame modules
  pgame.init()
  #creates display window with parameters
  stage = pgame.display.set_mode((500,500))
  #define 2-D array 
  rows = 20
  cols = 20
  
  running = True

#main game loop 
  while running:
    #loops through possible user interactions
    for event in pgame.event.get():
      #if user presses close button exits loop and display closes
      if event.type == pgame.QUIT:
        running = False

    #clearing screen
    stage.fill((255, 255, 255))

    #creating rectangle and defining position
    
    for i in range(rows):
      for j in range(cols):
          if i == 0 or i == 19 or j == 0 or j == 19:
            square = pgame.draw.rect(stage, (83,0,0), pgame.Rect(i*25,j*25,25,25))
            board_squares.append(square)
          elif i % 2 == 0 and j % 2 == 0:
            #creating grid
            square = pgame.draw.rect(stage, (100,100,100), pgame.Rect(i*25,j*25,25,25))
            board_squares.append(square)
          elif i % 2 != 0 and j % 2 != 0:
            square = pgame.draw.rect(stage, (100,100,100), pgame.Rect(i*25,j*25,25,25))
            board_squares.append(square)
          elif i % 2 != 0 and j % 2 == 0:
            #creating grid
            square = pgame.draw.rect(stage, (0,100,100), pgame.Rect(i*25,j*25,25,25))
            board_squares.append(square)
          elif i % 2 == 0 and j % 2 != 0:
            square = pgame.draw.rect(stage, (0,100,100), pgame.Rect(i*25,j*25,25,25))
            board_squares.append(square)
    #print(len(board_squares))
    np_board_squares = np.array(board_squares)
    #print(len(np_board_squares))
    #board_squares2d = np_board_squares.reshape((20,20))
    snake_icon.create_snake(stage, board_squares[57].center)
    pgame.display.flip()


  pgame.quit()
#calling function
board()




