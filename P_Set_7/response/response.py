from validators import email


def main():
    # Prompt user for email input
    user_input = input("Email: ")

    # Use validators.email to check if the input is a valid email
    if email(user_input):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()

# Mohammad_Reza_Mokhtari_Kia
