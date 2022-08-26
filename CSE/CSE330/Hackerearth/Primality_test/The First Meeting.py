from math import *


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
    minn = maxx = int()
    flag = True
    for ele in arr:
        if primality(ele):
            if flag:
                minn = maxx = ele
                flag = False
                continue
            if ele > maxx:
                maxx = ele
            if ele < minn:
                minn = ele
    if flag:
        print(-1)
        return
    print(maxx - minn)


if __name__ == "__main__":
    size = int(input())
    arr = list(map(int, input().split()))
    main(arr, size)
