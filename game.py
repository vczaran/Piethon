import pygame
import random

pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width,height))
pygame.display.update()
pygame.display.set_caption('Piethon')

white = (255, 255, 255)
brown = (150, 75, 0)
green = (0, 255, 0)
red = (255, 0, 0)

snake_segment = 10
speed = 30

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 50)

def message(msg, color):
    mesg = font.render(msg, True, color)
    screen.blit(mesg, [width/3, height/3])

def gameLoop():
    game_over = False
    game_close = False

    x = width/2
    y = height/2

    x_change = 0
    y_change = 0

    foodx = round(random.randrange(0, width - snake_segment)/10.0) * 10.0
    foody = round(random.randrange(0, width - snake_segment)/10.0) * 10.0

    while not game_over:

        while game_close is True:
            screen.fill(white)
            message('You Lost! Press Q to Quite or C to Play Again', red)
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

        if x >= width or x <= 0 or y >= height or y <= 0:
            game_close = True

        x += x_change
        y += y_change
        screen.fill(white)
        pygame.draw.rect(screen, green, [foodx, foody, snake_segment, snake_segment])
        pygame.draw.circle(screen, brown, (x, y), snake_segment)
        pygame.display.update()

        if x == foodx and y == foody:
            print("Yummy!")
        clock.tick(speed)

    pygame.quit()
    quit()

gameLoop()