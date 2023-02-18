import pygame
from words import get_random_word

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Hangman")
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
tomb = pygame.image.load("../images/tombstone.png").convert_alpha()
tomb_rect = tomb.get_rect(bottomright=(250, 150))

# Define the hangman parts
man = [pygame.Rect(50, 400, 100, 20), pygame.Rect(90, 100, 20, 320), pygame.Rect(90, 100, 240, 20),
       pygame.Rect(320, 100, 20, 60), pygame.draw.circle(screen, BLACK, (330, 180), 20, 1),
       pygame.Rect(320, 200, 20, 100), pygame.Rect(290, 300, 20, 100), pygame.Rect(350, 300, 20, 100)]


class Hangman:
    def __init__(self, word_len):
        self.incorrect_guesses = 0
        self.word = get_random_word()
        while len(self.word) != word_len:
            self.word = get_random_word()
        self.guessed_word = ["_" for i in range(len(self.word))]

    def start(self):
        game_running = True
        while game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.unicode.isalpha():
                        # check if the letter has already been guessed
                        if event.unicode in self.guessed_word:
                            continue
                        # check if the letter is in the word
                        if event.unicode in self.word:
                            for i in range(len(self.word)):
                                if self.word[i] == event.unicode:
                                    self.guessed_word[i] = event.unicode
                        else:
                            self.incorrect_guesses += 1

            if self.incorrect_guesses == len(man):
                text = font.render("You lose! The word was '%s'." % self.word, True, (255, 0, 0))
            elif "_" not in self.guessed_word:
                text = font.render("You win! The word was '%s'." % self.word, True, (0, 255, 0))
            else:
                text = font.render(" ".join(self.guessed_word), True, BLACK)
            screen.fill(WHITE)
            for i in range(self.incorrect_guesses):
                pygame.draw.rect(screen, BLACK, man[i])
            screen.blit(text, (10, 10))
            pygame.display.update()
            clock.tick(60)