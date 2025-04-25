#import pygame
import pygame as pgame
#define function to create board
def board():
  #initialize all pygame functions
  pgame.init()
  #creates display window with parameters
  stage = pgame.display.set_mode((1000,400))

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
    pgame.draw.rect(stage, (150,150, 150), pgame.Rect(150,100,100,150))
    pgame.display.flip()

  pgame.quit()
  
#calling function
board()
