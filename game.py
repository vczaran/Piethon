import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.update()
pygame.display.set_caption('Piethon')

white = (255, 255, 255)
brown = (150, 75, 0)
green = (0, 255, 0)

game_over = False

x = 300
y = 300

x_change = 0
y_change = 0

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -10
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = 10
                y_change = 0
            elif event.key == pygame.K_DOWN:
                x_change = 0
                y_change = 10
            elif event.key == pygame.K_UP:
                x_change = 0
                y_change = -10
    
    x += x_change
    y += y_change
    screen.fill(white)
    pygame.draw.circle(screen, brown, (x, y), 10)

    pygame.display.update()

    clock.tick(30)
   

pygame.quit()
quit()