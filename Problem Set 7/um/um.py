import re
import sys


def main():
    print(count(input("Text: ")))

def count(s):
    occurences = re.findall(r'\bUM\b,?', s, flags=re.IGNORECASE)
    count = len(occurences)
    return (count)

if __name__ == "__main__":
    main()
