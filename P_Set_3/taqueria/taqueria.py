# Menu dictionary
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Lowercase menu for case-insensitive matching
menu_lower = {key.lower(): value for key, value in menu.items()}

# Initialize total
total = 0

while True:
    try:
        # Prompt user for item
        item_input = input("Item: ").strip().lower()

        # If item exists in menu, add to total and print
        if item_input in menu_lower:
            total += menu_lower[item_input]
            print(f"Total: ${total:.2f}")

    except EOFError:
        # Ctrl+D ends program, move cursor to new line
        print("")
        break

# Mohammad_Reza_Mokhtari_Kia
