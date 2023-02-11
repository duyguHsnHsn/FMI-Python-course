import pygame

from enemy import Enemy
from player import Player, Bullet, BulletState
from utils import collision

pygame.init()

screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Space Invaders")
background = pygame.image.load('images/space.jpg')
background = pygame.transform.scale(background, (900, 600))
font = pygame.font.Font('freesansbold.ttf', 32)
clock = pygame.time.Clock()


class Game:
    def __init__(self, enemies_count):
        self._player = Player()
        self._enemies = []
        self._enemies_count = enemies_count
        self._bullet = Bullet()
        self._score = 0
        for i in range(self._enemies_count):
            self._enemies.append(Enemy())

    def _fire_bullet(self):
        self._bullet.state = BulletState.FIRE
        self._bullet.fire()
        screen.blit(self._bullet.img, (self._bullet.x, self._bullet.y))

    def show_score(self):
        result = font.render(str(self._score), True, (255, 255, 255))
        screen.blit(result, (10, 10))

    def _vanish_enemies(self):
        for i in range(self._enemies_count):
            self._enemies[i].y = 1500  # they vanish

    def game_over(self):
        result = font.render("Game over! " + "Your score: " + str(self._score), True, (255, 255, 255))
        screen.blit(result, (250, 400))

    def _check_movements(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self._player.x -= 30
                if self._bullet.state == BulletState.READY:
                    self._bullet.x -= 30
            if event.key == pygame.K_RIGHT:
                self._player.x += 30
                if self._bullet.state == BulletState.READY:
                    self._bullet.x += 30
            if event.key == pygame.K_SPACE:
                self._fire_bullet()

    def start(self):
        # Game loop
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                self._check_movements(event)

            screen.fill((0, 0, 0))
            screen.blit(background, (0, 0))

            for i in range(self._enemies_count):
                # end game
                if 400 < self._enemies[i].y < 600:
                    self._vanish_enemies()
                    self.game_over()
                    break

                self._enemies[i].relocate()
                if collision(self._enemies[i].x, self._enemies[i].y, self._bullet.x, self._bullet.y):
                    self._bullet.reset(self._player.x)
                    self._score += 1
                    self._enemies[i].reset()
                screen.blit(self._enemies[i].img, (self._enemies[i].x, self._enemies[i].y))

            if self._bullet.y <= 0:
                self._bullet.reset(self._player.x)

            if self._bullet.state == BulletState.FIRE:
                self._bullet.fire()
                screen.blit(self._bullet.img, (self._bullet.x, self._bullet.y))

            self.show_score()

            self._player.relocate()
            screen.blit(self._player.img, (self._player.x, self._player.y))

            pygame.display.update()
            clock.tick(60)


game = Game(5)
game.start()
