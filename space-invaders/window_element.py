import pygame


class WindowElement:
    def __init__(self, image: str, image_pixels: int, x: int, y: int):
        self.img = pygame.image.load(image)
        self.img = pygame.transform.scale(self.img, (image_pixels, image_pixels))
        self.x = x
        self.y = y
