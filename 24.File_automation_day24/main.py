with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()

with open("./Input/Letters/starting_letter.txt") as file:
    content = file.read()
    for name in names:
        strip_name = name.strip()
        letter = content.replace("[name]", strip_name)
        print(letter)
        with open(f"./Output/ReadyToSend/letter_for_{strip_name}.txt", mode="w") as f:
            f.write(letter)

