def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            final = gauge(percentage)
            print (final)
            break
        except (ValueError, ZeroDivisionError):
            pass

def convert(fraction):
    x, y = fraction.split(sep="/")
    if y == "0":
        raise ZeroDivisionError
    elif not x.isdigit() or not y.isdigit() or int(x) > int(y):
        raise ValueError
    else:
        x = int(x)
        y = int(y)
        percentage = (x / y) * 100
        return (percentage)

def gauge(percentage):
    if percentage <= 1:
        return ("E")
    elif percentage >= 99:
        return ("F")
    else:
        return str(round(percentage)) + "%"

if __name__ == "__main__":
    main()
