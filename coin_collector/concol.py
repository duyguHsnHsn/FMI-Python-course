import click

from game import *


@click.command()
@click.option(
    "-s",
    "--bot-speed",
    type=click.STRING,
    default="1",
    help="The speed of the bot that the user plays against.",
)
def cli(bot_speed: str) -> None:
    game = CoinCollectorGame(int(bot_speed))
    game.start()
