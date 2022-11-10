#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoRobots' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER m
#  2. 2D_INTEGER_ARRAY queries
#
nax = 1005
a = [0] * (nax)
b = [0] * (nax)

dp = [[0] * nax] * nax


def dist(i, j):
    if i == 0:
        return abs(b[j] - a[j])
    return abs(a[j] - b[i]) + abs(b[j] - a[j])


def twoRobots(m, queries):
    # Write your code here
    m = len(queries)

    global a, b
    for i in range(m):
        a[i + 1], b[i + 1] = queries[i][0], queries[i][1]

    global dp
    for i in range(nax):
        for j in range(1, nax):
            dp[i][j] = float("inf")

    res = float("inf")

    for i in range(m):
        for j in range(i, m + 1):
            if j == m:
                res = min(res, dp[i][j])
                continue

            me = dp[i][j]

            dp[i][j + 1] = min(dp[i][j + 1], me + dist(j, j + 1))
            dp[j][j + 1] = min(dp[j][j + 1], me + dist(i, j + 1))

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    queries = []

    for _ in range(n):
        queries.append(list(map(int, input().rstrip().split())))

    result = twoRobots(m, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
