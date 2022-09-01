from math import *

"""https://www.hackerearth.com/practice/math/number-theory/primality-tests/practice-problems/algorithm/primestring/"""


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


def occurence(s):
    d = dict();
    count = 0
    for strr in s:
        if strr not in d:
            d[strr] = 0
        d[strr] += 1
    return d


def main(s):
    re = ["NO", "YES"]
    d = occurence(s)
    if primality(len(d)):
        for i in d:
            if not primality(d[i]):
                return re[0]
        else:
            return re[1]
    else:
        return re[0]


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input().strip()
        result = main(s)
        print(result)