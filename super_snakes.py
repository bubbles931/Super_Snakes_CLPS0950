#import pygame & file code snake_icon
import pygame
import snake_icon
import food
import level_2
import level_3

def board():
  #initialize all pygame modules
  pygame.init()
  pygame.mixer.init()
  #creates display window with parameters
  stage = pygame.display.set_mode((500,500))
  pygame.display.set_caption("Super Snakes")
  #define 2-D array 
  rows = 20
  cols = 20
  movement_cols = 9 #x-movement 
  movement_rows = 9 #y-movement
  body_y = 8
  body_x = 9
  direction = ""  
  running = True
  image_display = True 
  desired_amount = 1
  curr_level = "Level 1"
  pre_instructions = f"Eat {desired_amount} food\nto level up\n and evolve to a Super Snake!"
  long_instructions = pre_instructions.split('\n')
  instructions = "Avoid the obstacles and your tail!"
  x = 100
  num_obstacles = 0
  speed = 7
  end_display = False
  music = "game_music.mp3"
  pygame.mixer.music.load(music) 
  eating_sound = pygame.mixer.Sound("eating.mp3")
  game_over_sound = pygame.mixer.Sound("game_over.mp3")
  desired_speed = 0


#main game loop:
  while running:
    while image_display:
      display_image = pygame.image.load("initial_board_screenshot.png")
      display_image = pygame.transform.scale(display_image, (500,500))
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RIGHT and direction != 'L' and direction != 'U' and direction != 'D':
              direction = 'R'
              image_display = False
              pygame.mixer.music.play(-1) 
      font = pygame.font.SysFont('Times New Roman', 30)
      level_txt_surface = font.render(curr_level, True, (255, 255, 255))
      instruction_txt_surface = font.render("To Start: Press your right key", False, (255, 255, 255))
      instruction_txt_surface_levels = font.render(instructions, False, (255, 255, 0))

    #showing image      
      stage.blit(display_image, (0,0))
      stage.blit(level_txt_surface, (193,100))
      stage.blit(instruction_txt_surface, (75,150))
      if curr_level == "Level 1" or curr_level == "Level 3":
        for i, line in enumerate(long_instructions):
          text_surface = font.render(line, True, (255, 255, 0))
          #text_surface = font.render(line, True, (255, 255, 255))
          text_rect = text_surface.get_rect(center=(236, 280 + i * 40))  # Adjust vertical center per line
          stage.blit(text_surface, text_rect)
        #stage.blit(text_surface, (175, 275 + i * 30))
      else:
        stage.blit(instruction_txt_surface_levels, (x,300))

      pygame.display.flip()

      #updating stage to display board squares and placing snake in assigned start position 
      board_squares = generating_board(stage, rows, cols)
      snake_icon.body_list[:] = [board_squares[movement_rows][movement_cols]]

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit() #if user presses close button exits loop and display closes
      direction, body_x, body_y = snake_icon.user_input(event, square, direction, body_x, body_y)

    #using the current assignment of direction to update position of the head and body    
    movement_rows, movement_cols, body_x, body_y = snake_icon.update_snake_position(direction, movement_rows, movement_cols, body_x, body_y)
    
    #updating body_list to draw the snakes head in board_square
    square = board_squares[movement_rows][movement_cols]
    snake_icon.body_list.insert(0, square)
    if len(snake_icon.body_list) > snake_icon.body_counter:
      snake_icon.body_list.pop()
    #drawing everything in these couple lines
    stage.fill((255, 255, 255))
    board_squares = generating_board(stage, rows, cols)
    snake_icon.create_snake(stage)

    #death barrier
    if movement_cols == 0 or movement_cols == 19 or movement_rows == 0 or movement_rows == 19:
      pygame.mixer.music.stop()
      game_over_sound.play()
      pygame.time.delay(1500)
      break

    food.board_squares = board_squares
    food.generate_food(stage)

    #checking if food and snake has collided
    bool = food.check_collison(stage)
    if bool:
      food.food_ate +=1
      eating_sound.play()
    font = pygame.font.SysFont('Times New Roman', 15)
    txt_surface = font.render("Ate: " + str(food.food_ate) + "/" + str(desired_amount), False, (255, 255, 255))
    stage.blit(txt_surface, (75,0))
    


    if food.food_ate == desired_amount and curr_level == "Level 1":
      pygame.mixer.music.pause()
      curr_level = "Level 2"
      food.food_ate = 0
      image_display = True
      movement_rows = 9
      movement_cols = 9
      body_y = 8
      body_x = 9
      direction = ""  
      x = 50
      desired_amount = 1
      num_obstacles = 6
      speed = 10

    
    if curr_level == "Level 2":
      if image_display == False: 
        level_2.generate_obstacles(stage, board_squares, num_obstacles)
        level_2.obstacle_collison()
        level_2.hit_body()
        pygame.mixer.music.unpause()

    if food.food_ate == desired_amount and curr_level == "Level 2":
      pygame.mixer.music.pause()
      curr_level = "Level 3"
      food.food_ate = 0
      image_display = True
      movement_rows = 9
      movement_cols = 9
      body_y = 8
      body_x = 9
      direction = "" 
      #pre_instructions = f"Eat {desired_amount} food\nto level up\n and evolve to a Super Snake!"
      #long_instructions = pre_instructions.split('\n') 
      pre_instructions = f"Keep avoiding your tail\n and even more obstacles!" #add instructions for level 3
      long_instructions = pre_instructions.split('\n') 
      desired_amount = 1 #add the amount you want
      level_2.obstacle_list.clear()
      num_obstacles = 15
      speed = 10
 
    if curr_level == "Level 3":
      if image_display == False: 
        pygame.mixer.music.unpause()
        level_3.set_up(stage, num_obstacles, board_squares)
    
    if food.food_ate == desired_amount and curr_level == "Level 3":
      pygame.mixer.music.pause()
      curr_level = "Level 4"
      food.food_ate = 0
      image_display = True
      movement_rows = 9
      movement_cols = 9
      body_y = 8
      body_x = 9
      direction = ""  
      instructions = "Bonus Level... MWahHAHAHAHA" #add instructions for level 4
      desired_amount = 3 #add the amount you want
      speed = 10
      desired_speed = 15

    if curr_level == "Level 4":

      if image_display == False: 
        pygame.mixer.music.unpause()
        level_2.hit_body()
        #initial_speed = speed
        if bool == True:
          while speed != desired_speed:
            speed += 1
            print(str(speed) + 'speed')
          if speed == desired_speed:
            print('test_run')
            desired_speed += 20
          print(str(desired_speed) + 'desired speed')

        #pygame.time.wait(1000)
        #speed = initial_speed
    
    #text that appears when player has won all the levels
      if food.food_ate == desired_amount and curr_level == "Level 4":
        end_display = True
      while end_display:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            end_display = False
            running = False
        display_image_end = pygame.image.load("end_img.jpg")
        display_image_end = pygame.transform.scale(display_image_end, (500,500))
        stage.blit(display_image_end, (0,0))
        
        font = pygame.font.SysFont('Times New Roman', 25)
        txt_surface = font.render("Congratulations you are the Super Snake!!", True, (0, 0, 0))
        stage.blit(txt_surface, (25,200))
        pygame.display.flip()


      
    pygame.display.update()
    pygame.time.Clock().tick(speed) 
    pygame.display.flip()
  
  pygame.display.flip()
  pygame.quit()

def generating_board(stage, rows, cols):
  #define function to create board and empty array board_squares to store position of each rectangle grid and to reference movement
  board_squares = []
  for j in range(rows):
      squares_row = []
      for i in range(cols):
          #creating the boder
          if i == 0 or i == 19 or j == 0 or j == 19:
            square = pygame.draw.rect(stage, (83,0,0), pygame.Rect(i*25,j*25,25,25))
            squares_row.append(square)
          elif (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
            #creating grid
            square = pygame.draw.rect(stage, (100,100,100), pygame.Rect(i*25,j*25,25,25))
            squares_row.append(square)
          elif (i % 2 != 0 and j % 2 == 0) or (i % 2 == 0 and j % 2 != 0):
            #creating grid
            square = pygame.draw.rect(stage, (0,100,100), pygame.Rect(i*25,j*25,25,25))
            squares_row.append(square)
      board_squares.append(squares_row)
  return board_squares


#calling function
board()