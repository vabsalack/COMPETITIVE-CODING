
# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

def getWays(money, coins):
    """ recursively find total ways to make change from coins for money and DP for overlap sub problems"""
    memo = {}

    def recursion(coins, money, index):

        if money == 0:
            return 1

        if index > len(coins) - 1:
            return 0

        memostr = f"{index}-{money}"
        if memostr in memo:
            return memo[memostr]

        amountwithcoin = 0
        ways = 0

        while amountwithcoin <= money:
            remaining = money - amountwithcoin
            ways += recursion(coins, remaining, index + 1)
            amountwithcoin += coins[index]

        memo[memostr] = ways

        return ways

    return recursion(coins, money, 0)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()


