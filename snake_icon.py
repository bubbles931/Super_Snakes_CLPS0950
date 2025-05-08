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

def user_input(event, square, direction, body_x, body_y):
    #if user presses close button exits loop and display closes
    #handling key pressing and assigning direction
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT and direction != 'L':
            direction = 'R'
            body_x = (square[1] / 25)
        elif event.key == pygame.K_LEFT and direction != 'R':
            direction = 'L'
            body_x = (square[1] / 25)
        elif event.key == pygame.K_UP and direction != 'D':
            direction = 'U'
            body_y = (square[0] / 25)
        elif event.key == pygame.K_DOWN and direction != 'U':
            direction = 'D'
            body_y = (square[0] / 25)
    return direction, body_x, body_y

#using the current assignment of direction to update position of the head and body    
def update_snake_position(direction, movement_rows, movement_cols, body_x, body_y):
    if direction == 'R':
        return movement_rows, movement_cols + 1, body_x, body_y + 1
    elif direction == 'L':
        return movement_rows, movement_cols - 1, body_x, body_y - 1
    elif direction == 'U':
        return movement_rows - 1, movement_cols, body_x - 1, body_y
    elif direction == 'D':
        return movement_rows + 1, movement_cols, body_x + 1, body_y
        
