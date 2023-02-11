import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Run and jump")
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 32)
enemy_image = pygame.image.load("images/enemy.png").convert_alpha()
background_image = pygame.image.load("images/background.png").convert()
player_image = pygame.image.load("images/marathon.png").convert_alpha()


class RunAndJumpGame:
    def __init__(self):
        self._game_gravity = 0
        self._score = 0
        self._enemy = enemy_image.get_rect(bottomright=(800, 530))
        self._background = pygame.transform.scale(background_image, (900, 600))
        self._player = player_image.get_rect(bottomleft=(80, 540))

    def _player_jump(self):
        self._game_gravity = -20

    def _fix_player_against_ground(self):
        if self._player.y > 480:
            self._player.y = 480

    def _move_enemy(self):
        self._enemy.x -= 3.5

    def _fix_enemy_against_screen_borders(self):
        if self._enemy.right <= 0:
            self._enemy.left = 900

    def start(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self._player.y == 480:
                        self._player_jump()

            screen.blit(self._background, (0, 0))
            screen.blit(enemy_image, self._enemy)
            screen.blit(player_image, self._player)

            self._move_enemy()
            self._fix_enemy_against_screen_borders()

            # collision
            if self._player.colliderect(self._enemy):
                run = False

            self._game_gravity += 1
            self._player.y += self._game_gravity
            self._fix_player_against_ground()

            if self._player.x == self._enemy.x:
                self._score += 1

            result = font.render(str(self._score), True, (255, 255, 255))
            screen.blit(result, (10, 10))
            pygame.display.update()
            clock.tick(60)


game = RunAndJumpGame()
game.start()