# Context: A semiprime is a product of two prime
# numbers, not necessarily distinct.
# Squares of prime numbers are also semiprimes.

# Problem: Find the numbers which are semiprimes,
# within a given range. For e.g. 1 to 100.


def isSemiprime(num):
    # start with the smallest prime
    prime = 2
    # initialize counter to 0
    count = 0
    # Design of while loop:
    # 1. if count exceeds 2, it is not a semiprime, e.g. 30 = 2*3*5
    # 2. when the number becomes 1, we have found the second prime
    while count < 3 and num != 1:
        # if the number is divisible by current prime,
        # increment count, else move to new prime
        if not (num % prime):
            num = num / prime
            count = count + 1
        else:
            prime = prime + 1
    # if count is two, given number is a semiprime
    return count == 2


for i in range(1, 100):
    if isSemiprime(i):
        print(i, end=" ")

# Result: 4 6 9 10 14 15 21 22 25 26 33 34 35 38 39 46 49
# 51 55 57 58 62 65 69 74 77 82 85 86 87 91 93 94 95
