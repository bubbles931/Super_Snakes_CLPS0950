#import pygame
import pygame as pgame
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
      for j in range(cols):
        board_squares.append((i,j))
        print(board_squares)
        for row in board_squares:
          for col in board_squares[row]:
            board_squares[row][col] = (i*100,j*100)

    
    Cfor i in range(rows):
      for j in range(cols):
          if i % 2 == 0 and j % 2 == 0:
            #creating grid
            pgame.draw.rect(stage, (100,100,100), pgame.Rect(i*100,j*100,100,100))
          elif i % 2 != 0 and j % 2 != 0:
            pgame.draw.rect(stage, (100,100,100), pgame.Rect(i*100,j*100,100,100))
          elif i % 2 != 0 and j % 2 == 0:
            #creating grid
            pgame.draw.rect(stage, (0,100,100), pgame.Rect(i*100,j*100,100,100))
          elif i % 2 == 0 and j % 2 != 0:
            pgame.draw.rect(stage, (0,100,100), pgame.Rect(i*100,j*100,100,100))
    pgame.display.flip()


  pgame.quit()

#calling function
board()




