# Алгоритм Евклида для нахождения НОД
def gcd(x, y):
    while y:
        x, y = y, x % y

    return x


# Перемножение всех элементов последовательности
def mul(arr):
    res = 1

    for el in arr:
        res *= el

    return res


# Дихотомический алгоритм возведения в степень O(logn)
def fast_degree(num, degree):
    if degree == 1:
        return num
    elif degree % 2 == 0:
        return fast_degree(num * num, degree // 2)
    else:
        return num * fast_degree(num, degree - 1)


# Бинарный алгоритм возведения в степень "справа налево"
def bin_degree(num, degree):
    degree = bin(degree)[2:]
    res = 1

    for ch in degree:
        res *= res
        res *= num if int(ch) else 1

    return res


# Бинарный алгоритм возведения в степень "справа налево" по модулю
def mod_degree(num, degree, mod):
    degree = bin(degree)[2:]
    res = 1

    for ch in degree:
        res *= res
        res *= num if int(ch) else 1
        res %= mod

    return res
