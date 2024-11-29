from functools import cache


@cache
def exp_sum(n, k=None):
    k = n if k is None else k

    if k == 0:
        return 0 if n else 1

    if k > n:
        return exp_sum(n, n)
    else:
        return exp_sum(n, k - 1) + exp_sum(n - k, k)


print(exp_sum(249))
