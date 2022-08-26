from math import *


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
    d = dict()
    count = 0
    for ele in s:
        if ele not in d:
            d[ele] = 0
            count += 1
        d[ele] += 1
    return d, count


def main(s):
    d, count = occurence(s)
    if primality(count):
        for i in d:
            if not primality(d[i]):
                print("NO")
                return
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input().strip()
        main(s)