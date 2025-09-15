import sys
import os


def main():
    # Check that exactly one command-line argument is provided
    if len(sys.argv) != 2:
        sys.exit("Usage: python lines.py filename.py")

    filename = sys.argv[1]

    # Check if the filename ends with .py
    if not filename.endswith(".py"):
        sys.exit("Error: File must have a .py extension")

    # Check if the file exists
    if not os.path.isfile(filename):
        sys.exit(f"Error: File '{filename}' does not exist")

    try:
        # Initialize line counter
        loc = 0

        # Open the file and read line by line
        with open(filename, "r") as file:
            for line in file:
                stripped = line.strip()  # Remove leading/trailing whitespace

                # Skip blank lines
                if stripped == "":
                    continue

                # Skip comment lines (lines starting with #)
                if stripped.startswith("#"):
                    continue

                # Count as a line of code
                loc += 1

        # Print the total lines of code
        print(loc)

    except Exception as e:
        # Catch unexpected errors
        sys.exit(f"Error reading file: {e}")


# Only run main() if this script is executed directly
if __name__ == "__main__":
    main()

# Mohammad_Reza_Mokhtari_Kia
