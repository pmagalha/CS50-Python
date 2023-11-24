from seasons import parse_date
import pytest
from datetime import date

def test_parse_date_valid():
    assert parse_date("2023-10-15") == True
    assert parse_date("1990-08-02") == True

def test_parse_date_invalid():
    with pytest.raises(ValueError):
        parse_date("Hello")
    with pytest.raises(ValueError):
        parse_date("1990-32-56")

if __name__ == "__main__":
    pytest.main()
