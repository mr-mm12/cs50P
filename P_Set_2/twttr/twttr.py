# Function to run the program
def main():
    txt = input("Input: ")       # Prompt the user for input
    print(shorten(txt))          # Call shorten() and print the result


# Function that removes vowels from the given word
def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]  # List of vowels
    out_txt = ""                         # Initialize empty string for result
    for ch in word:                      # Loop through each character
        if ch.lower() not in vowels:     # If character is NOT a vowel
            out_txt += ch                # Add it to result
    return out_txt                       # Return string without vowels


# Entry point of the program
if __name__ == "__main__":
    main()

# Mohammad_Reza_Mokhtari_Kia
