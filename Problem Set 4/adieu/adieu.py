def main():
    prompts = []
    count = 0
    while True:
        try:
            prompt = input("Name: ")
            count += 1
            prompts.append(prompt)
        except:
            print("Adieu, adieu, ", end="")
            oxford(prompts)
            break

def oxford(prompts):
    commas = len(prompts) - 1
    if len(prompts) == 1:
        print(f"to {prompts[0]}")
    elif len(prompts) == 2:
        print(f"to {prompts[0]} and {prompts[1]}")
    else:
        joined_prompts = ', '.join(prompts[:-1])
        print(f"to {joined_prompts}, and {prompts[-1]}")

if __name__ == "__main__":
    main()
