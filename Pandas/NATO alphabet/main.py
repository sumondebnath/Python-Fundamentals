"""
    Keyword Method with iterrows()

    {new_key:new_value for (index, row) in df.iterrows()}
"""

import pandas

data = pandas.read_csv("/home/sumon/Documents/Python/Pandas/NATO alphabet/nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)


def genarate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]

    except KeyError:
        print("Sorry, Only letters in the alphabets please!")
        genarate_phonetic()

    else:
        print(output_list)



genarate_phonetic()