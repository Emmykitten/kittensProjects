"""
higherlower.py
Emily Jacobson
9/14/2024
"""
from art import logo, vs
from game_data import data
import random

score = 0
game_continue = True
#Choose a random account
act_b = random.choice(data)
print(logo)


def format_data(account):
    """Takes act data and returns in a printable format"""
    act_name = account["name"]
    act_des = account["description"]
    act_country = account["country"]
    return f"{act_name} a {act_des}, from {act_country}"

def check_guess(guess, act_a_followers, act_b_followers):
    if act_a_followers > act_b_followers:
        return guess == "a"
    else:
        return guess == "b"


while game_continue:
    #Swap accounts
    act_a = act_b
    act_b = random.choice(data)

    #Make sure both accounts are not the same
    if act_a == act_b:
        act_b = random.choice(data)

    print(f"Compare A: {format_data(act_a)}.")
    print(vs)
    print(f"Against B: {format_data(act_b)}.")

    guess = input("Which has more followers? type 'A' or 'b' ").lower()

    act_a_followers = act_a["follower_count"]
    act_b_followers = act_b["follower_count"]

    print("\n" * 20)
    print(logo)

    #Check users answer
    answer = check_guess(guess,act_a_followers,act_b_followers)

    if answer:
        score += 1
        print(f"You are correct! Current score: {score}")
    else:
        score = score
        print(f"sorry that was incorrect :( Final score: {score}")
        game_continue = False
