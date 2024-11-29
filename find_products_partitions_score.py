# #  https://www.codewars.com/kata/571dd22c2b97f2ce400010d4
#
# from itertools import chain, combinations
#
from my_package.primes import prime_factors
# from my_package.math import fast_degree, mul
from my_package.tools import benchmark


prime_factors = benchmark(prime_factors)
#
#
# def unique_list(arr):
#     arr = map(sorted, arr)
#     arr = sorted(arr)
#     new_arr = []
#     for el in arr:
#         if not new_arr or el != new_arr[-1]:
#             new_arr.append(el)
#     return new_arr
#
#
# def find_factor_combinations(factors, combinations=None):
#     combinations = combinations or []
#
#     if len(factors) == 2:
#         return [factors]
#
#     new_combinations = []
#     for combination in find_factor_combinations(factors[1:], combinations):
#         factor = factors[0]
#         old_factors = []
#
#         while combination:
#             for i in range(len(combination)):
#                 new_combination = combination.copy()
#                 new_combination[i] *= factor
#                 new_combinations.append(old_factors + new_combination)
#
#             old_factors.append(factor)
#             factor = combination[0]
#             combination = combination[1:]
#
#     new_combinations.append(factors)
#     new_combinations = unique_list(new_combinations)
#     return new_combinations
#
#
# def find_spec_prod_part(n, mode):
#     modes = {'min': min, 'max': max}
#     primes = prime_factors(n)
#
#     if len(primes) < 2:
#         return "It is a prime number"
#
#     scores = []
#     for combination in find_factor_combinations(primes):
#         score = 0
#         factor = 0
#
#         for num in set(combination):
#             degree = combination.count(num)
#
#             score += fast_degree(num, degree)
#             factor += degree
#
#         score *= factor
#         scores.append([sorted(combination, reverse=True), score])
#
#     return modes[mode](scores, key=lambda el: el[-1])
#
#
# @benchmark
# def find_spec_prod_part2(n, mode):
#     modes = {'min': min, 'max': max}
#     primes = prime_factors(n)
#
#     if len(primes) < 2:
#         return "It is a prime number"
#
#     all_factors = []
#     for combination in set(chain.from_iterable(combinations(primes, x) for x in range(1, len(primes) + 1))):
#         all_factors.append(mul(combination))
#
#     all_factors_combinations = []
#     for combination in set(chain.from_iterable(combinations(all_factors, x) for x in range(2, len(all_factors) + 1))):
#         if mul(combination) == n:
#             all_factors_combinations.append(combination)
#
#     scores = []
#     for combination in all_factors_combinations:
#         score = 0
#         factor = 0
#
#         for num in set(combination):
#             degree = combination.count(num)
#
#             score += fast_degree(num, degree)
#             factor += degree
#
#         score *= factor
#         scores.append([sorted(combination, reverse=True), score])
#
#     return modes[mode](scores, key=lambda el: el[-1])
#
#
# # print(find_spec_prod_part(1416, 'max'))
#
# # primes = prime_factors(1416)
# # primes = prime_factors(1416)
# # primes = []
# # primes = primes[::-1]
# # print(find_spec_prod_part(7415, 'max'))
# print(find_spec_prod_part2(8262, 'max'))

from collections import Counter

seen = set()


def toOrderedTup(x): return tuple(sorted(x, reverse=True))


def score(x): return len(x) * sum(p ** f for p, f in Counter(x).items())


def uniq_partitions(tup):
    if tup not in seen and len(tup) > 1:
        seen.add(tup)
        yield [list(tup), score(tup)]
        for i, v in enumerate(tup):
            for j in range(i + 1, len(tup)):
                cnd = tup[:i] + tup[i + 1:j] + tup[j + 1:] + (v * tup[j],)
                yield from uniq_partitions(toOrderedTup(cnd))


primes = prime_factors(210)
primes = toOrderedTup(primes)
print(primes)
print(list(uniq_partitions(primes)))
