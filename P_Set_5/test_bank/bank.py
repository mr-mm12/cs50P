# Function to run the program
def main():
    greeting = input("Greeting: ").strip()   # Get input from the user
    print(f"${value(greeting)}")             # Call value() and print result


# Function that returns amount based on greeting
def value(greeting):
    # Case-insensitive comparison
    greeting = greeting.lower()

    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


# Entry point of the program
if __name__ == "__main__":
    main()

# Mohammad_Reza_Mokhtari_Kia
