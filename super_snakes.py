#import pygame
import pygame as pgame
#define function to create board

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
    pgame.draw.rect(stage, (100,100,100), pgame.Rect(0,0,50,50))
    pgame.display.flip()

  pgame.quit()

#calling function
board()
