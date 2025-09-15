def main():
    # Prompt user for time
    time_str = input("Time: ").strip()

    # Convert time to float hours
    time_float = convert(time_str)

    # Check meal times
    if 7 <= time_float <= 8:
        print("Breakfast time")
    elif 12 <= time_float <= 13:
        print("Lunch time")
    elif 18 <= time_float <= 19:
        print("Dinner time")
    # else: do nothing if not meal time

def convert(time):
    """Convert a string time #:# or ##:## to float hours."""
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    return hours + minutes / 60


if __name__ == "__main__":
    main()

# Mohammad_Reza_Mokhtari_Kia
