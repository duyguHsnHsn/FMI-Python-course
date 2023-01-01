import requests
import random

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)
WORDS = response.content.decode("utf-8").splitlines()


def get_random_word():
    return WORDS[random.randint(0, 10001)]
