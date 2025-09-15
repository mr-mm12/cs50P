from plates import is_valid

# ------------------------
# Valid plate tests
# ------------------------
def test_valid_plate_letters_only():
    assert is_valid("CS50") == True  # Letters followed by numbers

def test_valid_plate_letters_and_numbers():
    assert is_valid("AB123") == True  # Letters then numbers

def test_valid_min_length():
    assert is_valid("AB") == True  # Minimum length plate

def test_valid_max_length():
    assert is_valid("ABC123") == True  # Maximum length plate

# ------------------------
# Invalid plate tests
# ------------------------
def test_too_short_plate():
    assert is_valid("A") == False  # Too short

def test_too_long_plate():
    assert is_valid("ABCDEFG") == False  # Too long

def test_number_starts_with_zero():
    assert is_valid("AB012") == False  # First number is zero

def test_letter_after_number():
    assert is_valid("AB1C") == False  # Letter appears after number

def test_invalid_characters():
    assert is_valid("AB@12") == False  # Invalid punctuation

def test_first_two_not_letters():
    assert is_valid("1A234") == False  # First two not letters

def test_number_in_middle():
    assert is_valid("A1B2") == False  # Number appears before end

# Mohammad_Reza_Mokhtari_Kia
