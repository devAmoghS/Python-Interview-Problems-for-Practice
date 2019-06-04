import random
from math import ceil
from math import log10


def get_digits(n):
    if n > 0:
        digits = int(log10(n)) + 1
    elif n == 0:
        digits = 1
    else:
        digits = int(log10(-n)) + 2
    return digits


def karatsuba(x, y):
    # the base case for recursion
    if x < 10 and y < 10:
        return x * y

    # n is the number of digits in the highest input number
    n = max(get_digits(x), get_digits(y))

    n_2 = int(ceil(n / 2.0))
    n = n if n % 2 == 0 else n + 1

    # split the input numbers
    a, b = divmod(x, 10 ** n_2)
    c, d = divmod(y, 10 ** n_2)

    # applying the recursive steps
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba((a + b), (c + d)) - ac - bd

    # performs the multiplication
    z2 = (10 ** n) * ac
    z1 = (10 ** n_2) * ad_bc
    z0 = bd
    return z2 + z1 + z0


def test():
    for i in range(1000):
        x = random.randint(1, 10**5)
        y = random.randint(1, 10**5)
        expected = x*y
        result = karatsuba(x, y)
        if result != expected:
            return print("failed")
    return print("ok")


if __name__ == '__main__':
    test()
