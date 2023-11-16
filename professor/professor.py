import random
import sys

def main():
    score = 0
    level = get_level()

    for _ in range(10):
        x  = generate_integer(level)
        y  = generate_integer(level)
        result = x + y
        tries = 0
        guess = (input(f"{x} + {y} = "))
        if guess == str(result):
            score += 1
            continue
        elif guess != str(result):
            while tries < 3:
                print("EEE")
                tries += 1
                if tries == 3:
                    print(f"{x} + {y} = {result}")
                    break
                guess = (input(f"{x} + {y} = "))
                if guess != str(result):
                    continue
                elif guess == str(result):
                    score += 1
                    break
    return (print(f"Score: {score}"))

def get_level():
    while True:
        try:
            level = (input("Level: "))
            if level.isdigit() and int(level) in [1,2,3]:
                return int(level)
        except:
            sys.exit()

def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
    return x

if __name__ == "__main__":
    main()
