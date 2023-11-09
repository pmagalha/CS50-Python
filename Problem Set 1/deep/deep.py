#asking for an answer to the question
def main ():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    if answer.replace(" ", "") == "42" or answer.casefold() == "forty two" or answer.casefold() == "forty-two":
        print("Yes")
    else:
        print("No")

main ()
