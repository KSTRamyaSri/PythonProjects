import os
import secrets
import string
import sys
import time

class SecurityUI:
    @staticmethod
    def clear_line():
        sys.stdout.write("\r" + " " * 60 + "\r")
        sys.stdout.flush()

    @staticmethod
    def show_encryption_loader():
        """Simulates key derivation calculations for visual polish."""
        frames = ["Collecting entropy...", "Mixing bitwise salts...", "Finalizing hash token..."]
        for frame in frames:
            sys.stdout.write(f"\r    {frame}")
            sys.stdout.flush()
            time.sleep(0.4)
        SecurityUI.clear_line()

    @staticmethod
    def draw_header(title):
        """Sleek Cyber Block Header Design Pattern"""
        print("\n" + " " * 4 + "▄" * 44)
        print("    █" + " ".center(42) + "█")
        print("    █" + f"{title}".center(42) + "█")
        print("    █" + " ".center(42) + "█")
        print("    " + "▀" * 44 + "\n")


def generate_secure_password(length, use_upper, use_lower, use_digits, use_special):
    char_pool = ""
    if use_upper:   char_pool += string.ascii_uppercase
    if use_lower:   char_pool += string.ascii_lowercase
    if use_digits:  char_pool += string.digits
    if use_special: char_pool += string.punctuation

    if not char_pool:
        return None

    password_chars = []
    if use_upper:   password_chars.append(secrets.choice(string.ascii_uppercase))
    if use_lower:   password_chars.append(secrets.choice(string.ascii_lowercase))
    if use_digits:  password_chars.append(secrets.choice(string.digits))
    if use_special: password_chars.append(secrets.choice(string.punctuation))

    remaining_length = length - len(password_chars)
    password_chars += [secrets.choice(char_pool) for _ in range(remaining_length)]

    secure_shuffled = sorted(password_chars, key=lambda x: secrets.randbits(16))
    return "".join(secure_shuffled)


def evaluate_entropy_strength(length, use_upper, use_lower, use_digits, use_special):
    pool_size = 0
    if use_upper:   pool_size += 26
    if use_lower:   pool_size += 26
    if use_digits:  pool_size += 10
    if use_special: pool_size += 32

    if pool_size == 0 or length < 1:
        return "CRITICAL FAILURE"

    if length < 8:
        return "WEAK (Length too short for secure operations)"
    elif length < 15 or pool_size <= 36:
        return "MEDIUM (Vulnerable to dedicated dictionary clusters)"
    else:
        return "STRONG (Excellent cryptographic complexity index)"


def main():
    SecurityUI.draw_header("SECURE TOKEN GENERATOR")
    
    while True:
        try:
            print("CONFIGURATION POLICIES:")
            print("-----------------------")
            length = int(input("Enter target password length (Recommended >= 15): ").strip())
            if length < 6:
                print("Security Error: Passwords shorter than 6 characters are denied.\n")
                continue
        except ValueError:
            print("Input Parsing Mismatch: Whole integers required.\n")
            continue

        print("\nCHARACTER SET ENTROPY CONTROL:")
        print("---------------------------------")
        include_upper   = input("Include Uppercase Letters (A-Z)? (y/n): ").strip().lower() == 'y'
        include_lower   = input("Include Lowercase Letters (a-z)? (y/n): ").strip().lower() == 'y'
        include_digits  = input("Include Numerical Digits (0-9)?  (y/n): ").strip().lower() == 'y'
        include_special = input("Include Special Symbols (@-#-$)?  (y/n): ").strip().lower() == 'y'

        print("\n" + "-" * 50 + "\n")
        SecurityUI.show_encryption_loader()

        token = generate_secure_password(length, include_upper, include_lower, include_digits, include_special)

        if not token:
            print("Failure: You must select at least one character category.\n")
        else:
            strength = evaluate_entropy_strength(length, include_upper, include_lower, include_digits, include_special)
            
            SecurityUI.draw_header("SECURE CREDS LOGGED")
            print(f"    Generated Token: {token}")
            print(f"    Strength Metric: {strength}")
            print("\n" + "=" * 50 + "\n")

        rematch = input("Initialize a clean generation thread context? (yes/no): ").strip().lower()
        if rematch not in ['yes', 'y']:
            SecurityUI.draw_header("ENVIRONMENT SECURED")
            break
        print("\n" + "-" * 50 + "\n")


if __name__ == "__main__":
    main()