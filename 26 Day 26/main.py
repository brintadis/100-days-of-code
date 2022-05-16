import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

my_dict = {row.letter: row.code for (index, row) in data.iterrows()}

def generic_phonetic():
    word = input("Enter a word: ").upper()
    try:
        my_list = [my_dict[i] for i in word]
    except KeyError:
        print("Sorry, letters in the alphabet please.")
        generic_phonetic()
    else:
        print(my_list)

generic_phonetic()
