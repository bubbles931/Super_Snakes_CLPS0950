#will be using:
#   pygame.draw to create a snake 
#   pygame.event to assocaote keyboard moves w display moves
#   after this: potientally create a function that can get the snakes location 
#       to be called in game_logic.py or board.py to NOT populate food in the same boardsquare

import pygame

from super_snakes import board_squares

def create_snake(stage, center):
    head = pygame.draw.circle(stage, (255, 255, 0,), center, 10)

def create_snakemovement(movement_rows: int, movement_cols: int):
    #movement_cols = 0
    #movement_rows = 0
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                movement_cols += 1
            elif event.key == pygame.K_LEFT:
                movement_cols -= 1
            elif event.key == pygame.K_UP:
                movement_cols += 1 
            elif event.key == pygame.K_DOWN:
                movement_rows -= 1
    updated_position = board_squares[movement_rows][movement_cols]
    return updated_position
