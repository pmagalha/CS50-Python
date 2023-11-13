def main():
    name = input("> ")
    camel_to_snake(name)

def camel_to_snake(str):
    for char in str:
        if char.islower() == True:
            print (char, end="")
        elif char.isupper() == True:
            print ("_" + char.lower(), end="")
    print()


if __name__ == "__main__":
    main()
