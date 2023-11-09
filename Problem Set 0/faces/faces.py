def emoji(message):
    message = message.replace(":)", "🙂").replace(":(", "🙁")
    return message

def main():
    usr_input = input("Write message and emoji here: ")
    new_input = emoji(usr_input)
    print(new_input)

main()
