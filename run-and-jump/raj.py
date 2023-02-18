import click

from run_and_jump_game import *


@click.command(help="A simple game where you need to jump and run and endure some obstacles and collect coins.")
@click.option(
    "-c",
    "--coins",
    type=click.INT,
    default=1,
    help="The number of coins that are going to be collected. The number must be higher than 0.",
)
def cli(coins: int) -> None:
    if coins > 0:
        game = RunAndJumpGame(coins)
        game.start()
    else:
        click.echo("Your input for --coins is incorrect. please check the --help page.")
