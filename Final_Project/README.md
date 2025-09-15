# Password Generator
#### Video Demo:  <https://youtu.be/jsZs5br-UEg>
#### Description:

## Overview
My name is Mohammad Reza Mokhtari Kia
and this project is my final submission for **CS50’s Introduction to Programming with Python (CS50P)**.
It is a password generator and strength checker that allows users to create secure passwords of customizable length and difficulty.
The program not only generates random passwords but also evaluates their strength and provides feedback to the user.
Additionally, every generated password is saved into a text file so that users can keep track of their generated passwords.

The motivation behind this project was to design a practical tool that demonstrates fundamental programming concepts such as functions, conditionals, error handling, file I/O, and testing, while also being useful in real-world scenarios where password security is important.

---

## Files

### `project.py`
This is the **main program** file containing the entire logic for the password generator. It consists of the following functions:

- **`generate_password(length: int, difficulty: str) -> str`**
  Generates a password of the specified length and difficulty.
  - *easy*: digits only
  - *normal*: digits + symbols
  - *difficult*: digits + symbols + uppercase letters
  - *very difficult*: digits + symbols + uppercase + lowercase letters
  I chose this layered difficulty system to allow users with different needs to control how complex their password should be.

- **`check_strength(password: str) -> str`**
  Evaluates the strength of any given password.
  Returns one of: *Weak, Medium, Strong, Very Strong*.
  The logic is based on the diversity of characters (digits, lowercase, uppercase, symbols).
  This design makes the evaluation simple yet effective.

- **`save_password(password: str, filename: str = "passwords.txt") -> None`**
  Appends the generated password to a file (`passwords.txt`).
  This ensures users have a record of all generated passwords.
  I debated encrypting the saved passwords but chose plaintext for simplicity and transparency in this project context.

- **`main()`**
  Handles user interaction.
  It prompts for password length and difficulty, generates a password, evaluates its strength, prints the results, and saves the password to a file.
  Errors such as invalid input or too-short lengths are handled gracefully using `try`/`except`.

---

### `test_project.py`
This file contains **unit tests** for the project using `pytest`.
It ensures the correctness of core functionalities:
- Tests whether *easy* passwords contain only digits.
- Tests the `check_strength` function with various inputs.
- Tests that requesting a password shorter than 4 characters raises a `ValueError`.

Writing tests was an important design decision since it guarantees the program works as expected and prevents future bugs if the code is extended.

---

### `passwords.txt`
This file is generated automatically once the program runs. It stores each password created by the user, with each password on a new line. This simulates basic password management.

---

## Design Choices

1. **Difficulty Levels**:
   I designed four difficulty modes to make the program flexible.
   While some users may only need simple numeric passwords, others might prefer complex ones with symbols and mixed cases.

2. **Strength Evaluation**:
   Instead of a complex algorithm, I implemented a straightforward scoring system based on the presence of different character types.
   This balances simplicity with practicality for most real-life scenarios.

3. **File Saving**:
   I debated whether to encrypt the saved passwords. However, given the scope of CS50P, I decided to keep the saving mechanism simple.
   This also highlights the importance of **not storing real passwords in plaintext** in actual applications.

4. **Error Handling**:
   To make the program user-friendly, I included error messages for invalid inputs (e.g., too short passwords, unknown difficulty level).

---

## How to Run

1. Ensure you have Python installed.
2. Run the program with:
   ```bash
   python project.py

# Mohammad_Reza_Mokhtari_Kia
