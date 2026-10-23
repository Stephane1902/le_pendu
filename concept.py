HANGMANPICS = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
hidden_word = "Tacos"
hidden_word_lower = hidden_word.lower()
guess_random_word = ["*"] * len(hidden_word)
life_number = 6

while True:
    print("The word to find is:", "".join(guess_random_word), "and your number of lives is:", life_number)

    guess_letter = ""
    while len(guess_letter) !=1 or not guess_letter.isalpha():
        guess_letter = input("Enter a letter: ").lower()

    if guess_letter in hidden_word_lower:
        for i, char in enumerate(hidden_word_lower):
            if char == guess_letter:
                guess_random_word[i] = guess_letter
    else:
        life_number -= 1

    if hidden_word_lower == "".join(guess_random_word):
        print("You win! The word is:", hidden_word)
        break
    elif life_number == 0:
        print(HANGMANPICS[6])
        print("You loose! the correct word is:", hidden_word)
        break
    else:
        print(HANGMANPICS[6 - life_number])
