import pygame
import random
import snake_icon
import level_2

board_squares = None
food_list = []
running = True
food_ate = 0



#loading, displaying, and adding food to random board squares
def generate_food(stage):
    display_image = pygame.image.load("snake_food.png")
    display_image = pygame.transform.scale(display_image, (25, 25))
    if not food_list:
        #keep running until an open boardsquare is found
        while running:
            square = board_squares[random.randint(1, 18)][random.randint(1, 18)]
            if square not in snake_icon.body_list and square not in level_2.obstacle_list:
                food_list.append(square)
                break
    for square in food_list:
        stage.blit(display_image, square.topleft)

#checking if head of the snake collides with food 
#returning a boolean to use in super_snakes to increase food_ate count to display to user
def check_collison(stage) -> bool:
    bool = False
    head_location = snake_icon.body_list[0]
    for i in range(0, len(food_list)):
        food_location = food_list[i]
        if head_location == food_location:
            snake_icon.body_counter += 1
            food_list.pop(i)
            generate_food(stage)
            bool = True
            break
    return bool