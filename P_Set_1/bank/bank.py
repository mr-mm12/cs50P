import string  # Import library string

greet = input("Greeting: ").strip().lower().lstrip(
    string.punctuation)  # Getting input from the user

if greet.startswith("hello"):
    # If the sentence started with "hello"
    print("$0")

elif greet.startswith("h"):
    # If the sentence started with "h"
    print("$20")

else:
    # Otherwise
    print("$100")

# Mohammad_Reza_Mokhtari_Kia
