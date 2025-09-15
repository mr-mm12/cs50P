import emoji as em  # Import the emoji library and rename it as "em"

# Prompt the user to enter a string
txt = input("Input: ")

# Convert emoji codes/aliases in the text into actual emojis
em_txt = em.emojize(txt, language="alias")

# Print the final emojized text
print(f"Output: {em_txt}")

# Mohammad_Reza_Mokhtari_Kia
