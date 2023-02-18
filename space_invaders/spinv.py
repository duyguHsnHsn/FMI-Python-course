import click
from space_invaders_game import *


@click.command(help="This is space invaders game")
@click.option(
    "-e",
    "--enemies",
    prompt="Number of enemies:",
    type=click.INT,
    default=5,
    help="The number of enemies you are playing against. The maximum number of enemies you can play against is 20.")
def cli(enemies: int):
    if enemies in range(1, 21):
        game = SpaceInvader(enemies)
        game.start()
    else:
        click.echo("Your input for --enemies was incorrect! Please check the help page!")

