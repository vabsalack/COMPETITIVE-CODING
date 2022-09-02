"""https://www.hackerearth.com/practice/math/number-theory/primality-tests/practice-problems/algorithm/ma5terminds-birthday-party/"""


def sieve_count(n):
    sieve = [1] * (n + 1)
    sieve[0] = 0
    sieve[1] = 1
    for i in range(2, n + 1):
        if sieve[i] == 1:
            for j in range(i * i, n + 1, i):
                sieve[j] = 0
    s = 0
    for i in range(n + 1):
        s += sieve[i]
        sieve[i] = s

    return sieve


sieve = sieve_count(1000000)


def main(l, r):
    remain = sieve[r] - sieve[l - 1]
    return r - l + 1 - remain


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        l, r = list(map(int, input().split()))
        re = main(l, r)
        print(re)