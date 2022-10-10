#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'powerSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER X
#  2. INTEGER N
#

def powerSum(X, N):
    # Write your code here
    def recursion(x, n, start):

        count = 0

        for i in range(start, x):

            ans = x - i ** n

            if ans == 0:
                count += 1
            if ans > 0:
                count += recursion(ans, n, i + 1)
            if ans < 0:
                continue

        return count

    re = recursion(X, N, 1)
    return re


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input().strip())

    N = int(input().strip())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')

    fptr.close()
