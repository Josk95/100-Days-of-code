from art import logo
import random

EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5
def check_guess(guess, answer, turns):
    if guess < answer:
        print("Too low.")
        return turns -1
    elif guess > answer:
        print("To high.")
        return turns - 1
    else:
        print(f"You got it! The number was {answer}")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard':")

    if level.lower() == "easy":
        return EASY_LEVEL_TURN
    else:
        return  HARD_LEVEL_TURN

def game():
    print(logo)
    print("Welcome to the number guessing Game!")
    print("I'm thinking of a number between 1 and 100.")


    answer = random.randint(1, 100)
    number_of_guesses = set_difficulty()

    guess = 0
    while guess != answer and number_of_guesses > 0:

        print(f"You have {number_of_guesses} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        number_of_guesses = check_guess(guess, answer, number_of_guesses)

        if number_of_guesses == 0:
            print("You ran out of guesses! You loose!")
            return
        elif guess != answer:
            print("Guess again!")


game()






