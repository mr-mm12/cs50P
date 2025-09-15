import os
import sys
import csv
from tabulate import tabulate


def main():
    # Check if the number of command-line arguments is correct
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    # Check if the file exists
    elif not os.path.isfile(sys.argv[1]):
        print("File does not exist")
        sys.exit(1)
    # Check if the file has a .csv extension
    elif not sys.argv[1].endswith(".csv"):
        print("Not a CSV file")
        sys.exit(1)
    else:
        # If all checks pass, display the table
        table(sys.argv[1])


def table(user_input):
    # Open the CSV file
    with open(user_input, "r") as csv_file:
        # Read the CSV file into a dictionary reader
        tab = csv.DictReader(csv_file, delimiter=",")
        # Print the table formatted as ASCII art using "grid" style
        print(tabulate(tab, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    # Run the main function when executed directly
    main()

# Mohammad_Reza_Mokhtari_Kia
