# read the list of invited people
with open("Input/Names/invited_names.txt") as file:
    str_names = file.read()
    Invited_list = str_names.splitlines()
    print(Invited_list)

# read the starting letter
with open("Input/Letters/starting_letter.txt") as file:
    str_letter = file.read()


for name in Invited_list:
    new_letter = str_letter.replace("[name]", str(name))
    with open(f"Output/ReadyToSend/{name}.txt", "w") as file :
        file.write(new_letter)


