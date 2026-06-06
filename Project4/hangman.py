import random
import sys
import time

# List of mystery words for the game
WORD_BANK = [
    "PYTHON", "ENGINEERING", "COMPILER", "MATRIX", "DATABASE", 
    "ALGORITHM", "GITHUB", "TERMINAL", "VARIABLE", "FUNCTION", "DEBUGGING",
    "INHERITANCE", "ENCAPSULATION", "POLYMORPHISM", "ABSTRACTION",
    "NETWORK", "SECURITY", "ENCRYPTION", "DECRYPTION", "VIRTUALIZATION",
    "ARTIFICIAL", "INTELLIGENCE", "MACHINE", "LEARNING", "DOG", "CAT", 
    "ELEPHANT", "GIRAFFE", "KANGAROO", "PENGUIN", "DOLPHIN", "TIGER", 
    "LION", "BEAR","APPLE", "BANANA", "ORANGE", "STRAWBERRY", "WATERMELON", 
    "PINEAPPLE", "GRAPE", "PEACH", "CHERRY", "BLUEBERRY",
    "JAZZ", "BLUES", "ROCK", "CLASSICAL", "HIPHOP", "ELECTRONIC",
    "SOFTWARE", "HARDWARE", "FIRMWARE", "CLOUD",
    "MOVIE", "MUSIC", "BOOK", "GAME", "ART", "DANCE", "THEATER",
    "SPACE", "GALAXY", "PLANET", "ASTEROID", 
    "COMET", "BLACKHOLE", "SUPERNOVA", "NEBULA", "COSMOS"
]

# Array matrix mapping the 7 structural stages of the gallows visual art
HANGMAN_ART = [
    [
        "   +---+  ",
        "   |   |  ",
        "       |  ",
        "       |  ",
        "       |  ",
        "       |  ",
        "=========="
    ],
    [
        "   +---+  ",
        "   |   |  ",
        "   O   |  ",
        "       |  ",
        "       |  ",
        "       |  ",
        "=========="
    ],
    [
        "   +---+  ",
        "   |   |  ",
        "   O   |  ",
        "   |   |  ",
        "       |  ",
        "       |  ",
        "=========="
    ],
    [
        "   +---+  ",
        "   |   |  ",
        "   O   |  ",
        "  /|   |  ",
        "       |  ",
        "       |  ",
        "=========="
    ],
    [
        "   +---+  ",
        "   |   |  ",
        "   O   |  ",
        "  /|\\  |  ",
        "       |  ",
        "       |  ",
        "=========="
    ],
    [
        "   +---+  ",
        "   |   |  ",
        "   O   |  ",
        "  /|\\  |  ",
        "  /    |  ",
        "       |  ",
        "=========="
    ],
    [
        "   +---+  ",
        "   |   |  ",
        "   O   |  ",
        "  /|\\  |  ",
        "  / \\  |  ",
        "       |  ",
        "=========="
    ]
]

class UIController:
    @staticmethod
    def draw_header(title):
        print("\n" + " " * 4 + "▄" * 44)
        print("    █" + " ".center(42) + "█")
        print("    █" + f"{title}".center(42) + "█")
        print("    █" + " ".center(42) + "█")
        print("    " + "▀" * 44 + "\n")

    @staticmethod
    def render_gallows(wrong_guesses_count):
        """Prints the exact stage of the hangman state based on wrong counter."""
        print("    🎨 CURRENT STATUS:")
        for row in HANGMAN_ART[wrong_guesses_count]:
            print(f"    {row}")
        print("")


def play_hangman_round():
    secret_word = random.choice(WORD_BANK)
    guessed_letters = set()
    wrong_guesses = 0
    max_allowed_errors = 6

    UIController.draw_header("🪓  RETRO HANGMAN GAME  🪓")
    print("🤖 System has locked onto a random secret word. Start guessing letters!\n")

    while wrong_guesses < max_allowed_errors:
        # Display the visual gallows art structure
        UIController.render_gallows(wrong_guesses)

        # Generate the mystery word state (e.g., P _ T H _ N)
        display_word = [letter if letter in guessed_letters else "_" for letter in secret_word]
        print(f"👉 Mystery Word Target:  {' '.join(display_word)}")
        print(f"🗂️  Letters Guessed So Far: {', '.join(sorted(guessed_letters)) if guessed_letters else '[None]'}")
        print(f"⚠️  Mistakes Made: {wrong_guesses} / {max_allowed_errors}\n")

        # Win check optimization
        if "_" not in display_word:
            UIController.draw_header("🎉 DECRYPTION SUCCESSFUL 🎉")
            print(f"Excellent! You guessed the entire word correctly: **{secret_word}**\n")
            return True

        guess = input("👉 Enter a single letter guess: ").strip().upper()
        print("\n" + "-" * 50 + "\n")

        # Guard rails for validation checking rules
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Input Validation Error: Please input exactly one single alphabetic letter!\n")
            continue

        if guess in guessed_letters:
            print(f"ℹ️  Duplicate Warning: You already guessed the letter '{guess}'. Try another one!\n")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"🎯 GOOD SHOT! The letter '{guess}' exists in the secret word structure.\n")
        else:
            print(f"💥 MISS! The letter '{guess}' does not exist in the secret word layout.\n")
            wrong_guesses += 1

    # If execution loop exits here, the user ran out of guess allocations
    UIController.render_gallows(wrong_guesses)
    UIController.draw_header("💀 GAME OVER: PLAYER HANGED 💀")
    print(f"You ran out of attempts! The correct target word was: **{secret_word}**\n")
    return False


def main():
    while True:
        play_hangman_round()
        rematch = input("❓ Do you want to try another word? (yes/no): ").strip().lower()
        if rematch not in ['yes', 'y']:
            UIController.draw_header("👋 HANGMAN TERMINATED 👋")
            print("Game instance memory context dropped successfully.")
            break

if __name__ == "__main__":
    main()