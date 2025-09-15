from fpdf import FPDF

def main():
    # Prompt the user for their name
    name = input("Name: ")

    # Create a PDF object with portrait orientation and A4 size
    pdf = FPDF(orientation="P", unit="mm", format="A4")

    # Add a page to the PDF
    pdf.add_page()

    # Set font for the title
    pdf.set_font("Helvetica", "B", 24)

    # Add a title at the top of the page, centered horizontally
    pdf.cell(0, 30, "CS50 Shirtificate", align="C", ln=True)

    # Insert the shirt image centered on the page
    pdf.image("shirtificate.png", x=10, y=60, w=190)

    # Set font for the user's name
    pdf.set_font("Helvetica", "B", 24)

    # Set text color to white
    pdf.set_text_color(255, 255, 255)

    # Move cursor vertically to where the shirt is
    pdf.set_y(140)

    # Split name by words
    words = name.split()

    line = ""
    lines = []

    # Build lines without breaking words
    for word in words:
        if len(line + " " + word) <= 15:  # if adding word keeps line <= 15 chars
            if line:
                line += " " + word
            else:
                line = word
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)

    # Print lines
    for i, l in enumerate(lines):
        if i == len(lines) - 1:
            pdf.cell(0, 10, f"{l} took CS50", align="C", ln=True)
        else:
            pdf.cell(0, 10, l, align="C", ln=True)

    # Save the PDF
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()

# Mohammad_Reza_Mokhtari_Kia
