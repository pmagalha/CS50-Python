def main():
    string = input("Input: ")
    shortener(string)


def shortener(str):
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        for i in range(len(str)):
            if str[i] not in vowels:
                print (str[i], end="")
        print()

main()

