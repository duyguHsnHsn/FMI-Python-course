from enum import Enum

import pygame

from utils import fix_x_against_borders


class Player:
    def __init__(self):
        self.img = pygame.image.load("spaceship.png")
        self.img = pygame.transform.scale(self.img, (64, 64))
        self.x = 400
        self.y = 500

    def relocate(self):
        self.x = fix_x_against_borders(self.x)


class BulletState(Enum):
    READY = 1
    FIRE = 2


class Bullet:
    def __init__(self):
        self.img = pygame.image.load("circle.png")
        self.img = pygame.transform.scale(self.img, (16, 16))
        self.state = BulletState.READY
        self.x = 425  # player x + 25
        self.y = 490

    def fire(self):
        if self.state == BulletState.FIRE:
            self.y -= 3
