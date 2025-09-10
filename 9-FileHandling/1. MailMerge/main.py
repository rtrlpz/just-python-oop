PLACEHOLDER = '[name]'

# for each name in invited_names.txt

with open('../1. MailMerge/Input/Names/invited_names.txt') as names_files:
    names = names_files.readlines()

# Create a letter using starting_letter.txt

with open('../1. MailMerge/Input/Letters/starting_letter.txt') as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        print(new_letter.strip(' '))

        with open(f'../1. MailMerge/Output/ReadyToSend/letter_for_{stripped_name}.txt', 'w') as completed_letter:
            completed_letter.write(new_letter)



