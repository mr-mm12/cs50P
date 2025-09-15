import sys


def main():
    # Create an empty list to store names
    names = []

    # Keep prompting the user for names until EOF (Ctrl+D on Unix/Mac, Ctrl+Z on Windows)
    try:
        while True:
            name = input()  # <-- No prompt text
            names.append(name)
    except EOFError:
        # End of input, exit the loop gracefully
        pass

    # Generate the farewell message
    if len(names) == 1:
        output = names[0]
    elif len(names) == 2:
        output = f"{names[0]} and {names[1]}"
    else:
        output = ", ".join(names[:-1]) + f", and {names[-1]}"

    # Print the final adieu message
    print(f"Adieu, adieu, to {output}")

    # Exit with code 0
    sys.exit(0)

if __name__ == "__main__":
    main()

# Mohammad_Reza_Mokhtari_Kia
