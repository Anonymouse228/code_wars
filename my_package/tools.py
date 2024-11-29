from time import time


# Декоратор для измерения времени работы функции
def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print(f'time: {time() - start}')
        return result
    return wrapper
