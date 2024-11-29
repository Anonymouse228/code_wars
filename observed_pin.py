# https://www.codewars.com/kata/5263c6999e0f40dee200059d

from itertools import product


def get_pins(observed):
    variants = {'1': '124', '2': '1235', '3': '236', '4': '1457', '5': '24568', '6': '3569', '7': '478', '8': '05789',
                '9': '689', '0': '08'}

    combinations = ['']
    for ch in observed:
        new_combinations = []

        for i, combination in enumerate(combinations):
            new_combinations += [combination + n for n in variants[ch]]

        combinations = new_combinations

    return combinations


def get_pins2(observed):
    variants = ('08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')
    return [''.join(p) for p in product(*(variants[int(d)] for d in observed))]


print(get_pins2('9578'))
