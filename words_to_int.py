# https://www.codewars.com/kata/525c7c5ab6aecef16e0001a5


def parse_int(string):  # type: (str) -> int
    units = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10,
        'eleven': 11,
        'twelve': 12,
        'thirteen': 13,
        'fourteen': 14,
        'fifteen': 15,
        'sixteen': 16,
        'seventeen': 17,
        'eighteen': 18,
        'nineteen': 19,
        'twenty': 20,
        'thirty': 30,
        'forty': 40,
        'fifty': 50,
        'sixty': 60,
        'seventy': 70,
        'eighty': 80,
        'ninety': 90,
        'hundred': 100,
        'thousand': 1000,
        'million': 1000000,
    }

    answer = 0
    num = 0
    for unit in [s for s in string.split() if s != 'and']:
        if '-' in unit:
            a, b = unit.split('-')
            num += units[a] + units[b]
        elif units[unit] < 100:
            num += units[unit]
        elif units[unit] == 100:
            num *= units[unit]
        else:
            answer += num * units[unit]
            num = 0

    return answer + num


print(parse_int('six hundred sixty-six thousand six hundred sixty-six'))
