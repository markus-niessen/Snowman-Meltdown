"""Main game logic for Snowman Meltdown."""

import random

from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the current snowman stage and hidden word."""
    print(STAGES[mistakes])

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print()

def get_valid_guess(guessed_letters):
    """Gets a valid single letter guess from the user."""
    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("Please enter exactly one character.")
        elif not guess.isalpha():
            print("Please enter a letter.")
        elif guess in guessed_letters:
            print("You already guessed that letter.")
        else:
            return guess

def play_game():
    """Starts the Snowman Meltdown game."""
    secret_word = get_random_word()
    mistakes = 0
    guessed_letters = []
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = get_valid_guess(guessed_letters)
        print("You guessed:", guess)

        if guess in secret_word:
            guessed_letters.append(guess)
            print("Correct guess!")
        else:
            mistakes += 1
            print("Wrong guess!")

        word_completed = True

        for letter in secret_word:
            if letter not in guessed_letters:
                word_completed = False

        if word_completed:
            display_game_state(mistakes, secret_word, guessed_letters)
            print("You saved the snowman!")
            return

    display_game_state(mistakes, secret_word, guessed_letters)
    print("The snowman melted!")
    print("The secret word was:", secret_word)