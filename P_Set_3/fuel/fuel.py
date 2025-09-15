def get_fuel_fraction():
    while True:
        # Prompt user for input
        fraction = input("Fraction (X/Y): ").strip()

        try:
            # Split input into numerator (X) and denominator (Y)
            x_str, y_str = fraction.split("/")
            x = int(x_str)
            y = int(y_str)

            # Check for invalid values: zero denominator, numerator > denominator, or negative numbers
            if y == 0 or x > y or x < 0 or y < 0:
                continue  # Prompt again

            # Check for invalid values
            if y == 0 or x > y:
                continue  # Prompt again

            # Calculate fuel percentage
            percentage = round((x / y) * 100)

            # Determine output based on fuel level
            if percentage <= 1:
                return "E"  # Essentially empty
            elif percentage >= 99:
                return "F"  # Essentially full
            else:
                return f"{percentage}%"  # Normal percentage

        except (ValueError, ZeroDivisionError):
            # Catch invalid input (non-integers, zero division, etc.)
            continue  # Prompt again

# Main program
if __name__ == "__main__":
    print(get_fuel_fraction())

# Mohammad_Reza_Mokhtari_Kia
