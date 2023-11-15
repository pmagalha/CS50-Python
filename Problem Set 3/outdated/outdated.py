months = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}

def main():
    while True:
        try:
            date = input("Date: ")
            if "/" in date:
                m, d, y = map(int, date.split("/"))
            elif "," in date:
                date_stripped = date.split(" ")
                m = months.get(date_stripped[0])
                d = int(date_stripped[1].replace(",", ""))
                y = int(date_stripped[2])
            elif "/" not in date and "," not in date:
                raise ValueError
            if not 1 <= int(d) <= 31:
                continue
            if not 1 <= int(m) <= 12:
                continue
            print (f"{y:04}-{m:02}-{d:02}")
            break
        except ValueError:
            pass

if __name__ == "__main__":
    main()
