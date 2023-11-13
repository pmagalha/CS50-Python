def main():
    try:
        fuel = input("Fraction: ")
        x, y = fuel.split(sep="/")
        error_handling(x , y)
        percentage = (int(x)/int(y)) * 100
        if percentage <= 1:
            print ("E", end="")
        elif percentage >= 99:
            print ("F", end="")
        else:
            print (f"{int(round(percentage))}%")
    except ValueError:
            input("Fraction: ")
    except ZeroDivisionError:
            input("Fraction: ")

def error_handling(x , y):
    if not x.isdigit() or not y.isdigit() or int(x) > int(y):
        raise ValueError
    elif y == "0":
        raise ZeroDivisionError
    else:
        return (x, y)

main()
