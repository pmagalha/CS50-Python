import sys

if len(sys.argv) == 2:
    file_path = sys.argv[1]
    if not file_path.endswith('.py'):
        print("Not a Python file")
        sys.exit(1)
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            count = 0
            for line in lines:
                if not line.lstrip().startswith("#") and not line.isspace():
                    count += 1
            print (count)
    except FileNotFoundError:
        print ("File does not exist")

elif len(sys.argv) < 2:
    print ("Too few command-line arguments")
    sys.exit(1)
else:
    print ("Too many command-line arguments")
    sys.exit(1)
