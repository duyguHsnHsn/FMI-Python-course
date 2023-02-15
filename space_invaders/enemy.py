import random


from utils import fix_x_against_borders
from window_element import WindowElement


class EnemyElement(WindowElement):
    def __init__(self, image: str, image_pixels: int, x: int, y: int):
        super().__init__(image, image_pixels, x, y)
        self.direction = -1.5


class Enemy(EnemyElement):
    def __init__(self):
        super().__init__("../images/enemy.png", 64, random.randint(0, 830), random.randint(50, 120))

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
