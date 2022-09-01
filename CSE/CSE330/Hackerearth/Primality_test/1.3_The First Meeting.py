from math import *
"""https://www.hackerearth.com/practice/math/number-theory/primality-tests/practice-problems/algorithm/little-shino-and-prime-difference-38c91b0d/"""


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


def main(arr, s):
    maxx = -1
    minn = 10000000
    flag = False
    for ele in arr:
        if primality(ele):
            flag = True
            if maxx < ele:
                maxx = ele
            if minn > ele:
                minn = ele

    return maxx - minn if flag else -1


if __name__ == "__main__":
    '''
    size = int(input())
    arr = list(map(int, input().split()))
    re = main(arr, size)
    print(re) '''
    print(primality(3019))

