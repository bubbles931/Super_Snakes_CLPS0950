import pygame
import random
import snake_icon
import food
import level_2
import super_snakes

running = True

def level_4_logic(head_location, food_list, food_location, speed):
    for food_location in food_list:
        if head_location == food_location:
            speed = 20
            pygame.time.wait(3000)
            speed = 1
    
    return speed