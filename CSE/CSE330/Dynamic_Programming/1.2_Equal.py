#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'equal' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equal(arr):
    # Write your code here
    ways = [0]*5
    mini = min(arr)

    for i in range(5):
        for j in range(len(arr)):
            temp = arr[i] - mini
            steps = (temp // 5) + ((temp % 5) // 2) + ((temp % 5) % 2)
            ways[i] += steps

        mini -= 1

    return min(ways)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
