#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'xorAndSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#
# def binarytodeicmal(x):
#     pl = 0
#     decimal = 0
#     while x:
#         lsb = x % 10
#         x //= 10
#         if lsb:
#             decimal += pow(2, pl)
#         pl += 1
#     return decimal

def xorAndSum(a, b):
    # Write your code here
    # a, b = list(map(binarytodeicmal, map(int, [a, b])))

    a, b = int(a, 2), int(b, 2)
    total = 0
    for i in range(314160):
        if b == 0:
            break

        total += a ^ (b << i)

    total += (a * (314159 - i))

    return total % (10 ** 9 + 7)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    result = xorAndSum(a, b)

    fptr.write(str(result) + '\n')

    fptr.close()
