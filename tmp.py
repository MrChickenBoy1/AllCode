import pygame
import random

pygame.init()

WIN = pygame.display.set_mode((1280, 720))

x = 0
y = 0
while True:
    WIN.fill((random.randrange(0, 255), random.randrange (0, 255), random.randrange(0, 255)))
    pygame.draw.rect(WIN, (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)), pygame.Rect(random.randrange(0, 1280), random.randrange(0, 1280), random.randrange(0, 1280), random.randrange(0, 1280)))
    pygame.display.flip()

    
