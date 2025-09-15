import pytest
from fuel import convert, gauge

# Tests for convert(fraction)

def test_convert_valid_fractions():
    # Normal fractions
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("2/3") == 67  # Rounded to nearest integer
    assert convert("0/1") == 0
    assert convert("1/1") == 100

def test_convert_invalid_fraction_numerator_greater_than_denominator():
    # Numerator greater than denominator should raise ValueError
    with pytest.raises(ValueError):
        convert("5/4")

def test_convert_invalid_fraction_non_integer():
    # Non-integer numerator or denominator should raise ValueError
    with pytest.raises(ValueError):
        convert("a/3")
    with pytest.raises(ValueError):
        convert("1/b")
    with pytest.raises(ValueError):
        convert("1.5/2")

def test_convert_zero_denominator():
    # Denominator zero should raise ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_convert_negative_numbers():
    # Negative numerator or denominator should raise ValueError
    with pytest.raises(ValueError):
        convert("-1/2")
    with pytest.raises(ValueError):
        convert("1/-2")


# Tests for gauge(percentage)

def test_gauge_empty_and_full():
    # Gauge should return "E" for <=1 and "F" for >=99
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_gauge_normal_percentages():
    # Gauge should return percentage string for normal percentages
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
    assert gauge(2) == "2%"
    assert gauge(98) == "98%"

# Mohammad_Reza_Mokhtari_Kia
