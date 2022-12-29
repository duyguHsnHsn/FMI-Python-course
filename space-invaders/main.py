import pygame
import random
from utils import fix_x_against_borders
pygame.init()

screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Space Invaders")
background = pygame.image.load('space.jpg')
background = pygame.transform.scale(background, (900, 600))


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
        self.direction = -2

    def relocate(self):
        self.x = fix_x_against_borders(self.x)
        self.move_against_x()
        screen.blit(self.img, (self.x, self.y))

    def move_against_x(self):
        if self.x == 0:
            self.direction = 2
            self.move_against_y()
        if self.x == 830:
            self.direction = -2
            self.move_against_y()
        self.x += self.direction

    def move_against_y(self):
        self.y += 10


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
                player.x += 10
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    player.relocate()
    enemy.relocate()
    pygame.display.update()
