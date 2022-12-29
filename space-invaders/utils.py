import math


def fix_x_against_borders(x):
    if x < 0:
        x = 0
    if x > 830:
        x = 830
    return x


def collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt(math.pow(enemy_x - bullet_x, 2) + math.pow(enemy_y - bullet_y, 2))
    if distance < 50:  # collision has occurred
        return True
    return False


