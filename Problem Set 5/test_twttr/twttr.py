def main():
    prompt = input("")
    print(shorten(prompt))

def shorten(prompt):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    newstr = prompt
    for c in prompt:
        if c in vowels:
            newstr = newstr.replace(c , "")
    return (newstr)

if __name__ == "__main__":
    main()
