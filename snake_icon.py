#will be using:
#   pygame.draw to create a snake 
#   pygame.event to assocaote keyboard moves w display moves
#   after this: potientally create a function that can get the snakes location 
#       to be called in game_logic.py or board.py to NOT populate food in the same boardsquare

import pygame
body_counter = 3
body_list = []

def create_snake(stage):
    head = body_list[0]
    pygame.draw.circle(stage, (255, 255, 0,), head.center, 10)
    for i in range(1,len(body_list)):
        body = body_list[i]
        if i % 2 == 0:
            pygame.draw.rect(stage,(255,170,29), body)
        else:
            pygame.draw.rect(stage,(255,0,127), body)
