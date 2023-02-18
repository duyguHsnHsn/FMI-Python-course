import random

import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Run and jump")
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 32)
enemy_image = pygame.image.load("../images/enemy1.png").convert_alpha()
background_image = pygame.image.load("../images/background.png").convert()
player_image = pygame.image.load("../images/marathon.png").convert_alpha()
bird_image = pygame.image.load("../images/dove.png").convert_alpha()
coin_image = pygame.image.load("../images/dollar.png").convert_alpha()

winner_image = pygame.image.load("../images/winner.png").convert_alpha()
winner_rect = winner_image.get_rect(topleft=(350, 230))

lose_image = pygame.image.load("../images/game-over.png").convert_alpha()
lose_rect = winner_image.get_rect(topleft=(350, 230))


class RunAndJumpGame:
    def __init__(self, aimed_score: int):
        self._game_gravity = 0
        self._score = 0
        self._aimed_score = aimed_score
        self._enemy = enemy_image.get_rect(bottomright=(800, 530))
        self._background = pygame.transform.scale(background_image, (900, 600))
        self._player = player_image.get_rect(bottomleft=(80, 540))
        self._bird = bird_image.get_rect(bottomright=(800, 430))
        self._coin = coin_image.get_rect(bottomright=(800, 480))

    def _player_jump(self):
        self._game_gravity = -20

    def _fix_player_against_ground(self):
        if self._player.y > 480:
            self._player.y = 480

    def _move_enemy(self):
        self._enemy.x -= 3.5

    def _move_bird(self):
        self._bird.x -= 1.5

    def _move_coin(self):
        self._coin.x -= 2

    def _fix_enemy_against_screen_borders(self):
        if self._enemy.right <= 0:
            self._enemy.left = 900

    def _fix_birds_position(self):
        if self._bird.right <= 0:
            self._bird.left = random.randint(900, 920)

    def _fix_coin_position(self):
        self._coin.left = random.randint(900, 920)
        self._coin.y = random.randint(430, 500)

    def start(self):
        end = False
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
            screen.blit(bird_image, self._bird)
            screen.blit(coin_image, self._coin)

            if not end:
                self._move_enemy()
                self._move_bird()
                self._move_coin()
                self._fix_enemy_against_screen_borders()
                if self._coin.right <= 0:
                    self._fix_coin_position()
                self._fix_birds_position()

            # collision with the enemy
            if self._player.colliderect(self._enemy):
                screen.fill((0, 0, 0))
                screen.blit(lose_image, lose_rect)
                end = True

            # collision with the bird
            if self._player.colliderect(self._bird):
                screen.fill((0, 0, 0))
                screen.blit(lose_image, lose_rect)
                end = True

            if self._aimed_score == self._score:
                screen.fill((0, 0, 0))
                screen.blit(winner_image, winner_rect)
                end = True

            self._game_gravity += 1
            self._player.y += self._game_gravity
            self._fix_player_against_ground()

            if self._player.x == self._coin.x:
                self._score += 1
                self._fix_coin_position()

            result = font.render(str(self._score), True, (255, 255, 255))
            screen.blit(result, (10, 10))
            pygame.display.update()
            clock.tick(60)
