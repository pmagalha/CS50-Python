def main():
    x, y , z = input("Expression: ").split(" ")
    if y == "+":
        print (float(int(x) + int(z)))
    elif y == "-":
        print (float(int(x) - int(z)))
    elif y == "*":
        print (float(int(x) * int(z)))
    elif y == "/":
        print (float(int(x) / int(z)))

main()
