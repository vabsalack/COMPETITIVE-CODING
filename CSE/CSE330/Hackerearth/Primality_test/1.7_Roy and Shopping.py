from math import *

"""https://www.hackerearth.com/practice/math/number-theory/primality-tests/practice-problems/algorithm/roy-and-shopping-20/"""


def leastprimefactor(n):
    least = [0] * (n + 1)
    least[1] = 1
    for i in range(2, n + 1):
        if least[i] == 0:
            least[i] = i

            for j in range(i * i, n + 1, i):
                if least[j] == 0:
                    least[j] = i
    return least


least_prime = leastprimefactor(1000000)


def main(n):
    x = least_prime[n]
    # print(x)
    if x == n:
        return 0
    else:
        return n - x


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        mrp = int(input())
        re = main(mrp)
        print(re)