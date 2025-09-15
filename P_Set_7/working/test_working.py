import pytest
from working import convert


def test_basic_hours():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"


def test_hours_with_minutes():
    assert convert("9:15 AM to 5:45 PM") == "09:15 to 17:45"
    assert convert("10:30 PM to 8:05 AM") == "22:30 to 08:05"


def test_invalid_formats():
    import pytest
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")  # wrong separator
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")  # invalid hour
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")  # invalid minute

# Mohammad_Reza_Mokhtari_Kia
