import random
import sys
import time

class GameConsole:
    """Manages clean terminal styling and loading animations."""
    @staticmethod
    def clear_line():
        sys.stdout.write("\r" + " " * 60 + "\r")
        sys.stdout.flush()

    @staticmethod
    def show_loading(message="🤖 System is generating secret token... "):
        frames = ['▰▱▱▱▱▱▱', '▰▰▱▱▱▱▱', '▰▰▰▱▱▱▱', '▰▰▰▰▱▱▱', '▰▰▰▰▰▱▱', '▰▰▰▰▰▰▱', '▰▰▰▰▰▰▰']
        print(message, end="", flush=True)
        for frame in frames:
            sys.stdout.write(f"\r{message}[{frame}]")
            sys.stdout.flush()
            time.sleep(0.15)
        GameConsole.clear_line()

    print("\n" + "   " + "◇ " * 28)
    print("   " + "►►►  NUMBER GUESSING GAME  ◄◄◄".center(52))
    print("   " + "◇ " * 28 + "\n")  

    @staticmethod
    def draw_header(title):
        print("\n" + "=" * 50)
        print(f"{title.center(50)}")
        print("=" * 50 + "\n")

    @staticmethod
    def draw_footer():
        print("\n" + "-" * 50 + "\n")


def play_round(stats):
    GameConsole.draw_header("◇►►► CHOOSE YOUR DIFFICULTY ◄◄◄")
    print("  [1] Easy   (Range: 1-10,  Attempts: 5)")
    print("  [2] Medium (Range: 1-50,  Attempts: 7)")
    print("  [3] Hard   (Range: 1-100, Attempts: 10)\n")

    while True:
        choice = input("👉 Select difficulty (1-3): ").strip()
        if choice in ['1', '2', '3']:
            break
        print("❌ Invalid selection. Choose 1, 2, or 3.")

    # Difficulty Configurations Mapping
    configs = {
        "1": {"max_num": 10, "attempts": 5, "name": "Easy"},
        "2": {"max_num": 50, "attempts": 7, "name": "Medium"},
        "3": {"max_num": 100, "attempts": 10, "name": "Hard"}
    }
    
    current_config = configs[choice]
    secret_number = random.randint(1, current_config["max_num"])
    attempts_left = current_config["attempts"]
    
    GameConsole.draw_footer()
    GameConsole.show_loading(f"🎲 Setting up {current_config['name']} Mode... ")
    
    print(f"✅ Target Locked! Guess a number between 1 and {current_config['max_num']}.")
    print(f"📉 Total chances allowed: {attempts_left}\n")

    # Core game loop logic execution
    while attempts_left > 0:
        try:
            guess = input(f"◇◇ [Chances Left: {attempts_left}] Enter your guess: ").strip()
            guess = int(guess)
        except ValueError:
            print("❌ Input parsing error. Please enter a valid whole integer number!\n")
            continue

        if guess == secret_number:
            print(f"\n🎉 EXCELLENT JOB! You guessed the number {secret_number} correctly!")
            stats["wins"] += 1
            break
        elif guess < secret_number:
            print("📉 Too LOW! Try a bigger number.\n")
        else:
            print("📈 Too HIGH! Try a smaller number.\n")
            
        attempts_left -= 1

    if attempts_left == 0:
        print(f"\n💀 GAME OVER! You ran out of attempts.")
        print(f"The correct secret number was: {secret_number}")
        stats["losses"] += 1

    stats["rounds"] += 1


def main():
    # Session state tracking metrics dictionary
    stats = {"wins": 0, "losses": 0, "rounds": 0}
    
    while True:
        play_round(stats)
        
        # Display elegant spacious scoreboard matrix profile
        GameConsole.draw_header("📊 CURRENT SCOREBOARD 📊")
        print(f"  🏆 Total Wins   : {stats['wins']}")
        print(f"  ❌ Total Losses : {stats['losses']}")
        print(f"  🔄 Rounds Played: {stats['rounds']}")
        GameConsole.draw_footer()
        
        rematch = input("❓ Do you want to play another round? (yes/no): ").strip().lower()
        if rematch not in ['yes', 'y']:
            GameConsole.draw_header("👋 THANK YOU FOR PLAYING! 👋")
            print("Final scoreboard pushed successfully to memory terminal execution runtime tracker.")
            break

if __name__ == "__main__":
    main()