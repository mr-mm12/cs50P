from datetime import date, datetime
import sys
import inflect


def main():
    birth_str = input("Date of Birth (YYYY-MM-DD): ")

    try:
        # Parse date of birth
        birthdate = datetime.strptime(birth_str, "%Y-%m-%d").date()
    except ValueError:
        sys.exit("Invalid date format")

    # Today’s date (assume midnight)
    today = date.today()

    # Calculate minutes
    minutes = calculate_minutes(birthdate, today)

    # Convert number to words
    words = number_to_words(minutes)

    # Print result
    print(words.capitalize() + " minutes")


def calculate_minutes(birthdate, today):
    """Return total minutes between birthdate and today."""
    delta = today - birthdate
    return round(delta.days * 24 * 60)


def number_to_words(number):
    """Convert number to English words (with commas, hyphens, no 'and')."""
    p = inflect.engine()
    return p.number_to_words(number, andword="")


if __name__ == "__main__":
    main()

# Mohammad_Reza_Mokhtari_Kia
