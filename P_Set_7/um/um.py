import re
import sys

def main():
    # Prompt user for text input and print the number of "um" occurrences
    print(count(input("Text: ")))

def count(s):
    """
    Count the number of times "um" appears as a standalone word in the input string.
    The match is case-insensitive and does not count "um" inside other words.

    Args:
        s (str): Input text

    Returns:
        int: Number of standalone "um" occurrences
    """
    # Regex pattern explanation:
    # \b   -> Word boundary (ensures "um" is a whole word)
    # um   -> The literal word "um"
    # \b   -> Word boundary
    # re.IGNORECASE -> Match case-insensitively
    pattern = r'\bum\b'

    # Find all occurrences of "um" as a standalone word
    matches = re.findall(pattern, s, re.IGNORECASE)

    # Return the number of matches
    return len(matches)

if __name__ == "__main__":
    main()

# Mohammad_Reza_Mokhtari_Kia
