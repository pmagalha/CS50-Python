import sys
import csv

def check_args():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    for arg in sys.argv[1:]:
        if not arg.endswith(".csv"):
            print(f"Could not read {sys.argv[i]}")
            sys.exit(1)
    if len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

def read_file():
    new_csv = []
    with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file, fieldnames=['name', 'house'])
            for row in reader:
                name_parts = row['name'].split(',')
                last = name_parts[0].strip()
                if len(name_parts) > 1:
                    first = name_parts[1].strip()
                    new_csv.append({'first': first, 'last': last, 'house': row['house']})
            return (new_csv)

def write_file(new_csv):
    with open(sys.argv[2], "w", newline='') as new_file:
            fieldnames = ['first', 'last', 'house']
            writer = csv.DictWriter(new_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(new_csv)

def main():
    check_args()
    try:
        new_csv = read_file()
        write_file(new_csv)
    except FileNotFoundError:
        print(f"Could not read {sys.argv[1]}")
        sys.exit(1)

if __name__ == "__main__":
    main()
