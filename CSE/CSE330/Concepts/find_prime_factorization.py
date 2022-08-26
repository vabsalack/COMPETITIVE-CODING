from math import *


def primality(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, floor(sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def fermat_rule(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if (i ** n - i) % n != 0:
            return False
    return True


def find_factors(n):
    for i in range(1, floor(sqrt(n))):
        if n % i == 0:
            print(i, int(n / i))


def find_prime_factors(n):
    for i in range(2, n):
        if n % i == 0 and primality(i):
            print(i)


if __name__ == "__main__":
    n = int(input())
    print(primality(n))
