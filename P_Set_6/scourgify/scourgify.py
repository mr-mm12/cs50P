import os
import sys
import csv


def main():
    # Check if the user provided exactly 2 command-line arguments (input and output file)
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    # Check if the input file exists
    elif not os.path.isfile(sys.argv[1]):
        print(f"Could not read {sys.argv[1]}")
        sys.exit(1)

    # Check if input file has a .csv extension
    elif not sys.argv[1].endswith(".csv"):
        print("Not a CSV file")
        sys.exit(1)

    else:
        # Call the function to clean and convert the data
        scou(sys.argv[1], sys.argv[2])


def scou(input_file, output_file):
    # Open the input CSV file
    with open(input_file, "r") as file_1:
        reader = csv.DictReader(file_1)  # Read rows as dictionaries

        # Open the output CSV file
        with open(output_file, "w", newline="") as file_2:
            # Define the fieldnames (columns) for the new CSV file
            fieldnames = ["first", "last", "house"]

            # Create a DictWriter to write rows into the output file
            writer = csv.DictWriter(file_2, fieldnames=fieldnames)

            # Write the header row
            writer.writeheader()

            # Iterate through each row in the input CSV
            for row in reader:
                # The "name" column contains "last, first"
                last, first = row["name"].split(", ")
                house = row["house"]

                # Write the new row into the output file
                writer.writerow({
                    "first": first,
                    "last": last,
                    "house": house
                })


if __name__ == "__main__":
    main()

# Mohammad_Reza_Mokhtari_Kia
