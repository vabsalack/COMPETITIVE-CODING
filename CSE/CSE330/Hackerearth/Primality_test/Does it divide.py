from math import *

"""https://www.hackerearth.com/practice/math/number-theory/primality-tests/practice-problems/algorithm/does-it-divide-3c60b8fb/"""


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


def main(N):
    if N == 1:
        return "YES"
    return "NO" if primality(N + 1) else "YES"


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N = int(input())
        re = main(N)
        print(re)