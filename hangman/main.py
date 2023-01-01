from words import get_random_word
from os import system


class Hangman:
    def __init__(self):
        self.incorrect_count = 0
        self.word = get_random_word()
        self.guessed_word = []
        for i in range(len(self.word)):
            self.guessed_word.append("_")

    def play(self):
        guessed_letters = []
        while True:
            _ = system('clear')
            guessed_letters_str = ' '.join(guessed_letters)
            print(f'Your guesses: {guessed_letters_str}')
            print(self.draw_hangman())

            if self.guessed_word == self.word:
                print(self.word)
                print('You win!')
                break

            if self.incorrect_count >= 4:
                print("You lose!")
                print(f"The word was: {self.word}")
                break

            print(" ".join(self.guessed_word))
            print("Guess a letter!")
            guess = input()
            if guess not in guessed_letters:
                guessed_letters.append(guess)
            if guess in self.word:
                for i in range(len(self.word)):
                    if self.word[i] == guess:
                        self.guessed_word[i] = guess
            else:
                self.incorrect_count += 1

    def draw_hangman(self):
        if self.incorrect_count == 0:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
        elif self.incorrect_count == 1:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
        elif self.incorrect_count == 2:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |      \n"
                  "__|__\n")
        elif self.incorrect_count == 3:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |     \n"
                  "__|__\n")
        elif self.incorrect_count == 4:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")


game = Hangman()
game.play()