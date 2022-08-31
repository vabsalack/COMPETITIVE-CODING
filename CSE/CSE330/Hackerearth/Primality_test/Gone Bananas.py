from math import *

"""https://www.hackerearth.com/practice/math/number-theory/primality-tests/practice-problems/algorithm/monks-problem-ffeebf8a/"""


def primality(n):
    if n <= 1:
        return True
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, floor(sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def solve(N):
    # Your code goes here
    return "No" if primality(N) else "Yes"


T = int(input())
for _ in range(T):
    N = int(input())
    out_ = solve(N)
    print(out_)