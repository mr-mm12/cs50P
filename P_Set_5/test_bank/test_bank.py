from bank import value

# Test for greeting starting with "hello"
def test_hello():
    assert value("hello") == 0
    assert value("Hello there") == 0
    assert value("HELLO!") == 0

# Test for greeting starting with "h" but not "hello"
def test_h_not_hello():
    assert value("hi") == 20
    assert value("Howdy") == 20
    assert value("hELp") == 20

# Test for any other greeting
def test_other():
    assert value("good morning") == 100
    assert value("Heya") == 20      # because starts with "h" → 20
    assert value("What's up") == 100

# Mohammad_Reza_Mokhtari_Kia
