from math import *
'''https://www.hackerearth.com/practice/math/number-theory/primality-tests/practice-problems/algorithm/shootout-in-london-1/'''

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


def main(arr, n):
    re = []
    for i in range(n):
        t = arr[i]
        l = r = i
        while l != -1:
            if primality(arr[l]):
                break
            l -= 1

        while r != n:
            if primality(arr[r]):
                break
            r += 1

        if l == -1 and r == n:
            re.append(-1)

        elif l == -1:
            re.append(r + 1)

        elif r == n:
            re.append(l + 1)

        else:

            left = i - l
            right = r - i
            minn = l if left <= right else r
            # print(f"{(i, minn)}")
            re.append(minn + 1)

    return re


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    r = main(arr, n)
    print(*r)