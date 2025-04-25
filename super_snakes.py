#import pygame & Numpy
import pygame as pgame
import numpy as np
#define function to create board

board_squares = []

def board():
  #initialize all pygame modules
  pgame.init()
  #creates display window with parameters
  stage = pgame.display.set_mode((900,900))
  #define 2-D array 
  rows = 9
  cols = 9
  

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
      square_row = []
      for j in range(cols):
          if i == 0 or i == 8 or j == 0 or j == 8:
            square = pgame.draw.rect(stage, (83,0,0), pgame.Rect(i*100,j*100,100,100))
            square_row.append(square)
          elif i % 2 == 0 and j % 2 == 0:
            #creating grid
            square = pgame.draw.rect(stage, (100,100,100), pgame.Rect(i*100,j*100,100,100))
            square_row.append(square)
          elif i % 2 != 0 and j % 2 != 0:
            square = pgame.draw.rect(stage, (100,100,100), pgame.Rect(i*100,j*100,100,100))
            square_row.append(square)
          elif i % 2 != 0 and j % 2 == 0:
            #creating grid
            square = pgame.draw.rect(stage, (0,100,100), pgame.Rect(i*100,j*100,100,100))
            square_row.append(square)
          elif i % 2 == 0 and j % 2 != 0:
            square = pgame.draw.rect(stage, (0,100,100), pgame.Rect(i*100,j*100,100,100))
            square_row.append(square)
      board_squares.append(square_row)

    pgame.display.flip()


  pgame.quit()

#calling function
board()




