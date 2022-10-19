
"""https://www.hackerearth.com/practice/math/number-theory/primality-tests/practice-problems/algorithm/monks-problem-ffeebf8a/"""


def sieveoferatosthenes(x):
    sieve = [1] * (x + 1)
    sieve[0] = 0
    sieve[1] = 1
    i = 2
    while i * i <= x:
        if sieve[i] == 1:
            for j in range(i * i, x + 1, i):
                sieve[j] = 0
        i += 1
    return sieve


sieve = sieveoferatosthenes(1000000)


def solve(N):
    # Your code goes here
    return "No" if sieve[N] else "Yes"


T = int(input())
for _ in range(T):
    N = int(input())
    out_ = solve(N)
    print(out_)