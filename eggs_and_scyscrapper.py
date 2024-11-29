from functools import lru_cache, cache


# @lru_cache
@cache
def height(n, m):
    # if n == 0 or m == 0:
    #     return 0
    # elif n == 1:
    #     return m
    if n == 2:
        return (m * m + m) // 2
    elif n >= m:
        return 2 ** m - 1

    return height(n - 1, m - 1) + 1 + height(n, m - 1)


# print(height(477, 500))
# print(height(3, 10))

n = 2
for m in range(1, 11):
    print(f'f({n}, {m}) = {height(n, m)}')
