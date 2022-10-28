#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countArray' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER x


def countArray(n, k, x):
    # Return the number of ways to fill in the array.
    mod = pow(10, 9) + 7
    con = [0] * n
    nocon = [1] * n

    con[0] = 1 if x == 1 else 0
    nocon[0] = 0 if x == 1 else 1

    for i in range(1, n):
        con[i] = nocon[i - 1] % mod
        nocon[i] = (nocon[i - 1] * (k - 2) + con[i - 1] * (k - 1)) % mod

    return con[n - 1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = int(first_multiple_input[2])

    answer = countArray(n, k, x)

    fptr.write(str(answer) + '\n')

    fptr.close()
