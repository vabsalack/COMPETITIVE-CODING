#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'fibonacciModified' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER t1
#  2. INTEGER t2
#  3. INTEGER n
#


def fibonacciModified(t1, t2, n):
    """question is in 1 indexing, 1:t1, 2:t2, 3:... using memo as cache if n < 3 we return memo[n]
        or else computing fibo(n) and storing in memo[n] and then returning"""

    memo = {1: t1, 2: t2}

    def recursion(n):
        if n < 3 or n in memo:
            return memo[n]
        memo[n] = pow(recursion(n - 1), 2) + recursion(n - 2)
        return memo[n]

    return recursion(n)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    t1 = int(first_multiple_input[0])

    t2 = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    result = fibonacciModified(t1, t2, n)

    fptr.write(str(result) + '\n')

    fptr.close()
