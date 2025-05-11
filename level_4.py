import pygame
import snake_icon
import food

running = True
desired_speed = 20

def level_4_logic(stage, speed) -> int:
    initial_speed = speed
    bool = food.check_collison(stage)
    if bool:
        while speed != desired_speed:
            speed+=1
        speed = initial_speed
