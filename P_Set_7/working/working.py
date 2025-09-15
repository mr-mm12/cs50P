import re
import sys

def main():
    # Prompt user for 12-hour format hours and convert to 24-hour format
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        # check50 only cares that ValueError is raised
        raise

def convert(s):
    # Regex pattern to strictly match 12-hour format with optional minutes
    # Valid hours: 1-12, valid minutes: 00-59, AM/PM required, separated by ' to '
    pattern = r'^(1[0-2]|[1-9])(?::([0-5][0-9]))? (AM|PM) to (1[0-2]|[1-9])(?::([0-5][0-9]))? (AM|PM)$'

    # Match input string
    match = re.match(pattern, s.strip())

    if not match:
        raise ValueError("Invalid format")

    # Extract groups: start hour, start minute, start meridiem, end hour, end minute, end meridiem
    h1, m1, mer1, h2, m2, mer2 = match.groups()

    # Default minutes to 0 if not provided
    h1, h2 = int(h1), int(h2)
    m1, m2 = int(m1) if m1 else 0, int(m2) if m2 else 0

    # Validate minutes range
    if not (0 <= m1 < 60) or not (0 <= m2 < 60):
        raise ValueError("Invalid minutes")

    # Convert start hour to 24-hour format
    if mer1 == "AM":
        h1_24 = 0 if h1 == 12 else h1
    else:  # PM
        h1_24 = 12 if h1 == 12 else h1 + 12

    # Convert end hour to 24-hour format
    if mer2 == "AM":
        h2_24 = 0 if h2 == 12 else h2
    else:  # PM
        h2_24 = 12 if h2 == 12 else h2 + 12

    # Format hours and minutes with leading zeros
    start = f"{h1_24:02d}:{m1:02d}"
    end = f"{h2_24:02d}:{m2:02d}"

    return f"{start} to {end}"

if __name__ == "__main__":
    main()

# Mohammad_Reza_Mokhtari_Kia
