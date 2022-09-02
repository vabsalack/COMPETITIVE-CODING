from math import *


def primality(x):
    if x <= 1:
        return False
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    for i in range(5, floor(sqrt(x))+1, 6):
        if x % i == 0 or x % (i + 2) == 0:
            return False
    return True


def sieve_of_Eratosthenes(n):
    sieve = [1] * (n + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, n+1):
        if sieve[i] == 1:
            for j in range(i * i, n + 1, i):
                sieve[j] = 0

    for i in range(n+1):
        if sieve[i]:
            print(i, end=", ")


def sieve_count(n):
    sieve = [1] * (n + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, n+1):
        if sieve[i] == 1:
            for j in range(i * i, n + 1, i):
                sieve[j] = 0
    s = 0
    for i in range(n+1):
        s += sieve[i]
        sieve[i] = s

    return sieve


if __name__ == "__main__":
    num = int(input())
    sieve_of_Eratosthenes(num)
    print()
    print(*sieve_count(num))

