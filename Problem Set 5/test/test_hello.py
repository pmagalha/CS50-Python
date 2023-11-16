from hello import hello

def test_hello():
    assert hello() == "hello, world"

def test_arg():
    assert hello("David") == "hello, David"
