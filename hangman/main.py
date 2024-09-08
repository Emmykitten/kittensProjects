import random
import words
import art

word_list = words.words_list
gameover = False
display = ""
guessed_letters = set()
life = 0
chosen_word = random.choice(word_list)
length = len(chosen_word)
stages = art.stages
print("Word to guess:\n")
print("_ " * length)

while display != chosen_word and not gameover:
    print(f'{stages[life]}')
    guess = input("Guess a letter: ").lower()
    new_display = ""

    if guess in guessed_letters:
        print("You already guessed that letter")
        continue
    guessed_letters.add(guess)
    for letter in chosen_word:
        if letter == guess or letter in display:
            print(f"You guessed {guess}")
            new_display += letter
        else:
            new_display += "_ "
    display = new_display
    if guess not in chosen_word:
        if life < 6:
            life += 1
            print(f"{guess} is not a letter")
        else:
            gameover = True
            print(f"Sorry Game Over!\n The correct word was {chosen_word}")
    print(display)