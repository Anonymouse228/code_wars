# https://www.codewars.com/kata/53d40c1e2f13e331fc000c26

import time
from functools import cache
from sys import setrecursionlimit
from my_package.tools import benchmark
import numpy as np
from decimal import Decimal


# @benchmark
# def fib(n):
#     a, b = 1, 0
#
#     if n >= 0:
#         for i in range(n):
#             a, b = b, a + b
#     else:
#         for i in range(0, n, -1):
#             a, b = b - a, a
#
#     return b


# @benchmark
# def fib(n):
#     return pow(np.matrix([[1, 1], [1, 0]] if n >= 0 else [[0, 1], [1, -1]], dtype=Decimal), abs(n))[0, 1]


setrecursionlimit(1000000)


@cache
def fib(n):
    if n in (0, 1):
        return n
    return fib(n - 2) + fib(n - 1)


if __name__ == '__main__':
    start = time.time()
    answer = fib(10000)
    print(f'time: {time.time() - start}')
    print(answer)
