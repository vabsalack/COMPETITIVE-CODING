#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'stockmax' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

def stockmax(prices):
    """ using suffix max of array elements, and find difference btw prices and suffix max to sum profit"""
    suffix_max = [-1] * len(prices)
    indx = -1
    for i in range(len(prices)):

        if i < indx + 1:
            suffix_max[i] = suffix_max[i - 1]
            continue
        peak = prices[i]
        indx = i

        for j in range(i + 1, len(prices)):
            if prices[j] > peak:
                peak = prices[j]
                indx = j
        suffix_max[i] = peak

    profit = 0

    for i in range(len(prices)):
        profit += abs(prices[i] - suffix_max[i])
    return profit


def softmax2(prices):
    """ the approach is to find peak from last, and find diff btw prices[i] and peak to sum compute to profit"""
    peak = float("-inf")
    profit = 0

    for i in range(len(prices) - 1, -1, -1):
        peak = max(peak, prices[i])
        profit += (peak - prices[i])

    return profit


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)

        fptr.write(str(result) + '\n')

    fptr.close()
