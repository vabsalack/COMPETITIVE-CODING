#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countInversions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def mergesort(arr):
    if len(arr) == 1:
        return 0

    m = len(arr) // 2
    l, r = arr[:m], arr[m:]

    inv_cnt = mergesort(l) + mergesort(r)

    i = j = k = 0

    while i < len(l) and j < len(r):
        if r[j] < l[i]:
            arr[k] = r[j]
            j += 1

            inv_cnt += (len(l) - i)
        else:
            arr[k] = l[i]
            i += 1
        k += 1

    while i < len(l):
        arr[k] = l[i]
        i += 1
        k += 1

    while j < len(r):
        arr[k] = r[j]
        j += 1
        k += 1

    return inv_cnt


def countInversions(arr):
    # Write your code here
    inversion_count = mergesort(arr)
    return inversion_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
