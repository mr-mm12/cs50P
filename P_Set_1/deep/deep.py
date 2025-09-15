# Question + Convert to lowercase + Remove leading and trailing spaces
answer = input(
    "What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

deep = ["42", "forty two", "forty-two"]  # Words that are acceptable

if answer in deep:
    # Condition for the word to be in the "deep" list
    print("Yes")
else:
    # Otherwise
    print("No")

# Mohammad_Reza_Mokhtari_Kia
