from art import logo
import random
import os

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def init_game():
    output = {}
    user_random = []
    dealer_random = []

    user_random.append(deal_card())
    user_random.append(deal_card())
    dealer_random.append(deal_card())
    dealer_random.append(deal_card())

    output["user"] = user_random
    output["dealer"] = dealer_random

    print(f"Your cards: {output["user"]}, current score: {get_sum(output["user"])}")
    print(f"Computer's first card: {(output["dealer"][0])}")

    return output


def get_sum(input_list):

    if sum(input_list) > 21 and 11 in input_list:
        list.remove(input_list[11])
        list.append(1)

    return sum(input_list)


def get_winner(user_sum, dealer_sum):
    if dealer_sum == 21:
        print("Dealer got Blackjack! You loose!")
    elif user_sum == 21:
        print("Blackjack! You win")
    elif user_sum > 21:
        print("You went over. You loose")
    elif dealer_sum > 21:
        print("Dealer bust, You win!")
    elif user_sum == dealer_sum:
        print("It's a tie!")
    elif user_sum > dealer_sum:
        print("You win!")
    else:
        print("Dealer win")


def play():

    print(logo)
    player_cards = []
    dealer_cards = []

    deal_user_cards = True

    # Initialize game, deal cards
    for _ in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while deal_user_cards:

        print(f"Your cards: {player_cards}, current score: {get_sum(player_cards)}")
        print(f"Computer's first card: {dealer_cards[0]}")

        if get_sum(player_cards) > 21:
            deal_user_cards = False

        user_hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if user_hit == 'y':
            player_cards.append(deal_card())
        else:
            deal_user_cards = False

    while get_sum(dealer_cards) < 17:

        dealer_cards.append(deal_card())


    print(f"Your final hand: {player_cards}, final score: {get_sum(player_cards)}")
    print(f"Computer's final card: {dealer_cards}, final score: {get_sum(dealer_cards)}")

    get_winner(get_sum(player_cards), get_sum(dealer_cards))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    os.system('clear')
    play()










