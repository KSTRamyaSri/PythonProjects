import random
import sys
import time

# Dictionary mapping choices to their corresponding ASCII graphic illustrations
HAND_ART = {
    "ROCK": [
        "    _______      ",
        "---'   ____)     ",
        "      (_____)    ",
        "      (_____)    ",
        "      (____)     ",
        "---.__(___)      "
    ],
    "PAPER": [
        "    _______       ",
        "---'   ____)____  ",
        "          ______) ",
        "          _______)",
        "         _______) ",
        "---.__________)   "
    ],
    "SCISSORS": [
        "    _______       ",
        "---'   ____)____  ",
        "          ______) ",
        "       ──────────)",
        "      (____)      ",
        "---.__(___)       "
    ]
}

# 🧠 WINNING MATRIX DICTIONARY (Rules Engine Lookup Table)
# Format: MATRIX[PLAYER_CHOICE] = THE_CHOICE_IT_BEATS
WIN_RULES_MATRIX = {
    "ROCK": "SCISSORS",
    "PAPER": "ROCK",
    "SCISSORS": "PAPER"
}

class TerminalLayout:
    @staticmethod
    def draw_header(title):
        print("\n" + " " * 4 + "▄" * 44)
        print("    █" + " ".center(42) + "█")
        print("    █" + f"{title}".center(42) + "█")
        print("    █" + " ".center(42) + "█")
        print("    " + "▀" * 44 + "\n")

    @staticmethod
    def show_clash_animation():
        """Simulates anticipation by printing a countdown sequence."""
        print("    🤖 Chitti is calculating probability vectors... ", end="", flush=True)
        for count in ["3...", "2...", "1...", "💥 CLASH!"]:
            print(f"{count} ", end="", flush=True)
            time.sleep(0.4)
        print("\n")

    @staticmethod
    def render_hands_side_by_side(player_choice, computer_choice):
        """Stitches the 2D string matrices of both selections horizontally."""
        print(f"    [ PLAYER: {player_choice} ]".center(22) + "vs" + f"[ COMPUTER: {computer_choice} ]".center(24))
        print("-" * 50)
        for row in range(6):
            print(f"  {HAND_ART[player_choice][row]}      {HAND_ART[computer_choice][row]}")
        print("-" * 50 + "\n")


def play_tournament_round(scoreboard):
    TerminalLayout.draw_header("✂️  ROCK PAPER SCISSORS ENGINE  ✂️")
    print("⚡ OPTIONS MENU:")
    print("  [R] Rock 🪨")
    print("  [P] Paper 📄")
    print("  [S] Scissors ✂️\n")

    # Mapping user single character shorthand keys to operational strings
    input_map = {"R": "ROCK", "P": "PAPER", "S": "SCISSORS"}
    
    while True:
        user_input = input("👉 Enter your choice code (R, P, S): ").strip().upper()
        if user_input in input_map:
            player_move = input_map[user_input]
            break
        print("❌ Invalid token selection. Please enter R, P, or S.")

    computer_move = random.choice(["ROCK", "PAPER", "SCISSORS"])
    
    print("\n" + "-" * 50 + "\n")
    TerminalLayout.show_clash_animation()
    TerminalLayout.render_hands_side_by_side(player_move, computer_move)

    # Core Decision Processing Engine via Rules Matrix Lookup Table
    if player_move == computer_move:
        print("🤝 STALEMATE VALUE ENCOUNTERED! Both picked the same signature vector.\n")
        scoreboard["ties"] += 1
    elif WIN_RULES_MATRIX[player_move] == computer_move:
        print(f"🎉 PLAYER VICTORIOUS! {player_move} breaks through {computer_move} cleanly.\n")
        scoreboard["player_score"] += 1
    else:
        print(f"💀 COMPUTER WINS! {computer_move} engulfs {player_move} completely.\n")
        scoreboard["computer_score"] += 1


def main():
    # Session state scoreboard storage matrix
    tournament_stats = {"player_score": 0, "computer_score": 0, "ties": 0}
    
    while True:
        play_tournament_round(tournament_stats)
        
        TerminalLayout.draw_header("📊 TOURNAMENT MATRIX SCOREBOARD 📊")
        print(f"  🙍‍♂️ Player Score  : {tournament_stats['player_score']}")
        print(f"  🤖 Computer Score: {tournament_stats['computer_score']}")
        print(f"  🔄 Draw Ties     : {tournament_stats['ties']}")
        print("\n" + "=" * 50 + "\n")
        
        rematch = input("❓ Stay in matching tournament environment loop? (yes/no): ").strip().lower()
        if rematch not in ['yes', 'y']:
            if tournament_stats["player_score"] > tournament_stats["computer_score"]:
                print("\n 🙍‍♂️ Player wons the tournament! 🏆")
            elif tournament_stats["computer_score"] > tournament_stats["player_score"]:
                print("\n 🤖 Computer wons the tournament! 🏆")
            else:
                print("\n 🤝 The tournament ends in a draw! 🤝")
            TerminalLayout.draw_header("👋 TOURNAMENT DISCONNECTED 👋")
            break

if __name__ == "__main__":
    main()