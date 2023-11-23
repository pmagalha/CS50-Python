from bank import value

def test_0():
    assert value("hello") == 0
    assert value("HELLO") == 0

def test_20():
    assert value("hey") == 20
    assert value("howdy") == 20
    assert value("How yoU DoiN") == 20

def test_100():
    assert value("what's up?") == 100
    assert value("SuP") == 100
