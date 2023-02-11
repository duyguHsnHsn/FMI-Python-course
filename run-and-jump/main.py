import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Run and jump")
clock = pygame.time.Clock()

background = pygame.image.load("images/background.png").convert()
background = pygame.transform.scale(background, (900, 600))
enemy = pygame.image.load("images/enemy.png").convert_alpha()
enemy_x = 800

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.blit(background, (0, 0))
    screen.blit(enemy, (enemy_x, 500))
    enemy_x -= 2.5
    if enemy_x <= 0:
        enemy_x = 900
    pygame.display.update()
    clock.tick(60)