"""
blackjack.py
Emily Jacobson
9/9/2024
"""
import art
import random

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def display_cards(usr_cards, user_score, dlr_cards):
    """Display current cards for user and dealer"""
    print(f"Your cards: {usr_cards}, current score: {user_score}")
    print(f"Dealers first card: {dlr_cards[0]}")

def final_hand(usr_cards, dlr_cards, usr_score, dlr_score):
    """Once game is over, show final hand and call compare func"""
    user_score = calculate_score(usr_cards)
    dealer_score = calculate_score(dlr_cards)
    print(f"Your final hand: {usr_cards}, final score: {usr_score}")
    print(f"Dealers final hand: {dlr_cards}, final score: {dlr_score}")
    print(compare(user_score, dealer_score))

def compare(user_score, computer_score):
    """Compare the scores of the user and the computer to determine the winner."""
    if user_score != 0 or computer_score != 0:
        if user_score == 0:
            return "You win with a Blackjack!"
        if computer_score == 0:
            return "You lose. Dealer has a Blackjack!"
        if user_score > 21:
            return "You bust! You lose."
        if computer_score > 21:
            return "Dealer busts! You win."
        if user_score > computer_score:
            return "You win!"
        if user_score < computer_score:
            return "You lose."
        return "Draw!"
    return "Draw! Both have Blackjack!"


def play():
    user_cards = []
    dealer_cards = []
    # Clear terminal
    print("\033c", end="")
    print(art.logo)
    is_game_over = False
    while not is_game_over:
        for _ in range(2):
            user_cards.append(deal_card())
            dealer_cards.append(deal_card())
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)
        display_cards(user_cards, user_score, dealer_cards)
        if user_score == 0:
            final_hand(user_cards, dealer_cards, user_score, dealer_score)
        elif dealer_score == 0:
            final_hand(user_cards, dealer_cards, user_score, dealer_score)
        else:
            new_card = input("Type 'y' to get another card, type 'n' to pass ").lower()
            if new_card == "y":
                is_game_over = False
            elif new_card == "n":
                is_game_over = True
                while dealer_score != 0 and dealer_score < 17:
                    dealer_cards.append(deal_card())
                    dealer_score = calculate_score(dealer_cards)
                final_hand(user_cards, dealer_cards, user_score, dealer_score)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\033c", end="")
    play()