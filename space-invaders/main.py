import pygame
import math

from enemy import Enemy
from player import Player, Bullet, BulletState

pygame.init()

screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Space Invaders")
background = pygame.image.load('images/space.jpg')
background = pygame.transform.scale(background, (900, 600))
font = pygame.font.Font('freesansbold.ttf', 32)

player = Player()
enemies = []
enemies_count = 5
bullet = Bullet()
score = 0

for i in range(enemies_count):
    enemies.append(Enemy())


def fire_bullet():
    bullet.state = BulletState.FIRE
    bullet.fire()
    screen.blit(bullet.img, (bullet.x, bullet.y))


def collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt(math.pow(enemy_x - bullet_x, 2) + math.pow(enemy_y - bullet_y, 2))
    if distance < 50:  # collision has occurred
        return True
    return False


def show_score():
    result = font.render(str(score), True, (255, 255, 255))
    screen.blit(result, (10, 10))


# Game's loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x -= 30
                if bullet.state == BulletState.READY:
                    bullet.x -= 30
            if event.key == pygame.K_RIGHT:
                player.x += 30
                if bullet.state == BulletState.READY:
                    bullet.x += 30
            if event.key == pygame.K_SPACE:
                fire_bullet()
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    player.relocate()
    for i in range(enemies_count):
        enemies[i].relocate()
        if collision(enemies[i].x, enemies[i].y, bullet.x, bullet.y):
            bullet.reset(player.x)
            score += 1
            enemies[i].reset()
        screen.blit(enemies[i].img, (enemies[i].x, enemies[i].y))

    if bullet.y <= 0:
        bullet.reset(player.x)

    if bullet.state == BulletState.FIRE:
        bullet.fire()
        screen.blit(bullet.img, (bullet.x, bullet.y))

    screen.blit(player.img, (player.x, player.y))
    show_score()
    pygame.display.update()
