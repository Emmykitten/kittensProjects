import art
import random

#Variables
EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5
ANSWER = random.randint(1,100)

def check_answer(user_guess, attempts):
    """checks users guess against actual answer"""
    if user_guess == ANSWER:
        print("YOU WIN!")
        return user_guess
    elif user_guess > ANSWER:
        print("Too High")
        return attempts - 1
    elif user_guess < ANSWER:
        print("Too Low")
        return attempts - 1

def set_difficulty():
    """sets the difficulty of the game based on user response. Also has input checks"""
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard' ").lower()
        if difficulty == "easy":
            return EASY_ATTEMPTS
        elif difficulty == "hard":
            return HARD_ATTEMPTS
        else:
            print("Please choose a difficulty")
            continue

def play():
    print (art.logo)
    print("Welcome to the number guessing game!")
    print("Im thinking of a number between 1 and 100.")

    attempts = set_difficulty()
    guess = 0

    while guess != ANSWER:
        print(ANSWER)
        print(f"You have {attempts} remaining to guess the number")
        guess = int(input("Make a guess: "))
        attempts = check_answer(guess, attempts)
        if attempts == 0:
            print("You've run out of guesses :(")
            return
        else:
            print("Guess Again")
play()
