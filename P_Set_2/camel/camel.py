camel = input("camelCase: ").strip()
# Getting input from the user in "camelCase" form

snake = ""  # Variable definition

for i in camel:             # Loop through each character in the camelCase string
    if i.isupper():         # Check if the character is an uppercase letter
        snake += "_"        # If it is, add an underscore before it
        snake += i.lower()  # Convert the uppercase letter to lowercase and add it
    else:
        snake += i          # If it's not uppercase, just add the character as is


print(f"snake_case: {snake}")  # Printing text in "snake_case"

# Mohammad_Reza_Mokhtari_Kia
