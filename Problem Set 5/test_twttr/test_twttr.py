vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

def main():
    prompt = input("")
    shorten(prompt)

def shorten(prompt):
    newstr = prompt
    for c in prompt:
        if c in vowels:
            newstr = newstr.replace(c , "")
    print (newstr)

if __name__ == "__main__":
    main()
