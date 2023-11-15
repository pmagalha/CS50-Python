import random
import sys
from pyfiglet import Figlet

def main():
    available_fonts = Figlet().getFonts()
    num_args = len(sys.argv) - 1
    if num_args == 0:
        zeroargs(available_fonts)
    elif num_args == 2 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in available_fonts:
        twoargs(sys.argv[2])
    else:
        sys.exit("Invalid Usage")

def zeroargs(available_fonts):
    prompt = input("")
    randomized = Figlet(font=random.choice(available_fonts)).renderText(prompt)
    print(randomized)

def twoargs(usrfont):
    prompt = input("")
    usr_choice = Figlet(font=usrfont).renderText(prompt)
    print (usr_choice)

if __name__ == "__main__":
    main()
