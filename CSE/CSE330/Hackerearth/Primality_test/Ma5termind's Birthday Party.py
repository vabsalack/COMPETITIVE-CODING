"""https://www.hackerearth.com/practice/math/number-theory/primality-tests/practice-problems/algorithm/ma5terminds-birthday-party/"""


def erathonos(n):
    sieve = [1] * (n + 1)
    sieve[1] = 1

    for i in range(2, n + 1):
        if sieve[i] == 1:
            for j in range(i * i, n, i):
                if sieve[j] == 1:
                    sieve[j] = 0
    return sieve


sieve = erathonos(1000000)


def main(l, r):
    count = 0
    for i in range(l, r + 1):
        if not sieve[i]:
            count += 1

    return count


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        l, r = list(map(int, input().split()))
        re = main(l, r)
        print(re)