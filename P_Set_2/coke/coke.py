amount = 50         # Total amount due in cents
price = 0           # Amount inserted so far
cent = [25, 10, 5]  # List of valid coin denominations

while price < amount:
    # Keep asking for coins until enough money is inserted
    print(f"Amount Due: {amount - price}")  # Show remaining amount due
    insert = int(input("Insert Coin: "))   # Ask user to insert a coin
    if insert in cent:
        # Check if the coin is valid
        price += insert                    # Add valid coin to total inserted amount

print(f"Change Owed: {price - amount}")   # Print change owed (0 if exact amount)

# Mohammad_Reza_Mokhtari_Kia
