import re       # Regular expressions — for pattern searching in strings
import string   # Contains lists of characters like string.punctuation

def check_password_strength(password):
    """
    Analyzes a password and returns a strength score with feedback.

    Parameters:
        password (str): The password to analyze

    Returns:
        dict: Contains score, rating, and list of feedback messages
    """

    score = 0           # We'll add points for each passed criterion
    feedback = []       # List of suggestions to improve the password
    passed = []         # List of criteria the password passed

    # ── CRITERION 1: Length ──────────────────────────────────
    length = len(password)

    if length >= 16:
        score += 3
        passed.append("✅ Length is excellent (16+ characters)")
    elif length >= 12:
        score += 2
        passed.append("✅ Length is good (12+ characters)")
    elif length >= 8:
        score += 1
        passed.append("✅ Length is acceptable (8+ characters)")
    else:
        feedback.append(f"❌ Too short ({length} chars). Use at least 8 characters.")

    # ── CRITERION 2: Uppercase Letters ──────────────────────
    # re.search() looks for any match of the pattern in the string
    # [A-Z] means "any character from A to Z"
    if re.search(r'[A-Z]', password):
        score += 1
        passed.append("✅ Contains uppercase letters (A-Z)")
    else:
        feedback.append("❌ Add uppercase letters (A, B, C ... Z)")

    # ── CRITERION 3: Lowercase Letters ──────────────────────
    if re.search(r'[a-z]', password):
        score += 1
        passed.append("✅ Contains lowercase letters (a-z)")
    else:
        feedback.append("❌ Add lowercase letters (a, b, c ... z)")

    # ── CRITERION 4: Numbers ────────────────────────────────
    # \d means "any digit 0-9"
    if re.search(r'\d', password):
        score += 1
        passed.append("✅ Contains numbers (0-9)")
    else:
        feedback.append("❌ Add at least one number (0-9)")

    # ── CRITERION 5: Special Characters ─────────────────────
    # re.escape makes sure special chars like . * + are treated literally
    special_chars = re.escape(string.punctuation)   # All symbols: !@#$%^&*...
    if re.search(f'[{special_chars}]', password):
        score += 1
        passed.append("✅ Contains special characters (!@#$%...)")
    else:
        feedback.append("❌ Add special characters like ! @ # $ % ^ & *")

    # ── BONUS: Check for Common Weak Patterns ───────────────
    common_passwords = [
        "password", "123456", "qwerty", "abc123", "password123",
        "letmein", "admin", "welcome", "monkey", "dragon"
    ]
    if password.lower() in common_passwords:
        score = 0
        feedback.append("⚠️  This is a very common password! Never use it.")

    # ── BONUS: Repeated characters check ────────────────────
    # r'(.)\1{2,}' matches any character repeated 3+ times in a row
    if re.search(r'(.)\1{2,}', password):
        score = max(0, score - 1)   # Penalty: reduce score by 1
        feedback.append("⚠️  Avoid repeating the same character 3+ times (e.g., 'aaa')")

    # ── Calculate Final Rating ───────────────────────────────
    # Max possible score is 7 (3 for length + 4 for character types)
    if score >= 6:
        rating = "💪 VERY STRONG"
        color_hint = "Green"
    elif score >= 4:
        rating = "👍 STRONG"
        color_hint = "Blue"
    elif score >= 3:
        rating = "😐 MODERATE"
        color_hint = "Yellow"
    elif score >= 1:
        rating = "😟 WEAK"
        color_hint = "Orange"
    else:
        rating = "🚨 VERY WEAK"
        color_hint = "Red"

    return {
        "score": score,
        "max_score": 7,
        "rating": rating,
        "passed": passed,
        "feedback": feedback
    }


def display_result(password, result):
    """Prints the analysis results in a nicely formatted way."""
    print("\n" + "="*50)
    print("        🔑 PASSWORD STRENGTH REPORT")
    print("="*50)
    print(f"  Password : {'*' * len(password)}")   # Hide the actual password
    print(f"  Length   : {len(password)} characters")
    print(f"  Score    : {result['score']} / {result['max_score']}")
    print(f"  Rating   : {result['rating']}")

    # Visual progress bar
    filled = int((result['score'] / result['max_score']) * 20)
    bar = "█" * filled + "░" * (20 - filled)
    print(f"  Strength : [{bar}]")

    if result['passed']:
        print("\n  ── What's Good ──")
        for item in result['passed']:
            print(f"  {item}")

    if result['feedback']:
        print("\n  ── Suggestions ──")
        for item in result['feedback']:
            print(f"  {item}")

    print("="*50)


def main():
    print("Welcome to the Password Strength Checker!")

    while True:
        print("\nOptions: (1) Check a password   (2) Exit")
        choice = input("Choice: ").strip()

        if choice == "1":
            # getpass hides the password while typing (more secure)
            # But for learning, we use regular input so you can see it
            password = input("Enter a password to check: ")

            if not password:
                print("❌ Password cannot be empty!")
                continue

            result = check_password_strength(password)
            display_result(password, result)

            # Tips section
            print("\n💡 TIP: A strong password looks like: Tr0ub4dor&3")
            print("   Use a mix of ALL four types + make it 12+ chars long.")

        elif choice == "2":
            print("\nGoodbye! 👋")
            break

        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()
