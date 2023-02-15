import click
from game import *


@click.command(help="This is space invaders game")
@click.option("--enemies", prompt="Number of enemies:", help="The number of enemies you are playing against.")
def startGame(enemies):
    game = SpaceInvader(int(enemies))
    game.start()


if __name__=="__main__":
    startGame()