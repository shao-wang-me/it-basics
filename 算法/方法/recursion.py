from functools import reduce


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError
    if n == 0:
        return 1
    return factorial(n - 1) * n


print(factorial(100))


def factorial_tail(n: int, acc: int) -> int:
    """Python并不能优化尾递归"""
    if n < 0:
        raise ValueError
    if n == 0:
        return acc
    return factorial_tail(n - 1, acc * n)


print(factorial_tail(100, 1))


def factorial_loop(n: int) -> int:
    if n < 0:
        raise ValueError
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print(factorial_loop(100))
print(factorial_loop(1000))


def factorial_reduce(n: int) -> int:
    if n < 0:
        raise ValueError
    if n == 0:
        return 1
    return reduce(lambda x, y: x * y, range(1, n + 1))


print(factorial_reduce(100))
print(factorial_reduce(1000))
