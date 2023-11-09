def main():
    time_str = input ("What time is it?: ")
    converted_time = convert(time_str)
    if 7 <= converted_time <= 8:
        print("breakfast time")
    elif 12 <= converted_time <= 13:
        print("lunch time")
    elif 18 <= converted_time <= 19:
        print("dinner time")
    else:
        return 0

def convert(timer):
    h , m = map(float, timer.split(":"))
    return h + m / 60

if __name__ == "__main__":
    main()
