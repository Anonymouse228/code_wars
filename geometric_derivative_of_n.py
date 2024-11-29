# https://www.codewars.com/kata/572caa2672a38ba648001dcd/python

def get_prime_factors(number):
    n = 2
    factors = {}

    while n * n <= number:
        while number % n == 0:
            factors[n] = factors.setdefault(n, 0) + 1
            number //= n
        n += 1

    if number > 1:
        factors[number] = factors.setdefault(number, 0) + 1

    return factors


def f(n):
    n_ = 1
    primes = get_prime_factors(n)

    for prime, count in primes.items():
        if count > 1:
            n_ *= count * prime ** (count - 1)

    return n_
