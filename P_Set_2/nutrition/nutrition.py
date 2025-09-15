Fruit_Calories = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80
}  # Dictionary mapping fruit names to their calories

fruit = input("Item: ").strip().lower()  # Get input from user, remove extra spaces, convert to lowercase

if fruit in Fruit_Calories:
    # Check if the input fruit exists in the dictionary
    print(f"Calories: {Fruit_Calories[fruit]}")  # Print the calories of the fruit

# Mohammad_Reza_Mokhtari_Kia
