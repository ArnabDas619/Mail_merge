PLACEHOLDER = "[name]"
# read the list of invited people
with open("Input/Names/invited_names.txt") as file:
    str_names = file.read()
    Invited_list = str_names.splitlines()


# read the starting letter
with open("Input/Letters/starting_letter.txt") as file:
    str_letter = file.read()

for name in Invited_list:
    new_letter = str_letter.replace(PLACEHOLDER, str(name))
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as file:
        file.write(new_letter)
