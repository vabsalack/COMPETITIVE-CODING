#!/bin/python3

from math import *
import os
import random
import re
import sys
from collections import Counter


#
# Complete the 'primeXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
# def primality(n):
#     if n <= 1:
#         return False

#     if n in [2, 3]:
#         return True

#     if 0 in [n % 2, n % 3]:
#         return False

#     for i in range(5, floor(sqrt(n))+1, 6):
#         if 0 in [n % i, n % (i + 2)]:
#             return False

#     return True

# # def xor(ar):
# #     x = 0
# #     for i in range(len(ar)):
# #         x ^= ar[i]
# #     return primality(x)

# def primeXor(a):
# #     # Write your code here
# #     global ways
# #     ways = 0
# #     l = len(a)
# #     ss = []
# #     memo = set()
# #     def recursion(i):
# #         global ways
# #         if i >= l:

# #             if tuple(ss) in memo:
# #                 return
# #             memo.add(tuple(ss[:]))
# #             if xor(ss):
# #                 # print(ss)
# #                 ways += 1
# #             return

# #         ss.append(a[i])
# #         recursion(i + 1)
# #         ss.pop()
# #         recursion(i + 1)

# #     recursion(0)
# #     return ways
#    count = 0
#    c = Counter(a)
#    dp = [0]*8192
#    dp[0] = 1
#    cache = []
#    for e in c.keys():
#     even = c[e]//2+1
#     odd = (c[e] + 1)//2

#     dp = [(dp[i]*even + dp[i^e]*odd)%(10**9 + 7) for i in range(8192)]

#     for j in range(8192):
#         if primality(j):
#             count += dp[j]

#             if count > (10**9 + 7):
#                 count %= (10**9 + 7)

#     return count

def isPrime(x):
    if x == 1:
        return False

    if x == 2:
        return True

    for d in range(2, max(2, int(x ** 0.5)) + 1):
        if x % d == 0:
            return False
    return True


def primeXor(a):
    count = 0
    c = Counter(a)
    dp = [0] * 8192
    dp[0] = 1
    cache = []
    for e in c.keys():
        even = c[e] // 2 + 1
        odd = (c[e] + 1) // 2
        dp = [(dp[i] * even + dp[i ^ e] * odd) % (10 ** 9 + 7) for i in range(8192)]

    for j in range(8192):
        if isPrime(j):
            count += dp[j]
            if count > (10 ** 9 + 7):
                count = count % (10 ** 9 + 7)

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        a = list(map(int, input().rstrip().split()))

        result = primeXor(a)

        fptr.write(str(result) + '\n')

    fptr.close()
