import pygame
import snake_icon
import food

head_location = snake_icon.body_list[0] if snake_icon.body_list else None
food.food_list 
running = True

def level_4_logic(head_location, food_list, speed):
    for food_location in food_list:
        print("Checking:", head_location.topleft, "vs", food_location.topleft)
        if head_location.topleft == food_location.topleft:
            speed = 20
            print ("20")
            pygame.time.wait(3000)
            speed = 1
            print ("1")
    
    return speed