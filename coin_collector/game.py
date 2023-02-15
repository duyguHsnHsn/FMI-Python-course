import pygame
import random

from coin_collector.moving_element import MovingElement

# Initialize Pygame
pygame.init()

# Set up the window
win_width = 500
win_height = 500
screen = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Coin collector")
font = pygame.font.Font('freesansbold.ttf', 32)
clock = pygame.time.Clock()


class CoinCollectorGame:
    def __init__(self):
        # Set up the player and bot
        self.player = MovingElement(win_width, win_height, 50, "../images/purse.png", 5)
        self.bot = MovingElement(win_width, win_height, 50, "../images/robot.png", 2)
        self.bot.y = 10
        self.bot.rect = self.bot.image.get_rect(bottomleft=(self.bot.x, self.bot.y))

        # Set up the coins
        self.coins = []
        for i in range(10):
            coin = MovingElement(win_width, win_height, 50, "../images/star.png", 2)
            coin.x = random.randint(0, win_width - 20)
            coin.y = random.randint(0, win_height - 20)
            coin.rect = coin.image.get_rect(bottomright=(coin.x, coin.y))
            self.coins.append(coin)

        self.score = 0

    def _move_player(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.player.rect.x > 0:
            self.player.rect.x -= self.player.speed
        elif keys[pygame.K_RIGHT] and self.player.rect.x < win_width - 20:
            self.player.rect.x += self.player.speed
        if keys[pygame.K_UP] and self.player.rect.y > 0:
            self.player.rect.y -= self.player.speed
        elif keys[pygame.K_DOWN] and self.player.rect.y < win_height - 20:
            self.player.rect.y += self.player.speed

    def _move_bot(self):
        if self.bot.rect.x < self.player.rect.x:
            self.bot.rect.x += self.bot.speed
        elif self.bot.rect.x > self.player.rect.x:
            self.bot.rect.x -= self.bot.speed
        if self.bot.rect.y < self.player.rect.y:
            self.bot.rect.y += self.bot.speed
        elif self.bot.rect.y > self.player.rect.y:
            self.bot.rect.y -= self.bot.speed

    def start(self):
        game_running = True
        while game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_running = False
            self._move_player()
            self._move_bot()

            # Handle collision with coins
            for coin in self.coins:
                if self.player.rect.colliderect(coin.rect):
                    self.coins.remove(coin)
                    self.score += 1

            # Handle collision with bot
            if self.player.rect.colliderect(self.bot.rect):
                game_running = False

            # All coins collected
            if self.score == 10:
                game_running = False

            # Draw the game objects
            screen.fill((0, 0, 0))
            screen.blit(self.bot.image, self.bot.rect)
            screen.blit(self.player.image, self.player.rect)
            result = font.render(str(self.score), True, (255, 255, 255))
            screen.blit(result, (10, 10))
            for coin in self.coins:
                screen.blit(coin.image, coin.rect)
            pygame.display.update()
            clock.tick(60)
