from math import *


def sieveofatkin(limit):
    count = 0
    if limit >= 2:
        count += 1
    if limit >= 3:
        count += 1
    sieve = [False] * (limit + 1)
    x = 1
    while x * x <= limit:
        y = 1
        while y * y <= limit:
            n = 4 * x * x + y * y
            if n <= limit and (n % 12) in [1, 5]:
                sieve[n] ^= True
            n = 3 * x * x + y * y
            if n <= limit and n % 12 in [7]:
                sieve[n] ^= True
            n = 3 * x * x - y * y
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
            count += 1
    return count


def primality(x):
    if x <= 1:
        return False
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    for i in range(5, floor(sqrt(x)) + 1, 6):
        if x % i == 0 or x % (i + 2) == 0:
            return False
    return True


def main(l, r):
    memo = sieveofatkin(l-1)
    count = 0

    for i in range(l, r + 1):
        if primality(i):
            memo += 1
        if primality(memo):
            count += 1

    return count


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        l, r = list(map(int, input().split()))
        re = main(l, r)
        print(re)