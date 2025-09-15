import pytest
from project import generate_password, check_strength

def test_generate_password_easy():
    """Test if easy password is generated correctly with digits only."""
    pwd = generate_password(8, "easy")
    assert len(pwd) == 8
    assert all(c.isdigit() for c in pwd)

def test_check_strength_various():
    """Test password strength evaluation function."""
    assert check_strength("1234") == "Weak"
    assert check_strength("1234A") in ["Medium", "Strong", "Very Strong"]

def test_generate_password_invalid_length():
    """Test that generating a password shorter than 4 raises ValueError."""
    with pytest.raises(ValueError):
        generate_password(3, "easy")

# Mohammad_Reza_Mokhtari_Kia
