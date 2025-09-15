# List of month names
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    # Prompt user for a date
    date_input = input("Date: ").strip()

    try:
        if "/" in date_input:
            # Format: MM/DD/YYYY
            parts = date_input.split("/")
            if len(parts) != 3:
                continue  # Invalid format, reprompt

            month = int(parts[0])
            day = int(parts[1])
            year = int(parts[2])

        else:
            # Format: Month D, YYYY (exactly one comma)
            if "," not in date_input:
                continue  # Must have comma, else reprompt

            parts = date_input.split(",")
            if len(parts) != 2:
                continue  # More than one comma, invalid

            month_day = parts[0].strip().split()
            if len(month_day) != 2:
                continue  # Must be "Month D"

            month_str = month_day[0].capitalize()
            if month_str not in months:
                continue  # Invalid month

            month = months.index(month_str) + 1
            day = int(month_day[1])
            year = int(parts[1].strip())

        # Basic validity check
        if not (1 <= month <= 12) or not (1 <= day <= 31):
            continue  # Invalid month/day

        # Print ISO format
        print(f"{year:04}-{month:02}-{day:02}")
        break

    except ValueError:
        # Invalid integer conversion
        continue

# Mohammad_Reza_Mokhtari_Kia
