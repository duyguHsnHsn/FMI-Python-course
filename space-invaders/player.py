from enum import Enum

import pygame

from utils import fix_x_against_borders
from window_element import WindowElement


class Player(WindowElement):
    def __init__(self):
        super().__init__("images/spaceship.png", 64, 400, 500)

    def relocate(self):
        self.x = fix_x_against_borders(self.x)


class BulletState(Enum):
    READY = 1
    FIRE = 2


class Bullet(WindowElement):
    def __init__(self):
        super().__init__("images/circle.png", 16, 425, 490)
        self.state = BulletState.READY

    def fire(self):
        if self.state == BulletState.FIRE:
            self.y -= 5

    def reset(self, player_x):
        self.x = player_x + 25
        self.y = 490
        self.state = BulletState.READY
