#TODO: Create a letter using starting_letter.txt
PLACEHOLDER = "[name]"
names = open("./Input/Names/invited_names.txt", "r")
names_list = names.readlines()

with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()
    for name in names_list:
        format_name = name.strip()
        x = letter.replace(PLACEHOLDER, format_name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as new_file:
            new_file.write(x)