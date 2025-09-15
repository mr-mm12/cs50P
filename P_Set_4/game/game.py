import random


def GPI(prompt):
    """Prompt the user until they enter a positive integer."""
    while True:
        try:
            get_level = int(input(prompt))
            if get_level > 0:
                return get_level  # Return the positive integer
        except ValueError:
            pass  # Ignore invalid input and ask again


def main():
    # Ask user for the level
    get_level = GPI("Level: ")

    # Generate a random integer between 1 and get_level
    sn = random.randint(1, get_level)

    while True:
        g = GPI("Guess: ")
        if g < sn:
            print("Too small!")
        elif g > sn:
            print("Too large!")
        else:  # g == sn
            print("Just right!")
            break  # Exit the loop


if __name__ == "__main__":
    main()

# Mohammad_Reza_Mokhtari_Kia
