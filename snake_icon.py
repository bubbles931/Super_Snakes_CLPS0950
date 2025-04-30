#will be using:
#   pygame.draw to create a snake 
#   pygame.event to assocaote keyboard moves w display moves
#   after this: potientally create a function that can get the snakes location 
#       to be called in game_logic.py or board.py to NOT populate food in the same boardsquare

import pygame
counter = 1
body_list = []

def create_snake(stage, body_row, body_col, center):
    head = pygame.draw.circle(stage, (255, 255, 0,), center, 10)
    if counter != 0:
        if counter % 2 == 0:
            body = pygame.draw.rect(stage,(255,170,29), pygame.Rect((body_col)*25,(body_row)*25,25,25))
            body_list.append(body)
        else:
            body = pygame.draw.rect(stage,(255,0,127), pygame.Rect((body_col)*25,(body_row)*25,25,25))
            body_list.append(body)