#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'fairCut' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def fairCut(k, a):
    # Write your code here
    a.sort()
    n = len(arr)
    if 2 * k > n:
        k = n - k

    dp = [[math.inf for i in range(0, n + 1)] for j in range(0, n + 1)]
    dp[0][0] = 0

    for i in range(0, n):
        for j in range(0, i + 1):
            if i > k and i - j > n - k:
                continue
            to_li = dp[i][j] + arr[i] * (i - j - (n - k - (i - j)))
            to_lu = dp[i][j] + arr[i] * (j - (k - j))

            if dp[i + 1][j + 1] > to_li:
                dp[i + 1][j + 1] = to_li

            if dp[i + 1][j] > to_lu:
                dp[i + 1][j] = to_lu

    return dp[n][k]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = fairCut(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
