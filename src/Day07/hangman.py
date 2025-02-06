import random
import os
import common
from hangman_words import word_list
from hangman_art import logo, stages


lives = 6

print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

GAME_OVER = False
correct_letters = []

while not GAME_OVER:

    # TODO-6: - Update the code below to tell the user how many lives they have left.
    print(
        f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in correct_letters:
        print(f"You already guessed letter {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
    GAME_OVER = common.validate_game_over(lives, chosen_word, display)

    if lives > 0:
        os.system('clear')

        print(logo)
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        print("Word to guess: " + display)
        print(stages[lives])
