#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quickSort(arr):
    # Write your code here
    pivot = arr[0]
    down = 0
    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            down += 1
            arr[i], arr[down] = arr[down], arr[i]

    arr[0], arr[down] = arr[down], arr[0]

    print(arr)
    return arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
