menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total = 0.0
    while True:
        try:
            order = input("Item: ").title()
            if order in menu:
                prices = (menu[order])
                total += prices
                print("Total: ${:.2f}".format(total))
            else:
                print("Item not found in the menu. Please choose a valid item.")

        except Exception as e:
            break

__name__ == '__main__'
main()
