import click

from coin_collector_game import *


@click.command(help="A simple game played against a bot that is trying to stop you while you are collecting coins.")
@click.option(
    "-s",
    "--bot-speed",
    type=click.INT,
    default=1,
    help="The speed of the bot that the user plays against. It must be between 1 and 4.",
)
@click.option(
    "-c",
    "--coins",
    type=click.INT,
    default=5,
    help="The number of coins you are trying to collect. It must be between 1 and 10",
)
def cli(bot_speed: int, coins: int) -> None:
    if bot_speed in range(1, 5) and coins in range(1, 11):
        game = CoinCollectorGame(bot_speed, coins)
        game.start()
