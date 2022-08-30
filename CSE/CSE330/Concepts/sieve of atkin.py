from math import *


def SieveOfAtkin(limit):

    result = []

    if limit >= 2:
        # print(2, end=" ")
        result.append(2)
    if limit >= 3:
        # print(3, end=" ")
        result.append(3)
    sieve = [False] * (limit + 1)

    x = 1
    while x * x <= limit:
        y = 1
        while y * y <= limit:

            n = (4 * x * x) + (y * y)
            if n <= limit and (n % 12) in [1, 5]:
                sieve[n] ^= True

            n = (3 * x * x) + (y * y)
            if n <= limit and (n % 12) in [7]:
                sieve[n] ^= True

            n = (3 * x * x) - (y * y)
            if x > y and n <= limit and n % 12 in [11]:
                sieve[n] ^= True

            y += 1
        x += 1

    r = 5
    while r * r <= limit:
        if sieve[r]:
            for i in range(r * r, limit + 1, r * r):
                sieve[i] = False
        r += 1

    for i in range(5, limit + 1):
        if sieve[i]:
            # print(i, end=" ")
            result.append(i)

    return result


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


if __name__ == "__main__":
    num = int(input())
    re = SieveOfAtkin(num)
    print(*re)
    for i in re:
        print(primality(i), end=" ")

