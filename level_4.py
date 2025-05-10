import pygame
import snake_icon
import food

food.food_list 
running = True

def level_4_logic(head_location, food_list, speed):
    head_location = snake_icon.body_list[0]
    for food_location in food_list:
        print("Checking:", head_location, "vs food list", food_list, "vs food loc", food_location)
        if head_location == food_list:
            print ('food ate')
            speed = 20
            print ("20")
            pygame.time.wait(1000)
            speed = 1
            print ("1")
    
        return speed