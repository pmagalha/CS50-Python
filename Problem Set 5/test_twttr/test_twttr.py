from twttr import shorten

def test_upper():
    assert shorten("TWITTER") == "TWTTR"

def test_empty():
    assert shorten("") == ""

def test_novowels():
    assert shorten("rhythm") == "rhythm"

def test_onlyvowel():
    assert shorten("aeiou") == ""

def test_mixed():
    assert shorten("Hello123!@ World") == "Hll123!@ Wrld"


