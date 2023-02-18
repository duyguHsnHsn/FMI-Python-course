import click
from hangman_game import *


@click.command(help="This is a simple hangman game.")
@click.option(
    "-l",
    "--word-len",
    prompt="Length of the word:",
    default=4,
    type=click.INT,
    help="The length of the world you are going to guess. The default length is 5. The max length is 8.")
def cli(word_len):
    if word_len in range(0, 9):
        game = Hangman(int(word_len))
        game.start()
    else:
        click.echo("Wrong input for --world-len option! You should enter a number between 1 and 8!")
