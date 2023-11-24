import re
import inflect
import sys
from datetime import date

def main():
    input_date = input("Insert date (YYYY-MM-DD): ").strip()
    try:
        if parse_date(input_date):
            year, month, day = map(int, input_date.split("-"))
            input_date_ = date(year, month, day)
            today = date.today()
            diff = today - input_date_
            p = inflect.engine()
            print(f"{p.number_to_words(round(diff.days * 24 * 60), andword='').capitalize()} minutes")
    except ValueError :
        sys.exit("Invalid date")

def parse_date(input_date):
    if re.search(r"^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$", input_date):
        return (True)
    else:
        raise ValueError ("Invalid date")

if __name__ == "__main__":
    main()
