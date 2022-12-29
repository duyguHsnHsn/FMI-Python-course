import pygame
import random
from utils import fix_x_against_borders
pygame.init()

screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Space Invaders")


class Player:
    def __init__(self):
        self.img = pygame.image.load("spaceship.png")
        self.img = pygame.transform.scale(self.img, (64, 64))
        self.x = 400
        self.y = 500

    def relocate(self):
        self.x = fix_x_against_borders(self.x)
        screen.blit(self.img, (self.x, self.y))


player = Player()


class Enemy:
    def __init__(self):
        self.img = pygame.image.load("enemy.png")
        self.img = pygame.transform.scale(self.img, (64, 64))
        self.x = random.randint(0, 830)
        self.y = random.randint(50, 120)

    def relocate(self):
        self.x = fix_x_against_borders(self.x)
        screen.blit(self.img, (self.x, self.y))


enemy = Enemy()


# Game's loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x -= 10
            if event.key == pygame.K_RIGHT:
                player.y += 10
    screen.fill((0, 0, 0))
    player.relocate()
    enemy.relocate()
    pygame.display.update()
