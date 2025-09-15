from seasons import calculate_minutes, number_to_words
from datetime import date

def test_calculate_minutes_normal_year():
    d1 = date(2000, 1, 1)
    d2 = date(2001, 1, 1)
    assert calculate_minutes(d1, d2) == 525600


def test_calculate_minutes_leap_year():
    d1 = date(2020, 1, 1)
    d2 = date(2021, 1, 1)
    assert calculate_minutes(d1, d2) == 527040


def test_number_to_words_contains_parts():
    words = number_to_words(525600)
    assert "thousand" in words
    assert "hundred" in words

    words2 = number_to_words(1051200)
    assert "million" in words2
    assert "thousand" in words2

# Mohammad_Reza_Mokhtari_Kia
