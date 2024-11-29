from itertools import chain, combinations
from math import prod
import time


def prime_factors(number):
    n = 2
    factors = []

    while n * n <= number:
        while number % n == 0:
            factors.append(n)
            number //= n
        n += 1

    if number > 1:
        factors.append(number)

    return factors


def all_factors(number):
    n = 2
    factors = [1]

    while n * n <= number:
        div, mod = number // n, number % n
        if mod == 0:
            factors.append(n)
            if div != n:
                factors.append(div)
        n += 1

    if number > 1:
        factors.append(number)

    return factors


def ds_multof_pfs(n_min, n_max):
    answer = []

    for n in range(n_min, n_max + 1):
        primes = prime_factors(n)

        if not primes:
            continue

        delimiters = [1] + list(set(primes))

        for combination in set(chain.from_iterable(combinations(primes, x) for x in range(2, len(primes) + 1))):
            delimiters.append(prod(combination))

        if sum(delimiters) % sum(primes) == 0:
            answer.append(n)

    return answer


def ds_multof_pfs2(n_min, n_max):
    return [n for n in range(n_min, n_max + 1) if sum(all_factors(n)) % sum(prime_factors(n)) == 0]


start = time.time()
print(ds_multof_pfs(2, 152990))
print(f'time: {time.time() - start}')

start = time.time()
print(ds_multof_pfs2(2, 152990))
print(f'time: {time.time() - start}')

# print(all_factors(6))
