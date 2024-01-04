import pygame
import random

pygame.init()

white = (255, 255, 255)
brown = (150, 75, 0)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 102)
blue = (50, 153, 213)

width = 600
height = 400
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Piethon')

clock = pygame.time.Clock()

snake_segment = 10
speed = 15

font = pygame.font.SysFont('bahnschrift', 25)
score_font = pygame.font.SysFont('comicsans', 35)

def snake(block, list):
    for x in list:
        # pygame.draw.circle(screen, brown, (x[0], x[1]), block)
        pygame.draw.rect(screen, brown, [x[0], x[1], block, block])

def message(msg, color):
    mesg = font.render(msg, True, color)
    screen.blit(mesg, [width/6, height/3])

def gameLoop():
    game_over = False
    game_close = False

    x = width/2
    y = height/2

    x_change = 0
    y_change = 0

    snake_list = []
    snake_length = 1

    foodx = round(random.randrange(0, width - snake_segment)/10.0) * 10.0
    foody = round(random.randrange(0, height - snake_segment)/10.0) * 10.0

    while not game_over:

        while game_close is True:
            screen.fill(white)
            message('You Lost! Press Q to Quit or C to Play Again', red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_segment
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_segment
                    y_change = 0
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = snake_segment
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -snake_segment

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_change
        y += y_change
        screen.fill(white)
        pygame.draw.rect(screen, green, [foodx, foody, snake_segment, snake_segment])
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) >= snake_length:
            del snake_list[0]
        
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        snake(snake_segment, snake_list)

        pygame.display.update()

        if x == foodx and y == foody:
            foodx = round(random.randrange(0, width - snake_segment)/10.0) * 10.0
            foody = round(random.randrange(0, height - snake_segment)/10.0) * 10.0
            snake_length += 1

        clock.tick(speed)

    pygame.quit()
    quit()

gameLoop()


# import pygame
# import random
 
# pygame.init()
 
# white = (255, 255, 255)
# yellow = (255, 255, 102)
# black = (0, 0, 0)
# red = (213, 50, 80)
# green = (0, 255, 0)
# blue = (50, 153, 213)
 
# dis_width = 600
# dis_height = 400
 
# dis = pygame.display.set_mode((dis_width, dis_height))
# pygame.display.set_caption('Snake Game by Edureka')
 
# clock = pygame.time.Clock()
 
# snake_block = 10
# snake_speed = 15
 
# font_style = pygame.font.SysFont("bahnschrift", 25)
# score_font = pygame.font.SysFont("comicsansms", 35)
 
# def our_snake(snake_block, snake_list):
#     for x in snake_list:
#         pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
 
# def message(msg, color):
#     mesg = font_style.render(msg, True, color)
#     dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
 
# def gameLoop():
#     game_over = False
#     game_close = False
 
#     x1 = dis_width / 2
#     y1 = dis_height / 2
 
#     x1_change = 0
#     y1_change = 0
 
#     snake_List = []
#     Length_of_snake = 1
 
#     foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
#     foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
#     while not game_over:
 
#         while game_close is True:
#             dis.fill(blue)
#             message("You Lost! Press C-Play Again or Q-Quit", red)
 
#             pygame.display.update()
 
#             for event in pygame.event.get():
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_q:
#                         game_over = True
#                         game_close = False
#                     if event.key == pygame.K_c:
#                         gameLoop()
 
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 game_over = True
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     x1_change = -snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_RIGHT:
#                     x1_change = snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_UP:
#                     y1_change = -snake_block
#                     x1_change = 0
#                 elif event.key == pygame.K_DOWN:
#                     y1_change = snake_block
#                     x1_change = 0
 
#         if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
#             game_close = True
#         x1 += x1_change
#         y1 += y1_change
#         dis.fill(blue)
#         pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
#         snake_Head = []
#         snake_Head.append(x1)
#         snake_Head.append(y1)
#         snake_List.append(snake_Head)
#         if len(snake_List) > Length_of_snake:
#             del snake_List[0]
 
#         for x in snake_List[:-1]:
#             if x == snake_Head:
#                 game_close = True
 
#         our_snake(snake_block, snake_List)
 
 
#         pygame.display.update()
 
#         if x1 == foodx and y1 == foody:
#             foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
#             foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
#             Length_of_snake += 1
 
#         clock.tick(snake_speed)
 
#     pygame.quit()
#     quit()
 
 
# gameLoop()