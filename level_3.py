import pygame
import random
import snake_icon
import food
import level_2

board_squares = None
obstacle_list = []
running = True

def set_up(stage,num_obstacles, board_squares):
    level_2.generate_obstacles(stage, board_squares, num_obstacles)
    level_2.obstacle_collison()
    level_2.hit_body()