#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'mandragora' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY H as parameter.
#

def mandragora(H):
    # Write your code here
    H.sort()

    l = len(H)
    spoints = [i for i in range(2, len(H) + 2)]
    suffix_sum = [0] * l

    tot = 0
    for j in range(l - 1, -1, -1):
        tot += H[j]
        suffix_sum[j] = tot

    # print(suffix_sum)
    # print(spoints)

    re = max(suffix_sum[0], spoints[-1])

    for i in range(l - 1):
        heal = spoints[i] * suffix_sum[i + 1]
        print(heal)
        re = max(re, heal)

    return re


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        H = list(map(int, input().rstrip().split()))

        result = mandragora(H)

        fptr.write(str(result) + '\n')

    fptr.close()
