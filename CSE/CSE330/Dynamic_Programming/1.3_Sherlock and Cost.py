#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'cost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY B as parameter.
#

def cost(arr):
    # Write your code here
    x1, y1 = 0, 0

    for i in range(1, len(arr)):
        x = max(abs(arr[i] - arr[i - 1]) + x1, abs(arr[i] - 1) + y1)
        y = max(abs(1 - arr[i - 1]) + x1, y1)

        x1, y1 = x, y

    return max(x1, y1)


f


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        B = list(map(int, input().rstrip().split()))

        result = cost(B)

        fptr.write(str(result) + '\n')

    fptr.close()
