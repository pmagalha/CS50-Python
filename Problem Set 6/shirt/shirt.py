import sys
from PIL import Image
from PIL import ImageOps

def iscompatible(str1, str2):
    if str1.endswith(".jpeg"):
        n = 5
    else:
        n = 4
    return str1[-n:] == str2[-n:]

def arg_check():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    if len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    for arg in sys.argv[1:]:
        if not (arg.endswith(".jpeg") or arg.endswith(".png") or arg.endswith(".jpg")):
            print("Invalid output")
            sys.exit(1)
    if not iscompatible(sys.argv[1], sys.argv[2]):
        print("Input and output have different extensions")
        sys.exit(1)

def main():
    arg_check()
    try:
        input_img = Image.open(sys.argv[1])
        overlay_img = Image.open("shirt.png")
        input_img = ImageOps.fit(input_img, overlay_img.size, method=Image.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
        new_img = Image.new("RGB", input_img.size)
        new_img.paste(input_img, (0, 0))
        new_img.paste(overlay_img, (0, 0), overlay_img)
        new_img.save(sys.argv[2])
    except FileNotFoundError:
        print("Input does not exist")
        sys.exit(1)

if __name__ == "__main__":
    main()
