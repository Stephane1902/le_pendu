import eel
import random
import csv
from datetime import datetime
import json

DICT_FILE = "./data/dict.txt"
GAMES_FILE = "./data/games.csv"

ERRORS_LIMIT = 6

@eel.expose
def choose_random_word() -> int:
    with open(DICT_FILE, "r") as f:
        words = [l.strip() for l in f if l.strip()]

    selected_word = random.choice(words).lower()
    selected_word_length = len(selected_word)

    with open(GAMES_FILE, "a") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now(),
            selected_word,
            [],
            0,
            0
        ])

    return selected_word_length

@eel.expose
def play_user_move(char: str) -> dict[bool, list]:
    current_game = get_current_game()

    if int(current_game["total_errors"]) >= ERRORS_LIMIT:
        return

    current_word_to_guess = current_game["word_to_guess"]

    normalized_char = normalize_char(char)
    correct_locations = get_positions_of_char_in_word(current_word_to_guess, normalized_char)

    char_is_not_in_word = len(correct_locations) == 0

    updated_game = update_game_data(
        char = normalized_char,
        contains_error = char_is_not_in_word
    )

    user_has_won = all(l in updated_game["chars_already_tried"] for l in current_word_to_guess)
    is_end_of_game = int(updated_game["total_errors"]) == ERRORS_LIMIT or user_has_won

    return {
        "wordToGuess": current_word_to_guess if is_end_of_game else "",
        "playedCharacter": char,
        "roundIsSuccess" : not char_is_not_in_word,
        "correctLocationsOfRound" : correct_locations,
        "errorsNOfGame": updated_game["total_errors"],
        "isEndOfGame": is_end_of_game,
        "hasWon": user_has_won
    }

def get_current_game():
    with open(GAMES_FILE, newline='') as f:
        games = list(csv.DictReader(f))

    return games[-1]

def update_game_data(char: str, contains_error: bool) -> tuple[int]:
    current_game = get_current_game()

    current_game["chars_already_tried"] = json.loads(current_game["chars_already_tried"]) 
    current_game["chars_already_tried"].append(char)
    current_game["chars_already_tried"] = json.dumps(current_game["chars_already_tried"]) 

    current_game["total_tries"] = int(current_game["total_tries"]) + 1
    
    if contains_error:
        current_game["total_errors"] = int(current_game["total_errors"]) + 1

    with open(GAMES_FILE, newline='') as f:
        games = list(csv.DictReader(f))

    games[-1] = current_game

    with open(GAMES_FILE, "w") as f:
        writer = csv.DictWriter(f, fieldnames=games[0].keys())
        writer.writeheader()
        writer.writerows(games)

    return current_game

def get_positions_of_char_in_word(word: str, char: str) -> list[int]:          
    position = []

    for i, l in enumerate(word):        
        if l == char:                 
            position.append(i)   

    return position

def normalize_char(char: str) -> str:
    return char.lower()