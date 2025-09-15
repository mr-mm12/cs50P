from twttr import shorten

# Test with lowercase words
def test_lowercase():
    assert shorten("hello") == "hll"       # "e" and "o" removed
    assert shorten("twitter") == "twttr"   # "i" and "e" removed

# Test with uppercase words
def test_uppercase():
    assert shorten("HELLO") == "HLL"       # Remove "E" and "O"
    assert shorten("TWITTER") == "TWTTR"   # Remove "I" and "E"

# Test with mixed case words
def test_mixedcase():
    assert shorten("Twitter") == "Twttr"   # Works regardless of case
    assert shorten("CS50") == "CS50"       # No vowels removed

# Test with only vowels
def test_only_vowels():
    assert shorten("aeiouAEIOU") == ""     # All vowels removed

# Test with empty string
def test_empty_string():
    assert shorten("") == ""               # No characters remain

# Mohammad_Reza_Mokhtari_Kia
