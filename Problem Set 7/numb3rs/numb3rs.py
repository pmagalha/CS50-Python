import re

def validate(ip):
    if re.search (r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$", ip):
        return True
    return False


def main():
    ip = input("Iv4 Address: ").strip()
    print(validate(ip))

if __name__ == "__main__":
    main()
