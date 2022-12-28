import pygame

pygame.init()

screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Space Invaders")

# Game's loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


