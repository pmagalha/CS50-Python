import fuel
import pytest

def test_convert():
    assert fuel.convert("1/2") == 50
    assert fuel.convert("12/20") == 60
    assert fuel.convert("10/10") == 100

    with pytest.raises(ValueError):
        fuel.convert("8/3")

    with pytest.raises(ZeroDivisionError):
        fuel.convert("2/0")

    with pytest.raises(ValueError):
        fuel.convert("A/10")

def test_gauge():
    assert fuel.gauge(100) == "F"
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(50) == "50%"
