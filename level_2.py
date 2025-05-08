#this is the file for level 2
import pygame
import random
import snake_icon
import food

start_level_2 = False

def main(stage):
    stage.fill(100,100,100)

board_squares = None
obstacle_list = []
running = True


def level_2(stage,board_squares):
    display_image = pygame.image.load("obstacle_try2.webp")
    display_image = pygame.transform.scale(display_image, (25, 25))
    if not obstacle_list:
        #keep running until an open boardsquare is found
        while len(obstacle_list) < 6:
            square = board_squares[random.randint(2, 18)][random.randint(2, 18)]
            if square not in snake_icon.body_list and square not in food.food_list and square not in obstacle_list:
                obstacle_list.append(square)
  

    for square in obstacle_list:
        stage.blit(display_image, square.topleft)

def obstacle_collison(stage):
    head_location = snake_icon.body_list[0]
    if head_location in obstacle_list:
        pygame.quit()

def hit_body(stage):
    head_location = snake_icon.body_list[0]
    snake_icon.body_list
    if snake_icon.body_list.count(head_location) > 1:
        pygame.quit()
    



