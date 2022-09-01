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
    i = 2
    while i * i <= n:
        if sieve[i] == 1:
            for j in range(i * i, n + 1, i):
                sieve[j] = 0
        i += 1

    for i in range(n):
        if sieve[i]:
            print(i, end=" ")


if __name__ == "__main__":
    num = int(input())
    sieve_of_Eratosthenes(num)


