PLACE_HOLDER = '["Name"]'

with open("./Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    # print(names)

with open("./letter.txt") as letter_file:
    # print(letter_file)
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        final_name = stripped_name.replace(',', '')
        new_letter = letter_contents.replace(PLACE_HOLDER, final_name)
        # print(new_letter)
        with open(F"./ReadyToSend/letter_for{final_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)