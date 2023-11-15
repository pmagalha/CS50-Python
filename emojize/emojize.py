import sys
import emoji

def main():
    usrinput = input("")
    print(emoji.emojize(usrinput, language='alias'))

if __name__ == "__main__":
    main()
