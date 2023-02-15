import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the window
win_width = 640
win_height = 480
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Hangman")

# Set up the hangman parts
hangman_parts = [
    pygame.Rect(50, win_height - 50, 100, 20), # base
    pygame.Rect(100, 50, 20, win_height - 100), # post
    pygame.Rect(100, 50, 150, 20), # top
    pygame.Rect(240, 70, 10, 40), # head
    pygame.Rect(245, 110, 2, 100), # body
    pygame.Rect(240, 150, 10, 2), # left arm
    pygame.Rect(250, 150, 10, 2), # right arm
    pygame.Rect(245, 210, 2, 80), # left leg
    pygame.Rect(250, 210, 2, 80), # right leg
]
num_wrong_guesses = 0

# Set up the word list
word_list = ["python", "game", "hangman"]
word = random.choice(word_list)
guessed_word = ["_" for i in range(len(word))]

# Set up the font
font = pygame.font.SysFont(None, 32)

# Set up the clock
clock = pygame.time.Clock()

# Run the game loop
game_running = True
while game_running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode.isalpha():
                # Check if the letter has already been guessed
                if event.unicode in guessed_word:
                    continue

                # Check if the letter is in the word
                if event.unicode in word:
                    for i in range(len(word)):
                        if word[i] == event.unicode:
                            guessed_word[i] = event.unicode
                else:
                    num_wrong_guesses += 1

    # Check if the player has won or lost
    if num_wrong_guesses == len(hangman_parts):
        text = font.render("You lose! The word was '%s'." % word, True, (255, 0, 0))
        game_running = False
    elif "_" not in guessed_word:
        text = font.render("You win! The word was '%s'." % word, True, (0, 255, 0))
        game_running = False
    else:
        text = font.render(" ".join(guessed_word), True, (255, 255, 255))

    # Draw the game objects
    win.fill((0, 0, 0))
    for part in hangman_parts[:num_wrong_guesses]:
        pygame.draw.rect(win, (255, 255, 255), part)
    win.blit(text, (10, 10))
    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)

# Clean up Pygame
pygame.quit()