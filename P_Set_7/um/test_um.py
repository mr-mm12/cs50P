from um import count

def test_single_um():
    # Single "um" as a standalone word
    assert count("um") == 1

def test_multiple_um():
    # Multiple "um" occurrences
    assert count("Um, thanks, um...") == 2

def test_um_case_insensitive():
    # Different cases
    assert count("UM um Um uM") == 4

def test_um_not_substring():
    # "um" inside other words should not be counted
    assert count("yummy, aluminum, um") == 1

def test_um_with_punctuation():
    # "um" with punctuation marks
    assert count("Um? um! (um)") == 3

def test_no_um():
    # No "um" in text
    assert count("Hello world!") == 0

# Mohammad_Reza_Mokhtari_Kia
