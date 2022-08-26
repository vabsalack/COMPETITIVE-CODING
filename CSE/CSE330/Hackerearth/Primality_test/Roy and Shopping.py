from math import *


def primality(x):
    if x <= 1:
        return True
    if x == 2 or x == 3:
        return True, 0

    if x % 2 == 0:
        return False, 2
    if x % 3 == 0:
        return False, 3

    for i in range(5, floor(sqrt(x)) + 1, 6):
        if x % i == 0:
            return False, i
        if x % (i + 2) == 0:
            return False, i + 2
    return True, 0


def main(n):
    flag, z = primality(n)
    if flag:
        print(0)
    else:
        print(n - z)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        mrp = int(input())
        main(mrp)