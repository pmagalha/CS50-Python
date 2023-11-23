from tabulate import tabulate
import sys
import csv

def arg_check():
    if len(sys.argv) < 2:
        print ("Too few command-line arguments")
        sys.exit(1)
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    if not sys.argv[1].endswith(".csv"):
        print("Not a CSV file")
        sys.exit(1)

def create_menu():
    file_path = sys.argv[1]
    with open(file_path) as file:
        menu = []
        lines = csv.reader(file)
        for name, smallprice, largeprice in lines:
            pizza = {
            "name": name,
            "small": smallprice,
            "large": largeprice,
            }
            menu.append(pizza)
        return (menu)

def main():
    arg_check()
    try:
        if len(sys.argv) == 2:
            menu = create_menu()
        print(tabulate(menu, headers="firstrow", tablefmt="grid"))
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

main()
