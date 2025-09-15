import sys
import random
from pyfiglet import Figlet

# Create a Figlet object
figlet = Figlet()

# Get a list of all available fonts
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    # If no command-line arguments are given → choose a random font
    font = random.choice(fonts)

elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
    # If two arguments are given and the first one is -f or --font
    if sys.argv[2] in fonts:
        # Check if the second argument is a valid font
        font = sys.argv[2]
    else:
        sys.exit("Invalid font name.")
else:
    # If the arguments are invalid → exit with an error message
    sys.exit("Usage: python figlet.py [-f FONT]")

# Set the chosen font
figlet.setFont(font=font)

# Ask the user for input text
txt = input("Input: ")

# Render and print the text in the chosen font
print(figlet.renderText(txt))

# Mohammad_Reza_Mokhtari_Kia
