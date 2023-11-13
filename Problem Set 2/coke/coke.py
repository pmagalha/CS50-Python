def main():
    amount_left = 50
    while amount_left >= 0:
        amount_given = int(input("Insert Coin: "))
        amount_left = amount_left - amount_due(amount_given)
        if amount_left > 0:
            print ("Amount Due:", amount_left)
        elif amount_left == 0:
            print ("Change Owed: 0")
            break ;
        elif amount_left < 0:
            print ("Change Owed:" , -amount_left)
            break ;

def amount_due(amount_given):
    if amount_given == 25 or amount_given == 10 or amount_given == 5:
        return amount_given
    else:
        return (0)

main()
