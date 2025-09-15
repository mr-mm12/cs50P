import random
import string


def generate_password(length: int, difficulty: str) -> str:
    """
    Generate a random password based on the specified difficulty level.

    Parameters:
    - length: int, length of the password (minimum 4)
    - difficulty: str, one of "easy", "normal", "difficult", "very difficult"

    Returns:
    - str: the generated password
    """
    if length < 4:
        raise ValueError("Password length must be at least 4")

    # Character sets
    digits = string.digits
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    symbols = "@!#$%&*+/-._="

    # Choose character set based on difficulty
    if difficulty == "easy":
        chars = digits
    elif difficulty == "normal":
        chars = digits + symbols
    elif difficulty == "difficult":
        chars = digits + symbols + upper
    elif difficulty == "very difficult":
        chars = digits + symbols + upper + lower
    else:
        raise ValueError("Unknown difficulty level!")

    # Generate password
    return "".join(random.choice(chars) for _ in range(length))


def check_strength(password: str) -> str:
    """
    Evaluate the strength of a password.

    Returns one of: "Weak", "Medium", "Strong", "Very Strong"
    """
    strength = 0
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c.islower() for c in password):
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c in "@!#$%&*+/-._=" for c in password):
        strength += 1

    if strength <= 1:
        return "Weak"
    elif strength == 2:
        return "Medium"
    elif strength == 3:
        return "Strong"
    else:
        return "Very Strong"


def save_password(password: str, filename: str = "passwords.txt") -> None:
    """
    Save the password to a file.

    Each password is appended as a new line.
    """
    with open(filename, "a") as f:
        f.write(password + "\n")


def main():
    """
    Main function to run the password generator program.
    Asks user for password length and difficulty, generates password,
    checks strength, and saves it to a file.
    """
    try:
        wh = int(input("Number of characters in password: "))
        level = input("Difficulty? (easy / normal / difficult / very difficult): ").strip().lower()
        password = generate_password(wh, level)
        print("\nYour password is:", password)
        print("Strength:", check_strength(password))
        save_password(password)
        print("Password saved to passwords.txt\n")
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()

# Mohammad_Reza_Mokhtari_Kia
