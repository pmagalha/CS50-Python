from random import randrange

def main():
    while True:
        try:
            n = int(input("Level: "))
            rand = randrange(1, n + 1)
            guess = int(input("Guess: "))
            if guess > rand:
                print("Too large!")
            elif guess < rand:
                print("Too small!")
            else:
                print("Just right!")
                break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()
