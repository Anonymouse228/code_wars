import re
from collections import deque
from decimal import Decimal
from math import sqrt, pow
import time
import json

from my_package.math import fast_degree
from my_package.primes import ferma_test, eratosthenes_sieve
from my_package.tools import benchmark


def calculate_primes(d: dict, end: int) -> None:
    # primes = OrderedDict({2: True})
    # primes = {2: True}
    primes = deque([2])
    # primes = [2]

    for number in range(3, end, 2):
        limit = int(sqrt(number)) + 1
        for prime in primes:
            if prime > limit:
                # primes[number] = True
                primes.append(number)
                break
            if number % prime == 0:
                break
        else:
            # primes[number] = True
            primes.append(number)

    return primes


def calculate_primes2(end: int):
    primes = []

    for number in range(2, end):
        limit = int(sqrt(number)) + 2
        for j in range(2, limit):
            if number % j == 0:
                break
        else:
            primes.append(number)

    return primes


def is_prime(number):
    limit = int(Decimal(number).sqrt()) + 2
    # print(limit)
    # print(len(str(limit)))

    for num in range(2, limit):
        # print(num)
        if number % num == 0:
            return False

    return True


@benchmark
def function(n):
    sequence = []
    num = 1

    while len(sequence) < n:
        square = num ** 2
        cube = num ** 3

        if ferma_test(int(str(square)[::-1])) and ferma_test(int(str(cube)[::-1])):
            sequence.append(num)

        num += 1

    return sequence


# prime = fast_degree(2, 31) - 1
#
# start = time.time()
# # calculate_primes({}, 10000000)
# # print(calculate_primes2(2000000))
# print(is_prime(prime))
# print(f'time: {time.time() - start}')

# eratosthenes_sieve = benchmark(eratosthenes_sieve)
# primes = eratosthenes_sieve(1000000000)

# with open('primes.json', 'r') as file:
#     primes = json.load(file)
#
# print(primes[:100])

print(function(400))

# m = fast_degree(2, 521) - 1
# print(fast_degree(2, 521) - 1)
# print(fast_degree(100, m - 1) % m)
# print(ferma_test(fast_degree(2, 521) - 1))


