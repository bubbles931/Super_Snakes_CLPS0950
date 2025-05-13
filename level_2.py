#this is the file for level 2
import pygame
import random
import snake_icon
import food

pygame.init()
pygame.mixer.init()

obstacle_list = []
game_over_sound = pygame.mixer.Sound("game_over.mp3")

#function to generate obstacles randomly
def generate_obstacles(stage,board_squares, num_obstacles):
    display_image = pygame.image.load("obstacle_try2.webp")
    display_image = pygame.transform.scale(display_image, (25, 25))
    if not obstacle_list:
        obstacle_list.clear()
        #keep running until an open boardsquare is found
        while len(obstacle_list) <= num_obstacles:
            x = random.randint(2, 17)
            y = random.randint(2, 17)
            square = board_squares[x][y]
            if square not in snake_icon.body_list and square not in food.food_list and square not in obstacle_list and x != 9:
                obstacle_list.append(square)
  

    for square in obstacle_list:
        stage.blit(display_image, square.topleft)

#when snake hits obstacles game over
def obstacle_collison():
    head_location = snake_icon.body_list[0]
    if head_location in obstacle_list:
        pygame.mixer.music.stop()
        game_over_sound.play()
        pygame.time.delay(1500)
        pygame.quit()

#when snake hits body game over
def hit_body():
    head_location = snake_icon.body_list[0]
    snake_icon.body_list
    if snake_icon.body_list.count(head_location) > 1:
        pygame.mixer.music.stop()
        game_over_sound.play()
        pygame.time.delay(1500)
        pygame.quit()
    



