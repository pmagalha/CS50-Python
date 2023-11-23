import re
import sys


def main():
    s = (input("HTML: "))
    print(parse(s))


def parse(s):
    if matches := re.search(r'src="(https?://)?([^"]+)"', s):
        protocol = matches.group(1)
        url = matches.group(2)
        if "http:" in matches.group(1):
            protocol = protocol.replace("http:", "https:")
        if "youtube.com" in matches.group(2) and "embed/" in matches.group(2):
            url = url.replace("youtube.com", "youtu.be").replace("embed/", "")
        else:
            return (None)
        if "www." in matches.group(2):
            url = url.replace("www.", "")
        return (protocol + url)

if __name__ == "__main__":
    main()
