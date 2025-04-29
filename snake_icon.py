#will be using:
#   pygame.draw to create a snake 
#   pygame.event to assocaote keyboard moves w display moves
#   after this: potientally create a function that can get the snakes location 
#       to be called in game_logic.py or board.py to NOT populate food in the same boardsquare
import pygame
def create_snake(curr_position):
    head = pygame.draw.circle(curr_position, (255, 255, 0,), (100,100), 5)
