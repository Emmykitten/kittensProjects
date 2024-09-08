import random
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
word_list = ["aardvark", "baboon", "camel"]
gameover = False
display = ""
guessed_letters = set()
life = 0
chosen_word = random.choice(word_list)
print(chosen_word)
length = len(chosen_word)


while display != chosen_word and not gameover:
    print(f'{stages[life]}')
    print("_ " * length)
    guess = input("Guess a letter: ").lower()
    new_display = ""

    if guess in guessed_letters:
        print("You already guessed that letter")
        continue
    guessed_letters.add(guess)
    for letter in chosen_word:
        if letter == guess or letter in display:
            new_display += letter
        else:
            new_display += "_"
    display = new_display
    if guess not in chosen_word:
        if life < 6:
            life += 1
        else:
            gameover = True
            print(f"Sorry Game Over!\n The correct word was {chosen_word}")
    print(display)