import pygame

from enemy import Enemy
from player import Player, Bullet, BulletState

pygame.init()

screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Space Invaders")
background = pygame.image.load('space.jpg')
background = pygame.transform.scale(background, (900, 600))

player = Player()
enemy = Enemy()
bullet = Bullet()


def fire_bullet():
    bullet.state = BulletState.FIRE
    bullet.fire()
    screen.blit(bullet.img, (bullet.x, bullet.y))


# Game's loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x -= 20
                bullet.x -= 20
            if event.key == pygame.K_RIGHT:
                player.x += 20
                bullet.x += 20
            if event.key == pygame.K_SPACE:
                fire_bullet()
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    player.relocate()
    enemy.relocate()

    if bullet.state == BulletState.FIRE:
        bullet.fire()
        screen.blit(bullet.img, (bullet.x, bullet.y))

    screen.blit(player.img, (player.x, player.y))
    screen.blit(enemy.img, (enemy.x, enemy.y))
    pygame.display.update()
