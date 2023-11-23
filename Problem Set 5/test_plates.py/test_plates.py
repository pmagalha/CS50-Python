from plates import is_valid

def test_start():
    assert is_valid("CS50") == True
    assert is_valid("50CS") == False
    assert is_valid("C50") == False

def test_len():
    assert is_valid("X") == False
    assert is_valid("CS505050") == False
    assert is_valid("CCSSHHGG") == False

def test_numbers():
    assert is_valid("XXX111") == True
    assert is_valid("XXX011") == False
    assert is_valid("XXX11X") == False

def test_punctuation():
    assert is_valid("CS_50") == False
    assert is_valid("CSA 50") == False
    assert is_valid("CS50.") == False
