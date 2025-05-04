#will be using:
    #pygame.draw OR pygame.image to create/load food
    #food_list: append when generated and delete when eaten by snake
    #can create a new list for food_eaten and use len(food_eaten) 
    # to keep count of food eaten??

import pygame
import random
import snake_icon

board_squares = None
food_list = []
running = True

def generate_food(stage):
    display_image = pygame.image.load("snake_food.png")
    display_image = pygame.transform.scale(display_image, (25, 25))
    if not food_list:
        #keep running until an open boardsquare is found
        while running:
            square = board_squares[random.randint(1, 18)][random.randint(1, 18)]
            if square not in snake_icon.body_list:
                food_list.append(square)
                break

    for square in food_list:
        stage.blit(display_image, square.topleft)

def check_collison(stage):
    head_location = snake_icon.body_list[0]
    for i in range(0, len(food_list)):
        food_location = food_list[i]
        if head_location == food_location:
            snake_icon.body_counter += 1
            food_list.pop(i)
            generate_food(stage)
            break