from numb3rs import validate

def test_correct():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("1.1.1.1") == True

def test_wrong():
    assert validate("cat") == False
    assert validate("1.2.3.1000") == False
    assert validate("64.128.256.512") == False
