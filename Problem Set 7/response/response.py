import validators

def main():
    validator(input("What's your email? :").strip())

def validator(mail):
    if validators.email(mail):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
