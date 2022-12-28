import pygame

pygame.init()

screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Space Invaders")

# Player
player = pygame.image.load("spaceship.png")
player = pygame.transform.scale(player, (64, 64))
playerX = 400
playerY = 500


def put_player(x, y):
    if x < 0:
        x = 0
    if x > 830:
        x = 830
    screen.blit(player, (x, y))


# Game's loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX -= 10
            if event.key == pygame.K_RIGHT:
                playerX += 10
    screen.fill((0, 0, 0))
    put_player(playerX, playerY)
    pygame.display.update()
