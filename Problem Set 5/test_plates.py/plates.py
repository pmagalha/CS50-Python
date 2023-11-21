def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if lenght_valid(s) and isalphanum(s) and first2isalpha(s):
        if not s.isalpha():
            if firstdigitnot0(s):
                    return True
        else:
            return True
    return False

def lenght_valid(s):
    if 2 <= len(s) <= 6:
        return True

def isalphanum(s):
    if s.isalnum():
        return True

def first2isalpha(s):
    if s[:2].isalpha():
        return True

def firstdigitnot0(s):
    i = 2
    while i < len(s):
        if s[i].isdigit():
            k = i
            while k < len(s):
                if not s[k].isdigit():
                    return False
                k += 1
            return s[i] != "0"
        i += 1
    return False

if __name__ == "__main__":
    main()
