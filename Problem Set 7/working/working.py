import re

def main():
    s = input("Hours: ")
    print (convert(s))

def convert_groups(matches):
    hours1 , hours2 = int(matches.group(1)), int(matches.group(5))

    if matches.group(3):
        minutes1 = int(matches.group(3))
        minutes2 = int(matches.group(7))
    else:
        minutes1 = "00"
        minutes2 = "00"

    if "AM" in matches.group(4) and hours1 == 12:
        hours1 = 0
    elif "PM" in matches.group(4) and hours1 < 12:
        hours1 += 12
    if "AM" in matches.group(8) and hours2 == 12:
        hours2 = 0
    elif "PM" in matches.group(8) and hours2 < 12:
        hours2 += 12
        
    return f"{hours1:02}:{minutes1:02} to {hours2:02}:{minutes2:02}"

def convert(s):
    try:
        if matches := re.search (r"^(\d{1,2})(:?)([0-5]?[0-9]?) (AM|PM) to (\d{1,2})(:?)([0-5]?[0-9]?) (AM|PM)$", s):
            return convert_groups(matches)
        raise ValueError ("Invalid format")
    except ValueError as e:
        print (e)
        raise

if __name__ == "__main__":
    main()
