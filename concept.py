# Liste de 7 dessins du pendu : du dessin vide (0 erreur) au pendu complet (6 erreurs).
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

# Définition des variables.
hidden_word = "Snake"                           # Mot à deviner.
hidden_word_lower = hidden_word.lower()         # Mot à deviner en minuscule.
guess_random_word = ["*"] * len(hidden_word)    # Mot affiché au joueur, remplacé par des * pour ne pas le révéler.
life_number = 6

# La boucle de jeu.
while True:
    print("The word to find is:", "".join(guess_random_word), "and your number of lives is:", life_number)  # Affiche le mot masqué et les vies restantes.

    # Renseigner une lettre.
    guess_letter = ""
    while len(guess_letter) != 1 or not guess_letter.isalpha(): # Autorise uniquement la saisie d'une lettre, et bloque la saisie de chiffre et de caractère spéciaux.
        guess_letter = input("Enter a letter: ").lower()        # Lettre mise en minuscule, normalisé avec le mot mis en minuscule.

    if guess_letter in hidden_word_lower:               # Compare si la lettre est dans le mot à deviner.
        for i, char in enumerate(hidden_word_lower):    # Parcourt les lettres du mot à deviner.
            if char == guess_letter:                    # Si la lettre renseignée correspond à/aux lettres du mot à deviner.
                guess_random_word[i] = guess_letter     # Remplace le * par la lettre du mot.
    else:
        life_number -= 1

    print(HANGMANPICS[6 - life_number])                 # Fait apparaitre le pendu, en fonction de l'état de la partie.

    # Condition de Victoire/Défaite
    if hidden_word_lower == "".join(guess_random_word): # Si le joueur renseigne toutes les lettres, le joueur gagne.
        print("You win! The word is:", hidden_word)
        break
    elif life_number == 0:  # Fait apparaître le pendu entièrement si le joueur n'a plus de vie.
        print("You lose! the correct word is:", hidden_word)
        break