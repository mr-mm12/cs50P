import sys
import os
from PIL import Image, ImageOps


def main():
    # Check for correct number of command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # Get input and output file names from command-line arguments
    file_1 = sys.argv[1]
    file_2 = sys.argv[2]

    # Validate that input file exists
    if not os.path.isfile(file_1):
        sys.exit("Input does not exist")

    # Validate file extensions (input and output must both be images with same extension)
    valid_extensions = [".jpg", ".jpeg", ".png"]
    input_ext = os.path.splitext(file_1)[1].lower()
    output_ext = os.path.splitext(file_2)[1].lower()

    if input_ext not in valid_extensions:
        sys.exit("Invalid input")
    if output_ext not in valid_extensions:
        sys.exit("Invalid output")
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    # If all checks pass, process the images
    process(file_1, file_2)


def process(file_1, file_2):
    # Open the shirt overlay image
    shirt = Image.open("shirt.png")

    # Open the input image
    try:
        image = Image.open(file_1)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    # Resize and crop the input image to match shirt size
    image = ImageOps.fit(image, shirt.size)

    # Paste the shirt onto the input image with transparency
    image.paste(shirt, shirt)

    # Save the final output image
    image.save(file_2)


if __name__ == "__main__":
    main()

# Mohammad_Reza_Mokhtari_Kia
