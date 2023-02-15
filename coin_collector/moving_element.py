import pygame


class MovingElement:
    def __init__(self, win_width: int, win_height: int, randomizer: int, img_location: str, speed: int):
        self.x = win_width / 2 - randomizer / 2
        self.y = win_height - 60
        self.speed = speed
        self.image = pygame.image.load(img_location).convert_alpha()
        self.rect = self.image.get_rect(bottomright=(self.x, self.y))