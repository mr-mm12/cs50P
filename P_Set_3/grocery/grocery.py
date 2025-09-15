items = []  # Create a list

while True:
    try:
        # Get input from user
        item = input().strip().lower()
        items.append(item)
    except EOFError:
        # Ctrl+D ends input
        break

# Count and print each unique item in sorted order
for item in sorted(set(items)):
    print(f"{items.count(item)} {item.upper()}")

# Mohammad_Reza_Mokhtari_Kia
