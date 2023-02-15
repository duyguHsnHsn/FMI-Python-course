import click

from game import *


@click.command()
@click.option(
    "-e",
    "--enemies",
    type=click.STRING,
    default="1",
    help="The count of the enemies which the user plays against.",
)
def cli(enemies: str) -> None:
    game = SpaceInvader(int(enemies))
    game.start()
