#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
def intsum(x):
    sm = 0
    while x:
        sm += x % 10
        x //= 10
    return sm


def fsd(n):
    if n < 10:
        return n
    return fsd(intsum(n))


def superDigit(n, k):
    # Write your code here
    nsum = 0
    for i in n:
        nsum += ord(i) - ord("0")
    return fsd(nsum * k)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
