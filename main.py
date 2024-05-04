import pandas

# TODO 1. Create a dictionary in this format:
alpha_data = pandas.read_csv("nato_phonetic_alphabet.csv")
alpha_dict = {row.letter: row.code for (index, row) in alpha_data.iterrows()}
print(alpha_dict)


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    input_words = input("Enter a word:").upper()
    try:
        output_list = [alpha_dict[letter] for letter in input_words]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
