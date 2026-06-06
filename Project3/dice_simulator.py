import random
import sys
import time

# Dictionary mapping dice values to clean visual ASCII graphics
DICE_ART = {
    1: [
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
    ],
    2: [
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"
    ],
    3: [
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"
    ],
    4: [
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"
    ],
    5: [
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"
    ],
    6: [
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"
    ]
}

class TerminalUI:
    @staticmethod
    def draw_header(title):
        print("\n" + " " * 4 + "▄" * 44)
        print("    █" + " ".center(42) + "█")
        print("    █" + f"{title}".center(42) + "█")
        print("    █" + " ".center(42) + "█")
        print("    " + "▀" * 44 + "\n")

    @staticmethod
    def play_shuffle_animation(num_dice):
        """Simulates the physical shaking of dice before settling."""
        print("🎲 Shaking the dice cup...", end="", flush=True)
        for _ in range(6):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(0.12)
        print("\n")

    @staticmethod
    def print_dice_side_by_side(rolls):
        """Prints multiple dice blocks side by side instead of stacked vertically."""
        # Loop through each row (layer) of the dice ASCII layout matrix
        for row in range(5):
            line_str = "    "
            for value in rolls:
                line_str += DICE_ART[value][row] + "  "
            print(line_str)
        print("")


def main():
    TerminalUI.draw_header("🎲  3D DICE SIMULATOR  🎲")
    
    history_rolls = []
    
    while True:
        print("⚡ OPERATIONAL MENU:")
        print("  [1] Roll Single Die (1d6)")
        print("  [2] Roll Multiple Dice (Custom Squad)")
        print("  [3] View Session History Matrix")
        print("  [4] Exit Simulator\n")
        
        choice = input("👉 Enter choice (1-4): ").strip()
        print("-" * 50 + "\n")
        
        if choice == "1":
            TerminalUI.play_shuffle_animation(1)
            result = random.randint(1, 6)
            history_rolls.append([result])
            
            print(f"🎉 Result Vector Locked! You rolled a {result}:\n")
            TerminalUI.print_dice_side_by_side([result])
            
        elif choice == "2":
            try:
                count = input("👉 How many dice do you want to roll together?: ").strip()
                count = int(count)
                if count <= 0 or count > 6:
                    print("❌ Constraint Warning: Please enter a count between 1 and 6 to fit the screen layout safely.\n")
                    continue
            except ValueError:
                print("❌ Input parsing mismatch. Real integer constants required.\n")
                continue
                
            TerminalUI.play_shuffle_animation(count)
            results = [random.randint(1, 6) for _ in range(count)]
            history_rolls.append(results)
            
            print(f"🎉 Results Vector Locked! Sum total = {sum(results)}:\n")
            TerminalUI.print_dice_side_by_side(results)
            
        elif choice == "3":
            TerminalUI.draw_header("📊 ROLLING ARCHIVE MATRIX 📊")
            if not history_rolls:
                print("    [No runtime vectors recorded in active session state memory]")
            else:
                for idx, roll_set in enumerate(history_rolls, 1):
                    print(f"  • Batch #{idx}: {roll_set} (Total Sum: {sum(roll_set)})")
            print("\n" + "-" * 50 + "\n")
            
        elif choice == "4":
            TerminalUI.draw_header("👋 SIMULATION CONTEXT CLOSED 👋")
            break
        else:
            print("❌ Invalid menu action code indicator. Retry.\n")


if __name__ == "__main__":
    main()