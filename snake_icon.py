import pygame
body_counter = 3 #starting length of snake
body_list = []

def create_snake(stage):
    head = body_list[0]
    pygame.draw.circle(stage, (255, 255, 0,), head.center, 10)
    for i in range(1,len(body_list)):
        body = body_list[i]
        if i % 2 == 0:
            pygame.draw.rect(stage,(255,170,29), body)
        else:
            pygame.draw.rect(stage,(255,0,127), body)
