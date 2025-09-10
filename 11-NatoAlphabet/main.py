import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(fonetic_dict)


def generate_name():
    word = input('Enter a word: ').upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print('Only letters of the alphabet.')
        generate_name()
    else:
        print(output_list)

generate_name()