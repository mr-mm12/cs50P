def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Rule 1: Length between 2 and 6 characters
    if not (2 <= len(s) <= 6):
        return False

    # Rule 2: Must start with at least two letters
    if len(s) < 2 or not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Rule 3: Numbers must be at the end and first number cannot be '0'
    number_started = False
    for i, c in enumerate(s):
        if c.isdigit():
            if not number_started:
                # first number
                if c == '0':
                    return False
                number_started = True
        else:
            if number_started:
                # letter after number is invalid
                return False

    # Rule 4: No punctuation, spaces, or periods
    for c in s:
        if not c.isalnum():
            return False

    return True


main()

# Mohammad_Reza_Mokhtari_Kia
