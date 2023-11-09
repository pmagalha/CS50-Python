def square(n):
    result = n * n
    return result

def einstein(mass):
    e = mass * square(300000000)
    return e

def main():
    mass = int(input("Write the mass in kg here: "))
    result = einstein(mass)
    print(result)

if __name__ == "__main__":
    main()
