import pygame as pgame
#define function to create board
def board():
  #initialize 
  pgame.init()
  stage = pgame.display.set_mode((1000,400))

  running = True

  while running:
    for event in pgame.event.get():
      if event.type == pgame.QUIT:
        running = False

    stage.fill((255, 255, 255))

    pgame.draw.rect(stage, (150,150, 150), pgame.Rect(150,100,100,150))
    pgame.display.flip()

  pgame.quit()


