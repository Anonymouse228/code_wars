# https://www.codewars.com/kata/540d0fdd3b6532e5c3000b5b

from itertools import product, groupby
from re import findall


def get_coefficients(expr: str) -> tuple:
    x = findall(r'[^-\+\(\)\^0-9]', expr)[0]
    *_, a, b, n = ['1'] + findall(r'[\+-]?[0-9]+|[\+-]', expr)
    return '-1' if a == '-' else a, x, b, n


def get_readable_term(coefficient, x, degree):
    result = ''

    if coefficient == 0:
        return result

    if degree == 1:
        result += x
    elif degree > 1:
        result += f'{x}^{degree}'

    if coefficient == -1 and x in result:
        result = '-' + result
    elif coefficient == 1 and x in result:
        result = '+' + result
    else:
        result = f'{coefficient:+}{result}'

    return result


# def expand(expr):
#     a, x, b, n = get_coefficients(expr)
#     a += x
#
#     terms = []
#     for combination in product((a, b), repeat=int(n)):
#         value, degree = 1, 0
#         for coefficient in combination:
#             if x in coefficient:
#                 value *= int(coefficient[:-1])
#                 degree += 1
#             else:
#                 value *= int(coefficient)
#         terms.append((value, degree))
#
#     expr = ''
#     key = lambda t: t[-1]
#     for k, g in groupby(sorted(terms, key=key, reverse=True), key=key):
#         expr += get_readable_term(sum(list(zip(*list(g)))[0]), x, k)
#
#     return expr[1:] if expr[0] == '+' else expr


import re

P = re.compile(r'\((-?\d*)(\w)\+?(-?\d+)\)\^(\d+)')


def expand(expr):
    a, v, b, e = P.findall(expr)[0]

    if e == '0': return '1'

    o = [int(a != '-' and a or a and '-1' or '1'), int(b)]
    e, p = int(e), o[:]

    print((a, v, b, e))
    print(o, e, p)

    for _ in range(e - 1):
        p.append(0)
        p = [o[0] * coef + p[i - 1] * o[1] for i, coef in enumerate(p)]

    res = '+'.join(f'{coef}{v}^{e - i}' if i != e else str(coef) for i, coef in enumerate(p) if coef)

    return re.sub(r'\b1(?=[a-z])|\^1\b', '', res).replace('+-', '-')


print(expand('(-x+1)^2'))
