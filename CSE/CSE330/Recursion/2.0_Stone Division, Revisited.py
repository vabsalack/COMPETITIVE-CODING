#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'stoneDivision' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER n
#  2. LONG_INTEGER_ARRAY s
#

def stoneDivision(n, s):
    # Write your code here
    memo = {}
    s.sort()

    def recursion(n, s, memo):
        if n == 0 or n == 1:
            return 0
        if n in memo:
            return memo[n]

        max_moves = 0
        for x in s:
            moves = 0

            if n <= x:
                break

            if n != x and n % x == 0:
                moves += recursion(x, s, memo) * (n // x) + 1

            max_moves = max(max_moves, moves)

        memo[n] = max_moves
        return max_moves

    return recursion(n, s, memo)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        s = list(map(int, input().rstrip().split()))

        result = stoneDivision(n, s)

        fptr.write(str(result) + '\n')

    fptr.close()
