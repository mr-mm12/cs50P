import random


def main():
    score = 0  # Initialize score counter

    # Get a valid level from the user
    level = get_level()

    # Ask 10 questions
    for _ in range(10):
        x = generate_integer(level)  # Generate first random number
        y = generate_integer(level)  # Generate second random number
        correct_answer = x + y       # Calculate the correct answer

        tries = 0
        while tries < 3:
            try:
                guess = int(input(f"{x} + {y} = "))  # Prompt user for answer
                if guess == correct_answer:
                    score += 1
                    break  # Correct answer, move to next question
                else:
                    print("EEE")  # Wrong answer
            except ValueError:
                print("EEE")  # Non-integer input
            tries += 1

        # After 3 failed attempts, print the correct answer
        if tries == 3:
            print(correct_answer)

    # Print only the number of correct answers (required by check50)
    print(score)


def get_level():
    """Prompt the user until they enter a valid level: 1, 2, or 3"""
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass  # Ignore invalid input and prompt again


def generate_integer(level):
    """Return a random non-negative integer with 'level' digits"""
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        # If level is invalid, raise ValueError
        raise ValueError


if __name__ == "__main__":
    main()


# Mohammad_Reza_Mokhtari_Kia
