from hangman_art import stages, logo
import os


def game_lost_text(chosen_word):
    os.system('clear')
    print(logo)
    print(stages[0])
    print(f"IT WAS {chosen_word}!")
    print(f"***********************YOU LOSE**********************")


def game_win_text():
    print("****************************YOU WIN****************************")


def validate_game_over(lives, chosen_word, display):
    game_over = False

    if lives == 0:
        game_over = True

        game_lost_text(chosen_word)
        return True

    if "_" not in display:
        game_over = True
        game_win_text()

    return game_over
