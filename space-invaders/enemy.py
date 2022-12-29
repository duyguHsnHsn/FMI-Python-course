import random

import pygame

from utils import fix_x_against_borders


class Enemy:
    def __init__(self):
        self.img = pygame.image.load("images/enemy.png")
        self.img = pygame.transform.scale(self.img, (64, 64))
        self.x = random.randint(0, 830)
        self.y = random.randint(50, 120)
        self.direction = -1.5

    def relocate(self):
        self.x = fix_x_against_borders(self.x)
        self.move_against_x()

    def move_against_x(self):
        if self.x == 0:
            self.direction = 1.5
            self.move_against_y()
        if self.x == 830:
            self.direction = -1.5
            self.move_against_y()
        self.x += self.direction

    def move_against_y(self):
        self.y += 50

    def reset(self):
        self.x = random.randint(0, 830)
        self.y = random.randint(50, 120)
        self.direction = -1.5
