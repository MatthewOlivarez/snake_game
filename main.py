import sys, pygame
pygame.init()

size = width, height = 480, 480
black = 0, 0, 0
white = 250, 250, 250
green = 0, 250, 0

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake Game')

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    screen.fill(black)
    pygame.display.flip()