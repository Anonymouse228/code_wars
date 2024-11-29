from my_package.math import mod_degree, gcd
from json import load


# Вероятносный тест проверки простоты Ферма
def ferma_test(m: int, attempts: int = 100) -> bool:
    carmichael_numbers = [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841,
                          29341, 41041, 46657, 52633, 62745, 63973, 75361, 101101,
                          115921, 126217, 162401, 172081, 188461, 252601, 278545,
                          294409, 314821, 334153, 340561, 399001, 410041, 449065,
                          488881, 512461]

    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                     101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197,
                     199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,
                     317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439,
                     443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]

    if m in carmichael_numbers:
        return False

    for a in prime_numbers[:attempts]:
        if gcd(a, m) != 1 or mod_degree(a, m - 1, m) != 1:
            return False

    return True


# Решето Эратосфена
def eratosthenes_sieve(n: int) -> list:
    n += 1
    sieve = [True for _ in range(n)]
    i = 2

    while i * i <= n:
        for j in range(i * i, len(sieve), i):
            sieve[j] = False
        i = sieve.index(True, i + 1)

    return [i for i in range(2, n) if sieve[i]]


# Простые множители числа, не включая 1
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


# Простые множители числа, не включая 1,
def advanced_prime_factors(number, primes_path='my_package\data\primes.json'):
    n = 0
    factors = []

    with open(primes_path, 'r') as file:
        primes = load(file)

    while primes[n] * primes[n] <= number:
        while number % primes[n] == 0:
            factors.append(primes[n])
            number //= primes[n]
        n += 1

    if number > 1:
        factors.append(number)

    return factors


# Все множители числа, включая 1
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
