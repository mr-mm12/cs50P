from numb3rs import validate

def test_valid_ips():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("192.168.1.1") == True
    assert validate("190.54.1.0") == True
    assert validate("111.104.2.1") == True

def test_invalid_ips():
    assert validate("275.3.6.28") == False
    assert validate("192.168.001.1") == False
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False
    assert validate("01.2.3.4") == False

# Mohammad_Reza_Mokhtari_Kia
